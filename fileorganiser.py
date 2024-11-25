import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File categories based on extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css", ".php", ".rb", ".swift"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".bin", ".apk"],
    "Others": []
}

# Organize files in the chosen directory
def organize_files(directory):
    if not directory:
        messagebox.showerror("Error", "Please select a directory.")
        return
    try:
        # Create necessary folders and move files
        for category, extensions in FILE_CATEGORIES.items():
            os.makedirs(os.path.join(directory, category), exist_ok=True)
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                ext = os.path.splitext(item)[1].lower()
                folder = next((cat for cat, exts in FILE_CATEGORIES.items() if ext in exts), "Others")
                shutil.move(item_path, os.path.join(directory, folder, item))
        messagebox.showinfo("Success", "Files have been organized successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup with tkinter
def browse_directory():
    directory_path.set(filedialog.askdirectory())

# Main application setup
app = tk.Tk()
app.title("File Organizer | Developed by Abhinandan")
app.geometry("400x300")
app.resizable(False, False)

# Setting a background color
app.configure(bg="#f0f8ff")

# Main Frame for better layout management
main_frame = tk.Frame(app, bg="#ffffff", bd=2, relief="groove")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Directory path variable
directory_path = tk.StringVar()

# Adding some style
label_style = {"font": ("Helvetica", 12, "bold"), "bg": "#ffffff", "fg": "#333333"}
button_style = {
    "font": ("Helvetica", 10, "bold"), 
    "bg": "#20b2aa",  # Light teal background
    "fg": "#000000",  # White text for contrast
    "activebackground": "#2e8b57",  # Darker green for active effect
    "activeforeground": "#ffffff",
    "relief": "raised",
    "bd": 3
}
entry_style = {"font": ("Helvetica", 10), "width": 40, "relief": "sunken"}

# Header Label
header_label = tk.Label(main_frame, text="Organize Your Files", font=("Helvetica", 16, "bold"), bg="#ffffff", fg="#20b2aa")
header_label.pack(pady=15)

# Directory selection
tk.Label(main_frame, text="Select Directory to Organize:", **label_style).pack(pady=5)
directory_entry = tk.Entry(main_frame, textvariable=directory_path, **entry_style)
directory_entry.pack(pady=5)

# Browse Button
browse_button = tk.Button(main_frame, text="Browse", command=browse_directory, **button_style)
browse_button.pack(pady=5)

# Organize Button
organize_button = tk.Button(main_frame, text="Organize Files", command=lambda: organize_files(directory_path.get()), **button_style)
organize_button.pack(pady=15)

# Footer label
footer_label = tk.Label(app, text="Developed by Abhinandan | File Organizer", font=("Arial", 10), fg="gray", bg="#f0f8ff")
footer_label.pack(side="bottom", pady=10)

app.mainloop()
