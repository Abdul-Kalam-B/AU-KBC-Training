from flask import Flask,jsonify,request

app = Flask(__name__)

#sample data 

books = [
    {"id":1 , "title":"Rich dad poor dad","author":"Robert T.kiyosaki"},
    {"id":2 , "title":"Atomic Habits","author":"Morgan Housel"},
    {"id":3, "title":"48 laws of power","author":"Robert Greene"}
]

#GET all books
@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

#GET single book by ID
@app.route('/books/<int:book_id>',methods=['Get'])
def get_book(book_id):
    book = next((b for b in books if["id"] == book_id),None)
    return jsonify(book) if book else('',404)

#POST add a new book
@app.route('/books',methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

#PUT update an existing book
@app.route('/books/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    book = next(b for b in books if b["id"] == book_id),None
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    return ('',404)

#DELETE delete a book
@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return ('',204)
    
if __name__ == ' main ':
    app.run(debug = True)    