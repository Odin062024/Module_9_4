from flask import Flask, render_template, redirect, url_for, request, flash
from forms import BookForm
from models import books, Book
from flask import jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def list_books():
    return render_template('list_books.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(form.title.data, form.author.data, form.pages.data)
        books.append(new_book)
        flash('Book added successfully!', 'success')
        return redirect(url_for('list_books'))
    return render_template('add_book.html', form=form)

@app.route('/update/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    book = books[book_id]
    form = BookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.pages = form.pages.data
        flash('Book updated successfully!', 'success')
        return redirect(url_for('list_books'))
    return render_template('add_book.html', form=form)

@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    books.pop(book_id)
    flash('Book deleted!', 'danger')
    return redirect(url_for('list_books'))

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/api/books', methods=['GET'])
def api_list_books():
    return jsonify([{'title': book.title, 'author': book.author, 'pages': book.pages} for book in books])

@app.route('/api/books', methods=['POST'])
def api_add_book():
    data = request.json
    new_book = Book(data['title'], data['author'], data['pages'])
    books.append(new_book)
    return jsonify({'message': 'Book added successfully!'}), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def api_update_book(book_id):
    book = books[book_id]
    data = request.json
    book.title = data['title']
    book.author = data['author']
    book.pages = data['pages']
    return jsonify({'message': 'Book updated successfully!'})

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def api_delete_book(book_id):
    books.pop(book_id)
    return jsonify({'message': 'Book deleted!'})
