__author__ = 'djff'

# 1 a) Creating a dictionary called book
print "\n **** Defining dictionary book ****"
book = {'book1': 'java', 'book2': 'python', 'book3': 'html'}
print book

# 1 b) Adding book4 and book 5
print "\n **** Ading book4 and book5 to book ****"
book['book4'] = 'perl'

book['book5'] = 'javascript'
print book

# 1 b) Deleting book 3
print "\n **** Deleting book3 ****"
del book['book3']
print book

# 2 Creating new dictionary called new_book
print "\n **** Creating dictionary new_book ****"
new_book = {'new1': 'pascal', 'new2': 'basic', 'new3': 'ada'}
print new_book

# 2 adding new_book entries to book
print "\n **** Adding new_book to book ****"
book.update(new_book)
print book

# 3 using for loop to print items in book
print "\n **** using for loop to iterate over book items ****"
for key, value in book.items():
    print "%s:%s" % (key, value)

