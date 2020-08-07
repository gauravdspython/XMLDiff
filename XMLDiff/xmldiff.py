from lxml import etree
from xmldiff import main, formatting

sourcexmlname = "C:/xmlTest/source2.xml"
targetxmlname = "C:/xmlTest/target2.xml"

def compare_xmls(source_xml,target_xml):
    
    diff = main.diff_files(source_xml,target_xml,formatter=formatting.XMLFormatter())
    return diff

xml_difference = compare_xmls(sourcexmlname, targetxmlname)
print("Differences between two xml's are:", xml_difference)

