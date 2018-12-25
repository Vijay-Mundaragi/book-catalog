from app.catalog import main

@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)
