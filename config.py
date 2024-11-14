from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Membuat aplikasi Flask
app = Flask(__name__)

# Konfigurasi database MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://kris_lineshipis:7cd804800304874f9de124132c7851345564c718@j-nhi.h.filess.io:3305/kris_lineshipis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi objek database
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "home"

app.app_context().push()