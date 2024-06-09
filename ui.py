import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
from accuracy import sign

def open_gesture_window():
    gesture_window = tk.Toplevel(root)
    gesture_window.title("Gestures")
    gesture_window.configure(bg=background_color)

    # Get the screen width and height
    screen_width = gesture_window.winfo_screenwidth()
    screen_height = gesture_window.winfo_screenheight()

    # Set the gesture window size and position to fill the screen
    window_width = int(screen_width * 0.8)
    window_height = int(screen_height * 0.8)
    window_x = int((screen_width - window_width) / 2)
    window_y = int((screen_height - window_height) / 2)
    gesture_window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    # Load and display gesture image
    image_path = "gestures.png" 
    gesture_image = Image.open(image_path)
    gesture_image = gesture_image.resize((window_width, window_height), Image.ANTIALIAS)  
    gesture_image = ImageTk.PhotoImage(gesture_image)
    gesture_label = tk.Label(gesture_window, image=gesture_image, bg=background_color)
    gesture_label.image = gesture_image
    gesture_label.pack(fill="both", expand=True)

    gesture_window.mainloop()

def open_new_window(): 
    root.destroy()
    sign()
    # Add widgets or functionality to the new window

root = tk.Tk()
root.title("Main Window")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position to fit the screen
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Create a monochromatic background
background_color = "#F0F0F0"  # Custom background color
root.configure(bg=background_color)

image_path1 = "final.png"  
image1 = Image.open(image_path1)
image1 = image1.resize((300, 300), Image.ANTIALIAS)  
image1 = ImageTk.PhotoImage(image1)
image1_label = tk.Label(root, image=image1, bg=background_color)
image1_label.pack(side="left", padx=30, pady=30)

# Create a frame for the text and buttons
frame = tk.Frame(root, bg=background_color)
frame.pack()

# Create labels with highlighted and attractive appearance
label_font = font.Font(size=60, weight="bold")  # Increased font size
text_labels = ["Sign", "Language", "Recognition"]
for label_text in text_labels:
    label = tk.Label(frame, text=label_text, font=label_font, bg=background_color, fg="#333333")
    label.pack(pady=15)  # Increased padding

# Create a "Start" button with monochromatic appearance
button_font = font.Font(size=24, weight="bold")
start_button = tk.Button(frame, text="Start", font=button_font, bg="#333333", fg="white", activebackground="#555555", activeforeground="white", command=open_new_window)
start_button.pack(side="left", padx=(10, 20), pady=20)  # Updated padx value

# Create a "Show Gestures" button with increased width
show_gestures_button = tk.Button(frame, text="Show Gestures", font=button_font, bg="#333333", fg="white", activebackground="#555555", activeforeground="white", width=18, command=open_gesture_window)
show_gestures_button.pack(side="left", padx=(10, 20), pady=20)  # Updated padx value

# Load and display image
image_path = "f2.jpg"  # Replace with your own image path
image = Image.open(image_path)
image = image.resize((300, 300), Image.ANTIALIAS)  # Resize the image
image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=image, bg=background_color)
image_label.pack(side="right", padx=30, pady=30)

# Calculate the vertical center position for the frame
frame_position_y = (window_height - frame.winfo_reqheight()) // 2
frame.place(relx=0.5, rely=frame_position_y / window_height, anchor="center")

root.mainloop()
