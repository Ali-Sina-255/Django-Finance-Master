import random
from faker  import Faker 
from django.core.management.base import BaseCommand
from tracker.models import Transaction,Category, User

class Command(BaseCommand):
    help = 'Generate Transaction for testing'

    def handle(self, *args, **options):
        fake = Faker()
        # create category
        categories = ['Bills', 'Foot', 'Cloths', 'Medical', 'Housing','Salary','Social','Transport','Vacations']
        return 