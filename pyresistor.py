##########################################################
# PyResistor

# Description: This application aims to find quickly 
# the code of three colors corresponding to an electrical 
# resistor to a determined value.

# Author: Nicolas Chen
##########################################################

#!/usr/bin/python

from Tkinter import *
from math import log10

class PyResistor:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.title('PyResistor - Resistor Color Code')

        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", accelerator='Alt+F4', command=self.root.quit)
        menubar.add_cascade(label="Menu", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Instructions", command=self.help_resistor)
        helpmenu.add_command(label="About", command=self.about_resistor)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.drawResistor()
        Label(self.root, text ="Enter the value of the resistor (ohms), then press Enter:", font = ' arial 10 bold').grid(row =2)
        self.value = Entry(self.root)
        self.value.grid(row =3, pady=5)
        self.value.bind("<Return>", self.changeColors)

        self.colorsBand = ['black','saddle brown','red','orange','yellow',
                   'green','blue','purple','grey','white']
        self.root.mainloop()

    def help_resistor(self, event=None):
        self.help_window = Toplevel()
        self.help_window.title("Help - PyResistor")
        self.help_window.resizable(width=False, height=False)

        message1 = Label(self.help_window, text='Presentation:', font='arial 12 underline bold')
        message1.pack()

        message2 = Label(self.help_window, text='This application allows to find quickly the code of '
                                                'three colors corresponding to an electrical resistance '
                                                'to a determined value.')
        message2.pack()
        message3 = Label(self.help_window, text='\nOverview', font='arial 12 underline bold')
        message3.pack()
        message4 = Label(self.help_window, text='The colored bands indicate the value of the resistor (ohms). '
                                                'The first two bands indicate the first two digits of the numerical value.\n '
                                                'Then, we append these two digits a number of zeros equal to the indication '
                                                'provided by the third band.\n'
                                                'Here is the code of colors for a resistor:\n'
                                                'Black = 0; Brown = 1; Red = 2; Orange = 3; Yellow = 4; Green = 5; Blue = 6,'
                                                'Purple = 7, Grey = 8, White = 9')
        message4.pack()
        message5 = Label(self.help_window, text='\nActions', font='arial 12 underline bold')
        message5.pack()
        message6 = Label(self.help_window, text='Put the value in the textbox and press Enter to see the color code of the resistor.')
        message6.pack()

        button_quit = Button(self.help_window, text='OK', relief='ridge', command=self.help_window.destroy)
        button_quit.pack(side='bottom', pady=5)

    def about_resistor(self, event=None):
        self.version_window = Toplevel()
        self.version_window.title("Version - PyResistor")
        self.version_window.resizable(width=False, height=False)

        message0 = Label(self.version_window, text='PyResistor: Information - Version', font='arial 16')
        message0.grid(column=0, row=0, columnspan=2, pady=5, padx=10)
        message1 = Label(self.version_window, text='\n - Developer: Nicolas Chen')
        message1.grid(column=1, row=1, sticky=W)
        message2 = Label(self.version_window, text=' - Version: 1.0')
        message2.grid(column=1, row=2, sticky=W)
        message3 = Label(self.version_window, text=' - Release: 2016')
        message3.grid(column=1, row=3, sticky=W)
        message4 = Label(self.version_window, text=' - Copyright (c) 2016 nchen\n\n')
        message4.grid(column=1, row=4, sticky=W)

        message5 = Label(self.version_window,
                         text=' - For any information or suggestion, you can contact me at this email address:')
        message5.grid(column=1, row=5, sticky=W)
        message6 = Label(self.version_window, text='nchen.info@gmail.com', foreground='blue')
        message6.grid(column=1, row=6, columnspan=2)

        button_quit = Button(self.version_window, text='OK', relief='ridge', command=self.version_window.destroy)
        button_quit.grid(column=1, row=7, columnspan=2, pady=5)

    def drawResistor(self):
        self.can = Canvas(self.root, width=500, height =200, bg ='light blue')
        self.can.grid(row =1, pady =5, padx =5)
        self.can.create_line(20, 100, 480, 100, width =5)
        self.can.create_rectangle(130, 60, 370, 140, fill ='tan2', width =3)

        self.line = []
        #draw the bands on the resistor
        for x in range(85,150,24):
            self.line.append(self.can.create_rectangle(x*2,60,2*x+24,140,fill='black',width=0))

    def changeColors(self, event):
        self.valueText = self.value.get()
        try:
            valueOhms = float(self.valueText)
        except:
            errorValue =1
        else:
            errorValue =0
        if errorValue ==1 or valueOhms < 10 or valueOhms > 1e11 :
            self.Error()
        else:
            list =[0]*3
            logValue = int(log10(valueOhms))
            magnitude = 10**logValue
            # extraction of the first significant digit:
            list[0] = int(valueOhms/magnitude)
            decimal = valueOhms/magnitude - list[0]
            # extraction of the second significant digit:
            list[1] = int(decimal*10 + 0.5)
            # number of zeros to add the two significant digit:
            list[2] = logValue -1
            # coloring the three bands:
            for n in range(3):
                self.can.itemconfigure(self.line[n], fill =self.colorsBand[list[n]])

    def Error(self):
        self.value.configure(bg ='red')
        self.root.after(1000, self.deleteValue)
        for n in range(3):
            self.can.itemconfigure(self.line[n], fill =self.colorsBand[0])

    def deleteValue(self):
        self.value.configure(bg ='white')
        self.value.delete(0, len(self.valueText))

def main():
    PyResistor()

if __name__ == '__main__':
    main()