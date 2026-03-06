books = {}
members = {}

# Book keeping
def add_book():
    book = input("Enter book name: ")
    books[book] = "available"

# Register student/teacher
def register():
    name = input("Enter member name: ")
    members[name] = None

# Issue book
def issue():
    name = input("Enter member name: ")
    book = input("Enter book name: ")
    
    if books.get(book) == "available":
        books[book] = "issued"
        members[name] = book
        print("Book issued")
    else:
        print("Book not available")

# Return book
def return_book():
    name = input("Enter member name: ")
    book = members.get(name)
    
    if book:
        books[book] = "available"
        members[name] = None
        print("Book returned")

# Menu
while True:
    print("1.Add Book 2.Register 3.Issue Book 4.Return Book 5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        register()
    elif ch == "3":
        issue()
    elif ch == "4":
        return_book()
    elif ch == "5":
        break