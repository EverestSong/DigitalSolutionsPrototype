import csv

from django.core.management import BaseCommand
from Page1.models import teacher

class Command(BaseCommand):
    help = "Import Teacher data (Name, Email, Area) from a CSV file and create models."
     
    def add_arguments(self, parser):
        parser.add_argument("--path", type = str)

    def handle(self, *args, **kwargs):
        createdCount = 0
        updatedCount = 0

        path = kwargs['path']
        with open(path, 'rt', encoding = 'utf-8-sig') as f:
            reader = csv.DictReader(f, dialect = 'excel')

            for row in reader:
                obj, created = teacher.objects.update_or_create(
                    Email=row["Email"], 
                    defaults = {"Name" : row["Name"], "Area" : row["Area"]})

                if created:
                    createdCount += 1
                else:
                    updatedCount += 1

        print(f"Created {createdCount} teachers, updated {updatedCount} teachers.")