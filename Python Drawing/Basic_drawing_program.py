import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a canvas widget where the user can draw
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create a color picker
color_picker = tk.Button(root, text="Pick a color", command=pick_color)
color_picker.pack()

# Create a brush size selector
brush_size_label = tk.Label(root, text="Brush size:")
brush_size_label.pack()
brush_size_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
brush_size_slider.pack()

# Create a function that will be called when the user clicks and drags the mouse
def paint(event):
    # Get the current brush size and color
    brush_size = brush_size_slider.get()
    brush_color = "black"  # Placeholder - replace with chosen color
    
    # Draw a circle on the canvas at the current mouse position, using the selected brush size and color
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

# Bind the paint function to mouse events on the canvas
canvas.bind("<B1-Motion>", paint)

# Run the main loop
root.mainloop()
