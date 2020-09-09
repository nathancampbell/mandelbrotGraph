import sys, pygame, pygame.gfxdraw, time
from tkinter import *
import tkinter.messagebox as tk_messagebox
import tkinter as tk

def main():
    user_interface()


def is_float(string):
    try:
        float(string)
        return True
    except : ValueError
    return False

def handle_user_entries(i_x_pos, i_y_pos, i_r_value):
    if(is_float(i_x_pos) and is_float(i_y_pos) and is_float(i_r_value)):
        final_x_pos = float(i_x_pos)
        final_y_pos = float(i_y_pos)
        final_r_value = float(i_r_value)
        generate_mandelbrot_window(x_pos = final_x_pos, y_pos = final_y_pos, r_value = final_r_value)
    else:
        tk_messagebox.showwarning("Warning!", "You have entered an invalid number.")


def generate_mandelbrot_window(x_pos, y_pos, r_value):
    pygame.init()
    size = width, height = 1280, 720
    max_iteration = 84
    pygame.display.set_caption("Mandelbrot Graph")
    screen = pygame.display.set_mode(size)
    x_max = x_pos + r_value
    x_min = x_pos - r_value
    y_max = y_pos + r_value * (9/16)
    y_min = y_pos - r_value * (9/16)
    x_absolute_range = abs(x_min)+abs(x_max)
    y_absolute_range = abs(y_min)+abs(y_min)

    # Process every pixel in the window.
    for x in range (1, width):
        for y in range (1, height):
            # Rescale r and i (real and imaginary)
            # to their position on the number plane.
            r = (((x/width)*x_absolute_range)+x_min)
            i = (((y/height)*y_absolute_range)+y_min)
            
            # Iterate the function f(z) = z^2 + c, until its magnitude is greater than 4, 
            # or it has been iterated a sufficient number of times.
            iteration = 0
            while ((r*r + i*i <= 4) and (iteration < max_iteration)):
                temp_r = r*r - i*i + (((x/width)*x_absolute_range)+x_min)
                i = 2*r*i + (((y/height)*y_absolute_range)+y_min)
                r = temp_r
                iteration = iteration + 1

            # Color the pixel on the screen according to what iteration the function ended on.
            pygame.gfxdraw.pixel(screen, x, y, pygame.Color(50, 50, 255, iteration*3))
    
    # Update the display
    pygame.display.flip()

    # Save the image to a file
    #pygame.image.save(screen, ".\SavedImages\save-" + str(time.time()) + ".png")

    # Wait for the quit event
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

def user_interface():
    #initialize the gui
    window = tk.Tk()

    #create labels, 
    x_pos_label = tk.Label(text = "X position")
    x_pos_label.pack()
    x_pos_entry = tk.Entry()
    x_pos_entry.insert(0, "-.5")
    x_pos_entry.pack()
    y_pos_label = tk.Label(text = "Y position")
    y_pos_label.pack()
    y_pos_entry = tk.Entry()
    y_pos_entry.insert(0, "0")
    y_pos_entry.pack()
    r_value_label = tk.Label(text = "R value")
    r_value_label.pack()
    r_value_entry = tk.Entry()
    r_value_entry.insert(0, "2")
    r_value_entry.pack()

    #create a button to generate the mandelbrot set image in another window
    generation_button = tk.Button(
        text = "Generate Mandelbrot Image",
        width = 25,
        height = 5,
        command = lambda: handle_user_entries(x_pos_entry.get(), y_pos_entry.get(), r_value_entry.get())
    )
    generation_button.pack()
    
    #display the gui window and wait for events
    window.mainloop()

if __name__ == "__main__":
    main()