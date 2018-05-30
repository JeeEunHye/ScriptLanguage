# -*- coding: cp949 -*-
from readdata import *
from tkinter import *
from tkinter import font

Data = LoadXMLFromFile()

window = Tk()
window.geometry("450x600+750+200")

def CreateTitleLabel():
    title = "[응급의료기관 검색 프로그램]"
    titlefont = font.Font(window, size=20, weight='bold', family='Consolas')
    ltitle = Label(window, font=titlefont, text=title)
    ltitle.pack()
    ltitle.place(x=5, y=10)

def CreateSearchListBox():
    global SearchListBox
    TempFont = font.Font(window, size=15,weight='bold', family = 'Consolas')
    SearchListBox = Listbox(window, font = TempFont, activestyle = 'none',
                            width = 10, height = 2, borderwidth = 8, relief = 'ridge')
    SearchListBox.insert(1, "기관명")
    SearchListBox.insert(2, "주소")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=70)

def CreateInputLabel():
    global InputLabel
    TempFont = font.Font(window, size = 15, weight = 'bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10,y=140)

def CreateSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font = TempFont, borderwidth = 10, text = "검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=320, y=140)

def CreateRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=370,y=190)

    TempFont = font.Font(window, size = 10, family = 'Consolas')
    RenderText = Text(window, width = 49, height = 27, borderwidth = 8, relief = 'ridge',
                      yscrollcommand = RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10,y=195)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side = RIGHT, fill = Y)
    RenderText.configure(state='disabled')

def CreatePrintListButton():
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SearchButton = Button(window, font=TempFont, borderwidth=10, text="전체 출력", command=SearchLibList)
    SearchButton.pack()
    SearchButton.place(x=150, y=80)

def SearchButtonAction():
    global SearchListBox, InputLabel, RenderText
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = str(SearchListBox.curselection())
    if iSearchIndex == "()":
        pass
    elif iSearchIndex == "(0,)": #이름검색
        keyword = str(InputLabel.get())
        SearchLibName(keyword)
    elif iSearchIndex == "(1,)": #주소검색
        keyword = str(InputLabel.get())
        SearchLibAddress(keyword)
    RenderText.configure(state = 'disabled')

def SearchLibList():
    global Data, RenderText
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    i=0
    for location in Data.find_all("item"):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, "기관명  : ")
        RenderText.insert(INSERT, location.dutyname.string)
        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, "주소    : ")
        RenderText.insert(INSERT, location.dutyaddr.string)
        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, "분류명  : ")
        RenderText.insert(INSERT, location.dutyemclsname.string)
        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, "분류    : ")
        RenderText.insert(INSERT, location.dutyemcls.string)
        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, "대표전화: ")
        RenderText.insert(INSERT, location.dutytel1.string)
        RenderText.insert(INSERT, chr(10))
        try:
            RenderText.insert(INSERT, "응급전화: ")
            RenderText.insert(INSERT, location.dutytel3.string)
            RenderText.insert(INSERT, chr(10))
        except:
            pass
        RenderText.insert(INSERT, chr(10))
        RenderText.insert(INSERT, chr(10))
        i += 1
    RenderText.configure(state='disabled')

def SearchLibName(keyword):
    global Data, RenderText
    i=0
    for location in Data.find_all("item"):
        if keyword in location.dutyname.string:
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "기관명  : ")
            RenderText.insert(INSERT, location.dutyname.string)
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "주소    : ")
            RenderText.insert(INSERT, location.dutyaddr.string)
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "분류명  : ")
            RenderText.insert(INSERT, location.dutyemclsname.string)
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "분류    : ")
            RenderText.insert(INSERT, location.dutyemcls.string)
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "대표전화: ")
            RenderText.insert(INSERT, location.dutytel1.string)
            RenderText.insert(INSERT, chr(10))
            try:
                RenderText.insert(INSERT, "응급전화: ")
                RenderText.insert(INSERT, location.dutytel3.string)
                RenderText.insert(INSERT, chr(10))
            except:
                pass
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, chr(10))
            i += 1

def SearchLibAddress(keyword):
    global Data, RenderText
    i=0
    for location in Data.find_all("item"):
        if keyword in location.dutyaddr.string:
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "기관명  : ")
            RenderText.insert(INSERT, location.dutyname.string)
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "주소    : ")
            RenderText.insert(INSERT, location.dutyaddr.string)
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "분류명  : ")
            RenderText.insert(INSERT, location.dutyemclsname.string)
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "분류    : ")
            RenderText.insert(INSERT, location.dutyemcls.string)
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, "대표전화: ")
            RenderText.insert(INSERT, location.dutytel1.string)
            RenderText.insert(INSERT, chr(10))
            try:
                RenderText.insert(INSERT, "응급전화: ")
                RenderText.insert(INSERT, location.dutytel3.string)
                RenderText.insert(INSERT, chr(10))
            except:
                pass
            RenderText.insert(INSERT, chr(10))
            RenderText.insert(INSERT, chr(10))
            i += 1


CreateTitleLabel()
CreateSearchListBox()
CreateInputLabel()
CreateSearchButton()
CreatePrintListButton()
CreateRenderText()

window.mainloop()