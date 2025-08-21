# Invoice Generator

Python script that automates Invoice creation using PDFkit and jinja2 libraries. The jinja2 was used to create HTML layout for the PDF document that can accept python variables. PDFkit was used to convert HTML file into PDF file using tool called "Wkhtmltopdf". It can accept multiple invoices in the same file, it will seperate them and generate a pdf file for each invoice.

> [!IMPORTANT]
> I will be happy for any suggestions for improvements :)

To run the script:
1) Through command terminal navigate to scripts location
2) py main.py [filename]   -   filename is the file that contains the invoice information. Sample csv file is provided. !!!FOR NOW ONLY ACCEPTS CSV FILES!!!
3) Creates PDF files in the same directory.

Libraries and tools used:
- ![PDFkit](https://pypi.org/project/pdfkit/)
- ![jinja2](https://pypi.org/project/Jinja2/)
- ![wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)
- sys
- csv

requirements.txt - contains information about external libraries used that are not pre installed with python. 
