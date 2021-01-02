#!/usr/bin/env python
import PySimpleGUI as sg
import time

"""
 Timer Desktop Widget Creates a floating timer that is always on top of other windows You move it by grabbing anywhere on the window Good example of how to do a non-blocking, polling program using PySimpleGUI 
 Something like this can be used to poll hardware when running on a Pi
 While the timer ticks are being generated by PySimpleGUI's "timeout" mechanism, the actual value
  of the timer that is displayed comes from the system timer, time.time().  This guarantees an
  accurate time value is displayed regardless of the accuracy of the PySimpleGUI timer tick. If
  this design were not used, then the time value displayed would slowly drift by the amount of time
  it takes to execute the PySimpleGUI read and update calls (not good!)
"""


def time_as_int():
    return int(round(time.time() * 100))


# ----------------  Create Form  ----------------
sg.theme('Black')

layout = [[sg.Text('')],
          [sg.Text('', size=(8, 2), font=('Helvetica', 20),
                justification='center', key='text')],
          [sg.Button('Pause', key='-RUN-PAUSE-', button_color=('white', '#001480')),
           sg.Button('Reset', button_color=('white', '#007339'), key='-RESET-'),
           sg.Exit(button_color=('white', 'firebrick4'), key='-TIMEREXIT-')]]

timer_window = sg.Window('Running Timer', layout,
                   no_titlebar=True,
                   auto_size_buttons=False,
                   keep_on_top=True,
                   grab_anywhere=True,
                   element_padding=(0, 0))

current_time, paused_time, paused = 0, 0, False

goal = str(sg.popup_get_text('Enter time in minutes', 'Time is a man-made construct'))
while not goal.isdigit():
    sg.popup_error('bruh enter a number')
    goal = str(sg.popup_get_text('Enter time in minutes', 'Time is a man-made construct'))

start_time = time_as_int()
goal = int(goal) * 6000

while True:
    # --------- Read and update window --------
    if not paused:
        event, values = timer_window.read(timeout=10)
        current_time = time_as_int() - start_time
        if current_time >= goal:
            current_time, paused_time, paused = 0, 0, True
    else:
        event, values = timer_window.read()
    # --------- Do Button Operations --------
    if event in (sg.WIN_CLOSED, '-TIMEREXIT-'):        # ALWAYS give a way out of program
        break
    if event == '-RESET-':
        paused_time = start_time = time_as_int()
        current_time = 0
    elif event == '-RUN-PAUSE-':
        paused = not paused  # flipping the paused
        if paused:
            paused_time = time_as_int()
        else:
            start_time = start_time + time_as_int() - paused_time
        # Change button's text
        timer_window['-RUN-PAUSE-'].update('Run' if paused else 'Pause')

    # --------- Display timer in window --------
    timer_window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                        (current_time // 100) % 60,
                                                        current_time % 100))
timer_window.close()