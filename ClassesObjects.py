class Book :
    def __init__(self):
        self.title = ""
        self.author = ""
        self.numberOfPages = 0

# TODO Step 1 - instantiate an object of class Book and assign it to a variable named myBook
myBook = Book()

# TODO Step 2 - assign a value to the title, author and numberOfPages fields of your object.
myBook.title = "Meri Vyatha"
myBook.author = "Sobhit"
myBook.numberOfPages = 300

# Print the values
print("The title of the book is ", myBook.title, "\nIts author is",
      myBook.author, "\nIt contains ", myBook.numberOfPages)