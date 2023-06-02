from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book, delete_book
from models.book import *

@app.route("/books")
def index():
    return render_template("index.html", title="Home", books=books)

@app.route("/books/<index>")
def chosen_book(index):
    chosen_book = books[int(index)]
    return render_template("book_detail.html", book=chosen_book )

@app.route("/books", methods=["POST"])
def add_book():
    checked_out = True if "checked_out" in request.form else False
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    publisher = request.form["publisher"]
    description = request.form["description"]
    newbook = Book(
        title=title,
        author=author,
        genre=genre,
        publisher=publisher,
        description=description,
        checked_out = checked_out    
        )
    add_new_book(newbook)
    return redirect ("/books")

@app.route("/books/delete/<index>", methods=["POST"])
def delete_by_index(index):
    delete_book(int(index))
    return redirect ("/books")


    
