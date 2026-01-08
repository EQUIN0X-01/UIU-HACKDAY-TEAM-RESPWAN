# 🎯 Habit & Lifestyle Tracker - Installation & Setup Guide

## Welcome!

Thank you for choosing the Habit & Lifestyle Tracker application. This guide will help you get started in just a few minutes.

---

## 📋 Prerequisites

Before installing, ensure you have:

### Required
- **Windows Operating System** (Windows 10 or 11 recommended)
- **Python 3.8 or higher** - [Download from python.org](https://www.python.org/downloads/)
  - ⚠️ During installation, **check "Add Python to PATH"**
- **Internet connection** (for installing packages)
- **At least 100 MB free disk space**

### Optional
- Basic command line knowledge (helpful but not required)

---

## 🚀 Quick Installation (Recommended)

### Step 1: Verify Python Installation
1. Open Command Prompt (Windows Key + R, type `cmd`, press Enter)
2. Type: `python --version`
3. You should see something like: `Python 3.11.0` or similar
4. If you see "Python is not recognized", you need to install Python first

### Step 2: Navigate to Application Folder
```cmd
cd C:\Users\USER\OneDrive\Desktop\mahdi\HabitTrackerApp
```
(Replace the path with your actual folder location if different)

### Step 3: Run the Installer
Simply **double-click** the `install.bat` file in the HabitTrackerApp folder.

The installer will:
- ✅ Check your Python installation
- ✅ Update pip (package manager)
- ✅ Install all required packages (~150 MB download)
- ✅ Verify installation success

**Wait time**: 2-5 minutes depending on internet speed

### Step 4: Launch the Application
After installation completes, **double-click** the `run.bat` file.

The application window should open within seconds!

---

## 🛠️ Manual Installation (Alternative)

If the automatic installer doesn't work:

### 1. Open Command Prompt
- Press Windows Key + R
- Type `cmd` and press Enter

### 2. Navigate to Project Folder
```cmd
cd C:\Users\USER\OneDrive\Desktop\mahdi\HabitTrackerApp
```

### 3. Install Dependencies
```cmd
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the Application
```cmd
python main.py
```

---

## 📦 What Gets Installed

The following Python packages will be installed:

| Package | Version | Purpose |
|---------|---------|---------|
| customtkinter | 5.2.0+ | Modern GUI framework |
| pandas | 2.0.0+ | Data manipulation |
| numpy | 1.24.0+ | Numerical operations |
| matplotlib | 3.7.0+ | Charting (future use) |
| seaborn | 0.12.0+ | Statistical visualization |
| bcrypt | 4.0.0+ | Password security |
| python-dateutil | 2.8.0+ | Date parsing |
| pytz | 2023.3+ | Timezone support |
| Pillow | 10.0.0+ | Image handling |
| validators | 0.20.0+ | Input validation |
| plyer | 2.1.0+ | Notifications |
| schedule | 1.2.0+ | Task scheduling |

**Total Download Size**: ~150 MB  
**Installation Time**: 2-5 minutes

---

## ✅ Verify Installation

After installation, verify everything works:

### 1. Check Python Packages
```cmd
python -c "import customtkinter; print('CustomTkinter installed!')"
python -c "import pandas; print('Pandas installed!')"
python -c "import bcrypt; print('Bcrypt installed!')"
```

You should see success messages for each.

### 2. Run the Application
```cmd
python main.py
```

The login window should appear!

---

## 🎮 First Time Setup

### Creating Your First Account

1. **Click "Create New Account"** on the login page

2. **Step 1: Personal Information**
   - Enter your first and last name
   - Enter your date of birth (MM/DD/YYYY format)
   - Enter your phone number (with country code)
   - Enter your email address
   - Create a strong password (min 6 characters)
   - Confirm your password

3. **Step 2: Choose Username**
   - Pick a unique username (4-20 characters)
   - Click "Check" to verify availability
   - If taken, choose a suggestion or try another

4. **Step 3: Select Your Role**
   - **Student 📚**: For high school/college students
   - **Adult 💼**: For working professionals
   - **Senior 👴**: For elderly individuals
   - **Custom ⚙️**: Build your own
   - Optionally select your gender
   - Click "Complete Setup"

5. **Success!** Your account is created. Login to start tracking!

---

## 📚 Quick Start After Installation

### Day 1: Setup and First Log
1. Create your account
2. Explore the dashboard
3. Click "➕ Log Activity"
4. Enter data for a few trackers
5. Click "Save All Activities"
6. Return to dashboard to see your first entry!

### Day 2-7: Build Your Habit
1. Log activities at the same time each day
2. Watch your streak counter increase 🔥
3. See your progress visualizations grow
4. Check statistics to see weekly summaries

### Week 2+: Optimize
1. Review which trackers are most useful
2. Adjust your daily routine
3. Celebrate milestones (7-day streak!)
4. Keep building consistency

---

## 🔧 Troubleshooting

### Problem: "Python is not recognized"
**Solution**: 
1. Reinstall Python from python.org
2. **Check "Add Python to PATH" during installation**
3. Restart your computer
4. Try again

### Problem: "No module named 'customtkinter'"
**Solution**:
```cmd
python -m pip install customtkinter
```

### Problem: Install script fails
**Solutions**:
1. Check your internet connection
2. Run Command Prompt as Administrator
3. Try manual installation steps
4. Ensure no antivirus is blocking

### Problem: Application won't start
**Solutions**:
1. Make sure all packages installed successfully
2. Check Python version: `python --version` (need 3.8+)
3. Run from command line to see error messages:
   ```cmd
   python main.py
   ```
4. Check that data/ folder exists

### Problem: "Access Denied" or permission errors
**Solutions**:
1. Run Command Prompt as Administrator
2. Check folder permissions
3. Move application to a folder you have write access to

### Problem: Application crashes on startup
**Solutions**:
1. Delete `data/` folder and restart (will reset data)
2. Check for conflicting Python installations
3. Reinstall all packages:
   ```cmd
   pip uninstall -r requirements.txt -y
   pip install -r requirements.txt
   ```

---

## 🌐 System Requirements

### Minimum Requirements
- **OS**: Windows 10 (64-bit)
- **RAM**: 2 GB
- **Storage**: 200 MB free space
- **Display**: 1024x768 resolution
- **Python**: 3.8+

### Recommended Requirements
- **OS**: Windows 11 (64-bit)
- **RAM**: 4 GB or more
- **Storage**: 500 MB free space
- **Display**: 1920x1080 resolution
- **Python**: 3.11+

---

## 📖 Next Steps After Installation

### Learn the Basics
1. Read [QUICKSTART.md](QUICKSTART.md) for a 5-minute intro
2. Read [USER_GUIDE.md](USER_GUIDE.md) for comprehensive instructions
3. Check [README.md](README.md) for technical details

### Explore Features
- **Dashboard**: See your progress at a glance
- **Log Activity**: Enter daily tracking data
- **Statistics**: View 7-day summaries
- **Settings**: Customize theme and profile

### Get Help
- Check the USER_GUIDE.md for detailed help
- Review ARCHITECTURE.md to understand how it works
- Read FAQ section in USER_GUIDE.md

---

## 🎯 Usage Tips

### Daily Routine
1. **Morning**: Log yesterday's data (5 minutes)
2. **Evening**: Review dashboard, prepare for tomorrow
3. **Weekly**: Check statistics on Sunday

### Best Practices
- ✅ Log at the same time each day
- ✅ Start with 5-10 trackers maximum
- ✅ Be honest with entries
- ✅ Celebrate weekly milestones
- ❌ Don't worry about perfect scores
- ❌ Don't track too many things at once

### Data Safety
- **Backup regularly**: Copy the entire `data/` folder
- **Store safely**: Keep backups on USB or cloud storage
- **Privacy**: All data stays on your computer

---

## 🔄 Updating the Application

When a new version is released:

1. **Backup your data**:
   ```cmd
   copy C:\Users\USER\OneDrive\Desktop\mahdi\HabitTrackerApp\data\*.* C:\Backup\
   ```

2. **Download new version** and replace files

3. **Restore your data**:
   - Copy backed-up `data/` folder back
   - Your accounts and tracking history will be preserved

---

## 🗑️ Uninstalling

To remove the application:

1. **Backup data** (if you want to keep it)
2. **Delete the HabitTrackerApp folder**
3. **Optionally uninstall Python packages**:
   ```cmd
   pip uninstall customtkinter pandas numpy matplotlib seaborn bcrypt python-dateutil pytz pillow validators plyer schedule -y
   ```

---

## 📞 Support & Resources

### Documentation
- **Quick Start**: QUICKSTART.md
- **User Manual**: USER_GUIDE.md (5,000+ words)
- **Technical Docs**: README.md
- **Architecture**: ARCHITECTURE.md
- **Changelog**: CHANGELOG.md

### Self-Help
- Check USER_GUIDE.md troubleshooting section
- Review error messages carefully
- Verify Python and package versions

---

## ✨ You're All Set!

Congratulations! You've successfully installed the Habit & Lifestyle Tracker.

### What's Next?
1. ✅ Launch the application (`run.bat`)
2. ✅ Create your account
3. ✅ Start logging your first activities
4. ✅ Build your streak! 🔥

### Remember
- Consistency is key
- Progress over perfection
- Every entry counts
- Celebrate small wins

---

**🎯 Track your habits, Transform your life!**

*Ready to start? Double-click `run.bat` now!*

---

## 📊 Installation Checklist

- [ ] Python 3.8+ installed
- [ ] Python added to PATH
- [ ] Internet connection active
- [ ] Navigated to HabitTrackerApp folder
- [ ] Ran install.bat successfully
- [ ] All packages installed
- [ ] Application launches without errors
- [ ] Account created successfully
- [ ] First activity logged
- [ ] Dashboard displays correctly

Once all items are checked, you're ready to go! 🚀

---

*Installation Guide v1.0.0*  
*Last Updated: January 2026*
