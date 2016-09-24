from xml.dom import minidom
doc = minidom.parse("2.xml")
print doc.childNodes
print doc.firstChild
print doc.childNodes[0]
print doc.firstChild.toxml()
