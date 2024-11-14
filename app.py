from config import app, db
from routes.Book_bp import book_bp
from routes.Category_bp import category_bp
from routes.Author_bp import author_bp


app.register_blueprint(book_bp)
app.register_blueprint(category_bp)
app.register_blueprint(author_bp)

# Remove the if __name__ == '__main__': block
# and run the app with WSGI server

#if _name_ == "_main_":
#    app.run()
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)