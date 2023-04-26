import PyPDF2

pdf_path = 'test_task.pdf'
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    pdf_info = {}

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]

        text = page.extract_text()
        pdf_info[f'page{page_num + 1}_text'] = text

        # images = page.extractImages()
        # pdf_info[f'page{page_num + 1}_images'] = images
        #
        # metadata = pdf_reader.metadata()
        # pdf_info['metadata'] = metadata
        # первый раз работал с этой библиотекой, и что то не получается вытянуть мета и изображения :(

for page, text in pdf_info.items():
    print(f"=== {page} ===")
    print(text)

etalon_pdf_file_path = 'test_task.pdf'

def compare_pdf_files(etalon_pdf_file_path, input_pdf_file_path):
    with open(etalon_pdf_file_path, 'rb') as etalon_pdf_file:
        etalon_pdf_reader = PyPDF2.PdfReader(etalon_pdf_file)

        with open(input_pdf_file_path, 'rb') as input_pdf_file:
            input_pdf_reader = PyPDF2.PdfReader(input_pdf_file)
            num_etalon_pages = len(etalon_pdf_reader.pages)
            num_input_pages = len(input_pdf_reader.pages)
            if num_etalon_pages != num_input_pages:
                return False

            for page_num in range(num_etalon_pages):
                etalon_page = etalon_pdf_reader.pages[page_num]
                input_page = input_pdf_reader.pages[page_num]

                etalon_page_text = etalon_page.extract_text()
                input_page_text = input_page.extract_text()
                if etalon_page_text != input_page_text:
                    return False
            return True


input_pdf_file_path = 'test_task.pdf'
if compare_pdf_files(etalon_pdf_file_path, input_pdf_file_path):
    print('PDF файлы совпадают')
else:
    print('PDF файлы не совпадают')

