"Code Taken from Rena Redux project"

import io
import os
import re
import sys
import pathlib

#from time import sleep
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

output_dir = os.getcwd()
droppedfile = sys.argv[1]
file_name = pathlib.Path(droppedfile).stem

pattern = "[0-9]+"
number = re.findall(pattern, file_name)

ticket_number = "".join(map(str, number))

#sleep(10)

def stamper(pdf_path, ticket_number):

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFontSize(8)
    can.drawString(35, 60, "Ticket {0}".format(ticket_number))
    can.save()
    packet.seek(0)

    new_pdf = PdfReader(packet)
    current_pdf = PdfReader(open(pdf_path, 'rb'))
    output = PdfWriter()

    page = current_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    output_stream = open('Sales Quote for Ticket {0}.pdf'.format(str(ticket_number)), 'wb')
    output.write(output_stream)
    output_stream.close()

stamper(droppedfile,ticket_number)
