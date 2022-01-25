import PySimpleGUI as sg
import send
import receive
sg.theme('DarkAmber')
layout = [
          [sg.Listbox('',size=(75,20),key='-OUT-')],
          [sg.Text('发送弹幕: ', size=(8, 1)),sg.InputText('',key='-input-'),sg.Button("Go"),sg.Button("Exit"),sg.Button("Help")],
          [sg.Text('',key='-error-')]
         ]
window=sg.Window("Bilibili弹幕收发程序",layout)
while True:
    event,values=window.read(timeout=3)
    window['-OUT-'].update(receive.Receive())
    if event in (None,'Exit'):
        break
    if event=='Go':
        window['-error-'].update(send.Send(values['-input-']))
        window['-input-'].update("")
    if event=='Help':
        sg.popup('帮助: ','请先配置好同一目录下的config.json文件')
window.close()