# Import minidom from xml -> dom package
from xml.dom import minidom

# Create a parsed representation of xml document
xmldoc = minidom.parse('2.xml')

# Print the document in xml form
print xmldoc.toxml()
