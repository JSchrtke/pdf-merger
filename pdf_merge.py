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
            self._counter = 0
            raise StopIteration

        pdf_path = self._list[self._counter]
        self._counter += 1
        return pdf_path

    def __len__(self):
        return len(self._list)

    def print(self):
        for index, path in enumerate(self._list):
            print(f"{index}: {path}")

    def order(self):
        print("\nCurrent order:")
        self.print()
        print("\nNew order:")
        new_order = []
        for i, _ in enumerate(self._list):
            new_index = input(f"{i}: ")
            if new_index == "x":
                pass
            else:
                new_order.append(self._list[int(new_index)])
        print("\n")
        self._list = new_order


def merge(pdf_list, output_file):
    print(f"Merging into {output_file}")
    merger = PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_file)


def is_ordered(pdf_list):
    pdf_list.print()
    choice = input("Is this order okay? (y/n)\n")
    if choice == "y":
        return True
    else:
        return False


if __name__ == "__main__":
    path_to_pdfs = input("Enter path to directory containing pdf files:\n")
    pdf_list = PdfList(path_to_pdfs)

    while not is_ordered(pdf_list):
        pdf_list.order()
    
    output_name = input("Enter name for the ouput file:\n")
    output_file = os.path.join(path_to_pdfs, f"{output_name}.pdf")
    merge(pdf_list, output_file)
