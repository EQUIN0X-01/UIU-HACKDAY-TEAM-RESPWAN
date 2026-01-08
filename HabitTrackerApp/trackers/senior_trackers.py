"""
Senior Citizen Role Tracker Definitions
Pre-configured trackers for senior citizens
"""
from trackers.base_tracker import (
    DurationTracker, CounterTracker, RatingTracker,
    CheckboxTracker, NumericTracker, TimeTracker
)


def get_senior_trackers():
    """Get all pre-configured trackers for senior citizen role"""
    trackers = []
    
    # Medication Tracker - Morning
    tracker = CheckboxTracker(
        name="Morning Medication",
        description="Took morning medicines?"
    )
    tracker.icon = "💊"
    tracker.category = "medication"
    trackers.append(tracker)
    
    # Medication Tracker - Afternoon
    tracker = CheckboxTracker(
        name="Afternoon Medication",
        description="Took afternoon medicines?"
    )
    tracker.icon = "💊"
    tracker.category = "medication"
    trackers.append(tracker)
    
    # Medication Tracker - Evening
    tracker = CheckboxTracker(
        name="Evening Medication",
        description="Took evening medicines?"
    )
    tracker.icon = "💊"
    tracker.category = "medication"
    trackers.append(tracker)
    
    # Blood Pressure - Systolic
    tracker = NumericTracker(
        name="Blood Pressure (Systolic)",
        unit="mmHg",
        goal=120,
        min_val=80,
        max_val=200,
        description="Track systolic blood pressure reading"
    )
    tracker.icon = "❤️"
    tracker.category = "vitals"
    trackers.append(tracker)
    
    # Blood Pressure - Diastolic
    tracker = NumericTracker(
        name="Blood Pressure (Diastolic)",
        unit="mmHg",
        goal=80,
        min_val=50,
        max_val=130,
        description="Track diastolic blood pressure reading"
    )
    tracker.icon = "❤️"
    tracker.category = "vitals"
    trackers.append(tracker)
    
    # Blood Sugar Level
    tracker = NumericTracker(
        name="Blood Sugar",
        unit="mg/dL",
        goal=100,
        min_val=50,
        max_val=400,
        description="Track blood glucose levels"
    )
    tracker.icon = "🩸"
    tracker.category = "vitals"
    trackers.append(tracker)
    
    # Weight Tracker
    tracker = NumericTracker(
        name="Weight",
        unit="kg",
        goal=70,
        min_val=30,
        max_val=200,
        description="Weekly weight monitoring"
    )
    tracker.icon = "⚖️"
    tracker.category = "vitals"
    trackers.append(tracker)
    
    # Physical Activity
    tracker = DurationTracker(
        name="Walking Time",
        goal=0.5,
        description="Daily walking and light exercise"
    )
    tracker.icon = "🚶"
    tracker.category = "activity"
    trackers.append(tracker)
    
    # Exercise Duration
    tracker = DurationTracker(
        name="Light Exercise",
        goal=0.25,
        description="Stretching, chair exercises, light movement"
    )
    tracker.icon = "🧘"
    tracker.category = "activity"
    trackers.append(tracker)
    
    # Sleep Pattern
    tracker = DurationTracker(
        name="Sleep Duration",
        goal=7.0,
        description="Track hours of sleep"
    )
    tracker.icon = "💤"
    tracker.category = "health"
    tracker.min_value = 0
    tracker.max_value = 14
    trackers.append(tracker)
    
    # Sleep Quality
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
        goal=8,
        description="Track daily water consumption"
    )
    tracker.icon = "💧"
    tracker.category = "health"
    trackers.append(tracker)
    
    # Meal Timing
    tracker = CounterTracker(
        name="Meals",
        unit="meals",
        goal=3,
        description="Regular eating schedule tracking"
    )
    tracker.icon = "🍽️"
    tracker.category = "nutrition"
    trackers.append(tracker)
    
    # Social Interactions
    tracker = CounterTracker(
        name="Social Contacts",
        unit="interactions",
        goal=2,
        description="Calls, visits from family and friends"
    )
    tracker.icon = "👥"
    tracker.category = "social"
    trackers.append(tracker)
    
    # Hobby Time
    tracker = DurationTracker(
        name="Hobby Time",
        goal=1.0,
        description="Gardening, reading, crafts, hobbies"
    )
    tracker.icon = "🎨"
    tracker.category = "leisure"
    trackers.append(tracker)
    
    # Memory Exercises
    tracker = DurationTracker(
        name="Mental Exercise",
        goal=0.5,
        description="Puzzles, brain games, memory activities"
    )
    tracker.icon = "🧩"
    tracker.category = "cognitive"
    trackers.append(tracker)
    
    # Mood & Well-being
    tracker = RatingTracker(
        name="Daily Mood",
        max_rating=5,
        goal=4,
        description="Daily emotional check-in"
    )
    tracker.icon = "😊"
    tracker.category = "mental_health"
    trackers.append(tracker)
    
    # Pain/Discomfort Log
    tracker = RatingTracker(
        name="Pain Level",
        max_rating=10,
        goal=2,
        description="Rate pain/discomfort level (1=low, 10=severe)"
    )
    tracker.icon = "😣"
    tracker.category = "health"
    trackers.append(tracker)
    
    # Doctor Appointment Check
    tracker = CheckboxTracker(
        name="Doctor Appointment",
        description="Did you have/attend a doctor appointment?"
    )
    tracker.icon = "👨‍⚕️"
    tracker.category = "healthcare"
    trackers.append(tracker)
    
    return trackers
