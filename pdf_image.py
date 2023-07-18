from pdf2image import convert_from_path
import os 


folder_path = 'pdf'  # Path to the main folder containing PDF files


def PdfToImage(pdf_path, root):
    poppler_path = r"poppler-23.07.0/Library/bin"


    pages = convert_from_path(pdf_path = pdf_path, poppler_path = poppler_path)


    c = 1 

    for page in pages:
        img = f"img--{c}.png"
        page.save(os.path.join(root,img),"PNG")
        c+=1

def process_folder(folder_path):
    
    for root, dirs, files in os.walk(folder_path):
        
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                
                PdfToImage(pdf_path,root)
process_folder(folder_path)
