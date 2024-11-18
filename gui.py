# FreeSimpleGUI not compatible with Python 3.13
# (need to use earlier version of Python)

import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read() # The press of a button is en event
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
