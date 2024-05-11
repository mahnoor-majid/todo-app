import functions
import PySimpleGUI as sg
import time


sg.theme("DarkTeal6")
clock = sg.Text("", key="clock", font=("Helvetica", 9))
label = sg.Text("Type in a to-do:", font=("Helvetica", 12))
input_box = sg.InputText(tooltip="Enter to-do", key="todo", size=[47, 10])
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit", size=10)
complete_button = sg.Button("Complete", size=10)
exit_button = sg.Button("Exit", size=10)

window = sg.Window("My To-do App",
                   layout=[[clock], [label],[input_box, add_button],
                           [list_box, edit_button, complete_button], [exit_button]],
                   font=("Helvetica", 11))

while True:
    event, values = window.read(100)
    window["clock"].update(value=time.strftime("%b %d, %Y %H: %M: %S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item.", font=("Helvetica", 11))
        case "Complete":
            try:
                todo_to_remove = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item.", font=("Helvetica", 11))
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()