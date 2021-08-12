from django.core.management import BaseCommand
from .extract_data import extract_data_excel
import traceback


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-u', '--update', action='store_true', help='update database & elasticSearch')
        
    def handle(self, *args, **options):
        try:
            if options['update']:
               extract_data_excel()

        except Exception as e:
            traceback.print_exc()