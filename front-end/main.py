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
sg.theme("LightBrown3")


#----- functions -----#

#----- sublayouts -----#

# layout for the login page by Johan yeye kewl ;3
layoutthing = [
    [Text(" "*50),Button("Enter")]

]
# ---Login Column---#
bottom_right_column = Column([
    [Text("Username",size=(7,3))],
    [InputText(key="-USERNAME-",size=(37,5))],
    [Text("Password", size=(7,3))],
    [InputText(key="-PASSWORD-", size=(37,5))],
    [Column(layoutthing)]
])

#---Login PAGE---#

login_page_layout = [
    [Image(r'half_cat.png')],
    [Text('Track your progress, \nWith Cats!', size = (30,10), font='Courier'), bottom_right_column],
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
    # add goal button
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'plus_icon.png', border_width=0, key='-ADD_GOAL-')],
]

my_profile_layout = [
    [top_bar_layout],
    [Image(r'picture_placeholder.png'), badges_layout, goals_layout]
]


# layout for your profile
my_profile_layout = [
    [Image(r'picture_placeholder.png'), Column(badges_layout), Column(goals_layout)],
]

#----- layout -----#

# where we put all the page layouts together as columns
layout = [
    [Column(login_page_layout, visible=True, key='-LOGIN-')],
    [Column(top_bar_layout, visible=False, key='-TOP_BAR-')],
    [Column(my_profile_layout, visible=False, key='-MY_PROFILE-')],
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