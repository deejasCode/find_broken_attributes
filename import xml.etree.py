import xml.etree.ElementTree as ET

# Recursive function to check for broken attributes
def find_broken_attributes(element):
    for key, value in element.attrib.items():
        # Check if the attribute value contains a placeholder for a missing value
        if '${' in value and '}' in value:
            print(f"Broken Attribute: {key}='{value}' in element '{element.tag}'")
    
    # Recursively process child elements
    for child in element:
        find_broken_attributes(child)

# Example XML document
xml_data = '''
<root>
    <element1 attr1="value1" attr2="${missing_attr}" />
    <element2 attr1="value2" attr2="value3">
        <element3 attr1="${missing_attr}" />
    </element2>
</root>
'''

# Parse the XML document
root = ET.fromstring(xml_data)

# Call the recursive function to find broken attributes
find_broken_attributes(root)
