"""
Utility Functions for Habit Tracker Application
- Password hashing and verification
- Validation functions
- Date/time helpers
- Statistics calculations
"""
import bcrypt
import re
import validators
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Tuple
import pytz
from config import VALIDATION


class PasswordHasher:
    """Handle password hashing and verification using bcrypt"""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password using bcrypt"""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """Verify a password against its hash"""
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
        except Exception:
            return False


class Validators:
    """Validation functions for user inputs"""
    
    @staticmethod
    def validate_username(username: str) -> Tuple[bool, str]:
        """Validate username format"""
        if not username:
            return False, "Username cannot be empty"
        
        if len(username) < VALIDATION["username"]["min_length"]:
            return False, f"Username must be at least {VALIDATION['username']['min_length']} characters"
        
        if len(username) > VALIDATION["username"]["max_length"]:
            return False, f"Username must be at most {VALIDATION['username']['max_length']} characters"
        
        if not re.match(VALIDATION["username"]["pattern"], username):
            return False, "Username can only contain letters and numbers"
        
        return True, "Username is valid"
    
    @staticmethod
    def validate_password(password: str) -> Tuple[bool, str, str]:
        """Validate password and return strength"""
        if not password:
            return False, "Password cannot be empty", "weak"
        
        if len(password) < VALIDATION["password"]["min_length"]:
            return False, f"Password must be at least {VALIDATION['password']['min_length']} characters", "weak"
        
        # Calculate strength
        strength = "weak"
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        
        strength_score = sum([has_upper, has_lower, has_digit, has_special])
        
        if len(password) >= 8 and strength_score >= 3:
            strength = "strong"
        elif len(password) >= 6 and strength_score >= 2:
            strength = "medium"
        
        return True, "Password is valid", strength
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """Validate email format"""
        if not email:
            return False, "Email cannot be empty"
        
        if validators.email(email):
            return True, "Email is valid"
        else:
            return False, "Invalid email format"
    
    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, str]:
        """Validate phone number"""
        # Remove spaces, dashes, and parentheses
        clean_phone = re.sub(r'[\s\-\(\)]', '', phone)
        
        # Check if it starts with + for international format
        if clean_phone.startswith('+'):
            clean_phone = clean_phone[1:]
        
        # Check length
        if len(clean_phone) < VALIDATION["phone"]["min_length"]:
            return False, f"Phone number must be at least {VALIDATION['phone']['min_length']} digits"
        
        if len(clean_phone) > VALIDATION["phone"]["max_length"]:
            return False, f"Phone number must be at most {VALIDATION['phone']['max_length']} digits"
        
        # Check if all characters are digits
        if not clean_phone.isdigit():
            return False, "Phone number must contain only digits"
        
        return True, "Phone number is valid"
    
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        """Validate first/last name"""
        if not name:
            return False, "Name cannot be empty"
        
        if len(name) < VALIDATION["name"]["min_length"]:
            return False, f"Name must be at least {VALIDATION['name']['min_length']} characters"
        
        if len(name) > VALIDATION["name"]["max_length"]:
            return False, f"Name must be at most {VALIDATION['name']['max_length']} characters"
        
        if not re.match(VALIDATION["name"]["pattern"], name):
            return False, "Name can only contain letters and spaces"
        
        return True, "Name is valid"
    
    @staticmethod
    def validate_age(date_of_birth: datetime) -> Tuple[bool, str, int]:
        """Validate age from date of birth"""
        today = datetime.now()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        
        if age < VALIDATION["age"]["min"]:
            return False, f"You must be at least {VALIDATION['age']['min']} years old", age
        
        if age > VALIDATION["age"]["max"]:
            return False, "Invalid date of birth", age
        
        return True, "Age is valid", age


class DateTimeHelper:
    """Helper functions for date and time operations"""
    
    @staticmethod
    def get_time_of_day() -> str:
        """Get current time of day (morning, afternoon, evening, night)"""
        hour = datetime.now().hour
        
        if 5 <= hour < 12:
            return "morning"
        elif 12 <= hour < 17:
            return "afternoon"
        elif 17 <= hour < 21:
            return "evening"
        else:
            return "night"
    
    @staticmethod
    def format_date(date: datetime, format_str: str = "%B %d, %Y") -> str:
        """Format a datetime object to string"""
        return date.strftime(format_str)
    
    @staticmethod
    def get_day_name(date: datetime) -> str:
        """Get day name from date"""
        return date.strftime("%A")
    
    @staticmethod
    def calculate_age(date_of_birth: datetime) -> int:
        """Calculate age from date of birth"""
        today = datetime.now()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        return age
    
    @staticmethod
    def get_date_range(range_type: str) -> Tuple[datetime, datetime]:
        """Get start and end dates for different ranges"""
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        if range_type == "today":
            return today, today
        elif range_type == "week":
            # Start from Monday
            start = today - timedelta(days=today.weekday())
            end = start + timedelta(days=6)
            return start, end
        elif range_type == "month":
            start = today.replace(day=1)
            # Last day of month
            if today.month == 12:
                end = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
            else:
                end = today.replace(month=today.month + 1, day=1) - timedelta(days=1)
            return start, end
        elif range_type == "year":
            start = today.replace(month=1, day=1)
            end = today.replace(month=12, day=31)
            return start, end
        else:
            return today, today
    
    @staticmethod
    def get_days_between(start: datetime, end: datetime) -> int:
        """Get number of days between two dates"""
        return (end - start).days + 1
    
    @staticmethod
    def is_in_quiet_hours(start_time: str, end_time: str) -> bool:
        """Check if current time is within quiet hours"""
        now = datetime.now().time()
        start = datetime.strptime(start_time, "%H:%M").time()
        end = datetime.strptime(end_time, "%H:%M").time()
        
        if start <= end:
            return start <= now <= end
        else:
            # Quiet hours span midnight
            return now >= start or now <= end


class StatisticsCalculator:
    """Calculate statistics from tracking data"""
    
    @staticmethod
    def calculate_completion_percentage(actual: float, goal: float) -> float:
        """Calculate completion percentage"""
        if goal == 0:
            return 100.0 if actual > 0 else 0.0
        return min(100.0, (actual / goal) * 100)
    
    @staticmethod
    def calculate_average(values: List[float]) -> float:
        """Calculate average of values"""
        if not values:
            return 0.0
        return sum(values) / len(values)
    
    @staticmethod
    def calculate_streak(dates: List[datetime]) -> int:
        """Calculate current streak from list of dates"""
        if not dates:
            return 0
        
        # Sort dates in descending order
        sorted_dates = sorted(dates, reverse=True)
        
        # Check if today is in the list
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        
        if sorted_dates[0].date() != today and sorted_dates[0].date() != yesterday:
            return 0
        
        # Count consecutive days
        streak = 1
        for i in range(1, len(sorted_dates)):
            expected_date = sorted_dates[i-1].date() - timedelta(days=1)
            if sorted_dates[i].date() == expected_date:
                streak += 1
            else:
                break
        
        return streak
    
    @staticmethod
    def get_progress_category(percentage: float) -> str:
        """Get progress category from percentage"""
        if percentage <= 25:
            return "0-25"
        elif percentage <= 50:
            return "26-50"
        elif percentage <= 75:
            return "51-75"
        elif percentage <= 90:
            return "76-90"
        else:
            return "91-100"
    
    @staticmethod
    def calculate_trend(values: List[float]) -> str:
        """Calculate trend direction from values"""
        if len(values) < 2:
            return "stable"
        
        # Compare first half average with second half average
        mid = len(values) // 2
        first_half_avg = sum(values[:mid]) / mid
        second_half_avg = sum(values[mid:]) / (len(values) - mid)
        
        if second_half_avg > first_half_avg * 1.1:
            return "improving"
        elif second_half_avg < first_half_avg * 0.9:
            return "declining"
        else:
            return "stable"
    
    @staticmethod
    def get_weekly_summary(daily_data: Dict[str, float]) -> Dict:
        """Generate weekly summary from daily data"""
        total = sum(daily_data.values())
        avg = total / len(daily_data) if daily_data else 0
        max_val = max(daily_data.values()) if daily_data else 0
        min_val = min(daily_data.values()) if daily_data else 0
        
        return {
            "total": total,
            "average": avg,
            "max": max_val,
            "min": min_val,
            "days_logged": len(daily_data)
        }


def suggest_alternative_usernames(base_username: str, existing_usernames: List[str]) -> List[str]:
    """Suggest alternative usernames if chosen one is taken"""
    suggestions = []
    existing_lower = [u.lower() for u in existing_usernames]
    
    # Try with numbers at the end
    for i in range(1, 100):
        suggestion = f"{base_username}{i}"
        if suggestion.lower() not in existing_lower and len(suggestion) <= 20:
            suggestions.append(suggestion)
            if len(suggestions) >= 5:
                break
    
    # Try with different number patterns (e.g., 01, 001)
    if len(suggestions) < 5:
        for i in range(1, 100):
            suggestion = f"{base_username}{i:02d}"
            if suggestion.lower() not in existing_lower and len(suggestion) <= 20:
                suggestions.append(suggestion)
                if len(suggestions) >= 5:
                    break
    
    return suggestions[:5]


def format_duration(seconds: int) -> str:
    """Format seconds into human-readable duration"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    
    if hours > 0:
        return f"{hours}h {minutes}m"
    elif minutes > 0:
        return f"{minutes}m"
    else:
        return f"{seconds}s"


def format_number(number: float, decimals: int = 1) -> str:
    """Format number with specific decimal places"""
    return f"{number:.{decimals}f}"
