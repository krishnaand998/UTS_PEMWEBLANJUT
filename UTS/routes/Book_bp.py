from flask import Blueprint
from controllers.BookController import get_books, add_book, update_book, delete_book

book_bp = Blueprint('book_bp', __name__)

# Route for getting all books
book_bp.route('/api/books', methods=['GET'])(get_books)


# Route for creating a new book
book_bp.route('/api/books', methods=['POST'])(add_book)

# Route for updating a specific book (PATCH)
book_bp.route('/api/books/<int:book_id>', methods=['PATCH'])(update_book)

# Route for deleting a specific book (DELETE)
book_bp.route('/api/books/<int:book_id>', methods=['DELETE'])(delete_book)