import os
import json

from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.contrib.auth.models import User
from django.conf import settings

import json, os

JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(settings.JSON_PATH, file_name + '.json'),
              'r',
              encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):
    help = 'Fill DB new Data'

    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()

        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        product = load_from_json('products')

        Product.objects.all().delete()

        for prod in product:
            category_name = prod['category']
            prod['category'] = ProductCategory.objects.get(name=category_name)
            new_product = Product(**prod)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        super_user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
