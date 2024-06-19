import customtkinter as ctk
import subprocess
from tkinter import filedialog, messagebox, StringVar
import threading
import re

def video_to_audio(input_file, output_file, bitrate="192k"):
    command = [
        'ffmpeg', '-i', input_file, 
        '-vn',  # no video
        '-acodec', 'mp3',  # audio codec
        '-ab', bitrate,  # audio bitrate
        output_file
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    total_seconds = 0
    status_var.set("Converting...")

    for line in iter(process.stderr.readline, ''):
        if 'Duration' in line:
            match = re.search(r'Duration: (\d+):(\d+):(\d+)\.(\d+)', line)
            if match:
                hours, minutes, seconds, _ = map(int, match.groups())
                total_seconds = hours * 3600 + minutes * 60 + seconds
        elif 'time=' in line:
            match = re.search(r'time=(\d+):(\d+):(\d+)\.(\d+)', line)
            if match:
                hours, minutes, seconds, _ = map(int, match.groups())
                current_seconds = hours * 3600 + minutes * 60 + seconds
                progress = (current_seconds / total_seconds) * 100
                status_var.set(f"Converting... {int(progress)}%")
                status_label.update_idletasks()

    process.wait()
    status_var.set("Completed!")

    if process.returncode != 0:
        messagebox.showerror("Error", process.stderr.read())
    else:
        messagebox.showinfo("Success", "Conversion successful!")

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mkv *.avi")])
    if file_path:
        input_entry.delete(0, ctk.END)
        input_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio files", ".mp3")])
    if file_path:
        output_entry.delete(0, ctk.END)
        output_entry.insert(0, file_path)

def convert():
    input_file = input_entry.get()
    output_file = output_entry.get()
    bitrate = bitrate_entry.get() or "192k"

    if not input_file or not output_file:
        messagebox.showwarning("Input Error", "Please select both input and output files.")
        return
    
    threading.Thread(target=video_to_audio, args=(input_file, output_file, bitrate)).start()

# Create the main window
app = ctk.CTk()
app.title("Video to Audio Converter")

# Set the icon for the window and taskbar
app.iconbitmap("vta-icon.ico")

# Input file selection
ctk.CTkLabel(app, text="Select Input Video File:").grid(row=0, column=0, padx=10, pady=10)
input_entry = ctk.CTkEntry(app, width=300)
input_entry.grid(row=0, column=1, padx=10, pady=10)
ctk.CTkButton(app, text="Browse", command=select_input_file).grid(row=0, column=2, padx=10, pady=10)

# Output file selection
ctk.CTkLabel(app, text="Select Output Audio File:").grid(row=1, column=0, padx=10, pady=10)
output_entry = ctk.CTkEntry(app, width=300)
output_entry.grid(row=1, column=1, padx=10, pady=10)
ctk.CTkButton(app, text="Browse", command=select_output_file).grid(row=1, column=2, padx=10, pady=10)

# Bitrate selection
ctk.CTkLabel(app, text="Set Audio Bitrate (e.g, 192k):").grid(row=2, column=0, padx=10, pady=10)
bitrate_entry = ctk.CTkEntry(app, width=100)
bitrate_entry.grid(row=2, column=1, padx=10, pady=10)
bitrate_entry.insert(0, '192k')

# Status label
status_var = StringVar(value="Ready")
status_label = ctk.CTkLabel(app, textvariable=status_var)
status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Convert Button
ctk.CTkButton(app, text="Convert", command=convert).grid(row=4, column=0, columnspan=3, pady=20)

app.mainloop()
