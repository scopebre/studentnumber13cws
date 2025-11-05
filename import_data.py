import os
import csv
import django
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from datastorages.models import Category, Product, Order

def import_from_csv():
    try:
        files_imported = 0
        
        # Import Categories
        if os.path.exists('categories.csv'):
            with open('categories.csv', 'r') as file:
                reader = csv.DictReader(file)
                category_count = 0
                for row in reader:
                    Category.objects.get_or_create(
                        name=row['name'],
                        description=row['description']
                    )
                    category_count += 1
                print(f"✓ Imported {category_count} categories from categories.csv")
                files_imported += 1
        else:
            print("✗ categories.csv file not found")
        
        # Import Products
        if os.path.exists('products.csv'):
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                product_count = 0
                for row in reader:
                    try:
                        category = Category.objects.get(name=row['category'])
                        Product.objects.get_or_create(
                            name=row['name'],
                            defaults={
                                'description': row['description'],
                                'price': row['price'],
                                'category': category,
                                'stock_quantity': row['stock_quantity']
                            }
                        )
                        product_count += 1
                    except Category.DoesNotExist:
                        print(f"✗ Category '{row['category']}' not found for product '{row['name']}'")
            print(f"✓ Imported {product_count} products from products.csv")
            files_imported += 1
        else:
            print("✗ products.csv file not found")
        
        # Import Orders
        if os.path.exists('orders.csv'):
            with open('orders.csv', 'r') as file:
                reader = csv.DictReader(file)
                order_count = 0
                for row in reader:
                    try:
                        product = Product.objects.get(name=row['product'])
                        Order.objects.get_or_create(
                            product=product,
                            customer_name=row['customer_name'],
                            defaults={
                                'quantity': row['quantity'],
                                'total_price': row['total_price'],
                                'customer_email': row['customer_email']
                            }
                        )
                        order_count += 1
                    except Product.DoesNotExist:
                        print(f"✗ Product '{row['product']}' not found for order")
            print(f"✓ Imported {order_count} orders from orders.csv")
            files_imported += 1
        else:
            print("✗ orders.csv file not found")
        
        if files_imported > 0:
            print(f"✓ CSV import completed! {files_imported} files processed.")
        else:
            print("✗ No CSV files found for import. Please make sure categories.csv, products.csv, and orders.csv exist.")
        
    except Exception as e:
        print(f"✗ Error importing from CSV: {e}")

if __name__ == "__main__":
    import_from_csv()