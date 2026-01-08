"""
Configuration Constants for Habit Tracker Application
"""
import os
from pathlib import Path

# Application Info
APP_NAME = "KISEKI"
APP_VERSION = "1.0.0"
APP_TAGLINE = "Track your habits, Transform your life"

# Paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
USERS_DIR = DATA_DIR / "users"
ASSETS_DIR = BASE_DIR / "assets"
LOGS_DIR = BASE_DIR / "logs"

# Ensure directories exist
for directory in [DATA_DIR, USERS_DIR, ASSETS_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Database Files
USERS_DATA_FILE = DATA_DIR / "users_data.csv"
ACHIEVEMENTS_FILE = DATA_DIR / "achievements.csv"
QUOTES_FILE = DATA_DIR / "motivational_quotes.csv"
SYSTEM_CONFIG_FILE = DATA_DIR / "system_config.csv"

# User Roles
ROLES = {
    "student": "Student",
    "adult": "Adult/Professional",
    "senior": "Senior Citizen",
    "custom": "Custom"
}

# Role Emojis
ROLE_EMOJIS = {
    "student": "📚",
    "adult": "💼",
    "senior": "👴",
    "custom": "⚙️"
}

# Colors (Material Design)
COLORS = {
    "primary": {
        "student": "#2196F3",  # Blue
        "adult": "#4CAF50",    # Green
        "senior": "#9C27B0",   # Purple
        "custom": "#FF9800"    # Orange
    },
    "success": "#4CAF50",
    "warning": "#FFC107",
    "error": "#F44336",
    "info": "#2196F3",
    "text_dark": "#212121",
    "text_light": "#757575",
    "background": "#FAFAFA"
}

# Time of Day Greetings
GREETINGS = {
    "morning": "Good Morning",
    "afternoon": "Good Afternoon",
    "evening": "Good Evening",
    "night": "Good Night"
}

# Time Emojis
TIME_EMOJIS = {
    "morning": "🌅",
    "afternoon": "☀️",
    "evening": "🌆",
    "night": "🌙"
}

# Validation Rules
VALIDATION = {
    "username": {
        "min_length": 4,
        "max_length": 20,
        "pattern": r"^[a-zA-Z0-9]+$"
    },
    "password": {
        "min_length": 6,
        "max_length": 128
    },
    "name": {
        "min_length": 2,
        "max_length": 30,
        "pattern": r"^[a-zA-Z\s]+$"
    },
    "phone": {
        "min_length": 10,
        "max_length": 15
    },
    "age": {
        "min": 13,
        "max": 120
    }
}

# Window Settings
WINDOW_SIZE = "1200x800"
MIN_WINDOW_SIZE = (1000, 600)

# Session Settings
SESSION_TIMEOUT = 3600  # 1 hour in seconds
MAX_LOGIN_ATTEMPTS = 5

# Chart Settings
CHART_COLORS = [
    "#2196F3", "#4CAF50", "#FF9800", "#9C27B0",
    "#F44336", "#00BCD4", "#FFEB3B", "#795548"
]

# Motivational Messages by Progress Level
MOTIVATIONAL_MESSAGES = {
    "0-25": [
        "Every journey starts with a single step. You've got this! 💪",
        "Small steps lead to big changes. Keep going! 🌟",
        "Progress takes time. Be patient with yourself! 🌱"
    ],
    "26-50": [
        "You're building momentum! Keep going! 🚀",
        "Halfway there! Don't stop now! 💪",
        "Great start! You're on the right track! ⭐"
    ],
    "51-75": [
        "Great progress! You're more than halfway there! ⭐",
        "You're doing amazing! Keep pushing! 🎯",
        "Fantastic work! The finish line is in sight! 🏃"
    ],
    "76-90": [
        "Amazing work! You're crushing your goals! 🎯",
        "Outstanding effort! You're almost there! 🏆",
        "Incredible progress! Keep it up! 🌟"
    ],
    "91-100": [
        "Outstanding! You're absolutely killing it! 🏆",
        "Perfect! You're a habit champion! 👑",
        "Phenomenal! You've mastered your goals! ⭐"
    ]
}

# Streak Messages
STREAK_MESSAGES = {
    3: "3 days in a row! Building the habit! 🔥",
    7: "7 days straight! You're on fire! 🔥",
    14: "2 weeks! Amazing consistency! 🔥🔥",
    30: "30 days! This is now a lifestyle! 🔥🔥🔥",
    100: "100 days! You're unstoppable! 🏆"
}

# Achievement Definitions
ACHIEVEMENT_DEFINITIONS = [
    {"id": 1, "name": "First Steps", "desc": "Log your first activity", "criteria": "first_log", "value": 1, "icon": "🎯"},
    {"id": 2, "name": "3-Day Streak", "desc": "Log for 3 consecutive days", "criteria": "streak", "value": 3, "icon": "🔥"},
    {"id": 3, "name": "Week Warrior", "desc": "Complete 7 days in a row", "criteria": "streak", "value": 7, "icon": "⚡"},
    {"id": 4, "name": "Perfect Day", "desc": "Achieve 100% of daily goals", "criteria": "daily_completion", "value": 100, "icon": "⭐"},
    {"id": 5, "name": "Century Club", "desc": "Log 100 total hours", "criteria": "cumulative_hours", "value": 100, "icon": "💯"},
    {"id": 6, "name": "Consistency King", "desc": "30-day streak", "criteria": "streak", "value": 30, "icon": "👑"},
    {"id": 7, "name": "Dedication", "desc": "Use app for 90 days", "criteria": "days_active", "value": 90, "icon": "🎖️"},
    {"id": 8, "name": "Legend", "desc": "100-day streak", "criteria": "streak", "value": 100, "icon": "🏆"}
]

# Default Notification Settings
DEFAULT_NOTIFICATION_SETTINGS = {
    "enabled": True,
    "sound": True,
    "quiet_hours_start": "22:00",
    "quiet_hours_end": "07:00",
    "reminder_advance": 15,  # minutes
    "snooze_duration": 10    # minutes
}

# Theme Settings
THEMES = {
    "light": {
        "bg_color": "#FAFAFA",
        "fg_color": "#212121",
        "button_color": "#2196F3",
        "button_hover": "#1976D2"
    },
    "dark": {
        "bg_color": "#212121",
        "fg_color": "#FAFAFA",
        "button_color": "#2196F3",
        "button_hover": "#1976D2"
    }
}
