from xml.dom import minidom
xmldoc = minidom.parse('4.xml')
plist = xmldoc.getElementsByTagName('p')
print plist

for node in plist:
    print
    print node.toxml()
