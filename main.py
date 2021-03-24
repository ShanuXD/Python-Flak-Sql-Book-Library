from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
# import sqlite3


app = Flask(__name__)

# all_books = ["Blech(Manga)-9/10", "One Piece(Manga)-9.5/10"]
# db = sqlite3.connect("books.collections.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY UNIQUE,title varchar(250) NOT NULL UNIQUE, author varcahr(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES (1, 'MY HERO ACADEMIA','Horikoshi Kouhei', '9.1')")
# cursor.execute("INSERT INTO books VALUES(101, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-book-collection.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False)
#
#
# db.create_all()

# book_1 = Book(id=1, title="MY HERO ACADEMIA", author="Horikoshi Kouhei", rating=9.3)
# book_2 = Book(id=2, title="One Piece", author="Eiichiro Oda", rating=9.5)
# db.session.add(book_1)
# db.session.add(book_2)
db.session.commit()

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add")
def add():
    pass


if __name__ == "__main__":
    app.run(debug=True)

