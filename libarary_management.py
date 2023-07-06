"""write a library class with no_of_book and books as two instance variables. write a program to create a library from this library class and show how you can print all books an a book and get the number of books using diffrent methods . show that you program doesnt persist the boooks after the program is stopped """

class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are")
    for book in self.books:
      print(book)


l1 = Library()
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")
l1.showInfo()
    