# main.py
import PySimpleGUI as sg
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

# layout for the login page
login_page_layout = [
    [Image(r'cat.png')],
    [Text('Slogan'), Input()]
]

# layout for the info bar at top
top_bar_layout = [
    [Button('Friends'), Button('USERNAME_PLACEHOLDER'), Image(r'picture_placeholder.png')] # top row of the profile
]

# layout for the badges
badges_layout = [
    [Listbox]
]

my_profile_layout = [
    [top_bar_layout],
    [Image(r'picture_placeholder.png'), badges_layout, goals_layout]
]



#----- layout -----#

# where we put all the page layouts together as columns
layout = [
    [Column(login_page_layout, visible=False)],
    [Column(top_bar_layout, visible=True)],
]

window = Window('login test', layout)

#----- events -----#

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Friends':
        print("clicked on friends")


window.close()