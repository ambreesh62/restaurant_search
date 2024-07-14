import pandas as pd
from django.core.management.base import BaseCommand
from searchapp.models import Dish

class Command(BaseCommand):
    help = 'Load data from CSV into database'

    def handle(self, *args, **kwargs):
        url = "https://python-exercise.s3.ap-south-1.amazonaws.com/restaurants_small.csv"
        df = pd.read_csv(url)

        for _, row in df.iterrows():
            items = row['items'].split(',')  # Split items into a list

            for item in items:
                item = item.strip()  # Remove leading/trailing spaces
                if not Dish.objects.filter(name=item, restaurant=row['location']).exists():
                    # Initialize rating as None
                    rating = None

                    # Check if 'Rating:' is present in full_details and parse rating
                    if isinstance(row['full_details'], str) and 'Rating:' in row['full_details']:
                        rating_str = row['full_details'].split('Rating:')[1].strip()
                        try:
                            rating = float(rating_str)
                        except ValueError:
                            pass  # Handle if rating format is not as expected

                    Dish.objects.create(
                        name=item,
                        restaurant=row['location'],
                        rating=rating
                    )

        self.stdout.write(self.style.SUCCESS('Successfully loaded data'))
