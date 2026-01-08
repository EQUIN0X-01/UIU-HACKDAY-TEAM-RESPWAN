"""
Authentication Module for Habit Tracker Application
- Login Page
- Sign Up (Personal Info, Username, Role Selection)
- Password Recovery
"""
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

from data_handler import UserDataManager
from utils import Validators, suggest_alternative_usernames
from config import APP_NAME, APP_TAGLINE


class AuthenticationApp:
    """Main authentication window manager"""
    
    def __init__(self):
        """Initialize the authentication app"""
        self.root = ctk.CTk()
        self.root.title(f"{APP_NAME} - Login")
        self.root.geometry("560x660")
        
        # Set theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.palette = {
            "bg": "#F6F2EC",
            "card": "#FFFFFF",
            "accent": "#D77A34",
            "accent_dark": "#B8652A",
            "text": "#2C2622",
            "muted": "#6F6A64",
            "border": "#E6DCCF",
            "input_bg": "#FBF7F1",
            "error": "#C1483C",
            "success": "#2F8F5B",
            "success_dark": "#25744B"
        }
        self.fonts = {
            "title": ("Georgia", 30, "bold"),
            "header": ("Georgia", 22, "bold"),
            "subheader": ("Trebuchet MS", 14),
            "label": ("Trebuchet MS", 12),
            "body": ("Trebuchet MS", 13),
            "body_bold": ("Trebuchet MS", 13, "bold"),
            "button": ("Trebuchet MS", 13, "bold"),
            "small": ("Trebuchet MS", 10)
        }

        self.root.configure(fg_color=self.palette["bg"])
        self.root.minsize(520, 620)
        
        # Data managers
        self.user_manager = UserDataManager()
        
        # Current user data (for sign up process)
        self.current_signup_data = {}
        
        # Current page
        self.current_frame = None
        
        # Show login page
        self.show_login_page()
    
    def clear_frame(self):
        """Clear current frame"""
        for child in self.root.winfo_children():
            child.destroy()
        self.current_frame = None
    
    def show_login_page(self):
        """Display login page"""
        self.clear_frame()
        self.root.title(f"{APP_NAME} - Login")

        self.current_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.palette["card"],
            corner_radius=20,
            border_width=1,
            border_color=self.palette["border"]
        )
        self.current_frame.pack(fill="both", expand=True, padx=30, pady=30)

        # Logo and title
        title = ctk.CTkLabel(
            self.current_frame,
            text=APP_NAME,
            font=self.fonts["title"],
            text_color=self.palette["text"]
        )
        title.pack(pady=(20, 10))

        tagline = ctk.CTkLabel(
            self.current_frame,
            text=APP_TAGLINE,
            font=self.fonts["subheader"],
            text_color=self.palette["muted"]
        )
        tagline.pack(pady=(0, 30))

        # Username input
        username_label = ctk.CTkLabel(
            self.current_frame,
            text="Username",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        )
        username_label.pack(pady=(10, 5))

        self.login_username = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="Enter your username",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=300,
            height=40,
            font=self.fonts["body"]
        )
        self.login_username.pack(pady=5)

        # Password input
        password_label = ctk.CTkLabel(
            self.current_frame,
            text="Password",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        )
        password_label.pack(pady=(10, 5))

        self.login_password = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="Enter your password",
            show="*",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=300,
            height=40,
            font=self.fonts["body"]
        )
        self.login_password.pack(pady=5)

        # Error label
        self.login_error_label = ctk.CTkLabel(
            self.current_frame,
            text="",
            font=self.fonts["small"],
            text_color=self.palette["error"]
        )
        self.login_error_label.pack(pady=5)

        # Login button
        login_btn = ctk.CTkButton(
            self.current_frame,
            text="Login",
            command=self.handle_login,
            width=300,
            height=40,
            font=self.fonts["button"],
            fg_color=self.palette["accent"],
            hover_color=self.palette["accent_dark"],
            text_color="white"
        )
        login_btn.pack(pady=15)

        # Forgot password link
        forgot_password_btn = ctk.CTkButton(
            self.current_frame,
            text="Forgot Password?",
            command=self.show_password_recovery,
            width=300,
            height=30,
            fg_color="transparent",
            text_color=self.palette["accent"],
            hover_color=self.palette["input_bg"],
            font=self.fonts["small"]
        )
        forgot_password_btn.pack(pady=5)

        # OR divider
        or_label = ctk.CTkLabel(
            self.current_frame,
            text="OR",
            font=self.fonts["small"],
            text_color=self.palette["muted"]
        )
        or_label.pack(pady=10)

        # Create account button
        create_account_btn = ctk.CTkButton(
            self.current_frame,
            text="Create New Account",
            command=self.show_signup_personal_info,
            width=300,
            height=40,
            fg_color=self.palette["card"],
            text_color=self.palette["accent"],
            border_width=1,
            border_color=self.palette["accent"],
            hover_color=self.palette["input_bg"],
            font=self.fonts["button"]
        )
        create_account_btn.pack(pady=10)

        # Bind Enter key
        self.login_username.bind("<Return>", lambda e: self.handle_login())
        self.login_password.bind("<Return>", lambda e: self.handle_login())

    def handle_login(self):
        """Handle login button click"""
        username = self.login_username.get().strip()
        password = self.login_password.get()
        
        if not username or not password:
            self.login_error_label.configure(
                text="Please fill in all fields",
                text_color=self.palette["error"]
            )
            return
        
        # Authenticate
        user_data = self.user_manager.authenticate_user(username, password)
        
        if user_data is None:
            self.login_error_label.configure(
                text="Invalid username or password",
                text_color=self.palette["error"]
            )
            return
        
        if isinstance(user_data, dict) and 'error' in user_data:
            self.login_error_label.configure(
                text=user_data['error'],
                text_color=self.palette["error"]
            )
            return
        
        # Success - close auth window and open main app
        self.login_error_label.configure(
            text="Login successful!",
            text_color=self.palette["success"]
        )
        self.root.after(1000, lambda: self.open_main_app(user_data))
    
    def open_main_app(self, user_data):
        """Open main application dashboard"""
        self.root.destroy()
        # Import here to avoid circular imports
        from app_core import MainApplication
        app = MainApplication(user_data)
        app.run()
    
    def show_signup_personal_info(self):
        """Display signup page - Step 1: Personal Information"""
        self.clear_frame()
        self.root.title(f"{APP_NAME} - Create Account (1 of 3)")
        self.root.geometry("640x780")

        self.current_frame = ctk.CTkScrollableFrame(
            self.root,
            fg_color=self.palette["card"],
            corner_radius=20,
            border_width=1,
            border_color=self.palette["border"]
        )
        self.current_frame.pack(fill="both", expand=True, padx=30, pady=30)

        # Header
        header = ctk.CTkLabel(
            self.current_frame,
            text="Create Your Account",
            font=self.fonts["header"],
            text_color=self.palette["text"]
        )
        header.pack(pady=(10, 5))

        # Progress indicator
        progress_text = ctk.CTkLabel(
            self.current_frame,
            text="Step 1 of 3: Personal Information",
            font=self.fonts["subheader"],
            text_color=self.palette["muted"]
        )
        progress_text.pack(pady=(0, 20))

        # First Name
        ctk.CTkLabel(
            self.current_frame,
            text="First Name *",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.first_name = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="Enter your first name",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.first_name.pack(pady=5)

        # Last Name
        ctk.CTkLabel(
            self.current_frame,
            text="Last Name *",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.last_name = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="Enter your last name",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.last_name.pack(pady=5)

        # Date of Birth
        ctk.CTkLabel(
            self.current_frame,
            text="Date of Birth * (MM/DD/YYYY)",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.dob = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="MM/DD/YYYY",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.dob.pack(pady=5)

        # Phone Number
        ctk.CTkLabel(
            self.current_frame,
            text="Phone Number *",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.phone = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="+1 555-0123",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.phone.pack(pady=5)

        # Email
        ctk.CTkLabel(
            self.current_frame,
            text="Email Address *",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.email = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="your@email.com",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.email.pack(pady=5)

        # Password
        ctk.CTkLabel(
            self.current_frame,
            text="Password * (min 6 characters)",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.password = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="Create a password",
            show="*",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.password.pack(pady=5)

        # Password strength indicator
        self.password_strength = ctk.CTkLabel(
            self.current_frame,
            text="",
            font=self.fonts["small"],
            text_color=self.palette["muted"]
        )
        self.password_strength.pack(pady=2)
        self.password.bind("<KeyRelease>", self.update_password_strength)

        # Confirm Password
        ctk.CTkLabel(
            self.current_frame,
            text="Confirm Password *",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.confirm_password = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="Re-enter password",
            show="*",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.confirm_password.pack(pady=5)

        # Error label
        self.signup_error_label = ctk.CTkLabel(
            self.current_frame,
            text="",
            font=self.fonts["small"],
            text_color=self.palette["error"]
        )
        self.signup_error_label.pack(pady=5)

        # Buttons
        button_frame = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        button_frame.pack(pady=20)

        back_btn = ctk.CTkButton(
            button_frame,
            text="Back",
            command=self.show_login_page,
            width=150,
            height=40,
            fg_color=self.palette["card"],
            text_color=self.palette["accent"],
            border_width=1,
            border_color=self.palette["accent"],
            hover_color=self.palette["input_bg"],
            font=self.fonts["button"]
        )
        back_btn.pack(side="left", padx=10)

        next_btn = ctk.CTkButton(
            button_frame,
            text="Next",
            command=self.validate_and_go_to_username,
            width=150,
            height=40,
            fg_color=self.palette["accent"],
            hover_color=self.palette["accent_dark"],
            text_color="white",
            font=self.fonts["button"]
        )
        next_btn.pack(side="left", padx=10)

    def update_password_strength(self, event=None):
        """Update password strength indicator"""
        password = self.password.get()

        if not password:
            self.password_strength.configure(text="", text_color=self.palette["muted"])
            return

        is_valid, message, strength = Validators.validate_password(password)

        if strength == "weak":
            self.password_strength.configure(text="Strength: Weak", text_color=self.palette["error"])
        elif strength == "medium":
            self.password_strength.configure(text="Strength: Medium", text_color=self.palette["accent"])
        else:
            self.password_strength.configure(text="Strength: Strong", text_color=self.palette["success"])

    def validate_and_go_to_username(self):
        """Validate personal info and proceed to username creation"""
        # Get values
        first_name = self.first_name.get().strip()
        last_name = self.last_name.get().strip()
        dob = self.dob.get().strip()
        phone = self.phone.get().strip()
        email = self.email.get().strip()
        password = self.password.get()
        confirm_password = self.confirm_password.get()
        
        # Validate all fields
        if not all([first_name, last_name, dob, phone, email, password, confirm_password]):
            self.signup_error_label.configure(text="Please fill in all required fields")
            return
        
        # Validate first name
        valid, msg = Validators.validate_name(first_name)
        if not valid:
            self.signup_error_label.configure(text=f"First name: {msg}")
            return
        
        # Validate last name
        valid, msg = Validators.validate_name(last_name)
        if not valid:
            self.signup_error_label.configure(text=f"Last name: {msg}")
            return
        
        # Validate date of birth
        try:
            dob_date = datetime.strptime(dob, "%m/%d/%Y")
            valid, msg, age = Validators.validate_age(dob_date)
            if not valid:
                self.signup_error_label.configure(text=msg)
                return
        except ValueError:
            self.signup_error_label.configure(text="Invalid date format. Use MM/DD/YYYY")
            return
        
        # Validate phone
        valid, msg = Validators.validate_phone(phone)
        if not valid:
            self.signup_error_label.configure(text=msg)
            return
        
        # Check if phone exists
        if self.user_manager.phone_exists(phone):
            self.signup_error_label.configure(text="Phone number already registered")
            return
        
        # Validate email
        valid, msg = Validators.validate_email(email)
        if not valid:
            self.signup_error_label.configure(text=msg)
            return
        
        # Check if email exists
        if self.user_manager.email_exists(email):
            self.signup_error_label.configure(text="Email already registered")
            return
        
        # Validate password
        valid, msg, strength = Validators.validate_password(password)
        if not valid:
            self.signup_error_label.configure(text=msg)
            return
        
        # Check password match
        if password != confirm_password:
            self.signup_error_label.configure(text="Passwords do not match")
            return
        
        # Store data and proceed
        self.current_signup_data = {
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': dob,
            'phone': phone,
            'email': email,
            'password': password,
            'age': age
        }
        
        self.show_username_creation()
    
    def show_username_creation(self):
        """Display signup page - Step 2: Username Creation"""
        self.clear_frame()
        self.root.title(f"{APP_NAME} - Create Account (2 of 3)")
        self.root.geometry("560x600")

        self.current_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.palette["card"],
            corner_radius=20,
            border_width=1,
            border_color=self.palette["border"]
        )
        self.current_frame.pack(fill="both", expand=True, padx=30, pady=30)

        # Header
        header = ctk.CTkLabel(
            self.current_frame,
            text="Create Your Account",
            font=self.fonts["header"],
            text_color=self.palette["text"]
        )
        header.pack(pady=(20, 5))

        progress_text = ctk.CTkLabel(
            self.current_frame,
            text="Step 2 of 3: Choose a Username",
            font=self.fonts["subheader"],
            text_color=self.palette["muted"]
        )
        progress_text.pack(pady=(0, 30))

        # Username input
        ctk.CTkLabel(
            self.current_frame,
            text="Username *",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))

        username_frame = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        username_frame.pack(pady=5)

        self.username = ctk.CTkEntry(
            username_frame,
            placeholder_text="Choose a unique username",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=300,
            height=35,
            font=self.fonts["body"]
        )
        self.username.pack(side="left", padx=5)

        check_btn = ctk.CTkButton(
            username_frame,
            text="Check",
            command=self.check_username_availability,
            width=100,
            height=35,
            fg_color=self.palette["accent"],
            hover_color=self.palette["accent_dark"],
            text_color="white",
            font=self.fonts["button"]
        )
        check_btn.pack(side="left", padx=5)

        # Rules
        rules_text = "4-20 characters | Letters and numbers only | No spaces"
        rules_label = ctk.CTkLabel(
            self.current_frame,
            text=rules_text,
            font=self.fonts["small"],
            text_color=self.palette["muted"]
        )
        rules_label.pack(pady=5)

        # Availability status
        self.username_status = ctk.CTkLabel(
            self.current_frame,
            text="",
            font=self.fonts["body"],
            text_color=self.palette["muted"]
        )
        self.username_status.pack(pady=10)

        # Suggestions frame (hidden by default)
        self.suggestions_frame = ctk.CTkFrame(
            self.current_frame,
            fg_color=self.palette["input_bg"],
            corner_radius=12,
            border_width=1,
            border_color=self.palette["border"]
        )

        # Error label
        self.username_error_label = ctk.CTkLabel(
            self.current_frame,
            text="",
            font=self.fonts["small"],
            text_color=self.palette["error"]
        )
        self.username_error_label.pack(pady=5)

        # Buttons
        button_frame = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        button_frame.pack(pady=30)

        back_btn = ctk.CTkButton(
            button_frame,
            text="Back",
            command=self.show_signup_personal_info,
            width=150,
            height=40,
            fg_color=self.palette["card"],
            text_color=self.palette["accent"],
            border_width=1,
            border_color=self.palette["accent"],
            hover_color=self.palette["input_bg"],
            font=self.fonts["button"]
        )
        back_btn.pack(side="left", padx=10)

        next_btn = ctk.CTkButton(
            button_frame,
            text="Next",
            command=self.validate_and_go_to_role,
            width=150,
            height=40,
            fg_color=self.palette["accent"],
            hover_color=self.palette["accent_dark"],
            text_color="white",
            font=self.fonts["button"]
        )
        next_btn.pack(side="left", padx=10)

    def check_username_availability(self):
        """Check if username is available"""
        username = self.username.get().strip()

        if not username:
            self.username_status.configure(text="Please enter a username", text_color=self.palette["error"])
            return

        # Validate format
        valid, msg = Validators.validate_username(username)
        if not valid:
            self.username_status.configure(text=msg, text_color=self.palette["error"])
            return

        # Check availability
        if self.user_manager.username_exists(username):
            self.username_status.configure(text="Username taken", text_color=self.palette["error"])

            # Show suggestions
            existing = self.user_manager.get_all_usernames()
            suggestions = suggest_alternative_usernames(username, existing)

            self.suggestions_frame.pack(pady=10)

            # Clear previous suggestions
            for widget in self.suggestions_frame.winfo_children():
                widget.destroy()

            ctk.CTkLabel(
                self.suggestions_frame,
                text="Suggestions:",
                font=self.fonts["small"]
            ).pack(pady=5)

            for suggestion in suggestions:
                btn = ctk.CTkButton(
                    self.suggestions_frame,
                    text=suggestion,
                    command=lambda s=suggestion: self.use_suggestion(s),
                    width=200,
                    height=30,
                    fg_color=self.palette["card"],
                    text_color=self.palette["accent"],
                    border_width=1,
                    border_color=self.palette["accent"],
                    hover_color=self.palette["input_bg"],
                    font=self.fonts["small"]
                )
                btn.pack(pady=2)
        else:
            self.username_status.configure(text="Username available", text_color=self.palette["success"])
            self.suggestions_frame.pack_forget()

    def use_suggestion(self, suggestion):
        """Use suggested username"""
        self.username.delete(0, "end")
        self.username.insert(0, suggestion)
        self.check_username_availability()
    
    def validate_and_go_to_role(self):
        """Validate username and proceed to role selection"""
        username = self.username.get().strip()
        
        if not username:
            self.username_error_label.configure(text="Please enter a username")
            return
        
        # Validate format
        valid, msg = Validators.validate_username(username)
        if not valid:
            self.username_error_label.configure(text=msg)
            return
        
        # Check availability
        if self.user_manager.username_exists(username):
            self.username_error_label.configure(text="Username is already taken")
            return
        
        # Store and proceed
        self.current_signup_data['username'] = username
        self.show_role_selection()
    
    def show_role_selection(self):
        """Display signup page - Step 3: Role Selection"""
        self.clear_frame()
        self.root.title(f"{APP_NAME} - Create Account (3 of 3)")
        self.root.geometry("660x720")

        self.current_frame = ctk.CTkScrollableFrame(
            self.root,
            fg_color=self.palette["card"],
            corner_radius=20,
            border_width=1,
            border_color=self.palette["border"]
        )
        self.current_frame.pack(fill="both", expand=True, padx=30, pady=30)

        # Header
        header = ctk.CTkLabel(
            self.current_frame,
            text="Create Your Account",
            font=self.fonts["header"],
            text_color=self.palette["text"]
        )
        header.pack(pady=(10, 5))

        progress_text = ctk.CTkLabel(
            self.current_frame,
            text="Step 3 of 3: Choose Your Role",
            font=self.fonts["subheader"],
            text_color=self.palette["muted"]
        )
        progress_text.pack(pady=(0, 20))

        # Role selection
        ctk.CTkLabel(
            self.current_frame,
            text="I am a...",
            font=self.fonts["subheader"],
            text_color=self.palette["text"]
        ).pack(pady=10)

        self.selected_role = ctk.StringVar(value="student")

        # Role cards
        roles_data = [
            ("student", "Student", "Track studies, assignments, and student life"),
            ("adult", "Adult/Professional", "Manage work, health, and personal growth"),
            ("senior", "Senior Citizen", "Monitor health, medication, and wellness"),
            ("custom", "Custom", "Build your own personalized tracker")
        ]

        for role_id, role_name, desc in roles_data:
            role_frame = ctk.CTkFrame(
                self.current_frame,
                fg_color=self.palette["input_bg"],
                corner_radius=12,
                border_width=1,
                border_color=self.palette["border"]
            )
            role_frame.pack(pady=5, padx=20, fill="x")

            radio = ctk.CTkRadioButton(
                role_frame,
                text=role_name,
                variable=self.selected_role,
                value=role_id,
                font=self.fonts["body_bold"]
            )
            radio.pack(anchor="w", padx=15, pady=10)

            desc_label = ctk.CTkLabel(
                role_frame,
                text=desc,
                font=self.fonts["small"],
                text_color=self.palette["muted"]
            )
            desc_label.pack(anchor="w", padx=40, pady=(0, 10))

        # Gender (optional)
        ctk.CTkLabel(
            self.current_frame,
            text="Gender (Optional)",
            font=self.fonts["subheader"],
            text_color=self.palette["text"]
        ).pack(pady=(20, 10))

        self.gender = ctk.StringVar(value="")

        gender_frame = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        gender_frame.pack(pady=5)

        for gender in ["Male", "Female", "Other", "Prefer not to say"]:
            ctk.CTkRadioButton(
                gender_frame,
                text=gender,
                variable=self.gender,
                value=gender.lower(),
                font=self.fonts["body"]
            ).pack(side="left", padx=10)

        # Buttons
        button_frame = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        button_frame.pack(pady=30)

        back_btn = ctk.CTkButton(
            button_frame,
            text="Back",
            command=self.show_username_creation,
            width=150,
            height=40,
            fg_color=self.palette["card"],
            text_color=self.palette["accent"],
            border_width=1,
            border_color=self.palette["accent"],
            hover_color=self.palette["input_bg"],
            font=self.fonts["button"]
        )
        back_btn.pack(side="left", padx=10)

        complete_btn = ctk.CTkButton(
            button_frame,
            text="Complete Setup",
            command=self.complete_signup,
            width=200,
            height=40,
            fg_color=self.palette["success"],
            hover_color=self.palette["success_dark"],
            text_color="white",
            font=self.fonts["button"]
        )
        complete_btn.pack(side="left", padx=10)

    def complete_signup(self):
        """Complete the signup process"""
        role = self.selected_role.get()
        gender = self.gender.get()
        
        # Add to signup data
        self.current_signup_data['role'] = role
        self.current_signup_data['gender'] = gender
        self.current_signup_data['timezone'] = 'UTC-5'
        self.current_signup_data['preferred_units'] = 'metric'
        
        # Create user
        success = self.user_manager.create_user(self.current_signup_data)
        
        if success:
            messagebox.showinfo(
                "Success",
                f"Account created successfully!\nUsername: {self.current_signup_data['username']}"
            )
            self.show_login_page()
        else:
            messagebox.showerror("Error", "Failed to create account. Please try again.")
    
    def show_password_recovery(self):
        """Display password recovery page"""
        self.clear_frame()
        self.root.title(f"{APP_NAME} - Password Recovery")
        self.root.geometry("560x620")

        self.current_frame = ctk.CTkFrame(
            self.root,
            fg_color=self.palette["card"],
            corner_radius=20,
            border_width=1,
            border_color=self.palette["border"]
        )
        self.current_frame.pack(fill="both", expand=True, padx=30, pady=30)

        # Header
        header = ctk.CTkLabel(
            self.current_frame,
            text="Account Recovery",
            font=self.fonts["header"],
            text_color=self.palette["text"]
        )
        header.pack(pady=(20, 30))

        # Username
        ctk.CTkLabel(
            self.current_frame,
            text="Username",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.recovery_username = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="Enter your username",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.recovery_username.pack(pady=5)

        # Phone number for verification
        ctk.CTkLabel(
            self.current_frame,
            text="Phone Number",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.recovery_phone = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="Enter registered phone number",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.recovery_phone.pack(pady=5)

        # New password
        ctk.CTkLabel(
            self.current_frame,
            text="New Password",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.recovery_new_password = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="Enter new password",
            show="*",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.recovery_new_password.pack(pady=5)

        # Confirm new password
        ctk.CTkLabel(
            self.current_frame,
            text="Confirm Password",
            font=self.fonts["label"],
            text_color=self.palette["muted"]
        ).pack(pady=(10, 5))
        self.recovery_confirm_password = ctk.CTkEntry(
            self.current_frame,
            placeholder_text="Confirm new password",
            show="*",
            placeholder_text_color=self.palette["muted"],
            fg_color=self.palette["input_bg"],
            border_color=self.palette["border"],
            text_color=self.palette["text"],
            width=350,
            height=35,
            font=self.fonts["body"]
        )
        self.recovery_confirm_password.pack(pady=5)

        # Error label
        self.recovery_error_label = ctk.CTkLabel(
            self.current_frame,
            text="",
            font=self.fonts["small"],
            text_color=self.palette["error"]
        )
        self.recovery_error_label.pack(pady=10)

        # Buttons
        button_frame = ctk.CTkFrame(self.current_frame, fg_color="transparent")
        button_frame.pack(pady=20)

        back_btn = ctk.CTkButton(
            button_frame,
            text="Back to Login",
            command=self.show_login_page,
            width=150,
            height=40,
            fg_color=self.palette["card"],
            text_color=self.palette["accent"],
            border_width=1,
            border_color=self.palette["accent"],
            hover_color=self.palette["input_bg"],
            font=self.fonts["button"]
        )
        back_btn.pack(side="left", padx=10)

        reset_btn = ctk.CTkButton(
            button_frame,
            text="Reset Password",
            command=self.handle_password_reset,
            width=150,
            height=40,
            fg_color=self.palette["accent"],
            hover_color=self.palette["accent_dark"],
            text_color="white",
            font=self.fonts["button"]
        )
        reset_btn.pack(side="left", padx=10)

    def handle_password_reset(self):
        """Handle password reset"""
        username = self.recovery_username.get().strip()
        phone = self.recovery_phone.get().strip()
        new_password = self.recovery_new_password.get()
        confirm_password = self.recovery_confirm_password.get()
        
        if not all([username, phone, new_password, confirm_password]):
            self.recovery_error_label.configure(text="Please fill in all fields")
            return
        
        # Verify user exists and phone matches
        user_data = self.user_manager.get_user_data(username)
        if not user_data:
            self.recovery_error_label.configure(text="Username not found")
            return
        
        if user_data['phone'] != phone:
            self.recovery_error_label.configure(text="Phone number doesn't match")
            return
        
        # Validate new password
        valid, msg, strength = Validators.validate_password(new_password)
        if not valid:
            self.recovery_error_label.configure(text=msg)
            return
        
        # Check passwords match
        if new_password != confirm_password:
            self.recovery_error_label.configure(text="Passwords do not match")
            return
        
        # Update password
        success = self.user_manager.update_password(username, new_password)
        
        if success:
            messagebox.showinfo("Success", "Password reset successfully!")
            self.show_login_page()
        else:
            self.recovery_error_label.configure(text="Failed to reset password")
    
    def run(self):
        """Run the authentication app"""
        self.root.mainloop()


if __name__ == "__main__":
    app = AuthenticationApp()
    app.run()
