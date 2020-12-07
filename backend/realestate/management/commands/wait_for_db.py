import time 

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    ''' dajango pause command to wait for the database is available '''

    def handle(self, *args, **options):
        self.stdout.write('Waiting for the database...')
        db_conn = None
        while not db_conn:
             try:
                 db_conn = connections['default']
             except OperationalError:
                 self.stdout.write(self.style.ERROR('Database is not available...'))
                 time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is available!!!'))
                 
            
        
