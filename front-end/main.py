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

list_goals = []
list_goal_titles = []

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
    [Button('Friends', key='-FRIENDS-'),
     Button('USERNAME_PLACEHOLDER', key='-HOME-'),
     Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'picture_placeholder.png', border_width=0, image_subsample=2)] # top row of the profile
]

# layout for the badges
badges_layout = [
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'picture_placeholder.png', border_width=0, image_subsample=2)],
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'picture_placeholder.png', border_width=0, image_subsample=2)],
]

# layout for friend badges
friend_badges_layout = [
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'picture_placeholder.png', border_width=0, image_subsample=2)],
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'picture_placeholder.png', border_width=0, image_subsample=2)],
]

# layout for the goals
goals_layout = [
    [Text("GOALS")],
    # listing the goals
    [Listbox(values=[], enable_events=True, size=(40, 20), key='-GOALS_LIST-'), Button(button_color =(sg.theme_background_color(),sg.theme_background_color()), border_width = 0, image_filename = 'alarm_icon.png',key='-TIMER_BUTTON-' )],
    # add goal button
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'plus_icon.png', border_width=0, key='-ADD_GOAL-')],
]

# layout for the goals
friend_goals_layout = [
    [Text("GOALS")],
    # listing the goals
    [Listbox(values=[1, 2, 3], enable_events=True, size=(40, 20), key='-FRIEND_GOALS_LIST-')],
]

# layout for your profile
my_profile_layout = [
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'full_cat.png', border_width=0, image_subsample=2),
     Column(badges_layout),
     Column(goals_layout)],
]

# layout for the feed
feed_layout = [
    [Text('FRIEND PROFILE')],
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'full_cat.png', border_width=0, image_subsample=2), Column(friend_badges_layout), Column(friend_goals_layout)]
]

#----- layout -----#

# where we put all the page layouts together as a bunch of rows within one column
layout = [
    [Column(login_page_layout, visible=True, key='-LOGIN-'),
    Column(top_bar_layout, visible=False, key='-TOP_BAR-'),
    Column(my_profile_layout, visible=False, key='-MY_PROFILE-'),
    Column(feed_layout, visible=False, key='-FEED-')]
]

window = Window('login test', layout)

#----- events -----#

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # if statements for switching windows
    elif event == 'Enter':
        window['-LOGIN-'].update(visible=False)
        window['-TOP_BAR-'].update(visible=True)
        window['-MY_PROFILE-'].update(visible=True)
    elif event == '-FRIENDS-':
        window['-MY_PROFILE-'].update(visible=False)
        window['-FEED-'].update(visible=True)
    elif event == '-HOME-':
        window['-MY_PROFILE-'].update(visible=True)
        window['-FEED-'].update(visible=False)

    # if statements for other events

    # if user adds goal, prompt user input for goal info
    elif event == '-ADD_GOAL-':
        new_goal_title = sg.popup_get_text('Please input the title of the new goal', 'Goal Title')
        new_goal_desc = sg.popup_get_text('Please input the description of your goal', 'Goal Description')
        new_goal_time = str(sg.popup_get_text('Please input how much time you want to spend on this goal in minutes', 'Goal Time'))

        while not new_goal_time.isdigit():
            sg.popup_error('Please enter a valid number.')
            new_goal_time = str(sg.popup_get_text('Please input how much time you want to spend on this goal in minutes', 'Goal Time'))

        list_goals.append([new_goal_title, new_goal_desc, new_goal_time])
        list_goal_titles.append(new_goal_title)

        window['-GOALS_LIST-'].update(list_goal_titles)

    # user clicks on goal, bring up goal description
    elif event == '-GOALS_LIST-':

        desc = None

        for i in list_goals:
            if i[0] == values['-GOALS_LIST-'][0]:
                desc = i[1]

        # if there is no description/did not click on valid goal
        if desc is None: continue

        # print(values['-GOALS_LIST-'], 'Description:', desc)
        sg.popup_ok(values['-GOALS_LIST-'][0], desc)

    print(event)


window.close()