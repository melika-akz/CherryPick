from django.core.management import BaseCommand
from .extract_data import extract_excel
from .RealStateMapping import creat_realState
import traceback


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-i', '--insert', action='store_true', help='make index and insert data to elasticSearch')
        parser.add_argument('-m', '--make', action='store_true', help='make index realstate and insert data to elasticSearch')
        
    def handle(self, *args, **options):
        try:
            if options['insert']:
               extract_excel()

            if options['make']:
               creat_realState()

        except Exception as e:
            traceback.print_exc()
