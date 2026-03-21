import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")


list_frame = ctk.CTkFrame(app);
list_frame.pack(expand=True, fill="both", pady=10)
frame = ctk.CTkFrame(list_frame)
frame.pack(expand=True)

# Entry widget
entry = ctk.CTkEntry(frame, placeholder_text="Enter task", width=600, height=50)
entry.grid(row=0, column=0, padx=10)

# Button widget
button = ctk.CTkButton(frame, text="Add Task", width=100, height=50, bg_color="darkgreen", fg_color="darkgreen", hover_color="#45a049", corner_radius=10)
button.grid(row=0, column=1, padx=10)

label = ctk.CTkLabel(frame, text="Your tasks will appear here", width=200, height=50, bg_color="orangered", fg_color="orangered", corner_radius=10)
label.grid(row=1, column=0, columnspan=2, pady=20)

label2 = ctk.CTkLabel(frame, text="Your tasks will appear here", width=200, height=50, bg_color="orangered", fg_color="orangered", corner_radius=10)
label2.grid(row=2, column=0, columnspan=2, pady=20)

app.mainloop()