import tkinter as tk
from PIL import ImageGrab

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-transparentcolor", "black")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
canvas.pack()

def is_color_in_range(pixel, target, tol):
    return all(abs(pixel[i] - target[i]) <= tol for i in range(3))

def update_overlay():
    im = ImageGrab.grab()
    px = im.load()

    canvas.delete("all")

    for y in range(screen_height):
        for x in range(screen_width):
            pixel = px[x, y]
            #if pixel[0] == 36 and pixel[1] ==  25 and pixel[2] == 39:
            if is_color_in_range(pixel, (119, 88, 130), 15):
                canvas.create_rectangle(x-5, y-5, x+5, y+5, outline="lightgreen")
                #print(f"x={x}, y={y}")

    root.after(10, update_overlay)

root.geometry(f"{screen_width}x{screen_height}+0+0")

update_overlay()

root.mainloop()