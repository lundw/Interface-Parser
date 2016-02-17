import xml.etree.ElementTree as etree

xmldoc = etree.parse("Main.xml")

root = xmldoc.getroot()

root