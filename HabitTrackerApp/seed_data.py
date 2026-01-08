"""
Seed Script: Create test users with random activities
Run this script to populate the database with sample data for testing
"""
import sys
from pathlib import Path
import random
from datetime import datetime, timedelta

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from data_handler import UserDataManager, TrackerDataManager
from trackers.student_trackers import get_student_trackers
from trackers.adult_trackers import get_adult_trackers
from trackers.senior_trackers import get_senior_trackers


# Test user templates
TEST_USERS = [
    {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@example.com",
        "phone": "+1-555-0101",
        "date_of_birth": "03/15/2005",
        "password": "Alice123!",
        "username": "alice2005",
        "role": "student",
        "gender": "female"
    },
    {
        "first_name": "Bob",
        "last_name": "Smith",
        "email": "bob.smith@example.com",
        "phone": "+1-555-0102",
        "date_of_birth": "07/22/1990",
        "password": "Bob12345!",
        "username": "bobsmith",
        "role": "adult",
        "gender": "male"
    },
    {
        "first_name": "Carol",
        "last_name": "Williams",
        "email": "carol.williams@example.com",
        "phone": "+1-555-0103",
        "date_of_birth": "11/08/1955",
        "password": "Carol123!",
        "username": "carolw",
        "role": "senior",
        "gender": "female"
    },
    {
        "first_name": "David",
        "last_name": "Brown",
        "email": "david.brown@example.com",
        "phone": "+1-555-0104",
        "date_of_birth": "05/30/2003",
        "password": "David123!",
        "username": "davidb",
        "role": "student",
        "gender": "male"
    },
    {
        "first_name": "Emma",
        "last_name": "Davis",
        "email": "emma.davis@example.com",
        "phone": "+1-555-0105",
        "date_of_birth": "09/12/1985",
        "password": "Emma1234!",
        "username": "emmad",
        "role": "adult",
        "gender": "female"
    },
    {
        "first_name": "Noah",
        "last_name": "Kato",
        "email": "noah.kato@example.com",
        "phone": "+1-555-0106",
        "date_of_birth": "12/01/1992",
        "password": "Kiseki2026!",
        "username": "kisekipro",
        "role": "adult",
        "gender": "male",
        "activity_days": 60,
        "daily_trackers_min": 8,
        "daily_trackers_max": 12
    },
    {
        "first_name": "Maya",
        "last_name": "Singh",
        "email": "maya.singh@example.com",
        "phone": "+1-555-0107",
        "date_of_birth": "08/19/1995",
        "password": "Maya2026!",
        "username": "mayasingh",
        "role": "student",
        "gender": "female",
        "activity_days": 75,
        "daily_trackers_min": 7,
        "daily_trackers_max": 12
    },
    {
        "first_name": "Omar",
        "last_name": "Hassan",
        "email": "omar.hassan@example.com",
        "phone": "+1-555-0108",
        "date_of_birth": "04/03/1988",
        "password": "Omar2026!",
        "username": "omarhassan",
        "role": "adult",
        "gender": "male",
        "activity_days": 90,
        "daily_trackers_min": 8,
        "daily_trackers_max": 12
    }
]


def get_trackers_for_role(role: str):
    """Get trackers based on user role"""
    if role == "student":
        return get_student_trackers()
    elif role == "adult":
        return get_adult_trackers()
    elif role == "senior":
        return get_senior_trackers()
    return []


def generate_random_value(tracker):
    """Generate a random value for a tracker based on its type"""
    if tracker.tracker_type == "duration":
        # Random hours between 0 and goal * 1.5
        return round(random.uniform(0, tracker.goal * 1.5), 1)
    elif tracker.tracker_type == "counter":
        # Random count up to goal * 1.5
        return random.randint(0, int(tracker.goal * 1.5))
    elif tracker.tracker_type == "rating":
        # Random rating 1 to max
        return random.randint(1, int(tracker.max_value))
    elif tracker.tracker_type == "checkbox":
        # 70% chance of completion
        return 1 if random.random() > 0.3 else 0
    elif tracker.tracker_type == "numeric":
        # Random value within range
        return round(random.uniform(tracker.min_value, min(tracker.goal * 1.5, tracker.max_value)), 2)
    return 0


def create_test_users():
    """Create test users in the database"""
    user_manager = UserDataManager()
    created_users = []

    print("=" * 60)
    print("  Creating Test Users")
    print("=" * 60)

    for user_data in TEST_USERS:
        username = user_data['username']

        # Check if user already exists
        if user_manager.username_exists(username):
            print(f"  [skip] User '{username}' already exists")
            created_users.append(user_data)
            continue

        # Create user
        success = user_manager.create_user(user_data)
        if success:
            print(f"  [ok] Created user: {user_data['first_name']} {user_data['last_name']} (@{username})")
            created_users.append(user_data)
        else:
            print(f"  [fail] Failed to create user: {username}")

    return created_users

def add_random_activities(users):
    """Add random activities to users over a range of days"""
    print()
    print("=" * 60)
    print("  Adding Random Activities")
    print("=" * 60)

    today = datetime.now()

    for user_data in users:
        username = user_data['username']
        role = user_data['role']

        activity_days = int(user_data.get('activity_days', 14))
        min_trackers = int(user_data.get('daily_trackers_min', 3))
        max_trackers = int(user_data.get('daily_trackers_max', 6))
        if min_trackers > max_trackers:
            min_trackers, max_trackers = max_trackers, min_trackers

        print(f"\n  Adding activities for @{username} (Role: {role})")

        tracker_manager = TrackerDataManager(username)
        trackers = get_trackers_for_role(role)

        if not trackers:
            print(f"     No trackers found for role: {role}")
            continue

        max_trackers = min(max_trackers, len(trackers))
        min_trackers = min(min_trackers, max_trackers)
        if max_trackers <= 0:
            print("     No trackers available for activity generation")
            continue

        activity_count = 0

        # Generate activities for the past N days
        for days_ago in range(activity_days):
            date = today - timedelta(days=days_ago)
            date_str = date.strftime("%Y-%m-%d")

            daily_count = random.randint(min_trackers, max_trackers)
            daily_trackers = random.sample(trackers, daily_count)

            for tracker in daily_trackers:
                value = generate_random_value(tracker)

                activity_data = {
                    'date': date_str,
                    'tracker_type': tracker.tracker_type,
                    'tracker_name': tracker.name,
                    'value': value,
                    'goal': tracker.goal,
                    'unit': tracker.unit,
                    'completed': 'yes' if value >= tracker.goal else 'no'
                }

                if tracker_manager.log_activity(activity_data):
                    activity_count += 1

        print(f"     Added {activity_count} activities over {activity_days} days")

def add_random_reminders(users):
    """Add random reminders to users"""
    print()
    print("=" * 60)
    print("  Adding Random Reminders")
    print("=" * 60)

    reminder_templates = [
        {"title": "Morning Exercise", "description": "Do 30 minutes of exercise", "time": "07:00", "category": "health"},
        {"title": "Take Vitamins", "description": "Don't forget daily vitamins", "time": "08:00", "category": "health"},
        {"title": "Study Session", "description": "Complete study goals", "time": "10:00", "category": "academic"},
        {"title": "Drink Water", "description": "Stay hydrated!", "time": "12:00", "category": "health"},
        {"title": "Lunch Break", "description": "Eat a healthy meal", "time": "12:30", "category": "health"},
        {"title": "Afternoon Review", "description": "Review progress", "time": "16:00", "category": "general"},
        {"title": "Evening Walk", "description": "30 minute evening walk", "time": "18:00", "category": "health"},
        {"title": "Read a Book", "description": "Read for 20 minutes", "time": "20:00", "category": "learning"},
        {"title": "Sleep Reminder", "description": "Prepare for bed", "time": "22:00", "category": "health"},
    ]

    today = datetime.now()

    for user_data in users:
        username = user_data['username']
        tracker_manager = TrackerDataManager(username)

        # Add 2-4 random reminders
        num_reminders = random.randint(2, 4)
        selected_reminders = random.sample(reminder_templates, num_reminders)

        reminder_count = 0
        for reminder in selected_reminders:
            reminder_date = (today + timedelta(days=random.randint(0, 7))).strftime("%Y-%m-%d")

            reminder_data = {
                'title': reminder['title'],
                'description': reminder['description'],
                'date': reminder_date,
                'time': reminder['time'],
                'recurrence': random.choice(['once', 'daily', 'weekly']),
                'category': reminder['category'],
                'priority': random.choice(['low', 'medium', 'high']),
            }

            if tracker_manager.add_reminder(reminder_data):
                reminder_count += 1

        print(f"  Added {reminder_count} reminders for @{username}")

def run_seed():
    """Main function to run the seeding process"""
    print()
    print("Starting database seeding...")
    print()

    # Create users
    users = create_test_users()

    if not users:
        print("No users created. Exiting...")
        return

    # Add activities
    add_random_activities(users)

    # Add reminders
    add_random_reminders(users)

    print()
    print("=" * 60)
    print("  Seeding Complete!")
    print("=" * 60)
    print()
    print("Test accounts created:")
    print("-" * 40)
    for user in TEST_USERS:
        print(f"  Username: {user['username']}")
        print(f"  Password: {user['password']}")
        print(f"  Role: {user['role']}")
        if user.get('activity_days'):
            print(f"  Activity days: {user['activity_days']}")
        print()

