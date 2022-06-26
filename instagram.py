from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
async  def Pdf(id,kanal,user,xabar,link,vaqt):
    canvas = Canvas("hello.pdf", pagesize=A4)
    canvas.setFont("Times-Roman", 18)
    canvas.drawString(150, 300, f'ID: {id}')
    canvas.drawString(150, 280, f'KANAL: {kanal}')
    canvas.drawString(150, 260,  f'FOYDALANUVCHI: {user}')
    canvas.drawString(150, 240, f'TEXT: {xabar}')
    canvas.drawString(150,220,  f'LINK: {link}')
    canvas.drawString(150, 200,  f'VAQT: {vaqt}')
    canvas.save()