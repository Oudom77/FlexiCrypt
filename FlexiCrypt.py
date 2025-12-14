from ast import literal_eval
from rsa import newkeys, PublicKey, PrivateKey, encrypt, decrypt
from FileHandling import *
from color import *
from tkinter import Tk
from tkinter import filedialog

class FlexiCryptSystem:
    def __init__(self, input_file=None, output_file=None):
        if input_file:
            self.input_file = input_file
        if output_file:
            self.output_file = output_file

    def write_file(self, message = None, binary=False):
        write_file(message = message, binary = binary, output_file = self.output_file)

    def read_file(self, binary=False):
        return read_file(binary = binary, input_file = self.input_file)

    def process(self, message):
        pass

    def reverse(self, ciphertext):
        pass

    def openFile(self, title="Select file"):
            root = Tk()
            root.withdraw()
            root.lift()
            root.attributes("-topmost", True)
            if title == "Select .bin file":
                filepath = filedialog.askopenfilename(
                    parent = root,
                    title = title,
                    filetypes = [("Binary Files", "*.bin"), ("All Files", "*.*")]
                )
            elif "Key" in title:
                 filepath = filedialog.askopenfilename(
                    parent = root,
                    title = title,
                    filetypes = [("All Files", "*.*")]
                )
            else:
                filepath = filedialog.askopenfilename(
                    parent=root,
                    title=title,
                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
                )

            root.destroy()
            return filepath

    def saveFile(self, title="Save file as"):
        root = Tk()
        root.withdraw()
        root.lift()
        root.attributes("-topmost", True)

        filepath = filedialog.asksaveasfilename(
            parent=root,
            title=title,
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        root.destroy()
        return filepath