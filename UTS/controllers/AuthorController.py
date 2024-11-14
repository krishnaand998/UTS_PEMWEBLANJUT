from flask import jsonify, request
from models.AuthorModel import Author



def get_authors():
    authors = Author.query.all()
    return jsonify([author.to_dict() for author in authors])


def get_author(id):
    author = Author.query.get(id)
    if not author:
        return jsonify({'error': 'Author not found'}), 404
    return jsonify(author.to_dict())


def add_author():
    new_author_data = request.get_json()
    new_author = Author(name=new_author_data['name'])
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'message': 'Author added successfully!', 'author': new_author.to_dict()}), 201


def update_author(id):
    author = Author.query.get(id)
    if not author:
        return jsonify({'error': 'Author not found'}), 404
    updated_data = request.get_json()
    author.name = updated_data.get('name', author.name)
    db.session.commit()
    return jsonify({'message': 'Author updated successfully!', 'author': author.to_dict()})


def delete_author(id):
    author = Author.query.get(id)
    if not author:
        return jsonify({'error': 'Author not found'}), 404
    db.session.delete(author)
    db.session.commit()
    return jsonify({'message': 'Author deleted successfully!'})
