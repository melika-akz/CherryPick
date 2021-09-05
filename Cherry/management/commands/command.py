from django.core.management import BaseCommand
from .extract_data import extract_excel
import traceback


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-i', '--insert', action='store_true', help='insert data to elasticSearch')
        
    def handle(self, *args, **options):
        try:
            if options['update']:
               extract_excel()

        except Exception as e:
            traceback.print_exc()
