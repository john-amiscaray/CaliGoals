# main.py
import PySimpleGUI as sg
import time
from PySimpleGUI import InputCombo, Combo, Multiline, ML, MLine, Checkbox, CB, Check, Button, B, Btn, ButtonMenu, \
    Canvas, Column, Col, Combo, Frame, Graph, Image, InputText, Input, In, Listbox, LBox, Menu, Multiline, ML, MLine, \
    OptionMenu, Output, Pane, ProgressBar, Radio, Slider, Spin, StatusBar, Tab, TabGroup, Table, Text, Txt, T, Tree, \
    TreeData, VerticalSeparator, Window, Sizer
import back_end_integrations as back

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

def fill_goals(userId):
    goals = back.getUsersGoals(userId)

    for g in goals:
        list_goals.append([g['title'], g['description']])
        list_goal_titles.append(g['title'])

def fill_friends(userId):
    list_friends = back.getUserFriends(userId)



# ----- sublayouts -----#

# layout for the login page by Johan yeye kewl ;3
layoutthing = [
    [Text(" " * 50), Button("Enter")]

]
# ---Login Column---#
bottom_right_column = Column([
    [Text("Username", size=(7, 3))],
    [InputText(key="-USERNAME-", size=(37, 5))],
    [Text("Password", size=(7, 3))],
    [InputText(key="-PASSWORD-", size=(37, 5), password_char='*')],
    [Column(layoutthing)]
])

# ---Login PAGE---#

login_page_layout = [
    [Image(r'half_cat.png')],
    [Text('Track your progress, \nWith Cats!', size=(30, 10), font='Courier'), bottom_right_column],
]

# layout for the info bar at top
top_bar_layout = [
    [Button('Friends', key='-FRIENDS-'),
     Button('USERNAME_PLACEHOLDER', key='-HOME-'),
     Button(button_color=(sg.theme_background_color(), sg.theme_background_color()),
            image_filename=r'picture_placeholder.png', border_width=0, image_subsample=2)]  # top row of the profile
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
    [Text("GOALS")],
    # listing the goals
    [Listbox(values=[], enable_events=True, size=(40, 20), key='-GOALS_LIST-'),
     Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
            image_filename='alarm_icon.png', key='-TIMER_BUTTON-')],
    # add goal button
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'plus_icon.png', border_width=0, key='-ADD_GOAL-'), Text('New Goal')],
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
            border_width=0, image_subsample=2),
     Column(badges_layout),
     Column(goals_layout)],
]

# layout for the feed
feed_layout = [
    [Text(f'{current_friend["username"]}')],
    [Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=r'full_cat.png', border_width=0, image_subsample=2), Column(friend_badges_layout), Column(friend_goals_layout)]
]

# layout for friends frame
friends_frame_layout = [
    [Listbox(values=[3, 2, 1], enable_events=True, size=(20,20), key='-FRIENDS_LIST-')]
]


# # layout for the timer popup
# layout = [[sg.Text('')],
#           [sg.Text('', size=(8, 2), font=('Helvetica', 20),
#                 justification='center', key='text')],
#           [sg.Button('Pause', key='-RUN-PAUSE-', button_color=('white', '#001480')),
#            sg.Button('Reset', button_color=('white', '#007339'), key='-RESET-'),
#            sg.Exit(button_color=('white', 'firebrick4'), key='-TIMEREXIT-')]]
# 
# #Separate window for le timer.
# timer_window = sg.Window('Running Timer', layout,
#                    no_titlebar=True,
#                    auto_size_buttons=False,
#                    keep_on_top=True,
#                    grab_anywhere=True,
#                    element_padding=(0, 0))


# ----- layout -----#

# where we put all the page layouts together as a bunch of rows within one column
layout = [
    [Column(login_page_layout, visible=True, key='-LOGIN-'),
     Column(top_bar_layout, visible=False, key='-TOP_BAR-'),
     Column(my_profile_layout, visible=False, key='-MY_PROFILE-'),
     Column(feed_layout, visible=False, key='-FEED-')]
]

window = Window('login test', layout)

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
        except:
            sg.popup_error('wrong credentials')
            continue

        fill_goals(user_id)
        list_friends = back.getUserFriends(user_id)
        window['-GOALS_LIST-'].update(list_goal_titles)

        window['-LOGIN-'].update(visible=False)
        window['-TOP_BAR-'].update(visible=True)
        window['-MY_PROFILE-'].update(visible=True)
    # elif event == '-FRIENDS-':
    #     window['-MY_PROFILE-'].update(visible=False)
    #     window['-FEED-'].update(visible=True)
    elif event == '-HOME-':
        window['-MY_PROFILE-'].update(visible=True)
        window['-FEED-'].update(visible=False)

    # if the user wants to view friends list
    elif not f_window_active and event == '-FRIENDS-':
        f_window_active = True

        friends_list_layout = [
            [Frame('Your Friends', friends_frame_layout)],
            [Button('Add Friend', key='-ADD_FRIEND-')]
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
                    print(current_friend)

                    # after choosing a friend, close window
                    f_window_active = False
                    f_window.close()
                    click_friend = True


    # ---- dear lord the timer stuff ----#
    # elif event == '-TIMER_BUTTON-':
    #     print("clicked on timer button")
    #     goal = str(sg.popup_get_text('Enter time in minutes', 'Time is a man-made construct')) # POPUP FOR MINUTES
    #     while not goal.isdigit(): # MAKE SURE IT'S A NUMBER
    #         sg.popup_error('bruh enter a number')
    #         goal = str(sg.popup_get_text('Enter time in minutes', 'Time is a man-made construct'))
    #
    #     start_time = time_as_int()
    #     goal = int(goal) * 6000
    #
    #     current_time, paused_time, paused = 0, 0, False
    #
    #     while True:
    #         print("while this is true")
    #         if not paused:
    #             event, values = timer_window.read(timeout=10)
    #             current_time = time_as_int() - start_time
    #             if current_time >= goal:
    #                 paused = True
    #         else:
    #             event, values = timer_window.read()
    #
    #         # --------- Do Button Operations --------
    #         if event in (sg.WIN_CLOSED, '-TIMEREXIT-'):  # ALWAYS give a way out of program
    #             break
    #         if event == '-RESET-':
    #             paused_time = start_time = time_as_int()
    #             current_time = 0
    #         elif event == '-RUN-PAUSE-':
    #             paused = not paused  # flipping the paused
    #             if paused:
    #                 paused_time = time_as_int()
    #             else:
    #                 start_time = start_time + time_as_int() - paused_time
    #             # Change button's text
    #             timer_window['-RUN-PAUSE-'].update('Run' if paused else 'Pause')
    #         # --------- Display timer in window --------
    #         timer_window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
    #                                                                   (current_time // 100) % 60,
    #                                                                   current_time % 100))
    #
    #
    #
    #
    #
    # if event == '-TIMEREXIT-':
    #     timer_window.close()

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


window.close()
