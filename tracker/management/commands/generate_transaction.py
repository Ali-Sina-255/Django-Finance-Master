import random
from faker import Faker

from django.core.management.base import BaseCommand
from tracker.models import Transaction,Category, User

class Command(BaseCommand):
    help = 'Generate Transaction for testing'

    def handle(self, *args, **options):
        fake = Faker()
        # create category
        categories = ['Bills', 'Foot', 'Cloths', 'Medical', 'Housing','Salary','Social','Transport','Vacations']
        for category in categories:
            Category.objects.get_or_create(name= category)
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admins', password='open allah.')
        categories = Category.objects.all()
        types =   [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICE]
        for i in range(20):
            Transaction.objects.create(
                category = random.choice(categories),
                user=user,
                amount = random.uniform(1,2500),
                date = fake.date_between(start_date='-1y',end_date='today'),
                type = types
            )