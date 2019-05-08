## W.A, May 2019
## Proof of Concept v1
## Batch PDF writer 
import os
import PyPDF2

# set_path = os.path.join('C:', 'Users', 'waqas', 'Desktop', 'project_spider')

# Sample Dictionary for testing & passing data 
row = {
    "name" : "Pikachu",
    "type" : "Electric"
}

# Reads from Text file. Intende to read and pass data from here 
def read_file():
    set_data_file = os.chdir("\\Users\\waqas\\Desktop\\project_spider") # Directory for Data.txt
    print("Data.txt location: ", os.getcwd())
    filepath = 'Data.txt'
    with open(filepath) as fp:
        for counter, line in enumerate(fp):
            print("Line {}: {}".format(counter, line))

# Lists PDFs in dir 
def check_pdfs():
    total = 0
    for files in os.listdir("\\Users\\waqas\\Desktop\\project_spider\\PDFs"):
        if files.endswith(".pdf") and files != -1:
            total += 1
            print(total, "->", files)
        else:
            raise ValueError('A very bad thing happened, because there are no PDFs in:', os.getcwd())
            sys.exit()

# Write metadata to pdf 
def write_metadata():
    set_path_for_PDF = ("\\Users\\waqas\\Desktop\\project_spider\\")
    file_name = "sample.pdf"
    pdfFileObj = open(file_name, 'rb') # Read 
    pdfFileObj = open(file_name, 'wb') # Write 
    pdfWriter = PyPDF2.PdfFileWriter() # Initialise pdrWriter 
    pdfWriter.addMetadata({'Pokemon Name': row["name"]}) # Writing operation from dictionary
    pdfWriter.addMetadata({'Type': row["type"]}) # Writing operation from dictionary
    pdfWriter.write(pdfFileObj) # Write to pdfFileObj
    pdfFileObj.close()
    ##### Returning Object output for testing #####
    print("GET pdf Writer - ", pdfWriter)
    print("GET Pdf Object - ", pdfFileObj)
    print("GET File Name - ", file_name)
    print("GET Dict row - ", row)
    print("GET Curr dir - ", os.getcwd())
    print("GET File in Dir - ", os.listdir())

# main 
if __name__ == '__main__':
    read_file()
    write_metadata()
    check_pdfs()
