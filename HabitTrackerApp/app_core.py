"""
Main Application Core - Dashboard and Navigation
MVP Version with basic dashboard, activity logging, and settings
"""
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from typing import Dict, Any
import pandas as pd

from data_handler import TrackerDataManager, UserDataManager
from utils import DateTimeHelper, StatisticsCalculator
from config import APP_NAME, GREETINGS, MOTIVATIONAL_MESSAGES
from trackers.student_trackers import get_student_trackers
from trackers.adult_trackers import get_adult_trackers
from trackers.senior_trackers import get_senior_trackers


class MainApplication:
    """Main application window with dashboard"""
    
    def __init__(self, user_data: Dict[str, Any]):
        """Initialize main application"""
        self.user_data = user_data
        self.username = user_data['username']
        self.role = user_data['role']
        
        # Data managers
        self.tracker_manager = TrackerDataManager(self.username)
        self.user_manager = UserDataManager()
        
        # Load role-specific trackers
        self.load_role_trackers()
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title(f"{APP_NAME} - {user_data['first_name']}")
        self.root.geometry("1200x800")
        
        self.palettes = {
            "light": {
                "bg": "#F6F2EC",
                "card": "#FFFFFF",
                "accent": "#D77A34",
                "accent_dark": "#B8652A",
                "text": "#2C2622",
                "muted": "#6F6A64",
                "border": "#E6DCCF",
                "input_bg": "#FBF7F1",
                "success": "#2F8F5B",
                "success_dark": "#25744B",
                "error": "#C1483C",
                "error_dark": "#A93E35"
            },
            "dark": {
                "bg": "#1C1A18",
                "card": "#2A2622",
                "accent": "#D77A34",
                "accent_dark": "#B8652A",
                "text": "#F4EEE6",
                "muted": "#B6AEA5",
                "border": "#3A342F",
                "input_bg": "#231F1C",
                "success": "#4DB06B",
                "success_dark": "#3F8F57",
                "error": "#E06B61",
                "error_dark": "#B9554E"
            }
        }
        self.fonts = {
            "brand": ("Georgia", 18, "bold"),
            "title": ("Georgia", 20, "bold"),
            "section": ("Trebuchet MS", 16, "bold"),
            "body": ("Trebuchet MS", 13),
            "body_bold": ("Trebuchet MS", 13, "bold"),
            "small": ("Trebuchet MS", 11),
            "nav": ("Trebuchet MS", 13, "bold")
        }

        self.current_theme = user_data.get('theme', 'light')
        if self.current_theme not in self.palettes:
            self.current_theme = "light"
        self.palette = self.palettes[self.current_theme]
        ctk.set_appearance_mode(self.current_theme)
        self.root.configure(fg_color=self.palette["bg"])
        self.root.minsize(1100, 700)
        
        # Current page
        self.current_content_frame = None
        self.current_page = "dashboard"
        
        # Create UI
        self.create_main_layout()
        self.show_dashboard()
    
    def load_role_trackers(self):
        """Load trackers based on user role"""
        if self.role == "student":
            self.available_trackers = get_student_trackers()
        elif self.role == "adult":
            self.available_trackers = get_adult_trackers()
        elif self.role == "senior":
            self.available_trackers = get_senior_trackers()
        else:
            self.available_trackers = []
    
    def create_main_layout(self):
        """Create main application layout"""
        # Top bar
        self.create_top_bar()
        
        # Main content area
        self.content_container = ctk.CTkFrame(self.root, fg_color=self.palette["bg"])
        self.content_container.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Bottom navigation
        self.create_bottom_nav()
    
    def create_top_bar(self):
        """Create top navigation bar"""
        top_bar = ctk.CTkFrame(
            self.root,
            height=80,
            corner_radius=0,
            fg_color=self.palette["accent"]
        )
        top_bar.pack(fill="x", padx=0, pady=0)

        left_frame = ctk.CTkFrame(top_bar, fg_color="transparent")
        left_frame.pack(side="left", padx=20, pady=10)

        brand_label = ctk.CTkLabel(
            left_frame,
            text=APP_NAME,
            font=self.fonts["brand"],
            text_color="white"
        )
        brand_label.pack(anchor="w")

        time_of_day = DateTimeHelper.get_time_of_day()
        greeting = GREETINGS[time_of_day]
        welcome_label = ctk.CTkLabel(
            left_frame,
            text=f"{greeting}, {self.user_data['first_name']}",
            font=self.fonts["body_bold"],
            text_color="white"
        )
        welcome_label.pack(anchor="w")

        right_frame = ctk.CTkFrame(top_bar, fg_color="transparent")
        right_frame.pack(side="right", padx=20, pady=10)

        today = datetime.now()
        date_text = f"{DateTimeHelper.get_day_name(today)}, {DateTimeHelper.format_date(today)}"
        date_label = ctk.CTkLabel(
            right_frame,
            text=date_text,
            font=self.fonts["small"],
            text_color="white"
        )
        date_label.pack(anchor="e")

        streak = self.tracker_manager.calculate_streak()
        if streak > 0:
            streak_label = ctk.CTkLabel(
                right_frame,
                text=f"{streak} Day Streak",
                font=self.fonts["small"],
                text_color="white"
            )
            streak_label.pack(anchor="e")

    def create_bottom_nav(self):
        """Create bottom navigation bar"""
        nav_bar = ctk.CTkFrame(
            self.root,
            height=70,
            corner_radius=0,
            fg_color=self.palette["card"],
            border_width=1,
            border_color=self.palette["border"]
        )
        nav_bar.pack(fill="x", side="bottom", padx=0, pady=0)

        # Navigation buttons
        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Log Activity", self.show_activity_logger),
            ("Statistics", self.show_statistics),
            ("Settings", self.show_settings)
        ]

        for text, command in buttons:
            btn = ctk.CTkButton(
                nav_bar,
                text=text,
                command=command,
                width=220,
                height=46,
                font=self.fonts["nav"],
                fg_color=self.palette["card"],
                text_color=self.palette["text"],
                hover_color=self.palette["input_bg"],
                border_width=1,
                border_color=self.palette["border"]
            )
            btn.pack(side="left", expand=True, padx=8, pady=10)

    def apply_theme(self, mode: str, refresh: bool = True):
        """Apply theme colors and optionally rebuild the UI."""
        if mode not in self.palettes:
            mode = "light"
        self.current_theme = mode
        self.palette = self.palettes[mode]
        ctk.set_appearance_mode(mode)
        self.root.configure(fg_color=self.palette["bg"])
        if refresh:
            self.rebuild_layout()

    def rebuild_layout(self):
        """Rebuild layout after theme changes."""
        for child in self.root.winfo_children():
            child.destroy()
        self.current_content_frame = None
        self.create_main_layout()
        self.show_current_page()

    def show_current_page(self):
        """Restore the currently active page after a rebuild."""
        if self.current_page == "activity":
            self.show_activity_logger()
        elif self.current_page == "statistics":
            self.show_statistics()
        elif self.current_page == "settings":
            self.show_settings()
        else:
            self.show_dashboard()

    def handle_theme_change(self, mode: str):
        """Persist and apply a theme change."""
        if mode == self.current_theme:
            return
        self.user_data["theme"] = mode
        self.user_manager.update_user_profile(self.username, {"theme": mode})
        self.apply_theme(mode, refresh=True)

    def make_card(self, parent, corner_radius: int = 16):
        """Create a styled card frame"""
        return ctk.CTkFrame(
            parent,
            fg_color=self.palette["card"],
            corner_radius=corner_radius,
            border_width=1,
            border_color=self.palette["border"]
        )
    
    def clear_content(self):
        """Clear current content frame"""
        for child in self.content_container.winfo_children():
            child.destroy()
        self.current_content_frame = None
    
    def show_dashboard(self):
        """Display main dashboard"""
        self.current_page = "dashboard"
        self.clear_content()

        self.current_content_frame = ctk.CTkScrollableFrame(self.content_container, fg_color="transparent")
        self.current_content_frame.pack(fill="both", expand=True)

        # Overall Progress Section
        progress_frame = self.make_card(self.current_content_frame)
        progress_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            progress_frame,
            text="Today's Progress",
            font=self.fonts["section"],
            text_color=self.palette["text"]
        ).pack(pady=10)

        # Get today's data
        today_str = datetime.now().strftime("%Y-%m-%d")
        activities = self.tracker_manager.get_activities_by_date(today_str)

        if not activities.empty:
            # Calculate completion
            total_completion = 0
            for _, activity in activities.iterrows():
                if activity['goal'] > 0:
                    completion = min(100, (float(activity['value']) / float(activity['goal'])) * 100)
                    total_completion += completion

            avg_completion = total_completion / len(activities) if len(activities) > 0 else 0

            # Progress bar
            progress_bar = ctk.CTkProgressBar(
                progress_frame,
                width=600,
                height=26,
                fg_color=self.palette["border"],
                progress_color=self.palette["accent"]
            )
            progress_bar.pack(pady=10)
            progress_bar.set(avg_completion / 100)

            # Progress text
            category = StatisticsCalculator.get_progress_category(avg_completion)
            messages = MOTIVATIONAL_MESSAGES.get(category, ["Keep going!"])
            message = messages[0]

            ctk.CTkLabel(
                progress_frame,
                text=f"{avg_completion:.1f}% Complete - {message}",
                font=self.fonts["body"],
                text_color=self.palette["text"]
            ).pack(pady=10)
        else:
            ctk.CTkLabel(
                progress_frame,
                text="No activities logged today. Start tracking your habits!",
                font=self.fonts["body"],
                text_color=self.palette["muted"]
            ).pack(pady=20)

        # Quick Stats
        stats_frame = self.make_card(self.current_content_frame)
        stats_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            stats_frame,
            text="Quick Stats",
            font=self.fonts["section"],
            text_color=self.palette["text"]
        ).pack(pady=10)

        # Display tracker summary
        if not activities.empty:
            for _, activity in activities.head(5).iterrows():
                tracker_frame = self.make_card(stats_frame, corner_radius=12)
                tracker_frame.pack(fill="x", padx=10, pady=5)

                name_label = ctk.CTkLabel(
                    tracker_frame,
                    text=f"{activity['tracker_name']}",
                    font=self.fonts["body_bold"],
                    text_color=self.palette["text"]
                )
                name_label.pack(side="left", padx=10, pady=8)

                value_text = f"{activity['value']} / {activity['goal']} {activity['unit']}"
                value_label = ctk.CTkLabel(
                    tracker_frame,
                    text=value_text,
                    font=self.fonts["body"],
                    text_color=self.palette["muted"]
                )
                value_label.pack(side="right", padx=10, pady=8)

        # Available Trackers Section
        trackers_frame = self.make_card(self.current_content_frame)
        trackers_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            trackers_frame,
            text="Your Trackers",
            font=self.fonts["section"],
            text_color=self.palette["text"]
        ).pack(pady=10)

        for tracker in self.available_trackers[:6]:  # Show first 6
            tracker_card = self.make_card(trackers_frame, corner_radius=12)
            tracker_card.pack(fill="x", padx=10, pady=5)

            ctk.CTkLabel(
                tracker_card,
                text=tracker.name,
                font=self.fonts["body_bold"],
                text_color=self.palette["text"]
            ).pack(side="left", padx=10, pady=8)

            ctk.CTkLabel(
                tracker_card,
                text=tracker.description,
                font=self.fonts["small"],
                text_color=self.palette["muted"]
            ).pack(side="left", padx=10, pady=8)

    def show_activity_logger(self):
        """Display activity logging page"""
        self.current_page = "activity"
        self.clear_content()

        self.current_content_frame = ctk.CTkScrollableFrame(self.content_container, fg_color="transparent")
        self.current_content_frame.pack(fill="both", expand=True)

        # Header
        header = ctk.CTkLabel(
            self.current_content_frame,
            text=f"Log Today's Activities - {datetime.now().strftime('%B %d, %Y')}",
            font=self.fonts["title"],
            text_color=self.palette["text"]
        )
        header.pack(pady=20)

        # Create input forms for each tracker
        self.tracker_inputs = {}

        for tracker in self.available_trackers:
            tracker_frame = self.make_card(self.current_content_frame)
            tracker_frame.pack(fill="x", padx=20, pady=10)

            # Tracker title
            title_label = ctk.CTkLabel(
                tracker_frame,
                text=tracker.name,
                font=self.fonts["section"],
                text_color=self.palette["text"]
            )
            title_label.pack(anchor="w", padx=15, pady=10)

            # Description
            desc_label = ctk.CTkLabel(
                tracker_frame,
                text=tracker.description,
                font=self.fonts["small"],
                text_color=self.palette["muted"]
            )
            desc_label.pack(anchor="w", padx=15, pady=(0, 5))

            # Input based on tracker type
            if tracker.tracker_type == "duration" or tracker.tracker_type == "counter" or tracker.tracker_type == "numeric":
                input_frame = ctk.CTkFrame(tracker_frame, fg_color="transparent")
                input_frame.pack(anchor="w", padx=15, pady=10)

                entry = ctk.CTkEntry(
                    input_frame,
                    placeholder_text="Enter value",
                    placeholder_text_color=self.palette["muted"],
                    fg_color=self.palette["input_bg"],
                    border_color=self.palette["border"],
                    text_color=self.palette["text"],
                    width=200,
                    height=35,
                    font=self.fonts["body"]
                )
                entry.pack(side="left", padx=5)

                ctk.CTkLabel(
                    input_frame,
                    text=tracker.unit,
                    font=self.fonts["body"],
                    text_color=self.palette["text"]
                ).pack(side="left", padx=5)

                ctk.CTkLabel(
                    input_frame,
                    text=f"Goal: {tracker.goal} {tracker.unit}",
                    font=self.fonts["small"],
                    text_color=self.palette["muted"]
                ).pack(side="left", padx=15)

                self.tracker_inputs[tracker.name] = {"widget": entry, "type": tracker.tracker_type, "tracker": tracker}

            elif tracker.tracker_type == "checkbox":
                var = ctk.BooleanVar()
                checkbox = ctk.CTkCheckBox(
                    tracker_frame,
                    text="Completed",
                    variable=var,
                    font=self.fonts["body_bold"],
                    text_color=self.palette["text"]
                )
                checkbox.pack(anchor="w", padx=15, pady=10)

                self.tracker_inputs[tracker.name] = {"widget": checkbox, "var": var, "type": "checkbox", "tracker": tracker}

            elif tracker.tracker_type == "rating":
                input_frame = ctk.CTkFrame(tracker_frame, fg_color="transparent")
                input_frame.pack(anchor="w", padx=15, pady=10)

                var = ctk.IntVar(value=3)

                ctk.CTkLabel(
                    input_frame,
                    text="Rating:",
                    font=self.fonts["body"],
                    text_color=self.palette["text"]
                ).pack(side="left", padx=5)

                for i in range(1, int(tracker.max_value) + 1):
                    ctk.CTkRadioButton(
                        input_frame,
                        text=str(i),
                        variable=var,
                        value=i,
                        font=self.fonts["body"],
                        text_color=self.palette["text"]
                    ).pack(side="left", padx=3)

                self.tracker_inputs[tracker.name] = {"var": var, "type": "rating", "tracker": tracker}

        # Save button
        save_btn = ctk.CTkButton(
            self.current_content_frame,
            text="Save All Activities",
            command=self.save_activities,
            width=300,
            height=50,
            font=self.fonts["section"],
            fg_color=self.palette["success"],
            hover_color=self.palette["success_dark"],
            text_color="white"
        )
        save_btn.pack(pady=30)

    def save_activities(self):
        """Save all logged activities"""
        today_str = datetime.now().strftime("%Y-%m-%d")
        saved_count = 0
        
        for tracker_name, input_data in self.tracker_inputs.items():
            tracker = input_data['tracker']
            
            try:
                if input_data['type'] in ['duration', 'counter', 'numeric']:
                    value = input_data['widget'].get()
                    if value and value.strip():
                        value = float(value)
                        activity_data = {
                            'date': today_str,
                            'tracker_type': tracker.tracker_type,
                            'tracker_name': tracker.name,
                            'value': value,
                            'goal': tracker.goal,
                            'unit': tracker.unit,
                            'completed': 'yes' if value >= tracker.goal else 'no'
                        }
                        self.tracker_manager.log_activity(activity_data)
                        saved_count += 1
                
                elif input_data['type'] == 'checkbox':
                    value = 1 if input_data['var'].get() else 0
                    activity_data = {
                        'date': today_str,
                        'tracker_type': 'checkbox',
                        'tracker_name': tracker.name,
                        'value': value,
                        'goal': 1,
                        'unit': 'boolean',
                        'completed': 'yes' if value == 1 else 'no'
                    }
                    self.tracker_manager.log_activity(activity_data)
                    saved_count += 1
                
                elif input_data['type'] == 'rating':
                    value = input_data['var'].get()
                    activity_data = {
                        'date': today_str,
                        'tracker_type': 'rating',
                        'tracker_name': tracker.name,
                        'value': value,
                        'goal': tracker.goal,
                        'unit': 'stars',
                        'completed': 'yes' if value >= tracker.goal else 'no'
                    }
                    self.tracker_manager.log_activity(activity_data)
                    saved_count += 1
            
            except Exception as e:
                print(f"Error saving {tracker_name}: {e}")
        
        if saved_count > 0:
            messagebox.showinfo("Success", f"Saved {saved_count} activities!")
            self.show_dashboard()
        else:
            messagebox.showwarning("No Data", "No activities were logged. Please enter some values.")
    
    def show_statistics(self):
        """Display statistics page"""
        self.current_page = "statistics"
        self.clear_content()

        self.current_content_frame = ctk.CTkScrollableFrame(self.content_container, fg_color="transparent")
        self.current_content_frame.pack(fill="both", expand=True)

        # Header
        header = ctk.CTkLabel(
            self.current_content_frame,
            text="Your Statistics",
            font=self.fonts["title"],
            text_color=self.palette["text"]
        )
        header.pack(pady=20)

        # Get data for last 7 days
        end_date = datetime.now()
        start_date = end_date - pd.Timedelta(days=6)

        activities = self.tracker_manager.get_activities_by_date_range(
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d")
        )

        if activities.empty:
            ctk.CTkLabel(
                self.current_content_frame,
                text="No data available yet. Start logging your activities!",
                font=self.fonts["body"],
                text_color=self.palette["muted"]
            ).pack(pady=50)
            return

        # Summary statistics
        summary_frame = self.make_card(self.current_content_frame)
        summary_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            summary_frame,
            text="7-Day Summary",
            font=self.fonts["section"],
            text_color=self.palette["text"]
        ).pack(pady=10)

        # Calculate stats
        total_entries = len(activities)
        completed = len(activities[activities['completed'] == 'yes'])
        completion_rate = (completed / total_entries * 100) if total_entries > 0 else 0

        stats_text = f"Total Activities: {total_entries}\n"
        stats_text += f"Completed Goals: {completed}\n"
        stats_text += f"Completion Rate: {completion_rate:.1f}%"

        ctk.CTkLabel(
            summary_frame,
            text=stats_text,
            font=self.fonts["body"],
            text_color=self.palette["text"],
            justify="left"
        ).pack(pady=10, padx=20)

    def show_settings(self):
        """Display settings page"""
        self.current_page = "settings"
        self.clear_content()

        self.current_content_frame = ctk.CTkScrollableFrame(self.content_container, fg_color="transparent")
        self.current_content_frame.pack(fill="both", expand=True)

        # Header
        header = ctk.CTkLabel(
            self.current_content_frame,
            text="Settings",
            font=self.fonts["title"],
            text_color=self.palette["text"]
        )
        header.pack(pady=20)

        # Profile section
        profile_frame = self.make_card(self.current_content_frame)
        profile_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            profile_frame,
            text="Profile Information",
            font=self.fonts["section"],
            text_color=self.palette["text"]
        ).pack(pady=10)

        profile_text = f"Name: {self.user_data['first_name']} {self.user_data['last_name']}\n"
        profile_text += f"Username: @{self.username}\n"
        profile_text += f"Email: {self.user_data['email']}\n"
        profile_text += f"Role: {self.role.title()}\n"

        ctk.CTkLabel(
            profile_frame,
            text=profile_text,
            font=self.fonts["body"],
            text_color=self.palette["text"],
            justify="left"
        ).pack(pady=10, padx=20, anchor="w")

        # Theme selection
        theme_frame = self.make_card(self.current_content_frame)
        theme_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            theme_frame,
            text="Appearance",
            font=self.fonts["section"],
            text_color=self.palette["text"]
        ).pack(pady=10)

        theme_var = ctk.StringVar(value=self.current_theme)

        ctk.CTkLabel(
            theme_frame,
            text="Theme:",
            font=self.fonts["body"],
            text_color=self.palette["text"]
        ).pack(pady=5)

        theme_options = ctk.CTkFrame(theme_frame, fg_color="transparent")
        theme_options.pack(pady=10)

        ctk.CTkRadioButton(
            theme_options,
            text="Light",
            variable=theme_var,
            value="light",
            command=lambda: self.handle_theme_change("light"),
            font=self.fonts["body"],
            text_color=self.palette["text"]
        ).pack(side="left", padx=10)

        ctk.CTkRadioButton(
            theme_options,
            text="Dark",
            variable=theme_var,
            value="dark",
            command=lambda: self.handle_theme_change("dark"),
            font=self.fonts["body"],
            text_color=self.palette["text"]
        ).pack(side="left", padx=10)

        # Logout button
        logout_btn = ctk.CTkButton(
            self.current_content_frame,
            text="Logout",
            command=self.logout,
            width=300,
            height=45,
            font=self.fonts["nav"],
            fg_color=self.palette["error"],
            hover_color=self.palette["error_dark"],
            text_color="white"
        )
        logout_btn.pack(pady=30)

    def logout(self):
        """Logout and return to login screen"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.destroy()
            from auth import AuthenticationApp
            auth_app = AuthenticationApp()
            auth_app.run()
    
    def run(self):
        """Run the main application"""
        self.root.mainloop()
