# main.py
import PySimpleGUI as sg

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

slogan_layout = [
    sg.Text("Slogan"),
]

credentials_layout = [
    sg.Text("username"),
    sg.Input()
]

# login_bot_layout = [
#     [
#         sg.Column(slogan_layout),
#         sg.VSeparator(),
#         sg.Column(credentials_layout),
#     ]
# ]


logo_layout = [
    [sg.Image(r'cat.png')], # the login image
]


#----- layout -----#

layout = [
    [logo_layout],
    [slogan_layout],
]

window = sg.Window('login test', layout)

#----- events -----#

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


window.close()