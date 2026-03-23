import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x300")

To_do_data = {}

def display_tasks():

    # Clear old widgets except the input frame
    for widget in list_frame.winfo_children():
        if widget != frame:
            widget.destroy()

    row_index = 1

    for task_id, task_info in To_do_data.items():

        task_label = ctk.CTkLabel(
            list_frame,
            text=f"{task_id}. {task_info['task']} - {task_info['status']}",
            width=250,
            height=40,
            fg_color="orangered",
            corner_radius=10
        )
        task_label.grid(row=row_index, column=0, pady=5)

        complete_button = ctk.CTkButton(
            list_frame,
            text="Mark Complete",
            width=120,
            height=40,
            fg_color="darkgreen",
            hover_color="#45a049",
            corner_radius=10,
            command=lambda id=task_id: mark_complete(id)
        )
        complete_button.grid(row=row_index, column=1, padx=10)

        delete_button = ctk.CTkButton(
            list_frame,
            text="Delete",
            width=120,
            height=40,
            fg_color="darkred",
            hover_color="#a52a2a",
            corner_radius=10,
            command=lambda id=task_id: delete_task(id)
        )
        delete_button.grid(row=row_index, column=2, padx=10)

        row_index += 1


def get_data():
    task = entry.get().strip()

    if task == "":
        return

    task_id = len(To_do_data) + 1
    To_do_data[task_id] = {"task": task, "status": "incomplete"}

    entry.delete(0, "end")

    display_tasks()


def mark_complete(task_id):
    if task_id in To_do_data:
        To_do_data[task_id]["status"] = "complete"
    display_tasks()


def delete_task(task_id):
    if task_id in To_do_data:
        del To_do_data[task_id]
    display_tasks()


# Main task frame
list_frame = ctk.CTkFrame(app)
list_frame.pack(expand=True, padx=20, pady=20)

# Input frame
frame = ctk.CTkFrame(list_frame)
frame.grid(row=0, column=0, columnspan=3, pady=10)

entry = ctk.CTkEntry(frame, placeholder_text="Enter task", width=250, height=40)
entry.grid(row=0, column=0, padx=10)

button = ctk.CTkButton(
    frame,
    text="Add Task",
    width=120,
    height=40,
    fg_color="darkgreen",
    hover_color="#45a049",
    corner_radius=10,
    command=get_data
)
button.grid(row=0, column=1, padx=10)

display_tasks()

app.mainloop()