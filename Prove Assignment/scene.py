# Vinnicius Castro 
# Jan 21st 2023

# Example 1

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    
    # Call the draw_sky and draw_ground functions in this file.
    vc_draw_sky(canvas, scene_width, scene_height)
    # Call clouds and draw_oval functions in this file
    vc_clouds(canvas, 400, 450, 100, 350)
    vc_clouds(canvas, 300, 350, 50, 300)
    vc_clouds(canvas, 100, 400, 350, 325)

    vc_clouds(canvas, 650, 500, 750, 400)
    vc_clouds(canvas, 700, 450, 800, 350)
    vc_clouds(canvas, 625, 450, 750, 350)
    vc_clouds(canvas, 600, 500, 700, 400)

    vc_ground(canvas,0, 0,  scene_width, 100)

    vc_draw_pine_tree(canvas, 500, 100, 275)

    # Call ground/grass and draw_rectangle functions in this file
    
    for x in range(0, scene_width, 25):
        vc_random_size = random.randint(15,60)
        vc_newX = x + 10
        vc_grass(canvas, x, vc_random_size, vc_newX, 0)

    # x = 11
    # y = 50 
    for v in range(15, scene_width, 25):
        vc_random_size = random.randint(75,125)
        vc_newX = v + 10
        vc_grass2(canvas, v, vc_random_size, vc_newX, 25)
    for x in range(0, scene_width, 25):
        vc_random_size = random.randint(100, 150)
        vc_newX = x + 10
        vc_grass(canvas, x, vc_random_size, vc_newX, 50)

    

    
    draw_text(canvas, 50, 475, "Beautiful Morning", fill="purple")
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def vc_clouds(canvas, vc_x0, vc_y0, vc_x1, vc_y1):
    draw_oval(canvas, vc_x0, vc_y0, vc_x1, vc_y1, outline="snow1",fill="snow1")
def vc_ground(canvas,vc_right, vc_top, vc_left, vc_bottom):
    draw_rectangle(canvas, vc_right, vc_top, vc_left, vc_bottom, fill="goldenrod3")

def vc_grass(canvas, vc_right, vc_top, vc_left, vc_bottom):
    draw_rectangle(canvas, vc_right, vc_top,vc_left,vc_bottom, outline="green3", fill="green3")

def vc_grass2(canvas, vc_right, vc_top, vc_left, vc_bottom):
    draw_rectangle(canvas, vc_right, vc_top,vc_left,vc_bottom, outline="green", fill="green")


def vc_draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 10,
        scene_width, scene_height, width=0, fill="sky blue")




def vc_draw_pine_tree(canvas, vc_center_x, vc_bottom, vc_height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    vc_trunk_width = vc_height / 10
    vc_trunk_height = vc_height / 8
    vc_trunk_left = vc_center_x - vc_trunk_width / 2
    vc_trunk_right = vc_center_x + vc_trunk_width / 2
    vc_trunk_top = vc_bottom + vc_trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            vc_trunk_left, vc_trunk_top, vc_trunk_right, vc_bottom,
            outline="gray20", width=1, fill="tan3")

    vc_skirt_width = vc_height / 2
    vc_skirt_height = vc_height - vc_trunk_height
    vc_skirt_left = vc_center_x - vc_skirt_width / 2
    vc_skirt_right = vc_center_x + vc_skirt_width / 2
    vc_skirt_top = vc_bottom + vc_height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, vc_center_x, vc_skirt_top,
            vc_skirt_right, vc_trunk_top,
            vc_skirt_left, vc_trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)
# Call the main function so that
# this program will start executing.
main()