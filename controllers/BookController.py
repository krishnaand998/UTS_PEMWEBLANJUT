from flask import jsonify, request
from models.BookModel import Book
from models.CategoryModel import Category
from models.AuthorModel import Author

# Routes for Book

def get_books():
    books = Book.query.all()
    books_with_details = []

    for book in books:
        category = Category.query.get(book.category_id)
        author = Author.query.get(book.author_id)
        books_with_details.append({
            'id': book.id,
            'title': book.title,
            'year': book.year,
            'category_name': category.name if category else "No Category",
            'author_name': author.name if author else "No Author"
        })

    return jsonify({'status': 'success', 'data': {'books': books_with_details}, 'message': 'Books retrieved successfully'}), 200


def add_book():
    new_book_data = request.get_json()
    new_book = Book(
        title=new_book_data['title'],
        year=new_book_data['year'],
        category_id=new_book_data['category_id'],
        author_id=new_book_data['author_id']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully!', 'book': new_book.to_dict()}), 201


def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    updated_data = request.get_json()
    book.title = updated_data.get('title', book.title)
    book.year = updated_data.get('year', book.year)
    book.category_id = updated_data.get('category_id', book.category_id)
    book.author_id = updated_data.get('author_id', book.author_id)
    db.session.commit()
    return jsonify({'message': 'Book updated successfully!', 'book': book.to_dict()})

def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully!'})
