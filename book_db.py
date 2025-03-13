from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Step 1: Define the table structure
Base = declarative_base()

class BookFields(Base):
    __tablename__ = 'books_table'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    published_date = Column(Integer)

    def __repr__(self):
        return f"<BookFields(title={self.title}, author={self.author}, published_date={self.published_date})>"

class BookDB:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_book(self, title, author, published_date):
        """Adds a book to the database, ensuring no duplicates."""
        session = self.Session()

        # Check if the book already exists in the database
        existing_book = session.query(BookFields).filter_by(title=title, author=author).first()

        if existing_book:
            print(f"Error: The book '{title}' by {author} already exists in the database.")
            session.close()
            return  # Return early if the book exists

        # If the book doesn't exist, add the new book
        new_book = BookFields(title=title, author=author, published_date=published_date)
        session.add(new_book)
        session.commit()
        print(f"✅ Book '{title}' by {author} added successfully!")

        session.close()

    def get_books(self):
        """Fetches all books from the database."""
        session = self.Session()
        books = session.query(BookFields).all()
        session.close()
        return books

    def update_book(self, book_id, new_title=None, new_author=None, new_published_date=None):
        """Updates a book in the database."""
        session = self.Session()

        # Find the book by its ID
        book = session.query(BookFields).filter(BookFields.id == book_id).first()

        if book:  # If the book is found, update it
            if new_title:
                book.title = new_title
            if new_author:
                book.author = new_author
            if new_published_date:
                book.published_date = new_published_date

            session.commit()  # Save the changes to the database
            print(f"Book {book_id} updated.")
        else:
            print(f"Book {book_id} not found.")

        session.close()

    def delete_book(self, book_id):
        """Deletes a book from the database."""
        session = self.Session()

        # Find the book by its ID
        book = session.query(BookFields).filter(BookFields.id == book_id).first()

        if book:  # If the book is found, delete it
            session.delete(book)  # Delete the book
            session.commit()  # Save the changes to the database
            print(f"Book {book_id} deleted.")
        else:
            print(f"Book {book_id} not found.")

        session.close()

