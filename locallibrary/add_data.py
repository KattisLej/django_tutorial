import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")
django.setup()

from catalog.models import Author, Genre, Language, Book
def add_authors_and_books():
    # Create authors
    author1 = Author.objects.create(first_name='J.K.', last_name='Rowling', date_of_birth='1965-07-31')
    author2 = Author.objects.create(first_name='George', last_name='R.R. Martin', date_of_birth='1948-09-20')

    # Create genres
    genre1 = Genre.objects.create(name='Fantasy')
    genre2 = Genre.objects.create(name='Science Fiction')

    # Create languages
    language1 = Language.objects.create(name='English')
    language2 = Language.objects.create(name='Farsi')

    # Create books
    book1 = Book.objects.create(title='Harry Potter and the Philosopher\'s Stone', author=author1, summary='The first book in the Harry Potter series.', isbn='9780747532743', language=language1)
    book1.genre.add(genre1)

    book2 = Book.objects.create(title='A Game of Thrones', author=author2, summary='The first book in the A Song of Ice and Fire series.', isbn='9780553103540', language=language1)
    book2.genre.add(genre1)

    book3 = Book.objects.create(title='Harry Potter and the Chamber of Secrets', author=author1, summary='The second book in the Harry Potter series.', isbn='9780439064873', language=language1)
    book3.genre.add(genre1)

    book4 = Book.objects.create(title='A Clash of Kings', author=author2, summary='The second book in the A Song of Ice and Fire series.', isbn='9780553108033', language=language1)
    book4.genre.add(genre1)

    book5 = Book.objects.create(title='Harry Potter and the Prisoner of Azkaban', author=author1, summary='The third book in the Harry Potter series.', isbn='9780439136365', language=language1)
    book5.genre.add(genre1)

    book6 = Book.objects.create(title='Harry Potter and the Goblet of Fire', author=author1, summary='The fourth book in the Harry Potter series.', isbn='9780439139595', language=language1)
    book6.genre.add(genre1)

    book7 = Book.objects.create(title='A Storm of Swords', author=author2, summary='The third book in the A Song of Ice and Fire series.', isbn='9780553106633', language=language1)
    book7.genre.add(genre1)

    book8 = Book.objects.create(title='Harry Potter and the Order of the Phoenix', author=author1, summary='The fifth book in the Harry Potter series.', isbn='9780439358071', language=language1)
    book8.genre.add(genre1)

    book9 = Book.objects.create(title='Harry Potter and the Half-Blood Prince', author=author1, summary='The sixth book in the Harry Potter series.', isbn='9780439784542', language=language1)
    book9.genre.add(genre1)

    book10 = Book.objects.create(title='Harry Potter and the Deathly Hallows', author=author1, summary='The seventh and final book in the Harry Potter series.', isbn='9780545139700', language=language1)
    book10.genre.add(genre1)

    print("Data added successfully!")

if __name__ == "__main__":
    add_authors_and_books()
