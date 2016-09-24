from xml.dom import minidom
xmldoc = minidom.parse('4.xml')
reflist = xmldoc.getElementsByTagName('ref')
print reflist
print
print reflist[0].toxml()
print
print reflist[1].toxml()
