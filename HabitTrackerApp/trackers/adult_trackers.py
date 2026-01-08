"""
Adult/Professional Role Tracker Definitions
Pre-configured trackers for working adults
"""
from trackers.base_tracker import (
    DurationTracker, CounterTracker, RatingTracker,
    CheckboxTracker, NumericTracker, TimeTracker
)


def get_adult_trackers():
    """Get all pre-configured trackers for adult/professional role"""
    trackers = []
    
    # Work Hours Tracker
    tracker = DurationTracker(
        name="Work Hours",
        goal=8.0,
        description="Track daily work hours with overtime monitoring"
    )
    tracker.icon = "💼"
    tracker.category = "work"
    trackers.append(tracker)
    
    # Skill Development Time
    tracker = DurationTracker(
        name="Learning Time",
        goal=1.0,
        description="Time spent learning new skills or taking courses"
    )
    tracker.icon = "📚"
    tracker.category = "development"
    trackers.append(tracker)
    
    # Exercise/Fitness Tracker
    tracker = DurationTracker(
        name="Exercise",
        goal=1.0,
        description="Gym, yoga, running, or other fitness activities"
    )
    tracker.icon = "💪"
    tracker.category = "fitness"
    trackers.append(tracker)
    
    # Sleep Quality Tracker
    tracker = DurationTracker(
        name="Sleep Duration",
        goal=7.0,
        description="Track sleep hours (6-8 hours recommended)"
    )
    tracker.icon = "💤"
    tracker.category = "health"
    tracker.min_value = 0
    tracker.max_value = 14
    trackers.append(tracker)
    
    # Sleep Quality Rating
    tracker = RatingTracker(
        name="Sleep Quality",
        max_rating=5,
        goal=4,
        description="Rate how well you slept"
    )
    tracker.icon = "🛌"
    tracker.category = "health"
    trackers.append(tracker)
    
    # Water Intake
    tracker = CounterTracker(
        name="Water Intake",
        unit="glasses",
        goal=10,
        description="Stay hydrated (10 glasses daily)"
    )
    tracker.icon = "💧"
    tracker.category = "health"
    trackers.append(tracker)
    
    # Meal Timing
    tracker = CounterTracker(
        name="Meals",
        unit="meals",
        goal=3,
        description="Track breakfast, lunch, and dinner regularity"
    )
    tracker.icon = "🍽️"
    tracker.category = "nutrition"
    trackers.append(tracker)
    
    # Screen Time
    tracker = DurationTracker(
        name="Leisure Screen Time",
        goal=2.0,
        description="Non-work screen time and digital detox"
    )
    tracker.icon = "📱"
    tracker.category = "wellness"
    trackers.append(tracker)
    
    # Financial - Expenses
    tracker = NumericTracker(
        name="Daily Expenses",
        unit="dollars",
        goal=50,
        min_val=0,
        max_val=1000,
        description="Track daily spending"
    )
    tracker.icon = "💰"
    tracker.category = "finance"
    trackers.append(tracker)
    
    # Financial - Savings
    tracker = NumericTracker(
        name="Daily Savings",
        unit="dollars",
        goal=20,
        min_val=0,
        max_val=1000,
        description="Amount saved today"
    )
    tracker.icon = "💵"
    tracker.category = "finance"
    trackers.append(tracker)
    
    # Reading/Learning
    tracker = DurationTracker(
        name="Reading Time",
        goal=0.5,
        description="Books, articles, podcasts, learning content"
    )
    tracker.icon = "📖"
    tracker.category = "growth"
    trackers.append(tracker)
    
    # Social Connections
    tracker = CounterTracker(
        name="Social Interactions",
        unit="calls/meetings",
        goal=2,
        description="Calls to family/friends, social meetups"
    )
    tracker.icon = "📞"
    tracker.category = "social"
    trackers.append(tracker)
    
    # Mood & Stress Level
    tracker = RatingTracker(
        name="Daily Mood",
        max_rating=5,
        goal=4,
        description="Rate your overall mood and emotional state"
    )
    tracker.icon = "😊"
    tracker.category = "mental_health"
    trackers.append(tracker)
    
    # Stress Level
    tracker = RatingTracker(
        name="Stress Level",
        max_rating=5,
        goal=2,
        description="Rate your stress (1=low, 5=high)"
    )
    tracker.icon = "😰"
    tracker.category = "mental_health"
    trackers.append(tracker)
    
    # Self-care Activities
    tracker = DurationTracker(
        name="Self-Care Time",
        goal=0.5,
        description="Meditation, hobbies, relaxation activities"
    )
    tracker.icon = "🧘"
    tracker.category = "wellness"
    trackers.append(tracker)
    
    # Side Projects
    tracker = DurationTracker(
        name="Side Project Time",
        goal=1.0,
        description="Personal projects and growth activities"
    )
    tracker.icon = "🚀"
    tracker.category = "growth"
    trackers.append(tracker)
    
    # Daily Habits
    tracker = CheckboxTracker(
        name="Morning Routine",
        description="Completed morning routine?"
    )
    tracker.icon = "🌅"
    tracker.category = "habits"
    trackers.append(tracker)
    
    tracker = CheckboxTracker(
        name="Evening Routine",
        description="Completed evening routine?"
    )
    tracker.icon = "🌙"
    tracker.category = "habits"
    trackers.append(tracker)
    
    # Alcohol/Junk Food (Bad Habit Tracker)
    tracker = CounterTracker(
        name="Junk Food Avoided",
        unit="times",
        goal=0,
        description="Track avoidance of junk food and bad habits"
    )
    tracker.icon = "🚫"
    tracker.category = "habits"
    trackers.append(tracker)
    
    return trackers
