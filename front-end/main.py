# main.py
import PySimpleGUI as sg
#---- delete unused-----#
from PySimpleGUI import InputCombo, Combo, Multiline, ML, MLine, Checkbox, CB, Check, Button, B, Btn, ButtonMenu, Canvas, Column, Col, Combo, Frame, Graph, Image, InputText, Input, In, Listbox, LBox, Menu, Multiline, ML, MLine, OptionMenu, Output, Pane, ProgressBar, Radio, Slider, Spin, StatusBar, Tab, TabGroup, Table, Text, Txt, T, Tree, TreeData,  VerticalSeparator, Window, Sizer
'''
format:
- functions
- sublayouts
- layout
- event
- window.close()
'''

#----- functions -----#

#----- sublayouts -----#

login_page_layout = [
    [Image(r'cat.png')],
    [Text('Slogan'), InputText()]
]


#----- layout -----#

# where we put all the page layouts together as columns
layout = [
    [Column(login_page_layout, visible=True)]
]

window = Window('login test', layout)

#----- events -----#

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


window.close()