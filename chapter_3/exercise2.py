__author__ = 'djff'

# Creating a list called books
print "\n **** Creating a new list books ****"
books = ['python', 'java', 'javascript', 'php', 'html']
print books


# Adding items using append
print "\n **** adding items to books ****"
books.append('perl')
books.append('jquery')
print books


# Deleting java from list using pop
print "\n **** Removing java from books *****"
books.pop(2)
print books

#printing javascript using negative indexing
print "\n **** extracting javascript using negative indexing ****"
print books[-5]

# printing items from index 2 to index 4
print "\n ****Extracting items from index 2 to index 4 ****"
print books[2:5]

# creating list authors
print "\n **** Creating new list called authors ****"
authors = ['Monte Python', 'berckeley', 'java master', 'djff']
print authors

# adding authors to books, it can be done with '+' or with extend()
print "\n **** Adding authors to books"
books = books + authors
print books

# using for loop to print out books items
print "\n **** Using for loop to iterate on books ****"
for item in books:
    print item