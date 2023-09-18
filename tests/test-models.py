from django.test import TestCase
from Restaurant.models import Menu
from datetime import datetime


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title='title1', price=19.99, inventory=100)
        self.assertEqual(item.__str__(), "title1 : 19.99")
