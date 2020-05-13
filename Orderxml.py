import xml.etree.ElementTree as ET
import uuid
import random
import datetime

def main():
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    for i in range (3):
        for GUID_tag in root.findall('GUID'):
            id= uuid.uuid1()
            GUID_tag.text= str(id)
        for RefNum_tag in root.findall('RefNum'):
            refn= random.randint(0,1000000)
            RefNum_tag.text= str(refn)
        for FromDate_tag in root.findall('FromDate'):
            FromDate= datetime.datetime.now() + datetime.timedelta(days=i,seconds=i)
            FromDate_tag.text= str(FromDate.strftime("%x %X"))
        for ToDate_tag in root.findall('ToDate'):
            ToDate= FromDate + datetime.timedelta(days=1)
            ToDate_tag.text= str(ToDate.strftime("%x %X"))
        filename=f"sample{str(i)}.xml"
        tree.write(filename)

if __name__ == "__main__":
    main()