from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle

Content = [["Book No.", "Book Name", "Publication", "Quantity", "Price", "Total"],
           ["184758", "Data Structures Book", "Nirali Pub.", " 1 ", "270", "270/-"],
           ["139944", "Operating Systems Book", "Bellman Ford", " 1 ", "470", "470/-"],
           ["293749", "DBMS Book", "Parthasarathy", " 1 ", "700", "700/-"],
           ["132894", "Compiler Designing Book", "Techknowlegdge", " 1 ", "300", "300/-"],
           ["937383", "Software Engineering Book", "TecMax", " 1 ", "200", "200/-"],
           ["294898", "Machine Learning Book", "Nirali", " 1 ", "500", "500/-"],
           ["", "", "", "", "", ""],
           ["Total Bill:- ", "", '', "", "", "2440/-"]
           ]

mypdf = SimpleDocTemplate("receipt.pdf")

style = getSampleStyleSheet()
style.fontName = "Times New Roman"
style.fontStyle = "Itallic"
style.fontStyle = "Bold"

style = TableStyle([
    ("BOX", (8, 8), (4, 4), 4, colors.black),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (5, 0), colors.mediumpurple),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.lavender),
    ("ALIGN", (4, 0), (-1, -1), "CENTER"),
    ("BACKGROUND", (0, 1), (-1, -1), colors.lavenderblush),
])

table = Table(Content, style=style)


def colored_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColorRGB(6.8, 0.8, 0.8)  # Choose your background color here
    canvas.rect(80, 80, doc.width, doc.height, fill=True)
    canvas.restoreState()
    canvas.setFont("Helvetica-Bold", 16)
    canvas.drawString(270, 790, "Receipt")
    canvas.drawString(220, 820, "Brilliant Book Stores")


mypdf.build([table], onFirstPage=colored_background)
