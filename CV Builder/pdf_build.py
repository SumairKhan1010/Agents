from xhtml2pdf import pisa

def create(html_content):

    with open(f"outpu1t.pdf", "wb") as result_file:
        # Create the PDF directly from the HTML string
        pisa_status = pisa.CreatePDF(html_content, dest=result_file)
        
        # Check for compilation errors
        if pisa_status.err:
            print(f"❌ Error occurred during PDF generation: {pisa_status.err}")
        
        print(f"✅ PDF successfully generated and saved as 'output.pdf'")