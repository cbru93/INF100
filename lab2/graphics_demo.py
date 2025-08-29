from uib_inf100_graphics.simple import canvas, display

canvas.create_rectangle(100, 50, 300, 150, outline='red')
canvas.create_text(200, 100, text='Hei, grafikk!', font='Arial 20 bold')

display(canvas)
