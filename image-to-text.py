# installation
# !sudo apt install tesseract-ocr
# !pip install pytesseract

import pytesseract

img_path1 = './data/image/nepal.png'
img_path2 = './data/image/eng.jpg'
img_path3 = './data/image/nep2.png'
text = pytesseract.image_to_string(img_path3,lang='nep')
print(pytesseract.get_languages(config=''))
print(f"text : {text}")