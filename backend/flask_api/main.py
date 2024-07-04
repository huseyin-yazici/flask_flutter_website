from flask import Flask, request, jsonify
from flask_cors import CORS
from firebase_config import db

app = Flask(__name__)
CORS(app)

class Book:
    def __init__(self, title, author, summary, bookPic, country, writer, writerPic, year,categories):
        self.title = title
        self.author = author
        self.summary = summary
        self.bookPic = bookPic
        self.country = country
        self.writer = writer
        self.writerPic = writerPic
        self.year = year
        self.categories=categories

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    book = Book(
        title=data['title'],
        author=data['author'],
        summary=data['summary'],
        bookPic=data['bookPic'],
        country=data['country'],
        writer=data['writer'],
        writerPic=data['writerPic'],
        year=data['year'],
    categories=data['categories']
    )
    db.collection('books').add(book.__dict__)
    return jsonify({"message": "Book added successfully!"}), 201

@app.route('/books', methods=['GET'])
def get_books():
    books_ref = db.collection('books')
    books = [doc.to_dict() | {"id": doc.id} for doc in books_ref.stream()]
    return jsonify(books), 200

@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    db.collection('books').document(book_id).delete()
    return jsonify({"message": "Book deleted successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)