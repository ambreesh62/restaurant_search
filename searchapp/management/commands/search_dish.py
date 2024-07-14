from django.core.management.base import BaseCommand
from searchapp.models import Dish

class Command(BaseCommand):
    help = 'Search for a dish by name'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the dish to search for')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        dishes = Dish.objects.filter(name__icontains=name)
        
        if dishes.exists():
            for dish in dishes:
                self.stdout.write(f'{dish.name} - {dish.restaurant} - {dish.rating}')
        else:
            self.stdout.write(self.style.ERROR('No dishes found'))
