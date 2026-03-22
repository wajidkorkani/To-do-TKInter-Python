import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x200")

To_do_data = {}

def display_tasks():
    for task_id, task_info in To_do_data.items():
        task_label = ctk.CTkLabel(
            list_frame,
            text=f"{task_id}. {task_info['task']} - {task_info['status']}",
            width=250,
            height=40,
            fg_color="orangered",
            corner_radius=10
        )
        task_label.grid(row=task_id + 1, column=0, pady=5)
        
        button = ctk.CTkButton(
            list_frame,
            text="Mark Complete",
            width=120,
            height=40,
            fg_color="darkgreen",
            hover_color="#45a049",
            corner_radius=10
        )
        button.grid(row=task_id + 1, column=1, padx=10)
        button.configure(command=lambda id=task_id: mark_complete(id))
        
        delete_button = ctk.CTkButton(
            list_frame,
            text="Delete",
            width=120,
            height=40,
            fg_color="darkred",
            hover_color="#a52a2a",
            corner_radius=10
            )
        delete_button.grid(row=task_id + 1, column=2, padx=10)
        delete_button.configure(command=lambda id=task_id: delete_task(id))

list_frame = ctk.CTkFrame(app)
list_frame.pack(expand=True, padx=20, pady=20)

frame = ctk.CTkFrame(list_frame)
frame.grid(row=0, column=0, padx=10, pady=10)

# Entry widget
entry = ctk.CTkEntry(frame, placeholder_text="Enter task", width=250, height=40)
entry.grid(row=0, column=0, padx=10)

# Button widget
button = ctk.CTkButton(
    frame,
    text="Add Task",
    width=120,
    height=40,
    fg_color="darkgreen",
    hover_color="#45a049",
    corner_radius=10
)
button.grid(row=0, column=1, padx=10)

def get_data():
    task = entry.get()
    id = len(To_do_data) + 1
    To_do_data[id] = {"task": task, "status": "incomplete"}
    display_tasks()

button.configure(command=get_data)
display_tasks()

def mark_complete(task_id):
    To_do_data[task_id]["status"] = "complete"
    display_tasks()

# def delete_task(task_id):
#     del To_do_data[task_id]
#     # To_do_data.pop(task_id)
#     display_tasks()
def delete_task(task_id):
    if task_id in To_do_data:
        del To_do_data[task_id]
    display_tasks()
    
def Update():
    display_tasks()

app.mainloop()