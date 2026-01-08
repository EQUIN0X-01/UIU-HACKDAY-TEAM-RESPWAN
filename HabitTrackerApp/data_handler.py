"""
Data Handler Module for Habit Tracker Application
- CSV operations for user data
- User management
- Tracker data management
- Data import/export
"""
import pandas as pd
import csv
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any
from config import (
    USERS_DATA_FILE, USERS_DIR, ACHIEVEMENTS_FILE,
    QUOTES_FILE, ACHIEVEMENT_DEFINITIONS
)
from utils import PasswordHasher


class UserDataManager:
    """Manage user data in CSV files"""
    
    def __init__(self):
        """Initialize UserDataManager and create users file if not exists"""
        self._initialize_users_file()
        self._initialize_achievements_file()
        self._initialize_quotes_file()
    
    def _initialize_users_file(self):
        """Create users_data.csv if it doesn't exist"""
        if not USERS_DATA_FILE.exists():
            columns = [
                "username", "password_hash", "first_name", "last_name",
                "email", "phone", "date_of_birth", "role", "gender",
                "created_date", "last_login", "timezone", "preferred_units",
                "notification_enabled", "notification_sound", "quiet_hours_start",
                "quiet_hours_end", "theme", "failed_login_attempts"
            ]
            df = pd.DataFrame(columns=columns)
            df.to_csv(USERS_DATA_FILE, index=False)
    
    def _initialize_achievements_file(self):
        """Create achievements.csv if it doesn't exist"""
        if not ACHIEVEMENTS_FILE.exists():
            achievements_data = []
            for achievement in ACHIEVEMENT_DEFINITIONS:
                achievements_data.append({
                    "achievement_id": achievement["id"],
                    "name": achievement["name"],
                    "description": achievement["desc"],
                    "criteria_type": achievement["criteria"],
                    "criteria_value": achievement["value"],
                    "badge_icon": achievement["icon"],
                    "category": "milestone"
                })
            df = pd.DataFrame(achievements_data)
            df.to_csv(ACHIEVEMENTS_FILE, index=False)
    
    def _initialize_quotes_file(self):
        """Create motivational_quotes.csv if it doesn't exist"""
        if not QUOTES_FILE.exists():
            quotes = [
                {"category": "motivation", "quote": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
                {"category": "motivation", "quote": "Success is the sum of small efforts repeated day in and day out.", "author": "Robert Collier"},
                {"category": "motivation", "quote": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
                {"category": "perseverance", "quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
                {"category": "perseverance", "quote": "A journey of a thousand miles begins with a single step.", "author": "Lao Tzu"},
                {"category": "habit", "quote": "We are what we repeatedly do. Excellence, then, is not an act, but a habit.", "author": "Aristotle"},
                {"category": "habit", "quote": "Good habits are worth being fanatical about.", "author": "John Irving"},
                {"category": "growth", "quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
                {"category": "growth", "quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
            ]
            df = pd.DataFrame(quotes)
            df.to_csv(QUOTES_FILE, index=False)
    
    def username_exists(self, username: str) -> bool:
        """Check if username already exists"""
        try:
            df = pd.read_csv(USERS_DATA_FILE)
            return username.lower() in df['username'].str.lower().values
        except Exception:
            return False
    
    def email_exists(self, email: str) -> bool:
        """Check if email already exists"""
        try:
            df = pd.read_csv(USERS_DATA_FILE)
            return email.lower() in df['email'].str.lower().values
        except Exception:
            return False
    
    def phone_exists(self, phone: str) -> bool:
        """Check if phone number already exists"""
        try:
            df = pd.read_csv(USERS_DATA_FILE)
            return phone in df['phone'].values
        except Exception:
            return False
    
    def get_all_usernames(self) -> List[str]:
        """Get list of all usernames"""
        try:
            df = pd.read_csv(USERS_DATA_FILE)
            return df['username'].tolist()
        except Exception:
            return []
    
    def create_user(self, user_data: Dict[str, Any]) -> bool:
        """Create a new user account"""
        try:
            # Hash password
            password_hash = PasswordHasher.hash_password(user_data['password'])
            
            # Prepare user data
            new_user = {
                "username": user_data['username'].lower(),
                "password_hash": password_hash,
                "first_name": user_data['first_name'],
                "last_name": user_data['last_name'],
                "email": user_data['email'],
                "phone": user_data['phone'],
                "date_of_birth": user_data['date_of_birth'],
                "role": user_data['role'],
                "gender": user_data.get('gender', ''),
                "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "last_login": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "timezone": user_data.get('timezone', 'UTC'),
                "preferred_units": user_data.get('preferred_units', 'metric'),
                "notification_enabled": True,
                "notification_sound": True,
                "quiet_hours_start": "22:00",
                "quiet_hours_end": "07:00",
                "theme": "light",
                "failed_login_attempts": 0
            }
            
            # Add to CSV
            df = pd.read_csv(USERS_DATA_FILE)
            new_df = pd.DataFrame([new_user])
            if df.empty:
                df = new_df
            else:
                df = pd.concat([df, new_df], ignore_index=True)
            df.to_csv(USERS_DATA_FILE, index=False)
            
            # Create user-specific data file
            self._create_user_data_file(user_data['username'].lower())
            self._create_user_reminders_file(user_data['username'].lower())
            self._create_user_achievements_file(user_data['username'].lower())
            
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
    
    def _create_user_data_file(self, username: str):
        """Create individual user data CSV file"""
        user_file = USERS_DIR / f"{username}_data.csv"
        columns = [
            "date", "tracker_type", "tracker_name", "value",
            "goal", "unit", "notes", "completed"
        ]
        df = pd.DataFrame(columns=columns)
        df.to_csv(user_file, index=False)
    
    def _create_user_reminders_file(self, username: str):
        """Create individual user reminders CSV file"""
        reminders_file = USERS_DIR / f"{username}_reminders.csv"
        columns = [
            "reminder_id", "title", "description", "date", "time",
            "recurrence", "category", "priority", "tracker_link", "status"
        ]
        df = pd.DataFrame(columns=columns)
        df.to_csv(reminders_file, index=False)
    
    def _create_user_achievements_file(self, username: str):
        """Create individual user achievements CSV file"""
        achievements_file = USERS_DIR / f"{username}_achievements.csv"
        columns = ["achievement_id", "unlocked_date", "progress", "completed"]
        
        # Initialize with all achievements as not completed
        data = []
        for achievement in ACHIEVEMENT_DEFINITIONS:
            data.append({
                "achievement_id": achievement["id"],
                "unlocked_date": "",
                "progress": 0,
                "completed": "no"
            })
        
        df = pd.DataFrame(data)
        df.to_csv(achievements_file, index=False)
    
    def authenticate_user(self, username: str, password: str) -> Optional[Dict]:
        """Authenticate user and return user data if successful"""
        try:
            df = pd.read_csv(USERS_DATA_FILE)
            user_row = df[df['username'].str.lower() == username.lower()]
            
            if user_row.empty:
                return None
            
            user_data = user_row.iloc[0].to_dict()
            
            # Check if account is locked
            if user_data.get('failed_login_attempts', 0) >= 5:
                return {'error': 'Account locked due to too many failed attempts'}
            
            # Verify password
            if PasswordHasher.verify_password(password, user_data['password_hash']):
                # Reset failed attempts and update last login
                df.loc[df['username'].str.lower() == username.lower(), 'failed_login_attempts'] = 0
                df.loc[df['username'].str.lower() == username.lower(), 'last_login'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                df.to_csv(USERS_DATA_FILE, index=False)
                
                return user_data
            else:
                # Increment failed attempts
                current_attempts = user_data.get('failed_login_attempts', 0)
                df.loc[df['username'].str.lower() == username.lower(), 'failed_login_attempts'] = current_attempts + 1
                df.to_csv(USERS_DATA_FILE, index=False)
                return None
        except Exception as e:
            print(f"Authentication error: {e}")
            return None
    
    def get_user_by_phone(self, phone: str) -> Optional[Dict]:
        """Get user data by phone number"""
        try:
            df = pd.read_csv(USERS_DATA_FILE)
            user_row = df[df['phone'] == phone]
            
            if not user_row.empty:
                return user_row.iloc[0].to_dict()
            return None
        except Exception:
            return None
    
    def update_password(self, username: str, new_password: str) -> bool:
        """Update user password"""
        try:
            df = pd.read_csv(USERS_DATA_FILE)
            password_hash = PasswordHasher.hash_password(new_password)
            
            df.loc[df['username'].str.lower() == username.lower(), 'password_hash'] = password_hash
            df.to_csv(USERS_DATA_FILE, index=False)
            return True
        except Exception:
            return False
    
    def update_user_profile(self, username: str, updates: Dict) -> bool:
        """Update user profile information"""
        try:
            df = pd.read_csv(USERS_DATA_FILE)
            
            for key, value in updates.items():
                if key in df.columns and key != 'password_hash':
                    df.loc[df['username'].str.lower() == username.lower(), key] = value
            
            df.to_csv(USERS_DATA_FILE, index=False)
            return True
        except Exception:
            return False
    
    def get_user_data(self, username: str) -> Optional[Dict]:
        """Get complete user data"""
        try:
            df = pd.read_csv(USERS_DATA_FILE)
            user_row = df[df['username'].str.lower() == username.lower()]
            
            if not user_row.empty:
                return user_row.iloc[0].to_dict()
            return None
        except Exception:
            return None


class TrackerDataManager:
    """Manage tracker data for users"""
    
    def __init__(self, username: str):
        """Initialize TrackerDataManager for specific user"""
        self.username = username.lower()
        self.data_file = USERS_DIR / f"{self.username}_data.csv"
        self.reminders_file = USERS_DIR / f"{self.username}_reminders.csv"
    
    def log_activity(self, activity_data: Dict) -> bool:
        """Log a new activity/tracker entry"""
        try:
            df = pd.read_csv(self.data_file)
            
            new_entry = {
                "date": activity_data.get('date', datetime.now().strftime("%Y-%m-%d")),
                "tracker_type": activity_data['tracker_type'],
                "tracker_name": activity_data['tracker_name'],
                "value": activity_data['value'],
                "goal": activity_data.get('goal', 0),
                "unit": activity_data.get('unit', ''),
                "notes": activity_data.get('notes', ''),
                "completed": activity_data.get('completed', 'no')
            }
            
            new_df = pd.DataFrame([new_entry])
            if df.empty:
                df = new_df
            else:
                df = pd.concat([df, new_df], ignore_index=True)
            df.to_csv(self.data_file, index=False)
            return True
        except Exception as e:
            print(f"Error logging activity: {e}")
            return False
    
    def get_activities_by_date(self, date: str) -> pd.DataFrame:
        """Get all activities for a specific date"""
        try:
            df = pd.read_csv(self.data_file)
            return df[df['date'] == date]
        except Exception:
            return pd.DataFrame()
    
    def get_activities_by_date_range(self, start_date: str, end_date: str) -> pd.DataFrame:
        """Get activities within date range"""
        try:
            df = pd.read_csv(self.data_file)
            df['date'] = pd.to_datetime(df['date'])
            start_dt = pd.to_datetime(start_date)
            end_dt = pd.to_datetime(end_date)
            mask = (df['date'] >= start_dt) & (df['date'] <= end_dt)
            return df[mask]
        except Exception:
            return pd.DataFrame()
    
    def get_tracker_history(self, tracker_name: str, days: int = 30) -> pd.DataFrame:
        """Get history of a specific tracker"""
        try:
            df = pd.read_csv(self.data_file)
            df['date'] = pd.to_datetime(df['date'])
            
            # Get last N days
            end_date = datetime.now()
            start_date = end_date - pd.Timedelta(days=days)
            
            mask = (df['tracker_name'] == tracker_name) & (df['date'] >= start_date)
            return df[mask].sort_values('date')
        except Exception:
            return pd.DataFrame()
    
    def get_all_tracker_names(self) -> List[str]:
        """Get list of all unique tracker names for user"""
        try:
            df = pd.read_csv(self.data_file)
            return df['tracker_name'].unique().tolist()
        except Exception:
            return []
    
    def calculate_streak(self, tracker_name: Optional[str] = None) -> int:
        """Calculate current streak (overall or for specific tracker)"""
        try:
            df = pd.read_csv(self.data_file)
            df['date'] = pd.to_datetime(df['date'])
            
            if tracker_name:
                df = df[df['tracker_name'] == tracker_name]
            
            # Get unique dates with logged activities
            unique_dates = df['date'].dt.date.unique()
            unique_dates = sorted(unique_dates, reverse=True)
            
            if not len(unique_dates):
                return 0
            
            # Check if today or yesterday is in the list
            today = datetime.now().date()
            yesterday = today - pd.Timedelta(days=1).to_pytimedelta()
            
            if unique_dates[0] != today and unique_dates[0] != yesterday:
                return 0
            
            # Count consecutive days
            streak = 1
            for i in range(1, len(unique_dates)):
                expected_date = unique_dates[i-1] - pd.Timedelta(days=1).to_pytimedelta()
                if unique_dates[i] == expected_date:
                    streak += 1
                else:
                    break
            
            return streak
        except Exception:
            return 0
    
    def add_reminder(self, reminder_data: Dict) -> bool:
        """Add a new reminder"""
        try:
            df = pd.read_csv(self.reminders_file)
            
            # Generate reminder ID
            if df.empty:
                reminder_id = 1
            else:
                reminder_id = df['reminder_id'].max() + 1
            
            new_reminder = {
                "reminder_id": reminder_id,
                "title": reminder_data['title'],
                "description": reminder_data.get('description', ''),
                "date": reminder_data['date'],
                "time": reminder_data['time'],
                "recurrence": reminder_data.get('recurrence', 'once'),
                "category": reminder_data.get('category', 'general'),
                "priority": reminder_data.get('priority', 'medium'),
                "tracker_link": reminder_data.get('tracker_link', ''),
                "status": "pending"
            }
            
            new_df = pd.DataFrame([new_reminder])
            if df.empty:
                df = new_df
            else:
                df = pd.concat([df, new_df], ignore_index=True)
            df.to_csv(self.reminders_file, index=False)
            return True
        except Exception as e:
            print(f"Error adding reminder: {e}")
            return False
    
    def get_reminders_for_date(self, date: str) -> pd.DataFrame:
        """Get all reminders for a specific date"""
        try:
            df = pd.read_csv(self.reminders_file)
            return df[df['date'] == date]
        except Exception:
            return pd.DataFrame()
    
    def update_reminder_status(self, reminder_id: int, status: str) -> bool:
        """Update reminder status (pending, completed, dismissed)"""
        try:
            df = pd.read_csv(self.reminders_file)
            df.loc[df['reminder_id'] == reminder_id, 'status'] = status
            df.to_csv(self.reminders_file, index=False)
            return True
        except Exception:
            return False


class DataExporter:
    """Export data in various formats"""
    
    @staticmethod
    def export_to_csv(username: str, output_path: Path) -> bool:
        """Export all user data to CSV"""
        try:
            data_file = USERS_DIR / f"{username}_data.csv"
            df = pd.read_csv(data_file)
            df.to_csv(output_path, index=False)
            return True
        except Exception:
            return False
    
    @staticmethod
    def export_tracker_summary(username: str, tracker_name: str, output_path: Path) -> bool:
        """Export summary of specific tracker"""
        try:
            data_file = USERS_DIR / f"{username}_data.csv"
            df = pd.read_csv(data_file)
            tracker_data = df[df['tracker_name'] == tracker_name]
            tracker_data.to_csv(output_path, index=False)
            return True
        except Exception:
            return False
