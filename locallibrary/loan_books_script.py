import os
import django
from datetime import date, timedelta
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")
django.setup()

from catalog.models import BookInstance
from django.contrib.auth.models import User


def loan_books_to_users():
    # Get the test users
    user1 = User.objects.get(username='user1')
    user2 = User.objects.get(username='user2')

    # Get available book instances
    available_instances = BookInstance.objects.filter(status='a')

    # Randomly select and loan 3 books for each user
    for user in [user1, user2]:
        selected_instances = random.sample(list(available_instances), 3)

        for instance in selected_instances:
            instance.borrower = user
            instance.status = 'o'  # On loan
            # Randomly set due dates in the future or the past
            if random.choice([True, False]):
                due_date = date.today() + timedelta(days=random.randint(1, 7))  # Due back in the next 1 to 7 days
            else:
                due_date = date.today() - timedelta(days=random.randint(1, 14))  # Due back in the past 1 to 14 days
            instance.due_back = due_date
            instance.save()

    # Update remaining on-loan instances without borrower
    on_loan_instances = BookInstance.objects.filter(status='o', borrower=None)
    for instance in on_loan_instances:
        instance.borrower = random.choice([user1, user2])
        instance.save()

    print("Books loaned successfully!")


if __name__ == "__main__":
    loan_books_to_users()
