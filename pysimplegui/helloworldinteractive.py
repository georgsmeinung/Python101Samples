"""
Evaluating code from https://github.com/PySimpleGUI/PySimpleGUI
Required to work: PySimpleGUI availability
Install with: pip3 install pysimplegui
"""
import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='inputField')],
          [sg.Text(size=(40,1), key='outputLabel')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Interactive Hello World', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['outputLabel'].update('Hello ' + values['inputField'] + "! Thanks for trying PySimpleGUI", text_color='yellow')

# Finish up by removing from the screen
window.close()