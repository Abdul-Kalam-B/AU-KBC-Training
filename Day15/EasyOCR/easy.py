import easyocr 
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

reader = easyocr.Reader(['en'])

result = reader.readtext('images/book1.jpg')

for(bbox , text , prob) in result:
    print(text)
