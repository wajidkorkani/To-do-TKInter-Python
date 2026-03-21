import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x200")

To_do_data = {
    1: {"task": "Buy groceries", "status": "incomplete"},
    2: {"task": "Finish project report", "status": "incomplete"}
}

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

app.mainloop()