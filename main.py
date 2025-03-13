from book_operations import BookData
from book_db import BookDB

# main file
def main():

    # Step 1: Fetch book data from external API
    api_url = "https://openlibrary.org/search.json?q=python"
    book_api = BookData(api_url)

    # Fetch and parse the data
    json_data = book_api.get_json_data()
    books = book_api.parse_json_data(json_data)

    # Step 2: Insert fetched books into the database
    db_url = 'sqlite:///books.db'
    db = BookDB(db_url)
    for book in books:
        db.add_book(book['title'], book['author'], book['published_date'])
    print(f"✅ Added {len(books)} books successfully!")

    # Step 3: Retrieve and display books from the database
    print("\n📖 Books currently in the database:")
    stored_books = db.get_books()
    for stored_book in stored_books:
        print(f"{stored_book.title} by {stored_book.author} (Published in {stored_book.published_date})")

    # Step 4: Update a book (Example)
    if stored_books:
        book_id = stored_books[0].id  # Get the first book's ID
        print(f"\n✏️ Updating Book ID {book_id}...")
        db.update_book(book_id, new_title="Updated Python Book")
        print("✅ Book updated successfully!")

    # Step 5: Delete a book (Example)
    if stored_books:
        book_id = stored_books[-1].id  # Get the last book's ID
        print(f"\n🗑️ Deleting Book ID {book_id}...")
        db.delete_book(book_id)
        print("✅ Book deleted successfully!")

    # Step 6: Retrieve books again to confirm changes
    print("\n📖 Books after update & delete:")
    stored_books = db.get_books()
    for stored_book in stored_books:
        print(f"{stored_book.id}: {stored_book.title} by {stored_book.author} (Published in {stored_book.published_date})")

    # ✅ Dispose of the database connection at the end
    db.engine.dispose()

if __name__ == '__main__':
    main()