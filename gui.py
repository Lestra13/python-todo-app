import functions
import PySimpleGUI as Sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

Sg.theme('DarkPurple4')
clock_label = Sg.Text('', key='clock')
label = Sg.Text('Type in a todo')
input_box = Sg.InputText(tooltip="Enter a todo", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")

window = Sg.Window("Todo app",
                   layout=[[clock_label], [label],  [input_box, add_button], [list_box, edit_button, complete_button]],
                   font=("Helvetica", 20))

while True:

    event, values = window.read(timeout=998)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()

            if values['todo'] != "":
                todos.append(values['todo'] + "\n")
                functions.write_todos(todos)
                window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                Sg.popup("Please select an item first", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values['todo'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                Sg.popup("Please select an item first", font=("Helvetica", 20))
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case Sg.WINDOW_CLOSED:
            break

window.close()
