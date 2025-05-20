"""
Djnago command to wait for the database to be available.
This is useful for Docker containers to ensure that the database is up and running
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database"""
    
    def handle(self, *args, **options):
        pass