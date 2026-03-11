import csv

from django.core.management import BaseCommand
from Page1.models import teacher

class Command(BaseCommand):
    help = "Import Teacher data (Name, Email, Area) from a CSV file and create models."
     
    def add_arguments(self, parser):
        parser.add_argument("--path", type = str)

    def handle(self, *args, **kwargs):
        
        path = kwargs['path']
        with open(path, 'rt', encoding = 'utf-8-sig') as f:
            reader = csv.DictReader(f, dialect = 'excel')
            count = 0
            for row in reader:
                teacher.objects.create(Name=row["Name"], Email=row["Email"], Area=row["Area"])
                count += 1
        print("Added " + str(count) + " teacher(s)")