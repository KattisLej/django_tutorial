import os
import django
from datetime import date, timedelta
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")
django.setup()

from catalog.models import BookInstance, Book

def add_book_instances():
    books = Book.objects.all()

    # Define status choices
    status_choices = ['m', 'o', 'a', 'r']  # 'm': Maintenance, 'o': On loan, 'a': Available, 'r': Reserved

    # Create book instances for each book
    for book in books:
        num_instances = random.randint(2, 5)  # Number of instances per book (2 to 5)

        for _ in range(num_instances):
            status = random.choice(status_choices)
            due_back = None

            # If the status is not 'Available', set a future due back date
            if status != 'a':
                due_back = date.today() + timedelta(days=random.randint(7, 30))  # Due back date within the next 7 to 30 days

            BookInstance.objects.create(
                book=book,
                imprint=f"Imprint for {book.title}",
                status=status,
                due_back=due_back,
            )

    print("Book instances added successfully!")

if __name__ == "__main__":
    add_book_instances()
