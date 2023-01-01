from tkinter import *
from tkinter import filedialog
import os,sys,subprocess
def start_file_manager():
    def openFile():
        filepath = filedialog.askopenfilename(initialdir="/",
                                            title="Open file okay?",
                                            filetypes= (("text files","*.txt"),
                                            ("all files","*.*")))
        if sys.platform == 'win32':
            os.startfile(filepath)
        else:
            openr ='open' if sys.platform == 'darwin' else 'xdg-open'
            subprocess.call([openr,filepath])


    window = Tk()
    button = Button(text="Open",command=openFile)
    button.pack()
    window.mainloop()
if __name__ == "__main__":
    start_file_manager()