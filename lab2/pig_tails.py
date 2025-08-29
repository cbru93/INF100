from uib_inf100_graphics.simple import canvas, display

# Legs
canvas.create_rectangle(110, 230, 150, 300, fill="pink")
canvas.create_rectangle(300, 230, 340, 300, fill="pink")
canvas.create_rectangle(80, 260, 120, 330, fill="pink")
canvas.create_rectangle(280, 260, 320, 330, fill="pink")

# Ears
canvas.create_polygon(260, 70, 260, 30, 290, 60, fill="pink", outline="black")
canvas.create_polygon(310, 55, 330, 30, 340, 70, fill="pink", outline="black")

# Body
canvas.create_oval(50, 100, 350, 300, fill="pink")

# Head
canvas.create_oval(250, 50, 350, 150, fill="pink")

# Eyes
canvas.create_oval(280, 70, 295, 85, fill="black")
canvas.create_oval(320, 70, 335, 85, fill="black")

# Nose
canvas.create_oval(290, 100, 330, 130, fill="lightpink")
canvas.create_oval(295, 110, 305, 120, fill="black")
canvas.create_oval(315, 110, 325, 120, fill="black")

# Tail - positioned at the back of the pig with curls
canvas.create_line(60, 167, 50, 150, 40, 110, 60, 100, 65, 115, 55, 125, 45, 110, 57, 110)
# canvas.create_line(40, 180, 20, 160, 0, 180)   # Second curl
# canvas.create_line(0, 180, 20, 200, 40, 180)   # Third curl
# canvas.create_line(40, 180, 60, 200, 80, 180)  # Fourth curl

display(canvas)
