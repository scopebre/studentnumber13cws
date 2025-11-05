import os
import csv
import django
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from datastorages.models import Category, Product, Order

def export_to_csv():
    try:
        # Export Categories
        with open('categories.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'description'])
            for category in Category.objects.all():
                writer.writerow([category.name, category.description])
        print("✓ Exported categories to categories.csv")
        
        # Export Products
        with open('products.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'description', 'price', 'category', 'stock_quantity'])
            for product in Product.objects.all():
                writer.writerow([
                    product.name,
                    product.description,
                    product.price,
                    product.category.name,
                    product.stock_quantity
                ])
        print("✓ Exported products to products.csv")
        
        # Export Orders
        with open('orders.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['product', 'quantity', 'total_price', 'customer_name', 'customer_email'])
            for order in Order.objects.all():
                writer.writerow([
                    order.product.name,
                    order.quantity,
                    order.total_price,
                    order.customer_name,
                    order.customer_email
                ])
        print("✓ Exported orders to orders.csv")
        
        print("✓ Data exported successfully!")
        
    except Exception as e:
        print(f"✗ Error exporting to CSV: {e}")

if __name__ == "__main__":
    export_to_csv()