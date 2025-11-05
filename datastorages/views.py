from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product, Order
import sys
import os

# Add the project root to Python path to import our scripts
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def data_dashboard(request):
    categories_count = Category.objects.count()
    products_count = Product.objects.count()
    orders_count = Order.objects.count()
    
    return render(request, 'datastorages/data_dashboard.html', {
        'categories_count': categories_count,
        'products_count': products_count,
        'orders_count': orders_count,
    })

def generate_data(request):
    try:
        # Import and run generate_data
        from generate_data import generate_sample_data
        generate_sample_data()
        return redirect('data_dashboard')
    except Exception as e:
        categories_count = Category.objects.count()
        products_count = Product.objects.count()
        orders_count = Order.objects.count()
        return render(request, 'datastorages/data_dashboard.html', {
            'categories_count': categories_count,
            'products_count': products_count,
            'orders_count': orders_count,
            'message': f'Error generating data: {e}',
            'message_type': 'error'
        })

def import_data(request):
    try:
        # Check if CSV files exist before importing
        csv_files = ['categories.csv', 'products.csv', 'orders.csv']
        missing_files = []
        
        for csv_file in csv_files:
            if not os.path.exists(csv_file):
                missing_files.append(csv_file)
        
        if missing_files:
            categories_count = Category.objects.count()
            products_count = Product.objects.count()
            orders_count = Order.objects.count()
            missing_files_str = ", ".join(missing_files)
            return render(request, 'datastorages/data_dashboard.html', {
                'categories_count': categories_count,
                'products_count': products_count,
                'orders_count': orders_count,
                'message': f'Missing CSV files: {missing_files_str}. Please make sure these files exist in the project root directory.',
                'message_type': 'error'
            })
        
        # Import and run import_data
        from import_data import import_from_csv
        import_from_csv()
        
        # Success message
        categories_count = Category.objects.count()
        products_count = Product.objects.count()
        orders_count = Order.objects.count()
        return render(request, 'datastorages/data_dashboard.html', {
            'categories_count': categories_count,
            'products_count': products_count,
            'orders_count': orders_count,
            'message': 'Data imported successfully from CSV files!',
            'message_type': 'success'
        })
        
    except Exception as e:
        categories_count = Category.objects.count()
        products_count = Product.objects.count()
        orders_count = Order.objects.count()
        return render(request, 'datastorages/data_dashboard.html', {
            'categories_count': categories_count,
            'products_count': products_count,
            'orders_count': orders_count,
            'message': f'Error importing data: {e}',
            'message_type': 'error'
        })

def clear_data(request):
    try:
        from django.db import transaction
        with transaction.atomic():
            Order.objects.all().delete()
            Product.objects.all().delete()
            Category.objects.all().delete()
        
        # Success message
        categories_count = Category.objects.count()
        products_count = Product.objects.count()
        orders_count = Order.objects.count()
        return render(request, 'datastorages/data_dashboard.html', {
            'categories_count': categories_count,
            'products_count': products_count,
            'orders_count': orders_count,
            'message': 'All data cleared successfully!',
            'message_type': 'success'
        })
    except Exception as e:
        categories_count = Category.objects.count()
        products_count = Product.objects.count()
        orders_count = Order.objects.count()
        return render(request, 'datastorages/data_dashboard.html', {
            'categories_count': categories_count,
            'products_count': products_count,
            'orders_count': orders_count,
            'message': f'Error clearing data: {e}',
            'message_type': 'error'
        })

def export_data(request):
    try:
        # Import and run export_data
        from export_data import export_to_csv
        export_to_csv()
        
        # Success message
        categories_count = Category.objects.count()
        products_count = Product.objects.count()
        orders_count = Order.objects.count()
        return render(request, 'datastorages/data_dashboard.html', {
            'categories_count': categories_count,
            'products_count': products_count,
            'orders_count': orders_count,
            'message': 'Data exported successfully to CSV files!',
            'message_type': 'success'
        })
    except Exception as e:
        categories_count = Category.objects.count()
        products_count = Product.objects.count()
        orders_count = Order.objects.count()
        return render(request, 'datastorages/data_dashboard.html', {
            'categories_count': categories_count,
            'products_count': products_count,
            'orders_count': orders_count,
            'message': f'Error exporting data: {e}',
            'message_type': 'error'
        })