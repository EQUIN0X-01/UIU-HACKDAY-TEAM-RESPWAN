# Habit & Lifestyle Tracker - Complete User Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Creating Your Account](#creating-your-account)
3. [Logging In](#logging-in)
4. [Understanding the Dashboard](#understanding-the-dashboard)
5. [Logging Daily Activities](#logging-daily-activities)
6. [Viewing Statistics](#viewing-statistics)
7. [Managing Settings](#managing-settings)
8. [Tracker Types Explained](#tracker-types-explained)
9. [Tips for Success](#tips-for-success)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### First Time Setup

1. **Install the Application**
   - Double-click `install.bat` to automatically install all requirements
   - Wait for the installation to complete (this may take a few minutes)

2. **Launch the Application**
   - Double-click `run.bat` to start the app
   - Or open a terminal and run `python main.py`

3. **Create Your Account**
   - The login page will appear
   - Click "Create New Account" to begin signup

---

## Creating Your Account

The signup process has 3 easy steps:

### Step 1: Personal Information

Fill in your details:
- **First Name**: Your given name (letters only, 2-30 characters)
- **Last Name**: Your family name (letters only, 2-30 characters)
- **Date of Birth**: Format MM/DD/YYYY (must be 13+ years old)
- **Phone Number**: Your phone with country code (e.g., +1 555-0123)
- **Email**: Your email address (must be unique)
- **Password**: Create a strong password (minimum 6 characters)
  - The strength meter shows: Weak ⚠️ | Medium ✓ | Strong ✓✓
  - Recommended: Include uppercase, numbers, and special characters
- **Confirm Password**: Re-enter your password to confirm

**Validation Tips:**
- All fields marked with * are required
- Real-time validation shows errors immediately
- Green checkmarks indicate valid inputs

### Step 2: Choose Username

- **Username Requirements:**
  - 4-20 characters
  - Letters and numbers only (no spaces or special characters)
  - Case insensitive (stored in lowercase)
  - Must be unique

- **Check Availability:**
  - Click "Check" button to verify if username is available
  - ✓ Green = Available
  - ✗ Red = Already taken
  
- **Username Suggestions:**
  - If your username is taken, the app will suggest alternatives
  - Click any suggestion to auto-fill and check again

### Step 3: Select Your Role

Choose the role that best fits you:

#### 📚 Student
**Best for:** High school and college students
**Includes trackers for:**
- Study hours (with subject breakdown)
- Assignments and homework
- Exam preparation
- Sleep cycles
- Reading habits
- Exercise and physical activity
- Screen time monitoring
- Meal regularity
- Budget and savings
- Mood tracking
- Social time
- Extracurricular activities

#### 💼 Adult/Professional
**Best for:** Working adults and professionals
**Includes trackers for:**
- Work hours (with overtime monitoring)
- Skill development and learning
- Exercise and fitness
- Sleep quality
- Water intake and nutrition
- Screen time management
- Financial tracking (expenses, savings)
- Reading and personal growth
- Social connections
- Mood and stress levels
- Self-care activities
- Side projects

#### 👴 Senior Citizen
**Best for:** Elderly individuals and caregivers
**Includes trackers for:**
- Medication schedules (morning, afternoon, evening)
- Vital signs (blood pressure, blood sugar)
- Weight monitoring
- Physical activity (walking, light exercise)
- Sleep patterns
- Hydration and meals
- Social interactions
- Hobbies and leisure
- Memory exercises
- Mood and well-being
- Pain levels
- Doctor appointments

#### ⚙️ Custom
**Best for:** Users who want complete control
**Features:**
- Build your own tracker set from scratch
- Mix and match from all role templates
- Create custom trackers
- Maximum flexibility

**Optional Information:**
- **Gender**: Male, Female, Other, or Prefer not to say
- This is completely optional

---

## Logging In

### Login Page Features

1. **Username**: Enter your username (case insensitive)
2. **Password**: Enter your password
3. **Remember Me**: Check this to stay logged in (optional)
4. **Login Button**: Click to access your account
5. **Forgot Password?**: Click to recover your account
6. **Create New Account**: For new users

### Security Features
- Account locks after 5 failed login attempts
- Passwords are securely hashed (never stored as plain text)
- Session timeout after inactivity

### Password Recovery

If you forgot your password:
1. Click "Forgot Password?" on login page
2. Enter your username
3. Enter your registered phone number for verification
4. Create a new password
5. Confirm the new password
6. Click "Reset Password"

---

## Understanding the Dashboard

The dashboard is your home screen with 4 main sections:

### 1. Top Bar
- **Welcome Message**: Changes based on time of day
  - 🌅 Good Morning (5 AM - 12 PM)
  - ☀️ Good Afternoon (12 PM - 5 PM)
  - 🌆 Good Evening (5 PM - 9 PM)
  - 🌙 Good Night (9 PM - 5 AM)
- **Current Date**: Shows day and date
- **Streak Counter**: 🔥 Shows consecutive days of logging
  - 3 days: "3 days in a row! Building the habit! 🔥"
  - 7 days: "7 days straight! You're on fire! 🔥"
  - 30 days: "30 days! This is now a lifestyle! 🔥🔥🔥"

### 2. Overall Progress Section
- **Progress Bar**: Visual representation of today's completion
  - Color-coded by performance:
    - 🔴 Red (0-25%): "Needs Attention"
    - 🟠 Orange (26-50%): "Getting Started"
    - 🟡 Yellow (51-75%): "Making Progress"
    - 🟢 Light Green (76-90%): "Doing Great"
    - 🟢 Dark Green (91-100%): "Excellent!"

- **Motivational Message**: Dynamic encouragement based on progress
  - Changes to keep you motivated
  - Special messages for streak milestones

### 3. Quick Stats
- Shows summary of today's logged activities
- Displays first 5 trackers with values
- Format: Tracker Name | Current Value / Goal Value Unit

### 4. Your Trackers
- Lists your role-based trackers
- Shows icon, name, and description
- Quick overview of what you can track

### 5. Bottom Navigation Bar
Four main sections accessible from any page:
- **🏠 Dashboard**: Return to home screen
- **➕ Log Activity**: Enter today's data
- **📊 Statistics**: View progress and analytics
- **⚙️ Settings**: Manage profile and preferences

---

## Logging Daily Activities

### Activity Logging Page

Click "➕ Log Activity" to open the data entry form.

### Page Header
- Shows current date: "Log Today's Activities - [Date]"
- Scrollable form with all your trackers

### Input Forms by Tracker Type

#### 1. Duration/Counter/Numeric Trackers
**Examples**: Study Hours, Water Intake, Weight

**How to use:**
- See tracker name with icon (e.g., 📚 Study Hours)
- Read the description below
- Enter value in the input box
- Unit is displayed next to input
- Goal reminder shown: "Goal: X units"

**Tips:**
- Enter decimal values for hours (e.g., 2.5 for 2 hours 30 minutes)
- Leave blank if you don't want to log that tracker today

#### 2. Checkbox Trackers
**Examples**: Made Bed, Took Medication, Morning Routine

**How to use:**
- Check the box if completed
- Uncheck if not done
- Simple yes/no tracking

#### 3. Rating Trackers
**Examples**: Daily Mood, Sleep Quality, Stress Level

**How to use:**
- Select a radio button for your rating
- Usually 1-5 stars (⭐)
- 1 = Lowest, 5 = Highest
- Choose the number that best represents your experience

### Saving Your Data

1. **Fill in as many trackers as you want**
   - You don't need to fill all of them
   - Only filled trackers will be saved

2. **Click "Save All Activities"**
   - Green button at bottom of page
   - Saves all entered values at once

3. **Success Confirmation**
   - Shows how many activities were saved
   - Automatically returns to dashboard
   - Dashboard updates with your new data

### Best Practices
- ✅ Log activities at the same time each day
- ✅ Be honest with your entries
- ✅ It's okay to miss a day - just resume tomorrow
- ✅ Review your progress weekly
- ❌ Don't worry about perfect scores
- ❌ Don't enter fake data to boost stats

---

## Viewing Statistics

Click "📊 Statistics" to view your progress analytics.

### 7-Day Summary

**Displays:**
- Total activities logged in last 7 days
- Number of completed goals
- Overall completion rate (percentage)

**Interpretation:**
- **High completion rate (80%+)**: Excellent consistency! 🏆
- **Medium completion rate (50-79%)**: Good progress, keep going! ⭐
- **Low completion rate (<50%)**: Room for improvement 💪

### Understanding Your Data

**Total Activities**: Count of all tracker entries
- Higher numbers = more consistent tracking

**Completed Goals**: How many times you met or exceeded your targets
- This is what matters most!

**Completion Rate**: Percentage of goals achieved
- Your success metric
- Track this over time to see improvement

---

## Managing Settings

Click "⚙️ Settings" to access configuration options.

### Profile Information
View your account details:
- Full name
- Username
- Email address
- Role

*Note: To edit profile info, contact support or create a new account*

### Appearance Settings

**Theme Selection:**
- **Light Mode**: Default, easier on eyes in bright environments
- **Dark Mode**: Easier on eyes in low-light conditions
- Click a radio button to switch immediately
- Setting is saved automatically

### Logout

**To logout:**
1. Click "🚪 Logout" button (red button at bottom)
2. Confirm you want to logout
3. Returns to login screen

**Security Note:** Always logout when using shared computers

---

## Tracker Types Explained

### Duration Trackers ⏱️
**Purpose**: Track time spent on activities
**Unit**: Hours (can use decimals)
**Examples**: 
- Study Hours: 2.5 (2 hours 30 minutes)
- Exercise Time: 1.0 (1 hour)
- Work Hours: 8.5 (8 hours 30 minutes)

**How goals work:**
- Set target hours per day
- Green if you meet or exceed goal
- Yellow if you're 50-99% of goal
- Red if below 50%

### Counter Trackers 🔢
**Purpose**: Count discrete items
**Unit**: Various (glasses, pages, meals, etc.)
**Examples**:
- Water Intake: 8 (8 glasses)
- Reading Pages: 25 (25 pages)
- Meals: 3 (3 meals)

**How goals work:**
- Set target count per day
- Simple comparison: did you hit the number?

### Rating Trackers ⭐
**Purpose**: Rate quality or intensity on a scale
**Unit**: Stars or numbers (1-5 or 1-10)
**Examples**:
- Daily Mood: 4/5 (Good mood)
- Sleep Quality: 3/5 (Average sleep)
- Stress Level: 2/5 (Low stress)

**Interpretation:**
- Higher numbers = better (for mood, quality)
- Lower numbers = better (for stress, pain)
- Check tracker description for direction

### Checkbox Trackers ✅
**Purpose**: Simple yes/no completion
**Unit**: Boolean (true/false)
**Examples**:
- Made Bed: Checked = Yes
- Took Medication: Unchecked = No
- Morning Routine: Checked = Complete

**How goals work:**
- Goal is always to check the box
- Completion = 100% if checked, 0% if not

### Numeric Trackers 📊
**Purpose**: Track measurements and values
**Unit**: Various (kg, mmHg, dollars, etc.)
**Examples**:
- Weight: 72.5 kg
- Blood Pressure: 120/80 mmHg
- Daily Expenses: $25.00

**How goals work:**
- Can be target value (e.g., maintain 70kg)
- Can be threshold (e.g., keep under $50)
- Direction depends on tracker

---

## Tips for Success

### Building the Habit

1. **Start Small**
   - Don't try to track everything at once
   - Begin with 3-5 most important trackers
   - Add more as habit forms

2. **Log at Same Time Daily**
   - Morning: Log previous day before starting your day
   - Evening: Log before bed as part of night routine
   - Consistency creates habit

3. **Be Patient**
   - Takes 21 days to form a habit
   - Don't get discouraged by missed days
   - Focus on weekly trends, not daily perfection

### Maximizing Results

4. **Set Realistic Goals**
   - Goals should challenge you but be achievable
   - 80% success rate is excellent
   - Adjust goals if consistently too easy or too hard

5. **Review Weekly**
   - Check statistics every Sunday
   - Identify patterns and trends
   - Celebrate wins, learn from struggles

6. **Use Streaks Wisely**
   - Streaks are motivating but not everything
   - Breaking a streak doesn't erase progress
   - Focus on long-term consistency

### Staying Motivated

7. **Read Motivational Messages**
   - Dashboard shows progress-based encouragement
   - Let these keep you inspired

8. **Track What Matters to You**
   - Only log what you actually care about
   - Remove trackers that don't serve your goals
   - Quality over quantity

9. **Celebrate Milestones**
   - 7-day streak
   - 30-day streak
   - 90% completion week
   - Personal bests

---

## Troubleshooting

### Common Issues

#### "Username already taken"
**Solution**: Choose a different username or try suggestions

#### "Password too weak"
**Solution**: Add uppercase letters, numbers, or special characters

#### "Account locked"
**Cause**: 5 failed login attempts
**Solution**: Use password recovery or wait 1 hour

#### "No data available in statistics"
**Cause**: Haven't logged any activities yet
**Solution**: Go to Log Activity and enter some data

#### Application won't start
**Causes:**
- Python not installed
- Dependencies not installed
- Wrong Python version

**Solutions:**
1. Check Python: `python --version` (need 3.8+)
2. Reinstall dependencies: Run `install.bat`
3. Manual install: `pip install -r requirements.txt`

#### Data not saving
**Possible causes:**
- File permissions issue
- CSV files open in another program
- Disk full

**Solutions:**
1. Close Excel/spreadsheet programs
2. Check disk space
3. Run application as administrator

### Getting Help

**Before asking for help:**
1. Check this guide thoroughly
2. Try restarting the application
3. Check README.md for technical details

**When reporting issues:**
- Describe what you were doing
- Include any error messages
- Mention your operating system
- State Python version

---

## Frequently Asked Questions

### General

**Q: Is my data safe?**
A: Yes! All data is stored locally on your computer in the `data/` folder. Nothing is sent to the internet.

**Q: Can I use this offline?**
A: Yes! The application works completely offline.

**Q: Can I access my data on multiple computers?**
A: Not automatically. You would need to manually copy the `data/` folder.

### Data Management

**Q: How do I backup my data?**
A: Copy the entire `HabitTrackerApp/data/` folder to a safe location (USB drive, cloud storage).

**Q: How do I restore from backup?**
A: Replace the `data/` folder with your backed-up copy.

**Q: Can I edit my old entries?**
A: Currently no. You can only add new entries. This ensures data integrity.

**Q: Can I delete activities?**
A: Not from the UI currently. Advanced users can edit CSV files directly.

### Trackers

**Q: Can I add custom trackers?**
A: In the current MVP version, you're limited to role-based trackers. Custom tracker builder is planned for future updates.

**Q: Can I change my role?**
A: Not currently. You would need to create a new account. Choose carefully during signup!

**Q: How many trackers should I use?**
A: Start with 5-10. More than 15 can become overwhelming.

### Progress

**Q: What's a good completion rate?**
A: 70-80% is excellent! Perfect 100% isn't necessary and can cause stress.

**Q: My streak broke, should I start over?**
A: No! Your historical data remains. Just start a new streak. Consistency matters more than streaks.

**Q: How long until I see results?**
A: Most people see behavior changes in 3-4 weeks of consistent tracking.

---

## Keyboard Shortcuts

- `Tab`: Move between input fields
- `Enter`: Submit/Confirm (on login page)
- `Esc`: Cancel/Close dialogs

---

## Data Privacy

### What data is collected?
- Personal info (name, email, phone, DOB)
- Activity tracking data
- User preferences

### Where is data stored?
- Locally on your computer
- In CSV files in `data/` folder
- Never sent to external servers

### Who can access my data?
- Only you (and anyone with physical access to your computer)
- No cloud sync means complete privacy

---

## Future Features (Planned)

- 📊 Advanced charts and graphs
- 📅 Calendar view of activities
- 🔔 Desktop reminder notifications
- 🏆 Achievement badges and gamification
- 📤 Export to PDF reports
- 🤖 AI insights and pattern detection
- ⚙️ Custom tracker builder
- 📱 Mobile version (long-term)

---

## Credits

**Application**: Habit & Lifestyle Tracker  
**Version**: 1.0.0 (MVP)  
**Framework**: CustomTkinter + Python  
**Design**: Material Design 3 inspired  

---

**🎯 Remember: Progress over perfection. Every entry counts!**
