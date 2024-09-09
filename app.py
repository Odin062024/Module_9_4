from flask import Flask, render_template, redirect, url_for, request, flash
from forms import BookForm
from models import books, Book

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
