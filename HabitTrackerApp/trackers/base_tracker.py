"""
Base Tracker Class
All specific trackers inherit from this base class
"""
from typing import Dict, Any, Optional
from datetime import datetime


class BaseTracker:
    """Base class for all tracker types"""
    
    def __init__(self, name: str, tracker_type: str, unit: str, goal: float = 0, description: str = ""):
        """
        Initialize base tracker
        
        Args:
            name: Tracker name (e.g., "Study Hours")
            tracker_type: Type (duration, counter, rating, checkbox, numeric, time)
            unit: Unit of measurement (hours, glasses, stars, etc.)
            goal: Default goal value
            description: Brief description of tracker
        """
        self.name = name
        self.tracker_type = tracker_type
        self.unit = unit
        self.goal = goal
        self.description = description
        self.icon = ""
        self.category = ""
        self.customizable = True
        self.min_value = 0
        self.max_value = 100
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert tracker to dictionary"""
        return {
            "name": self.name,
            "tracker_type": self.tracker_type,
            "unit": self.unit,
            "goal": self.goal,
            "description": self.description,
            "icon": self.icon,
            "category": self.category,
            "customizable": self.customizable,
            "min_value": self.min_value,
            "max_value": self.max_value
        }
    
    def validate_value(self, value: Any) -> bool:
        """Validate if a value is acceptable for this tracker"""
        try:
            num_value = float(value)
            return self.min_value <= num_value <= self.max_value
        except:
            return False


class DurationTracker(BaseTracker):
    """Tracker for time duration (hours, minutes)"""
    
    def __init__(self, name: str, goal: float = 0, description: str = ""):
        super().__init__(name, "duration", "hours", goal, description)
        self.min_value = 0
        self.max_value = 24


class CounterTracker(BaseTracker):
    """Tracker for counting items (glasses, meals, etc.)"""
    
    def __init__(self, name: str, unit: str, goal: float = 0, description: str = ""):
        super().__init__(name, "counter", unit, goal, description)
        self.min_value = 0
        self.max_value = 50


class RatingTracker(BaseTracker):
    """Tracker for rating/scale (1-5 stars, 1-10 scale)"""
    
    def __init__(self, name: str, max_rating: int = 5, goal: float = 5, description: str = ""):
        super().__init__(name, "rating", "stars", goal, description)
        self.min_value = 1
        self.max_value = max_rating


class CheckboxTracker(BaseTracker):
    """Tracker for yes/no or completed/not completed"""
    
    def __init__(self, name: str, description: str = ""):
        super().__init__(name, "checkbox", "boolean", 1, description)
        self.min_value = 0
        self.max_value = 1


class NumericTracker(BaseTracker):
    """Tracker for numeric values (weight, blood pressure, etc.)"""
    
    def __init__(self, name: str, unit: str, goal: float = 0, min_val: float = 0, max_val: float = 1000, description: str = ""):
        super().__init__(name, "numeric", unit, goal, description)
        self.min_value = min_val
        self.max_value = max_val


class TimeTracker(BaseTracker):
    """Tracker for specific times (bedtime, meal time)"""
    
    def __init__(self, name: str, description: str = ""):
        super().__init__(name, "time", "HH:MM", 0, description)
