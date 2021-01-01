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
    [Image(r'picture_placeholder.png')],
    [Image(r'picture_placeholder.png')],
]

# layout for the goals
goals_layout = [
    [Text("GOALS")],
    # listing the goals
    [Listbox(values=[1, 2, 3], enable_events=True, size=(40, 20), key='-GOALS_LIST-'), Button(key='-TIMER_BUTTON-')],
    [Button("+", key='-ADD_GOAL-')],
]

# layout for your profile
my_profile_layout = [
    [Image(r'picture_placeholder.png'), Column(badges_layout), Column(goals_layout)],
]

#----- layout -----#

# where we put all the page layouts together as columns
layout = [
    [Column(login_page_layout, visible=False, key='-LOGIN-')],
    [Column(top_bar_layout, visible=True, key='-TOP_BAR-')],
    [Column(my_profile_layout, visible=True, key='-MY_PROFILE-')],
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