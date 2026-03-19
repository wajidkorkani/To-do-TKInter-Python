import customtkinter as ctk

# To-do list
To_Do = []

# Create window
app = ctk.CTk()
app.title("To-Do")
app.geometry("600x600")

# Frame for tasks
task_frame = ctk.CTkFrame(app)
task_frame.pack(pady=10, fill="both", expand=True)
task_frame._bg_color = "black"

# Function to display tasks
def show_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for item in To_Do:
        text = item["task"]
        checkbox = ctk.CTkCheckBox(task_frame, text=text)
        checkbox.pack(anchor="w", padx=10, pady=5)

# Function to add task
def add_task():
    task = entry.get()
    if task:
        To_Do.append({"task": task, "completed": False})
        entry.delete(0, "end")
        show_tasks()

# Entry box
entry = ctk.CTkEntry(app, placeholder_text="Enter new task")
entry.pack(pady=10)

# Add button
add_btn = ctk.CTkButton(app, text="Add Task", command=add_task)
add_btn.pack(pady=5)

# Show tasks initially
show_tasks()

app.mainloop()