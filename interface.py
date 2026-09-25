import PySimpleGUI as sg
from Parser import *
parser=Parser()
location=str(sg.popup_get_file('Give me youre file'))

with open(location) as f:
  s=f.read()

layout = [[sg.Multiline(s,key='-INPUT-')],[sg.Button("Continue")]]

window = sg.Window('Input youre string', layout)

event, values = window.read()

window.close()

print(parser.parse(values["-INPUT-"]))