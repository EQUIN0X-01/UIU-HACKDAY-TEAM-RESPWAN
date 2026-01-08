"""
Student Role Tracker Definitions
Pre-configured trackers for students
"""
from trackers.base_tracker import (
    DurationTracker, CounterTracker, RatingTracker,
    CheckboxTracker, NumericTracker, TimeTracker
)


def get_student_trackers():
    """Get all pre-configured trackers for student role"""
    trackers = []
    
    # Study Hours Tracker
    tracker = DurationTracker(
        name="Study Hours",
        goal=4.0,
        description="Track daily study time across subjects"
    )
    tracker.icon = "📚"
    tracker.category = "academic"
    trackers.append(tracker)
    
    # Assignment/Homework Tracker
    tracker = CounterTracker(
        name="Assignments Completed",
        unit="assignments",
        goal=3,
        description="Track completed assignments and homework"
    )
    tracker.icon = "📝"
    tracker.category = "academic"
    trackers.append(tracker)
    
    # Sleep Cycle Tracker
    tracker = DurationTracker(
        name="Sleep Duration",
        goal=8.0,
        description="Monitor sleep duration (7-9 hours recommended)"
    )
    tracker.icon = "💤"
    tracker.category = "health"
    tracker.min_value = 0
    tracker.max_value = 14
    trackers.append(tracker)
    
    # Screen Time Monitor
    tracker = DurationTracker(
        name="Screen Time",
        goal=3.0,
        description="Track daily digital device usage"
    )
    tracker.icon = "📱"
    tracker.category = "wellness"
    trackers.append(tracker)
    
    # Reading Tracker
    tracker = CounterTracker(
        name="Reading Pages",
        unit="pages",
        goal=20,
        description="Track pages read daily"
    )
    tracker.icon = "📖"
    tracker.category = "learning"
    trackers.append(tracker)
    
    # Physical Activity
    tracker = DurationTracker(
        name="Exercise Time",
        goal=0.5,
        description="Daily physical activity (30+ minutes)"
    )
    tracker.icon = "🏃"
    tracker.category = "health"
    trackers.append(tracker)
    
    # Water Intake
    tracker = CounterTracker(
        name="Water Intake",
        unit="glasses",
        goal=8,
        description="Track daily water consumption"
    )
    tracker.icon = "💧"
    tracker.category = "health"
    trackers.append(tracker)
    
    # Meal Regularity
    tracker = CounterTracker(
        name="Meals",
        unit="meals",
        goal=3,
        description="Track regular meal consumption"
    )
    tracker.icon = "🍽️"
    tracker.category = "health"
    trackers.append(tracker)
    
    # Savings/Budget Tracker
    tracker = NumericTracker(
        name="Daily Expenses",
        unit="dollars",
        goal=10,
        min_val=0,
        max_val=500,
        description="Track pocket money and expenses"
    )
    tracker.icon = "💰"
    tracker.category = "finance"
    trackers.append(tracker)
    
    # Mood Tracker
    tracker = RatingTracker(
        name="Daily Mood",
        max_rating=5,
        goal=4,
        description="Rate your mood and emotions"
    )
    tracker.icon = "😊"
    tracker.category = "wellness"
    trackers.append(tracker)
    
    # Social Time
    tracker = DurationTracker(
        name="Social Time",
        goal=2.0,
        description="Time spent with friends and social activities"
    )
    tracker.icon = "👥"
    tracker.category = "social"
    trackers.append(tracker)
    
    # Extracurricular Activities
    tracker = DurationTracker(
        name="Extracurricular",
        goal=1.0,
        description="Time in clubs, sports, and hobbies"
    )
    tracker.icon = "⚽"
    tracker.category = "activities"
    trackers.append(tracker)
    
    # Made Bed (Daily Habit)
    tracker = CheckboxTracker(
        name="Made Bed",
        description="Did you make your bed today?"
    )
    tracker.icon = "🛏️"
    tracker.category = "habits"
    trackers.append(tracker)
    
    return trackers
