from unittest.mock import patch
# call a management command from code
from django.core.management import call_command
from django.db.utils import OperationalError
#https://docs.djangoproject.com/en/3.1/topics/testing/overview/
from django.test import TestCase


class CommmandTests(TestCase):
    def test_wait_for_db_ready(self):
        '''
        test for the database is ready/available
        (means no OperationalErrot)
        '''
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        '''Testing wait for db'''
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertGreaterEqual(gi.call_count, 6)




