'''
By Lily "Bingo" Marvin for the UAH Salmon Archives, specifically for use on the Saturn V Collection project.
Begun 3/30/25. Made in Python.
'''

import tkinter as tk
from tkinter import ttk
from tkinter import font

#Create main window.
root = tk.Tk()
root.title("Algae")
root.minsize(600, 600)
root.maxsize(600, 600)
root.geometry("500x500+50+50")

#Instantiate variables.
LastUpdatedMaster = "N/A"
LastUpdatedNASA = "N/A"
LastUpdatedLCNAF = "N/A"
LastUpdatedLCSH = "N/A"

mainColor = "medium sea green"
subColor = "PaleGreen3"

mainFont = font.Font(family="Cambria", size=14, weight="normal")
#End variable instantiation.

#Make main window prettier.
root.configure(background=mainColor, padx=15, pady=15)

def when_last_updated():
    '''
    when_last_updated() reads the text file storing the dates that each database
    was last updated in Algae and stores them to be printed later.

    It was implemented this way to make updating databases easier, as well as
    making updates to the databases as simple as uploaded text files.
    '''
    LUFile = open("last_updated.txt", 'r')

    global LastUpdatedMaster
    global LastUpdatedNASA
    global LastUpdatedLCNAF
    global LastUpdatedLCSH

    LastUpdatedMaster = LUFile.readline()
    LastUpdatedNASA = LUFile.readline()
    LastUpdatedLCNAF = LUFile.readline()
    LastUpdatedLCSH = LUFile.readline()

    LUFile.close()

def info_window():
    info = tk.Toplevel(root, padx=10, pady=10)
    info.title("Algae - Info")
    info.configure(background=subColor)
    info.minsize(500,500)
    info.maxsize(500,500)

    infoBlurb = tk.Label(info, background=subColor, font=mainFont, text="Algae is a tool made for the UAH Salmon Library Archives.\nIt takes a list of terms and compares them to controlled\nvocabulary databases to quickly validate them.\n")

    when_last_updated()

    textMaster = tk.Label(info, background=subColor, font=mainFont, text="Master last updated on " + LastUpdatedMaster)
    textNASA = tk.Label(info, background=subColor, font=mainFont, text="NASA last updated on " + LastUpdatedNASA)
    textLCNAF = tk.Label(info, background=subColor, font=mainFont, text="LCNAF last updated on " + LastUpdatedLCNAF)
    textLCSH = tk.Label(info, background=subColor, font=mainFont, text="LCSH last updated on " + LastUpdatedLCSH)

    emailText = tk.Label(info, background=subColor, font=mainFont, text="\nIf any are outdated, check Algae's GitHub page for\nany recent updates. If there are none, feel free to\n reach out on GitHub or at poryden.art@gmail.com")

    closeInfo = tk.Button(info, text="Close", command=info.destroy)
   
    infoBlurb.pack()
    textMaster.pack()
    textNASA.pack()
    textLCNAF.pack()
    textLCSH.pack()
    emailText.pack()

    closeInfo.pack(side=tk.BOTTOM)

def howTo_window():
    howTo = tk.Toplevel(root, padx=10, pady=10)
    howTo.title("Algae - Help")
    howTo.configure(background=subColor)
    howTo.minsize(500,500)
    howTo.maxsize(500,500)



    helpBlurb = tk.Label(howTo, background=subColor, font=mainFont, text="To use Algae, yadyaydaydya")

    closeHelp = tk.Button(howTo, text="Close", command=howTo.destroy)

    helpBlurb.pack()

    closeHelp.pack(side=tk.BOTTOM)


infoOpen = tk.Button(root, text="Info", command=info_window, padx=10, pady=10)
helpOpen = tk.Button(root, text="How to use", command=howTo_window, padx=10, pady=10)

infoOpen.grid(row=0, column=0)
helpOpen.grid(row=0, column=1)



'''
notebook = ttk.Notebook(frame)
notebook.pack(expand=True, fill="both")

tools_tab = tk.Frame(notebook, bg="lightblue")
filters_tab = tk.Frame(notebook, bg="lightgreen")
'''
#tk.Label(root, text="Nothing will work unless you do.", bg="subColor").pack()
#tk.Label(root, text="- Maya Angelou", bg="subColor").pack()