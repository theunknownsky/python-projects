class Library:
	def __init__(self, books, users, borrowers, borrowed_books):
		"""Constructor of the class 'Library'"""
		self.books = books
		self.users = users
		self.borrowers = borrowers
		self.borrowed_books = borrowed_books
	def print_a_book(book):
		"""Print a book."""
		print("Book name: {}\nBook ID: {}\nBook Quantity: {}".format(book.name, book.id, book.quantity))
	def print_a_user(user):
		"""Prints a user."""
		print("Username: {}\nUser ID: {}".format(user.name, user.id))
	def add_books(self):
		"""This method add books to the library."""
		book_id = 1000
		book_name = input("Enter Book Name: ")
		if book_name not in self.books.keys():
			book_id += (len(self.books) + 1)
			book_quantity = int(input("Enter Book Quantity: "))
			book = Book(book_name, book_id, book_quantity)
			self.books[book.name] = (str(book.id), book.quantity)
			print("\nNotice: {} books of {} added.".format(book.quantity, book.name))
		else:
			print("We already have that book here.")
	def print_books(self):
		"""This method shows every book the library has."""
		if len(self.books) > 0:
			print("------------------------------------------------")
			for book_name, book_details in self.books.items():
				book_id, book_quantity = book_details
				book = Book(book_name, book_id, book_quantity)
				book.print_a_book()
				print("------------------------------------------------")
		else:
			print("We don't have books here yet.")
	def print_books_by_prefix(self):
		"""This method shows every book the library has that starts with the prefix the user gives."""
		if len(self.books) > 0:
			ctr = 0
			prefix = input("Enter prefix: ")
			print("------------------------------------------------")
			for book_name in self.books:
				if book_name.startswith(prefix.upper()) or book_name.startswith(prefix.lower()):
					ctr += 1
					book_id, book_quantity = self.books[book_name]
					book = Book(book_name, book_id, book_quantity)
					book.print_a_book()
					print("------------------------------------------------")
			if ctr == 0:
				print("We don't have a book that starts with {}".format(prefix))
				print("------------------------------------------------")
		else:
			print("We don't have books here yet.")
	def add_user(self):
		"""This method registers a user to the library."""
		user_name = input("Enter username: ")
		if user_name not in self.users:
			user_id = (len(self.users) + 1)
			user_password = input("Enter password: ")
			confirm_password = input("Confirm password: ")
			if confirm_password == user_password:
				user = User(user_name, user_id, user_password)
				self.users[user.name] = (user.id, user.password)
				print("{} is now registered in the library.".format(user.name))
			else:
				print("Password must be the same.")
		else:
			print("Username already exists.")
	def print_users(self):
		"""This method shows every user that the library has."""
		if len(self.users) > 0:
			print("------------------------------------------------")
			for user_name, user_details in self.users.items():
				user_id, user_password = user_details
				user = User(user_name, user_id, user_password)
				user.print_a_user()
				print("------------------------------------------------")
		else:
			print("There are no users registered here yet.")
	def borrow_book(self):
		"""This method lets the user borrow a book."""
		if len(self.books) > 0 and len(self.users) > 0:
			user_name = input("Enter username: ")
			if user_name in self.users:
				password = input("Enter password: ")
				if password == self.users[user_name][1]:
					library.print_books()
					book_to_be_borrowed = input("What do you want to borrow? ")
					if book_to_be_borrowed in self.books and self.books[book_to_be_borrowed][1] > 0:
						if user_name not in self.borrowers:
							user_id = len(self.borrowers)
							borrower = Borrower(user_name, user_id, book_to_be_borrowed)
							self.books[borrower.borrowed_books] = (self.books[borrower.borrowed_books][0], (self.books[borrower.borrowed_books][1] - 1)) # faulty
							self.borrowers.append(borrower.username)
							self.borrowed_books.append([borrower.borrowed_books])
							print("The book {} is successfully borrowed.".format(borrower.borrowed_books))
						elif user_name in self.borrowers:
							user_id = self.borrowers.index(user_name)
							if book_to_be_borrowed not in self.borrowed_books[user_id]:
								self.books[book_to_be_borrowed] = (self.books[book_to_be_borrowed][0], (self.books[book_to_be_borrowed][1] - 1)) # faulty
								self.borrowed_books[user_id].append(book_to_be_borrowed)
								print("The book {} is successfully borrowed.".format(book_to_be_borrowed))
							else:
								print("You already borrowed this book!")

					else:
						print("{} is not available at the moment.".format(book_to_be_borrowed))
				else:
					print("Wrong password.")
			else:
				print("{} is not registered in the library.".format(user_name))
		else:
			if len(self.books) == 0 and len(self.users) == 0:
				print("There are no books nor users registered yet.")
			elif len(self.books) == 0:
				print("There are no books registered yet.")
			elif len(self.users) == 0:
				print("There are no users registered yet.")
	def return_book(self):
		"""This method returns the book that the user borrowed."""
		if len(self.borrowers) > 0:
			username = input("Enter username: ")
			if username in self.borrowers:
				password = input("Enter password: ")
				if password == self.users[username][1]:
					print("Username: {}".format(username))
					print("------------------------------------------------")
					print("Books Borrowed by {}".format(username))
					print("------------------------------------------------")
					index = self.borrowers.index(username)
					for book in self.borrowed_books[index]:
						print("Book Name: {}\nBook ID: {}".format(book, self.books[book][0]))
						print("------------------------------------------------")
					book_to_return = input("Enter book to return: ")
					if book_to_return in self.borrowed_books[index]:
						self.books[book_to_return] = (self.books[book_to_return][0], (self.books[book_to_return][1] + 1))
						self.borrowed_books[index].remove(book_to_return)
						print("{} successfully returned. Thank you.".format(book_to_return))
						if len(self.borrowed_books[index]) == 0:
							self.borrowed_books.remove(self.borrowed_books[index])
							self.borrowers.remove(self.borrowers[index])
					else:
						if book_to_return not in self.books:
							print("There are no books named as '{}' in our library.".format(book_to_return))
						elif book_to_return not in self.borrowed_books[index]:
							print("You haven't borrowed the book '{}' in our library yet.".format(book_to_return))
				else:
					print("Wrong password.")
			else:
				print("{} haven't borrowed anything.".format(username))
		else:
			print("There are no borrowers at the moment.")
	def print_user_borrowed_book(self):
		"""This method shows the books the user borrowed from the library."""
		if len(self.borrowers) > 0:
			username = input("Enter username: ")
			if username in self.borrowers:
				password = input("Enter password: ")
				if password == self.users[username][1]:
					print("Username: {}".format(username))
					print("------------------------------------------------")
					print("Books Borrowed by {}".format(username))
					print("------------------------------------------------")
					index = self.borrowers.index(username)
					for book in self.borrowed_books[index]:
						print("Book Name: {}\nBook ID: {}".format(book, self.books[book][0]))
						print("------------------------------------------------")
				else:
					print("Wrong password.")
			else:
				print("{} haven't borrowed anything.".format(username))
		else:
			print("There are no borrowers at the moment.")

					
class Book(Library):
	def __init__(self, name, id, quantity):
		"""Constructor of the class 'Book'"""
		self.name = name
		self.id = id
		self.quantity = quantity

class User(Library):
	def __init__(self, name, id, password):
		"""Constructor of the class 'User'"""
		self.name = name
		self.id = id
		self.password = password

class Borrower(Library):
	def __init__(self, username, user_id, borrowed_books):
		"""Constructor of the class 'Borrower'"""
		self.username = username
		self.user_id = user_id
		self.borrowed_books = borrowed_books

def choicePrompt():
	"""Function for choosing an action inside the library."""
	choice = 0
	while (choice < 1 or choice > 9):
		print("\nProgram Options: \n 1. Add book \n 2. Print library books \n 3. Print books by prefix \n 4. Add user \n 5. Borrow book \n 6. Return book \n 7. Print users borrowed book \n 8. Print users \n 9. Exit\n")
		choice = int(input("Enter your choice (from 1 to 9): "))
	return choice

# books: {Book Name: (ID, Quantity), ...}
# dummy values: {"Python": ("1001", 6), "C++": ("1002", 8), "Carbon": ("1003", 3)}
books = {}
# users: {Username: (ID, Password), ...}
# dummy values: {"Vonn": (1, "qwer"), "Sky": (2, "SSS")}
users = {}	
# borrowers: [Username, ...]
# dummy values: ["Sky"]
borrowers = []
# borrowed_books: [[book1, ...], [book3. book1, ...], ...]
# dummy values: ["C++"]
borrowed_books = []

library = Library(books, users, borrowers, borrowed_books)

choice = 0
while (choice != 9):
	choice = choicePrompt()
	if choice == 1:
		library.add_books()
	elif choice == 2:
		library.print_books()
	elif choice == 3:
		library.print_books_by_prefix()
	elif choice == 4:
		library.add_user()
	elif choice == 5:
		library.borrow_book()
	elif choice == 6:
		library.return_book()
	elif choice == 7:
		library.print_user_borrowed_book()
	elif choice == 8:
		library.print_users()
	elif choice == 9:
		print("\nThank you for using the library app. ")
		break