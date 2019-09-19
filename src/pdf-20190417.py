# title: How to Work With a PDF in Python
# author: Mike Driscoll
# date: Apr 17, 2019
# url: https://realpython.com/pdf-python/

import PyPDF2


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}:
    
    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information


if __name__ == '__main__':
    path = 'reportlab-sample.pdf'
    extract_information(path)
