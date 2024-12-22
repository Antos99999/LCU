import PySimpleGUI as sg

def GUI():
    print("GUI")
    layout = [[sg.Text("Enter match ID")],
              [sg.InputText(key='-INPUT-')],
              [sg.Button('Save ID', enable_events=True), sg.Button('Cancel')]]
    window = sg.Window('Hello Example', layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        raise SystemExit
    elif event == 'Save ID':
        ID = values['-INPUT-']
        if not ID.isdigit():
            sg.popup('ERROR - Only numbers are allowed')
            window.close()
            exit(1)
    window.close()
    return ID
