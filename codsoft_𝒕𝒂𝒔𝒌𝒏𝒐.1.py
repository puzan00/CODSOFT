#Todolist project
import tkinter as tk

todo_list = []

def display_tasks():
    task_list.delete(0, tk.END)
    for i, task in enumerate(todo_list, start=1):
        task_list.insert(tk.END, f"{i}) {task}")

def add_task():
    task = task_entry.get()
    if task:
        todo_list.append(task)
        task_entry.delete(0, tk.END)
        display_tasks()

def edit_task():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        new_task = task_entry.get()
        if new_task:
            todo_list[index] = new_task
            task_entry.delete(0, tk.END)
            display_tasks()

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        todo_list.pop(index)
        display_tasks()

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")  
root.resizable(False, False)  

# Set the background color of the window
root.configure(bg="#FFFFF0")

# Create a label for the task list
list_label = tk.Label(root, text="To-Do List", font=("Arial", 14))
list_label.pack()

# Create a listbox to display tasks
task_list = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
task_list.pack()

# Create an entry field for task input
task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.pack()

# Create a frame for the action buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create buttons for actions with background color and display them in a row with margin
add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Arial", 12), background="#32CD32")
edit_button = tk.Button(button_frame, text="Edit Task", command=edit_task, font=("Arial", 12), background="#32CD32")
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Arial", 12), background="#E34234")

add_button.pack(side=tk.LEFT, padx=8, pady=20)
edit_button.pack(side=tk.LEFT, padx=8, pady=20)
delete_button.pack(side=tk.LEFT, padx=8, pady=20)

display_tasks()

root.mainloop()
