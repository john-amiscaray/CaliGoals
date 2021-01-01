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

login_page_layout = [
    [sg.Image(r'cat.png')],
    [sg.Text('Slogan'), sg.Input(), sg.Text("I love waffles")]
]


#----- layout -----#

# where we put all the page layouts together as columns
layout = [
    [sg.Column(login_page_layout, visible=True)]
]

window = sg.Window('login test', layout)

#----- events -----#

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


window.close()