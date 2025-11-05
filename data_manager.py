import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import transaction

def print_menu():
    menu = """
    Manage Data Tool
    ================
    1. Clear Data from Database
    2. Generate Data to Database
    3. Import Data from csv
    4. Export Data to csv
    5. Exit
    """
    print(menu)

def clear_data():
    from datastorages.models import Category, Product, Order
    
    confirm = input("Are you sure you want to clear all data? (y/n): ")
    if confirm == 'y':
        try:
            with transaction.atomic():
                Order.objects.all().delete()
                Product.objects.all().delete()
                Category.objects.all().delete()
            print("✓ All data cleared successfully!")
        except Exception as e:
            print(f"✗ Error clearing data: {e}")
    else:
        print("Operation cancelled.")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            clear_data()
        elif choice == '2':
            from generate_data import generate_sample_data
            generate_sample_data()
        elif choice == '3':
            from import_data import import_from_csv
            import_from_csv()
        elif choice == '4':
            from export_data import export_to_csv
            export_to_csv()
        elif choice == '5':
            print("Thanks for your time! Have a nice day! ^.^")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()