import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")

# Entry widget
entry = ctk.CTkEntry(app, placeholder_text="Enter task", width=600, height=50)
entry.grid(row=0, column=4, padx=20, pady=20)

# Button widget
button = ctk.CTkButton(app, text="Add Task", width=100, height=50, bg_color="darkgreen", fg_color="darkgreen", hover_color="#45a049", corner_radius=10)
button.grid(row=0, column=5, padx=20, pady=20)

app.mainloop()