from oop.book_class import Book
from oop.library_system import Book as LibBook, EBook, PrintBook, Library

def test_book_class():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)          # Uses __str__
    print(repr(my_book))    # Uses __repr__
    del my_book             # Triggers __del__

def test_library_system():
    my_library = Library()

    classic_book = LibBook("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()

def main():
    print("Testing Book class:")
    test_book_class()
    print("\nTesting Library system:")
    test_library_system()

if __name__ == "__main__":
    main()
