import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from consumer.models.consumer import Consumer

PATH_TO_CONSUMER_CSV_FILE = os.path.join(settings.BASE_DIR, "consumer/assets/consumers.csv")


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(PATH_TO_CONSUMER_CSV_FILE, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                Consumer.objects.create(id=row['id'], street=row['street'],
                                        status=row['status'], previous_jobs_count=row['previous_jobs_count'],
                                        amount_due=row['amount_due'],
                                        lat=row['lat'], lng=row['lng'])
