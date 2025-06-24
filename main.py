from oop.book_class import Book
from oop.library_system import Book as LibBook, EBook, PrintBook, Library
from oop.polymorphism_demo import Shape, Rectangle, Circle
from oop.class_static_methods_demo import Calculator

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

def test_polymorphism():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

def test_class_static_methods():
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

def main():
    print("Testing Book class:")
    test_book_class()
    print("\nTesting Library system:")
    test_library_system()
    print("\nTesting Polymorphism:")
    test_polymorphism()
    print("\nTesting Class and Static Methods:")
    test_class_static_methods()

if __name__ == "__main__":
    main()
