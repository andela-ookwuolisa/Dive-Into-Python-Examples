from xml.dom import minidom
xmldoc = minidom.parse('3.xml')
title = xmldoc.childNodes[0].childNodes[1].firstChild.data
# Before converting to encoding
print title

# After converting to real encoding
title = title.encode('koi8-r')
print title
