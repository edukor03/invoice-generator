import sys
import pdfkit
import jinja2
import csv

def create_pdf(context, filename):
    # Load jinja and templates environemnts
    template_location = jinja2.FileSystemLoader('./templates/')
    loader = jinja2.Environment(loader=template_location)

    # Get template and the text
    template = loader.get_template("invoice_template.html") # Load a template file 
    text = template.render(context) # Add our data to the html file

    # Configure pdfkit and create a pdf file from the string
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_string(text, filename, configuration=config, css="./css/mainstyle.css")
    print(f"[*] PDF file created: {filename}")

# It will create context (dict with all the data needed) and a filename for saving pdf file.
def create_context(tempInvoice, items, total):
    context = {
        'invoice_number': tempInvoice['Invoice Number'],
        'company_name': tempInvoice['Company Name'],
        'company_address': tempInvoice['Company Address'],
        'company_email': tempInvoice['Company Email'],
        'date': tempInvoice['Date'],
        'customer_name': tempInvoice['Customer Name'],
        'customer_address': tempInvoice['Customer Address'],
        'customer_email': tempInvoice['Customer Email'],
        'items': items,
        'notes': tempInvoice['Notes'],
        'total': total,
        'payment_method': 'N/A',
        'account_number': 'N/A'
    }
    # Creates a file name that will be used to name the PDF file.
    file_name = f"{tempInvoice['Invoice Number']}_{tempInvoice['Date']}_{tempInvoice['Customer Name']}.pdf"
    return context, file_name

# Enables to input the invoice filename in the command console before running the python script
if len(sys.argv) < 2:
    print("Usage: py main.py [filename]")
    sys.exit(1)
invoices_file = sys.argv[1]


# Replace with the file you want or use invoices_file for command line input
with open(invoices_file, newline="") as file:
    reader = csv.DictReader(file)
    info = list(reader)

# Create temp lists to store info for each invoice
tempInvoice = info[0]
items = []
total = 0

# Go through each row and check if the invoice is the same as the set invoice form the start.
# If on the new line invoice is the same, add all data relevant to the item to the item list.
# Once it spots a different invoice, it will run create context function passing current invoice, all the items data and the total price.
# PDF Function creates a PDF file.
# Else is used to start the new Invoice process.
for row in info:
    if row['Invoice Number'] == tempInvoice['Invoice Number']:
        items.append((row['Item Description'],row['Quantity'],row['Unit Price'],row['Total']))
        total += int(row['Total'])
        if row == info[len(info)-1]:
            context, file_name = create_context(tempInvoice=tempInvoice, items=items, total=total)
            create_pdf(context=context, filename=file_name)
    elif row['Invoice Number'] != tempInvoice['Invoice Number']:
        context, file_name = create_context(tempInvoice=tempInvoice, items=items, total=total)
        create_pdf(context=context, filename=file_name)

        tempInvoice = row

        # Reset the list
        items = []
        total = 0

        # Enter the new values
        items.append((row['Item Description'],row['Quantity'],row['Unit Price'],row['Total']))
        total += int(row['Total'])

