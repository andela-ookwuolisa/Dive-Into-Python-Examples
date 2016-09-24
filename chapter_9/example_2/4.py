from xml.dom import minidom
doc = minidom.parse('2.xml')

docnode = doc.firstChild
print "printing doc node"
print docnode.toxml()

docchildren = docnode.childNodes
print "\n\nprinting doc's children nodes"
print docchildren

print "\n\nFirst child of docchildren"
print docchildren[0].toxml()
# Same as
# print docnode.firstChild.toxml()

print "\n\nSecond child of docchildren"
print docchildren[1].toxml()

