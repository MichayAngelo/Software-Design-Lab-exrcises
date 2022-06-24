from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font


class ImageDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Image")
        self.setResizable(False)
        imageLabel = self.addLabel(text = "",row = 0, column = 0, sticky = "NSEW")
        textLabel = self.addLabel(text = "Anya", row = 1, column = 0, sticky = "NSEW")
        self.image = PhotoImage(file = "ANYA.gif")
        imageLabel["image"] = self.image
        font = Font(family = "Verdana", size = 20 )
        textLabel["font"] = font
        textLabel["foreground"] = "blue"


def main():
    ImageDemo().mainloop()


if __name__ == "__main__":
    main()