import sys, pygame, pygame.gfxdraw, time
pygame.init()
size = width, height = 1280, 720
max_iteration = 84
pygame.display.set_caption("Mandelbrot Graph")
screen = pygame.display.set_mode(size)
x_min = -2.5
x_max = 1
x_absolute_range = abs(x_min)+abs(x_max)
y_min = -1.3
y_max = 1.3
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
        if event.type == pygame.QUIT: sys.exit()