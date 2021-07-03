class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    def displayAvailableBooks(self):
        print("Available Books are : ")
        for i in self.books:
            print(f"* {i}")
    def borrowBooks(self, bookname):
        if bookname in self.books:
            print(f"The book {bookname}  has been issued, please keep it safe and retru in time")
            self.books.remove(bookname)
    def retunBook(self, bookname):
        self.books.append(bookname)
        print(f"thanks for retuning {bookname}.")
class Student:
    pass

if __name__== "__main__":
    centralLibrary = Library(["DevildBreath", "Python", "EvilDead", "2020", 'Java'])
    centralLibrary.displayAvailableBooks()


