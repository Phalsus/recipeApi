"""
Test custom django managements commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as psycopg2_error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db if db is ready"""
        patched_check.return_value = True

        call_command("wait_for_db")

        patched_check.assert_called_once_with(databases=["default"])

    def test_wait_for_db_delay(self, patched_check):
        """Test waiting for db when getting operational error"""
        patched_check.side_effect = [psycopg2_error] * 2 + \
            [OperationalError] * 3 + [True] 