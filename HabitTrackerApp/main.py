"""
Main Entry Point for Habit & Lifestyle Tracker Application
Run this file to start the application
"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import and run authentication app
from auth import AuthenticationApp
from config import APP_NAME, APP_TAGLINE


def main():
    """Main entry point"""
    print("=" * 60)
    print(f"  {APP_NAME}")
    print(f"  {APP_TAGLINE}")
    print("=" * 60)
    print()
    print("Starting application...")
    print()
    
    try:
        # Create and run authentication app
        app = AuthenticationApp()
        app.run()
    except Exception as e:
        print(f"Error starting application: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")


if __name__ == "__main__":
    main()
