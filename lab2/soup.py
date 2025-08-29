from uib_inf100_graphics.simple import canvas, display

def draw_soup_can(can, x, y, bg_color, text_color):
    """Draw a soup can with specified colors at given coordinates."""
    can.create_rectangle(x, y+10, x+100, y+130, fill=bg_color)
    can.create_oval(x, y, x+100, y+20, fill='gray')
    can.create_oval(x, y+120, x+100, y+140, fill='gray')
    can.create_text(x+50, y+50, text='SOUP',
                       fill=text_color, font=('Arial', 16, 'bold'))

draw_soup_can(canvas, 50, 30, 'red', 'yellow')
draw_soup_can(canvas, 250, 30, 'blue', 'orange')
draw_soup_can(canvas, 50, 130, 'green', 'purple')
draw_soup_can(canvas, 250, 130, 'cyan', 'orange')

display(canvas)
