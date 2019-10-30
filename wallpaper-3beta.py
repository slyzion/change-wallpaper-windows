#############################
#
#  Made by:  Pc1h6a9h6
#  Name:     ChangeWallpaper
#  Version:  3-beta
#
#############################

from tkinter import *
from tkinter.filedialog import *
import os, shutil

class Wallpaper:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x160')
        self.root.wm_title("Wallpaper")

        label = Label(self.root, text="Escolha a imagem de fundo:", fg="Black", font="Arial 10 bold")
        label.place(x=8, y=10)

        self.entry = Entry(self.root, fg="blue")
        self.entry.place(x=20, y=50, width=330)

        button1 = Button(self.root, text="···", command=self.abrir)
        button1.place(x=360, y=47, width=25)

        button2 = Button(self.root, text="Change Wallpaper!", command=self.change)
        button2.place(x=75, y=100, width=250)

        self.root.mainloop()

    # função abrir
    def abrir(self):
        fileName = askopenfilename(title = "Browse Image")
        self.entry.delete(0, 'end')
        self.entry.insert(0, fileName)


    def change(self):
        user=os.environ["USERNAME"]
        fileFrom = self.entry.get()

        if fileFrom == "":
            openF = Tk()
            openF.geometry("250x150")
            openF.wm_title("Error!")
            Label(openF, text="Por favor insira uma imagem!", fg="Black", font="Arial 10 bold").place(x=25, y=50)
        
        # Erase existing wallpaper
        try:
            os.remove("C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles\\CachedImage_????_???_POS?.jpg")
            os.remove("C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")
        except:
            pass
    
        # Create the new wallpaper
        try:
            shutil.copy2(fileFrom, "C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles\\CachedImage_1600_900_POS4.jpg")
            shutil.copy2(fileFrom, "C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")
        except:
            pass


if __name__ == "__main__":
    Wallpaper()
