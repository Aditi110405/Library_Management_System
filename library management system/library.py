import os

class book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author

    def __str__(self):
        return f"{self.book_id},{self.title},{self.author}"

class Library(book):
    def __init__(self,filename="Books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 3:
                        book_id,title,author = data
                        self.books.append(book(book_id,title,author))

    def save_books(self):
        with open(self.filename,"w") as file:
            for b in self.books:
                file.write(f"{b.book_id},{b.title},{b.author}\n")

    def add_book(self):
        book_id=int(input("Enter book id:"))
        title=input("Enter book title:")
        author=input("Enter book author:")

        for b in self.books:
            if b.book_id == book_id:
                print("This Book already exists")
                return

        self.books.append(book(book_id,title,author))
        self.save_books()
        print("Book Added")

    def view_all_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\n------ Book List ------")
            for b in self.books:
                print(b)
            print()

    def search_book(self):
        key= input("Enter book id or title: ").lower()
        found=False
        for b in self.books:
            if key in b.book_id.lower() or key in b.title.lower():
                print(b)
                found=True
        if not found:
            print("Book not found")

    def edit_book(self):
        book_id=input("Enter book id:")
        for b in self.books:
            if b.book_id == book_id:
                print("Leave blank if you dont want to change the field")
                new_title = input(f"New Title {b.title}: ")
                new_author = input(f"New Author {b.author}: ")

                if new_title:
                    b.title = new_title
                if new_author:
                    b.author = new_author

                self.save_books()
                print("Book Updated Successfully")
                return
        print("Book not found")

    def delete_book(self):
        book_id =input("Enter book id:")
        for b in self.books:
            if b.book_id == book_id:
                self.books.remove(b)
                self.save_books()
                print("book deleted successfully")
                return
        print("Book not found")


def main():

    library = Library()

    while True:
        print("*** Library Management System ***")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Edit Book")
        print("5. Delete Book")
        print("6. Exit\n")

        choice=input("Enter your choice:")

        if choice == "1":
            print("add Book")
            library.add_book()
        elif choice == "2":
            print("View All Books")
            library.view_all_books()
        elif choice == "3":
            print("Search Book")
            library.search_book()
        elif choice == "4":
            print("Edit Book")
            library.edit_book()
        elif choice == "5":
            print("Delete Book")
            library.delete_book()
        elif choice == "6":
            print("Existing library system. Goodbye!")
            break
        else:
            print("Invalid choice")




if __name__ == '__main__':
    main()



