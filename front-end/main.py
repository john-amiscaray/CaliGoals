# main.py
import PySimpleGUI as sg
import time
import timer
from PySimpleGUI import InputCombo, Combo, Multiline, ML, MLine, Checkbox, CB, Check, Button, B, Btn, ButtonMenu, \
    Canvas, Column, Col, Combo, Frame, Graph, Image, InputText, Input, In, Listbox, LBox, Menu, Multiline, ML, MLine, \
    OptionMenu, Output, Pane, ProgressBar, Radio, Slider, Spin, StatusBar, Tab, TabGroup, Table, Text, Txt, T, Tree, \
    TreeData, VerticalSeparator, Window, Sizer
import back_end_integrations as back
from copy import deepcopy
'''
format:
- functions
- sublayouts
- layout
- event
- window.close()
'''
sg.theme("LightBrown3")

#----- values -----#
user = ''
list_goals = []
list_goal_titles = []
list_friends = []
current_friend = {
            "userId": 0,
            "username": "default",
            "password": "", # set blank for obvious reasons
            "growthAmount": 0,
            "profilePicture": None}

# ----- functions -----#

def time_as_int():
    return int(round(time.time() * 100))

list_goals = []
list_goal_titles = []
growth = 0

def getCatLevel(growth):
    # YOU CAN EDIT THESE VALUES IN THE FUTURE I DIDN'T PUT MUCH THOUGHT INTO THIS
    if growth >= 9000:
        return 'level4.png'
    elif growth >= 6000:
        return 'level3.png'
    elif growth >= 3000:
        return 'level2.png'
    else:
        return 'level1.png'


def refresh_growth(userId):
    global growth
    growth = back.getGrowth(userId)

def fill_goals(userId):
    goals = back.getUsersGoals(userId)
    refresh_growth(userId)
    for g in goals:
        list_goals.append([g['title'], f"Description:\n{g['description']}\nTimeSpent: {g['timeSpent'] // 6000} minutes"])
        list_goal_titles.append(g['title'])

def fill_friends(userId):
    list_friends = back.getUserFriends(userId)


def update_goals():
    global list_goals, list_goal_titles
    list_goals = []
    list_goal_titles = []
    fill_goals(user_id)
    window['-GOALS_LIST-'].update(list_goal_titles)


# ----- sublayouts -----#

# layout for the login page by Johan yeye kewl ;3
layoutthing = [
    [Text(" " *48), Button("Enter", font=('Courier', 10))]
]

# ---Login Column---#
bottom_right_column = Column([
    [Text("Username", size=(10, 2), font=('Courier', 12))],
    [InputText(key="-USERNAME-", size=(37, 5), background_color='#E0DEDE')],
    [Text("Password", size=(10, 2), font=('Courier', 12))],
    [InputText(key="-PASSWORD-", size=(37, 5), password_char='*', background_color='#E0DEDE')],
    [Column(layoutthing)]
])

# ---Login PAGE---#
bot_page = [
    [Text('\n\n\nTrack your progress, \nWith Cats!', size=(30, 10), font=('Courier', 12, 'bold'), justification='center'), bottom_right_column],
]

login_page_layout = [
    [Image(r'half_cat.png')],
    [Frame('', bot_page, background_color=sg.theme_input_background_color(), border_width=0)]
]

# layout for the info bar at top
top_bar_frame_layout = [
    [Text('Welcome to CaliGoals!', justification='centre', font=('Courier', 12), background_color=sg.theme_button_color()[0])],
    [Button(button_color=(sg.theme_button_color()[0], sg.theme_button_color()[0]),
            image_filename=r'paw_icon.png', border_width=0, key='-FRIENDS-'),
     Button(button_color=(sg.theme_button_color()[0], sg.theme_button_color()[0]),
            image_filename=r'home_icon.png', border_width=0, key='-HOME-'),
     Text(' '*40, text_color=sg.theme_button_color()[0], background_color=sg.theme_button_color()[0]),
     Button(button_color=(sg.theme_button_color()[0], sg.theme_button_color()[0]),
            image_filename=r'default_pfp.png', border_width=0, image_subsample=8)]  # top row of the profile
]

top_bar_layout = [
    [Frame('', top_bar_frame_layout, background_color=sg.theme_button_color()[0], border_width=5)]
]

# layout for the badges
badges_layout = [
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),
            image_filename=r'picture_placeholder.png', border_width=0, image_subsample=2)],
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),
            image_filename=r'picture_placeholder.png', border_width=0, image_subsample=2)],
]

# layout for friend badges
friend_badges_layout = [
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),
            image_filename=r'picture_placeholder.png', border_width=0, image_subsample=2)],
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),
            image_filename=r'picture_placeholder.png', border_width=0, image_subsample=2)],
]

# layout for the goals
goals_layout = [
    [Text("GOALS", font=('Courier', 12))],
    # listing the goals
    [Listbox(values=[], enable_events=True, size=(40, 20), font=('Courier', 10), key='-GOALS_LIST-'),
     Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
            image_filename='alarm_icon.png', key='-TIMER_BUTTON-')],
    # add goal button
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'plus_icon.png', border_width=0, key='-ADD_GOAL-', image_size=(100, 100)), Text('New Goal', font=('Courier', 12))],
]

# layout for the goals
friend_goals_layout = [
    [Text("GOALS")],
    # listing the goals
    [Listbox(values=[1, 2, 3], enable_events=True, size=(40, 20), key='-FRIEND_GOALS_LIST-')],
]

# layout for your profile
my_profile_layout = [
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'full_cat.png',
            border_width=0, image_subsample=2, key='-YOUR_CAT-'),
     Column(badges_layout),
     Column(goals_layout)],
]

# layout for the feed
feed_layout = [
    [Text(f'{current_friend["username"]}', key='-CURRENT_FRIEND-', size=(29, 0), justification='center', font=('courier', 26))],
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'full_cat.png', border_width=0, image_subsample=2, key='-FRIEND_CAT-'), Column(friend_badges_layout), Column(friend_goals_layout)]
]

# layout for friends frame
friends_frame_layout = [
    [Listbox(values=[3, 2, 1], enable_events=True, size=(20,20), key='-FRIENDS_LIST-')]
]


# layout for the timer popup
layout = [[sg.Text('')],
          [sg.Text('', size=(8, 2), font=('Helvetica', 20),
                justification='center', key='text')],
          [sg.Button('Pause', key='-RUN-PAUSE-', button_color=('white', '#001480')),
           sg.Button('Reset', button_color=('white', '#007339'), key='-RESET-'),
           sg.Exit(button_color=('white', 'firebrick4'), key='-TIMEREXIT-')]]

#Separate window for le timer.
timer_window = sg.Window('Running Timer', layout,
                   no_titlebar=True,
                   auto_size_buttons=False,
                   keep_on_top=True,
                   grab_anywhere=True,
                   element_padding=(0, 0))


# ----- layout -----#

# where we put all the page layouts together as a bunch of rows within one column
layout = [
    [Column(login_page_layout, visible=True, key='-LOGIN-'),
     Column(top_bar_layout, visible=False, key='-TOP_BAR-'),
     Column(my_profile_layout, visible=False, key='-MY_PROFILE-'),
     Column(feed_layout, visible=False, key='-FEED-')]
]

window = Window('CaliGoals', layout)

# ----- events -----#
#
# start_time = time_as_int()
# current_time, paused_time, paused = 0, 0, False

f_window_active = False
click_friend = False
while True:
    event, values = window.read(timeout=100)

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Friends':
        print("clicked on friends")

    # if statements for switching pages
    elif event == 'Enter':
        user = values['-USERNAME-']
        password = values['-PASSWORD-']

        try:
            user_id = back.login((user, password))
            window['-HOME-'].update(text=user)
        except:
            sg.popup_error('wrong credentials')
            continue

        fill_goals(user_id)
        list_friends = back.getUserFriends(user_id)

        window['-GOALS_LIST-'].update(list_goal_titles)
        window['-LOGIN-'].update(visible=False)
        window['-TOP_BAR-'].update(visible=True)
        window['-MY_PROFILE-'].update(visible=True)
        window['-YOUR_CAT-'].update(image_filename=getCatLevel(growth))

    elif event == '-HOME-':
        window['-MY_PROFILE-'].update(visible=True)
        window['-FEED-'].update(visible=False)

    elif event == '-TIMER_BUTTON-':
        # check if the user selected a goal
        try:
            print(values['-GOALS_LIST-'][0])
        except:
            sg.popup_quick_message('Select a goal to time!', font=('Courier', 12, 'bold'), background_color='yellow')
            continue

        time_spent = timer.openTimer()
        if time_spent is not None:
            back.addGrowth(user_id, time_spent)
            refresh_growth(user_id)
            window['-YOUR_CAT-'].update(image_filename=getCatLevel(growth))
            back.addTimeToGoal(user_id, values['-GOALS_LIST-'][0], time_spent)
            update_goals()
    # if the user wants to view friends list
    elif not f_window_active and event == '-FRIENDS-':
        f_window_active = True
        friends_list_layout = [
            [Frame('Your Friends', deepcopy(friends_frame_layout), font=('Courier', 12))],
            [Button('Add Friend', key='-ADD_FRIEND-', font=('Courier', 10))]
        ]
        f_window = Window('Friends', friends_list_layout)

    # while friends list page is active
    elif f_window_active:
        ev2, vals2 = f_window.read(timeout=100)

        # update list of friends
        f_window['-FRIENDS_LIST-'].update([f['username'] for f in list_friends])

        if ev2 == sg.WIN_CLOSED:
            f_window_active = False
            f_window.close()

        # if they click on friends list, set current friend to friend clicked.
        elif ev2 == '-FRIENDS_LIST-':
            for f in list_friends:
                if f['username'] == vals2['-FRIENDS_LIST-'][0]:
                    current_friend = f
                    window['-CURRENT_FRIEND-'].update(value=current_friend['username'])
                    window['-FRIEND_GOALS_LIST-'].update([i['title'] for i in back.getUsersGoals(f["userId"])])
                    window['-FRIEND_CAT-'].update(image_filename=getCatLevel(f["growthAmount"]))
                    # after choosing a friend, close window
                    f_window_active = False
                    f_window.close()
                    click_friend = True

    # if statements for other events

    # if user adds goal, prompt user input for goal info
    # if the user clicked on a friend
    elif click_friend:
        click_friend = False
        window['-MY_PROFILE-'].update(visible=False)
        window['-FEED-'].update(visible=True)

    elif event == '-ADD_GOAL-':

        # popup returns None if cancelled then continues
        new_goal_title = sg.popup_get_text('Please input the title of the new goal', 'Goal Title')
        if new_goal_title is None: continue
        new_goal_desc = sg.popup_get_text('Please input the description of your goal', 'Goal Description')
        if new_goal_desc is None: continue
        new_goal_time = sg.popup_get_text('Please input how much time you want to spend on this goal in minutes', 'Goal Time')
        if new_goal_time is None: continue

        new_goal_time = sg.popup_get_text('Please input how much time you want to spend on this goal in minutes', 'Goal Time')

        while not str(new_goal_time).isdigit():
            sg.popup_error('Please enter a valid number.')
            new_goal_time = str(
                sg.popup_get_text('Please input how much time you want to spend on this goal in minutes', 'Goal Time'))

        list_goals.append([new_goal_title, new_goal_desc, new_goal_time])
        list_goal_titles.append(new_goal_title)

        window['-GOALS_LIST-'].update(list_goal_titles)

        back.addGoal(user_id, new_goal_title, time_as_int(), time_as_int() + 1, new_goal_desc)

    # user clicks on goal, bring up goal description
    elif event == '-GOALS_LIST-':
        desc = None

        # search for goal
        for i in list_goals:
            if i[0] == values['-GOALS_LIST-'][0]:
                desc = i[1]

        # if there is no description/did not click on valid goal
        if desc is None: continue

        # print(values['-GOALS_LIST-'], 'Description:', desc)

        sg.popup_ok(values['-GOALS_LIST-'][0], desc)

    elif event == '-YOUR_CAT-':
        sg.popup_quick_message('Meow!', auto_close_duration=100, font=('Courier', 30, 'bold'), background_color='#BEF2F8')


window.close()
