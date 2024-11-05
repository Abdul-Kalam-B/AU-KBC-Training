class Library():
    
    def __init__(self,list):
         self.book_list = list
         self.available_books = list = list[:]
         self.book_lending = {}

    def display_available_books(self):
        for book in self.available_books:
            print(book)
    def display_all_books(self):
        for book in self.book_list:
            print(book)
    def lend_book(self,name,book):
        if book not in self.book_list:
            print('Incorrect book name, Please check book list')
            return
        if book in self.available_books:
            self.book_lending.update({book:name})
            self.available_books.remove(book)
            print("Your can take your Book..")
        else:
            print("This book is taken by "+ self.book_lending[book])
    def return_book(self,book):
        del self.book_lending[book]
        self.available_books.append(book)



if __name__ == '__main__':

    lib = Library(['Rich dad poor dad','Atomic Habits','Psychology of money','48 laws of power','Ikigai'])
    print("Welcome to library")
    print("Enter a option")

    while True:
        print("1.Display available books")
        print("2.Display all books")
        print("3.Borrow a book")
        print("4.Return a book")
        print("5.Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            lib.display_available_books()

        elif user_choice == '2':
            lib.display_all_books()

        elif user_choice == '3':
            name = input("Enter user name: ")
            book = input("Enter book name: ")
            lib.lend_book(name,book)

        elif user_choice == '4':
            book = input("Enter the name of the book: ")
            lib.return_book(book)

        elif user_choice == '5':
            break

        else:
            print("Invalid option")
