"""
Djnago command to wait for the db to be available.
This is useful for containers to ensure that the db is up and running
"""
import time

from psycopg2 import OperationalError as psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        """
        stdout.write command is running in the background,we can see the output
        """
        self.stdout.write("waiting for database.....")

        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
