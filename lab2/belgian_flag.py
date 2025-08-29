# belgian_flag.py

def draw_belgian_flag(canvas, x1, y1, x2, y2):
    """Draw a Belgian flag with black, yellow, and red vertical stripes."""

    stripe_width = (x2 - x1) / 3

    # Black stripe
    black_x1 = x1
    black_y1 = y1
    black_x2 = black_x1 + stripe_width
    black_y2 = y2

    canvas.create_rectangle(black_x1, black_y1, black_x2, black_y2, fill='black')

    # Yellow stripe
    yellow_x1 = black_x2
    yellow_y1 = black_y1
    yellow_x2 = yellow_x1 + stripe_width
    yellow_y2 = black_y2

    canvas.create_rectangle(yellow_x1, yellow_y1, yellow_x2, yellow_y2, fill='yellow')

    # Red stripe
    red_x1 = yellow_x2
    red_y1 = black_y1
    red_x2 = red_x1 + stripe_width
    red_y2 = black_y2

    canvas.create_rectangle(red_x1, red_y1, red_x2, red_y2, fill='red')