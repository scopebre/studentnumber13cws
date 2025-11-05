import os
import django
import sys
import random
from faker import Faker

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import transaction
from datastorages.models import Category, Product, Order

def generate_sample_data():
    try:
        fake = Faker()
        
        # Get counts before generation
        categories_before = Category.objects.count()
        products_before = Product.objects.count()
        orders_before = Order.objects.count()
        
        print("Before generation:")
        print(f"  Categories: {categories_before}")
        print(f"  Products: {products_before}")
        print(f"  Orders: {orders_before}")
        
        with transaction.atomic():
            # Get the next available ID to make names unique
            next_category_id = Category.objects.count() + 1
            
            # Create Categories with random data - exactly 25
            category_base_names = [
                "Electronics", "Books", "Clothing", "Home & Garden", "Sports", 
                "Toys", "Beauty", "Automotive", "Food", "Health",
                "Furniture", "Jewelry", "Music", "Movies", "Art",
                "Office", "Pet", "Baby", "Tools", "Gardening",
                "Fitness", "Travel", "Stationery", "Crafts", "Party"
            ]
            
            categories = []
            for i, base_name in enumerate(category_base_names):
                # Create unique category name using next available ID
                category_name = f"{base_name} {next_category_id + i}"
                category = Category.objects.create(
                    name=category_name,
                    description=fake.text(max_nb_chars=100)
                )
                categories.append(category)
                print(f"Created category: {category.name}")
            
            # Get the next available product ID
            next_product_id = Product.objects.count() + 1
            
            # Create Products with random data - exactly 25
            products = []
            product_templates = [
                ("Wireless", ["Headphones", "Mouse", "Keyboard", "Speaker", "Charger"]),
                ("Smart", ["Phone", "Watch", "TV", "Home", "Device"]),
                ("Portable", ["Speaker", "Charger", "Projector", "Monitor", "Storage"]),
                ("Gaming", ["Mouse", "Keyboard", "Headset", "Controller", "Monitor"]),
                ("Professional", ["Camera", "Microphone", "Tablet", "Laptop", "Display"])
            ]
            
            for i in range(25):
                # Generate unique product name using next available ID
                prefix_type = random.choice(product_templates)
                product_name = f"{prefix_type[0]} {random.choice(prefix_type[1])} {next_product_id + i}"
                
                product = Product.objects.create(
                    name=product_name,
                    description=fake.text(max_nb_chars=200),
                    price=round(random.uniform(10.0, 2000.0), 2),
                    category=random.choice(categories),
                    stock_quantity=random.randint(5, 200)
                )
                products.append(product)
                print(f"Created product: {product.name} - ${product.price}")
            
            # Create Orders with random data - exactly 25
            for i in range(25):
                product = random.choice(products)
                quantity = random.randint(1, 5)
                total_price = round(product.price * quantity, 2)
                
                order = Order.objects.create(
                    product=product,
                    quantity=quantity,
                    total_price=total_price,
                    customer_name=fake.name(),
                    customer_email=fake.email()
                )
                print(f"Created order: {order.customer_name} - {order.product.name} x{order.quantity}")
            
            # Get counts after generation
            categories_after = Category.objects.count()
            products_after = Product.objects.count()
            orders_after = Order.objects.count()
            
            # Calculate new records created
            new_categories_count = categories_after - categories_before
            new_products_count = products_after - products_before
            new_orders_count = orders_after - orders_before
            
            print(f"\nData Generation Summary:")
            print(f"  Categories: {categories_before} -> {categories_after} (+{new_categories_count} new)")
            print(f"  Products: {products_before} -> {products_after} (+{new_products_count} new)")
            print(f"  Orders: {orders_before} -> {orders_after} (+{new_orders_count} new)")
            
            print(f"Successfully generated {new_categories_count} new categories, {new_products_count} new products, and {new_orders_count} new orders!")
            
    except Exception as e:
        print(f"Error generating data: {e}")

if __name__ == "__main__":
    generate_sample_data()