import customtkinter
from tkinter import filedialog, END
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("dark-blue")  

def Get_Data():
    def pdf_to_text(pdf_path):
        images = convert_from_path(pdf_path)
        text = ""

        for image in images:
            text += pytesseract.image_to_string(image)

        return text

    def select_pdf():
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            extracted_text = pdf_to_text(file_path)
            display_text(extracted_text)

    def display_text(text):
        text_area.delete(1.0, END)  
        text_area.insert(END, text)  

    app = customtkinter.CTk()
    app.title("PDF Text Extractor | Made by Justin Afaneh")
    app.geometry("800x600")  

    frame = customtkinter.CTkFrame(app)
    frame.pack(expand=True, fill='both', padx=10, pady=10)


    text_area = customtkinter.CTkTextbox(frame, wrap='word')
    text_area.pack(expand=True, fill='both', padx=10, pady=(10, 5)) 

    scrollbar = customtkinter.CTkScrollbar(frame, command=text_area.yview)
    scrollbar.pack(side='right', fill='y')

    text_area.configure(yscrollcommand=scrollbar.set)

    select_button = customtkinter.CTkButton(app, text="Open PDF", command=select_pdf)
    select_button.pack(side='bottom', pady=10) 

    app.mainloop()

Get_Data()
