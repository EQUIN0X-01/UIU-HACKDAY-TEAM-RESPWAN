"""
Automated Test Script
Tests core functionality and captures any errors
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from data_handler import UserDataManager, TrackerDataManager
from trackers.student_trackers import get_student_trackers
from trackers.adult_trackers import get_adult_trackers
from trackers.senior_trackers import get_senior_trackers
from utils import Validators, DateTimeHelper, StatisticsCalculator, PasswordHasher
from datetime import datetime
import pandas as pd


def test_user_authentication():
    """Test user login and data retrieval"""
    print("\n🔐 Testing User Authentication...")
    print("-" * 40)
    
    user_manager = UserDataManager()
    
    # Test valid login
    test_cases = [
        ("alice2005", "Alice123!"),
        ("bobsmith", "Bob12345!"),
        ("carolw", "Carol123!"),
    ]
    
    for username, password in test_cases:
        try:
            result = user_manager.authenticate_user(username, password)
            if result and not isinstance(result, dict) or (isinstance(result, dict) and 'error' not in result):
                print(f"  ✅ Login successful: @{username}")
            else:
                print(f"  ❌ Login failed: @{username} - {result}")
        except Exception as e:
            print(f"  ❌ ERROR authenticating @{username}: {e}")
    
    # Test invalid login
    try:
        result = user_manager.authenticate_user("alice2005", "wrongpassword")
        if result is None:
            print(f"  ✅ Invalid password correctly rejected")
        else:
            print(f"  ⚠️  Invalid password not rejected properly")
    except Exception as e:
        print(f"  ❌ ERROR testing invalid password: {e}")


def test_tracker_data_retrieval():
    """Test tracker data operations"""
    print("\n📊 Testing Tracker Data Retrieval...")
    print("-" * 40)
    
    test_users = ["alice2005", "bobsmith", "carolw", "davidb", "emmad"]
    
    for username in test_users:
        try:
            tracker_manager = TrackerDataManager(username)
            
            # Test get all tracker names
            names = tracker_manager.get_all_tracker_names()
            print(f"  @{username}: {len(names)} unique trackers")
            
            # Test streak calculation
            streak = tracker_manager.calculate_streak()
            print(f"    Streak: {streak} days")
            
            # Test date range query
            today = datetime.now()
            start = (today - pd.Timedelta(days=7)).strftime("%Y-%m-%d")
            end = today.strftime("%Y-%m-%d")
            activities = tracker_manager.get_activities_by_date_range(start, end)
            print(f"    Activities (last 7 days): {len(activities)}")
            
            # Test today's activities
            today_str = today.strftime("%Y-%m-%d")
            today_activities = tracker_manager.get_activities_by_date(today_str)
            print(f"    Today's activities: {len(today_activities)}")
            
        except Exception as e:
            print(f"  ❌ ERROR for @{username}: {e}")
            import traceback
            traceback.print_exc()


def test_tracker_definitions():
    """Test tracker class definitions"""
    print("\n📋 Testing Tracker Definitions...")
    print("-" * 40)
    
    roles = [
        ("student", get_student_trackers),
        ("adult", get_adult_trackers),
        ("senior", get_senior_trackers),
    ]
    
    for role_name, get_trackers in roles:
        try:
            trackers = get_trackers()
            print(f"  {role_name.title()}: {len(trackers)} trackers defined")
            
            # Check each tracker has required attributes
            for tracker in trackers:
                assert hasattr(tracker, 'name'), f"Missing 'name' in {tracker}"
                assert hasattr(tracker, 'tracker_type'), f"Missing 'tracker_type' in {tracker}"
                assert hasattr(tracker, 'unit'), f"Missing 'unit' in {tracker}"
                assert hasattr(tracker, 'goal'), f"Missing 'goal' in {tracker}"
            
            print(f"    ✅ All trackers have required attributes")
            
        except Exception as e:
            print(f"  ❌ ERROR for {role_name}: {e}")
            import traceback
            traceback.print_exc()


def test_validators():
    """Test input validators"""
    print("\n✅ Testing Validators...")
    print("-" * 40)
    
    # Test username validation
    test_usernames = [
        ("validuser", True),
        ("ab", False),  # Too short
        ("valid123", True),
        ("invalid user", False),  # Contains space
        ("user@name", False),  # Contains special char
    ]
    
    for username, expected_valid in test_usernames:
        try:
            valid, msg = Validators.validate_username(username)
            status = "✅" if valid == expected_valid else "❌"
            print(f"  {status} Username '{username}': {msg if not valid else 'Valid'}")
        except Exception as e:
            print(f"  ❌ ERROR validating username '{username}': {e}")
    
    # Test email validation
    test_emails = [
        ("test@example.com", True),
        ("invalid-email", False),
        ("user@domain.co.uk", True),
    ]
    
    for email, expected_valid in test_emails:
        try:
            valid, msg = Validators.validate_email(email)
            status = "✅" if valid == expected_valid else "❌"
            print(f"  {status} Email '{email}': {msg if not valid else 'Valid'}")
        except Exception as e:
            print(f"  ❌ ERROR validating email '{email}': {e}")
    
    # Test password validation
    test_passwords = [
        ("short", False),
        ("validpassword123", True),
        ("Str0ng!Pass", True),
    ]
    
    for password, expected_valid in test_passwords:
        try:
            valid, msg, strength = Validators.validate_password(password)
            status = "✅" if valid == expected_valid else "❌"
            print(f"  {status} Password '{password[:4]}...': {strength} - {msg if not valid else 'Valid'}")
        except Exception as e:
            print(f"  ❌ ERROR validating password: {e}")


def test_statistics_calculator():
    """Test statistics calculations"""
    print("\n📈 Testing Statistics Calculator...")
    print("-" * 40)
    
    try:
        # Test progress category
        categories = [
            (0, "0-25"),
            (25, "0-25"),
            (50, "26-50"),
            (75, "51-75"),
            (90, "76-90"),
            (100, "91-100"),
        ]
        
        for progress, expected_category in categories:
            result = StatisticsCalculator.get_progress_category(progress)
            status = "✅" if result == expected_category else "❌"
            print(f"  {status} Progress {progress}%: Category '{result}'")
    
    except Exception as e:
        print(f"  ❌ ERROR in statistics calculator: {e}")
        import traceback
        traceback.print_exc()


def test_date_time_helper():
    """Test date/time utilities"""
    print("\n🕐 Testing DateTimeHelper...")
    print("-" * 40)
    
    try:
        # Test time of day
        time_of_day = DateTimeHelper.get_time_of_day()
        print(f"  ✅ Time of day: {time_of_day}")
        
        # Test format date
        today = datetime.now()
        formatted = DateTimeHelper.format_date(today)
        print(f"  ✅ Formatted date: {formatted}")
        
        # Test day name
        day_name = DateTimeHelper.get_day_name(today)
        print(f"  ✅ Day name: {day_name}")
        
    except Exception as e:
        print(f"  ❌ ERROR in DateTimeHelper: {e}")
        import traceback
        traceback.print_exc()


def test_data_integrity():
    """Test data file integrity"""
    print("\n💾 Testing Data Integrity...")
    print("-" * 40)
    
    from config import USERS_DATA_FILE, USERS_DIR
    
    try:
        # Check users file
        if USERS_DATA_FILE.exists():
            df = pd.read_csv(USERS_DATA_FILE)
            print(f"  ✅ Users file: {len(df)} users")
            
            # Check for required columns
            required_cols = ['username', 'password_hash', 'email', 'role']
            missing = [col for col in required_cols if col not in df.columns]
            if missing:
                print(f"  ❌ Missing columns: {missing}")
            else:
                print(f"  ✅ All required columns present")
        else:
            print(f"  ❌ Users file not found")
        
        # Check user data files
        user_files = list(USERS_DIR.glob("*_data.csv"))
        print(f"  ✅ User data files: {len(user_files)}")
        
        for user_file in user_files[:3]:  # Check first 3
            try:
                df = pd.read_csv(user_file)
                print(f"    {user_file.name}: {len(df)} entries")
            except Exception as e:
                print(f"    ❌ Error reading {user_file.name}: {e}")
        
    except Exception as e:
        print(f"  ❌ ERROR checking data integrity: {e}")
        import traceback
        traceback.print_exc()


def run_all_tests():
    """Run all automated tests"""
    print("=" * 60)
    print("  🧪 Running Automated Tests")
    print("=" * 60)
    
    test_user_authentication()
    test_tracker_data_retrieval()
    test_tracker_definitions()
    test_validators()
    test_statistics_calculator()
    test_date_time_helper()
    test_data_integrity()
    
    print()
    print("=" * 60)
    print("  🏁 Tests Complete!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
