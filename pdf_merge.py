import os

from PyPDF2 import PdfFileMerger


class PdfList:
    def __init__(self, path):
        self._counter = 0
        self._path = path
        self._list = [
            os.path.join(self._path, file_name)
            for file_name in os.listdir(self._path)
            if ".pdf" in file_name
        ]

    def __iter__(self):
        return self

    def __next__(self):
        if self._counter > len(self._list) - 1:
            raise StopIteration

        pdf_path = self._list[self._counter]
        self._counter += 1
        return pdf_path

    def __len__(self):
        return len(self._list)


if __name__ == "__main__":
    path_to_pdfs = input("Enter path to directory containing pdf files: ")
    pdf_list = PdfList(path_to_pdfs)

    output_file = os.path.join(path_to_pdfs, "output.pdf")
    print(f"Merging into {output_file}")
    
    merger = PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_file)
