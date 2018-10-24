from xml.etree import ElementTree as ET

path = r"D:\App_data\Deep_Learning_Data\yolo\VOCdevkit\VOC2012\Annotations\2007_000027.xml"
root = ET.parse(path).getroot()
print(root.tag, ":", root.attrib)

# for child in root:
#     print(child.tag,":",child.attrib)

filename = root.find("filename").text
print(filename)

obj = root.find("object")
for part in obj.iter("part"):
    xmin = part.find("bndbox/xmin").text
    print(xmin)
