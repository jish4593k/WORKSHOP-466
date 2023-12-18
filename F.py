

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd
import torch
from scipy.stats import mode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class PDFGenerator:
    def __init__(self, master):
        self.master = master
        self.master.geometry('600x400')
        self.master.title("Advanced PDF Generator")

        self.df = pd.read_csv("topics.csv")
        self.output_file = "output_advanced.pdf"

        self.canvas = tk.Canvas(self.master, width=500, height=250)
        self.canvas.pack()

        self.btn_generate_pdf = tk.Button(
            master=self.master,
            text="Generate PDF",
            command=self.generate_pdf
        )
        self.btn_generate_pdf.pack(pady=10)

    def generate_pdf(self):
        pdf = canvas.Canvas(self.output_file, pagesize=letter)

        for index, row in self.df.iterrows():
            self.draw_header_footer(pdf, row['Topic'])
            self.draw_lines(pdf)

            for _ in range(row['Pages'] - 1):
                pdf.showPage()
                self.draw_lines(pdf)

        pdf.save()

    def draw_header_footer(self, pdf, topic):
        header_font = ("Arial", 16)
        footer_font = ("Times-Italic", 8)

        # Header
        pdf.setFont(*header_font)
        pdf.setFillColorRGB(254, 100, 100)
        pdf.drawString(10, 770, topic)

        # Footer
        pdf.setFont(*footer_font)
        pdf.setFillColorRGB(180, 180, 180)
        pdf.drawString(10, 15, topic)

    def draw_lines(self, pdf):
        y = 760
        while y > 10:
            pdf.line(10, y, 200, y)
            y -= 10

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFGenerator(root)
    root.mainloop()
