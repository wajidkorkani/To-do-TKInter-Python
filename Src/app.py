import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")

frame = ctk.CTkFrame(app)
frame.pack(expand=True)
# Entry widget
entry = ctk.CTkEntry(frame, placeholder_text="Enter task", width=600, height=50)
entry.grid(row=0, column=0, padx=10)

# Button widget
button = ctk.CTkButton(frame, text="Add Task", width=100, height=50, bg_color="darkgreen", fg_color="darkgreen", hover_color="#45a049", corner_radius=10)
button.grid(row=0, column=1, padx=10)

app.mainloop()