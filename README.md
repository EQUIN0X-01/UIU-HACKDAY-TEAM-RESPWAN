# Habit & Lifestyle Tracker Application

A comprehensive desktop application for tracking habits, health, and lifestyle activities with role-based customization for Students, Adults/Professionals, and Senior Citizens.

## Features

### ✨ Core Features (MVP)
- **User Authentication**
  - Secure login/signup system
  - Password recovery
  - User profile management
  
- **Role-Based Trackers**
  - **Student**: Study hours, assignments, sleep, reading, exercise, mood, etc.
  - **Adult/Professional**: Work hours, fitness, sleep quality, finances, stress, self-care, etc.
  - **Senior Citizen**: Medication, vital signs, physical activity, social interactions, etc.
  - **Custom**: Build your own personalized trackers

- **Dashboard**
  - Welcome message with time-based greetings
  - Overall progress visualization
  - Streak tracking
  - Quick stats overview
  - Motivational messages

- **Activity Logging**
  - Easy-to-use forms for all tracker types
  - Duration trackers (hours/minutes)
  - Counter trackers (glasses, meals, etc.)
  - Rating trackers (mood, quality ratings)
  - Checkbox trackers (yes/no completion)
  - Numeric trackers (weight, blood pressure, expenses)

- **Statistics**
  - 7-day activity summary
  - Completion rates
  - Historical data views

- **Settings**
  - Profile management
  - Theme customization (Light/Dark mode)
  - Logout functionality

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python main.py
   ```

## Project Structure

```
HabitTrackerApp/
├── main.py                  # Application entry point
├── auth.py                  # Authentication & signup pages
├── app_core.py              # Main application & dashboard
├── data_handler.py          # CSV data management
├── utils.py                 # Utility functions
├── config.py                # Configuration constants
├── requirements.txt         # Python dependencies
├── trackers/                # Tracker definitions
│   ├── base_tracker.py
│   ├── student_trackers.py
│   ├── adult_trackers.py
│   └── senior_trackers.py
├── data/                    # Data storage
│   ├── users_data.csv       # All user accounts
│   ├── achievements.csv     # Achievement definitions
│   ├── motivational_quotes.csv
│   └── users/               # Individual user data
│       ├── username_data.csv
│       ├── username_reminders.csv
│       └── username_achievements.csv
├── assets/                  # Application resources
└── logs/                    # Application logs
```

## Usage Guide

### Creating an Account

1. Click "Create New Account" on the login page
2. **Step 1**: Enter personal information
   - First and last name
   - Date of birth (must be 13+)
   - Phone number
   - Email address
   - Password (min 6 characters)
3. **Step 2**: Choose a unique username
4. **Step 3**: Select your role
   - Student 📚
   - Adult/Professional 💼
   - Senior Citizen 👴
   - Custom ⚙️

### Logging Activities

1. Click "➕ Log Activity" in the bottom navigation
2. Fill in values for your trackers
3. Click "Save All Activities"

### Viewing Statistics

1. Click "📊 Statistics" to view:
   - 7-day activity summary
   - Completion rates
   - Progress trends

### Managing Settings

1. Click "⚙️ Settings" to:
   - View profile information
   - Change theme (Light/Dark)
   - Logout

## Tracker Types

### Duration Trackers
- Track time spent (hours/minutes)
- Examples: Study hours, exercise time, work hours

### Counter Trackers
- Count discrete items
- Examples: Water glasses, meals, social interactions

### Rating Trackers
- Rate on a scale (1-5 stars, 1-10 scale)
- Examples: Mood, sleep quality, stress level

### Checkbox Trackers
- Simple yes/no completion
- Examples: Made bed, took medication, morning routine

### Numeric Trackers
- Track numeric values
- Examples: Weight, blood pressure, daily expenses

## Role-Specific Trackers

### Student Trackers 📚
- Study Hours
- Assignments Completed
- Sleep Duration
- Screen Time
- Reading Pages
- Exercise Time
- Water Intake
- Meals
- Daily Expenses
- Daily Mood
- Social Time
- Extracurricular Activities

### Adult/Professional Trackers 💼
- Work Hours
- Learning Time
- Exercise
- Sleep Duration & Quality
- Water Intake
- Meals
- Screen Time
- Daily Expenses
- Daily Savings
- Reading Time
- Social Interactions
- Mood & Stress Level
- Self-Care Time
- Side Project Time

### Senior Citizen Trackers 👴
- Medication (Morning, Afternoon, Evening)
- Blood Pressure (Systolic, Diastolic)
- Blood Sugar
- Weight
- Walking Time
- Light Exercise
- Sleep Duration & Quality
- Water Intake
- Meals
- Social Contacts
- Hobby Time
- Mental Exercise
- Daily Mood
- Pain Level

## Data Storage

All data is stored locally in CSV files:
- **Security**: Passwords are hashed using bcrypt
- **Privacy**: All data stays on your local machine
- **Backup**: Simply copy the `data/` folder

## Customization

### Changing Goals
Edit tracker goals by modifying values in the activity logging page.

### Adding Custom Trackers
Choose "Custom" role during signup to build your own tracker set.

## Troubleshooting

### Application won't start
- Ensure Python 3.8+ is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`

### Login issues
- Check username/password are correct
- Account locked after 5 failed attempts (contact support)

### Data not saving
- Check file permissions in `data/` directory
- Ensure CSV files are not open in another program

## Development Status

This is an MVP (Minimum Viable Product) version with core features implemented.

### Implemented ✅
- User authentication system
- Role-based tracker templates
- Activity logging
- Basic dashboard
- Settings page
- CSV data storage

### Planned Features 🚀
- Advanced data visualizations (charts, graphs)
- Reminder system with notifications
- Achievement and gamification system
- Data export (PDF reports)
- Advanced analytics and insights
- Custom tracker builder
- Goal customization
- Calendar views

## Technical Stack

- **GUI Framework**: CustomTkinter (modern, Material Design-style)
- **Data Handling**: Pandas, CSV
- **Security**: bcrypt password hashing
- **Visualization**: Matplotlib, Seaborn (planned)
- **Date/Time**: python-dateutil, pytz

## Contributing

This is a personal project. For bug reports or feature suggestions, please document them clearly.

## License

Personal use project. All rights reserved.

## Version

**Version**: 1.0.0 (MVP)  
**Last Updated**: January 2026

## Author

Developed as a comprehensive habit tracking solution with focus on role-based customization and user experience.

---

**🎯 Track your habits, Transform your life!**
