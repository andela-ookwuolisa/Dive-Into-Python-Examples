from xml.dom import minidom
doc = minidom.parse('2.xml')

# NL = New Line character

docnode = doc.firstChild
docchildren = docnode.childNodes
first_account_node = docchildren[1]

# NL
# print first_account_node.childNodes[0].toxml()

# Number node
number_node = first_account_node.childNodes[1]
# number_node is still node so we have children
print number_node.firstChild.data
# print number_node.firstChild.toxml()

# NL
# print first_account_node.childNodes[2].toxml()

# Name node
name_node = first_account_node.childNodes[3]
print name_node.firstChild.data

# NL
# print first_account_node.childNodes[4].toxml()

# Balance node
balance_node = first_account_node.childNodes[5]
print balance_node.firstChild.data
