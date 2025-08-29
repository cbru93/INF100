from uib_inf100_graphics.simple import canvas, display

def draw_marilyn(canvas, x, y):
    # Background
    canvas.create_rectangle(x, y, x+100, y+100, fill='red', outline='')

    # Face
    canvas.create_oval(x+20, y+20, x+80, y+80, outline='yellow', width=2)

    # Eyes
    canvas.create_oval(x+35, y+40, x+45, y+50, fill='yellow', outline='')
    canvas.create_oval(x+55, y+40, x+65, y+50, fill='yellow', outline='')

    # Mouth
    canvas.create_arc(x+35, y+50, x+65, y+70, start=180, extent=180,
                      fill='yellow', outline='')

# Drawing four faces
draw_marilyn(canvas, 50, 50)
draw_marilyn(canvas, 250, 50)
draw_marilyn(canvas, 50, 250)
draw_marilyn(canvas, 250, 250)

display(canvas)
