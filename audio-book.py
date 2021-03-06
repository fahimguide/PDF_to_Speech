# importing needed libraries

import pyttsx3, pdfplumber, PyPDF2,os
from gtts import gTTS

# get the fle name
file = r"C:\Users\Administrateur\PycharmProjects\pythonProject\Pandas 1.x Cookbook.pdf"
# open the file in binary reading
file_obj = open(file, 'rb')
# create pdf file reader
file_reader = PyPDF2.PdfFileReader(file_obj)

# get the number of pages
total_pages = file_reader.numPages

# create pdf plumber and loop throw the number of pages

with pdfplumber.open(file) as pdf:
    text = ''
    for i in range(0,total_pages):
        page = pdf.pages[i]
        text += page.extract_text()
final_output = gTTS(text=text, lang='en')
print('generating speech')
final_output.save('Pandas 1.x Cookbook.mp3')
print('creating audio')
os.system('Pandas 1.x Cookbook.mp3')


