from django.core.management.base import BaseCommand

from universities.import_data import import_data


class Command(BaseCommand):
    help = 'Import data from csv file'

    def handle(self, *args, **options):
        try:
            import_data()
            print("Done")
        except Exception as e:
            print(e)