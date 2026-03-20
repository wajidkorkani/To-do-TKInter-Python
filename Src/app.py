import customtkinter as ctk

# To-do list
To_Do = []

# Create window
app = ctk.CTk()
app.title("To-Do")
app.geometry("600x600")

# Frame for tasks
task_frame = ctk.CTkFrame(app)
task_frame.pack(pady=20, expand=True)
task_frame._bg_color = "white"

# Entry box
entry = ctk.CTkEntry(app, placeholder_text="Enter new task")
entry.pack(pady=20)

# Add button
add_btn = ctk.CTkButton(app, text="Add Task", command=print("Task added"))
add_btn.pack(pady=5)

app.mainloop()