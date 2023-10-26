from fpdf import FPDF


name = input("Name: ")

pdf = FPDF()

final = f"{name} took CS50"

pdf.add_page()
pdf.set_font("helvetica", "B", 45)
pdf.cell(0, 60, text="CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=0, y=70)
pdf.set_font_size(29)
pdf.set_text_color(255, 255, 255)
pdf.text(x=45, y=150, text=final)


pdf.set_auto_page_break(auto=False)
pdf.output("shirtificate.pdf")
