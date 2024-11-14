from flask import Blueprint
from controllers.AuthorController import get_author, add_author, update_author, delete_author

author_bp = Blueprint('author_bp', __name__)

# Route for getting all books
author_bp.route('/api/author', methods=['GET'])(get_author)

# Route for getting a specific book
author_bp.route('/api/author/<int:author_id>', methods=['GET'])(get_author)

# Route for creating a new book
author_bp.route('/api/author', methods=['POST'])(add_author)

# Route for updating a specific book (PATCH)
author_bp.route('/api/author/<int:author_id>', methods=['PATCH'])(update_author)


# Route for deleting a specific book (DELETE)
author_bp.route('/api/author/<int:author_id>', methods=['DELETE'])(delete_author)