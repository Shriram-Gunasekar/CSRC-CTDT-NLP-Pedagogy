from PyPDF2 import PdfReader
text = PdfReader('todo_dummy_merged.pdf')
length = len(text.pages)
text = ''.join([text.pages[i].extract_text() for i in range(length)])
print(text)