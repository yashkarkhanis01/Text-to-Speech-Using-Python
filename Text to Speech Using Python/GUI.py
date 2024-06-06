import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from gtts import gTTS
import os

def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    language = language_entry.get()
    
    if not text:
        messagebox.showerror("Error", "Please enter text to convert.")
        return
    
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save("output.mp3")
        os.system("start output.mp3")  # Play the audio
        messagebox.showinfo("Success", "Audio generated and played.")
    except ValueError:
        messagebox.showerror("Error", f"Language '{language}' is not supported.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Load and display background image
bg_image = Image.open("bg.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Center the window
window_width = 500
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Create and position widgets
input_frame = tk.Frame(root, bg="white", bd=5)
input_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

text_label = tk.Label(input_frame, text="Enter Text:")
text_label.grid(row=0, column=0, padx=10, pady=5)

text_entry = tk.Text(input_frame, height=5, width=50)
text_entry.grid(row=0, column=1, padx=10, pady=5)

language_label = tk.Label(input_frame, text="Language (optional):")
language_label.grid(row=1, column=0, padx=10, pady=5)

language_entry = tk.Entry(input_frame)
language_entry.grid(row=1, column=1, padx=10, pady=5)

convert_button = tk.Button(input_frame, text="Convert to Speech", command=text_to_speech)
convert_button.grid(row=2, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()
