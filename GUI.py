import tkinter as tk
import PIL

# intit the root
root = tk.Tk()
root.title("Play Chess")

# Board size constants
BOARD_SIZE = 400
SQUARE_SIDE = BOARD_SIZE / 8


# mapping of Board indicies to GUI image anchors (and vice versa)
def board_to_gui(x, y):
    return SQUARE_SIDE * x, SQUARE_SIDE * y


def gui_to_board(x, y):
    return x / SQUARE_SIDE, y / SQUARE_SIDE


# Start Canvas
canvas = tk.Canvas(root, width=600, height=600)
counter = 0
for x in range(50, 400, 50):
    for y in range(50, 400, 50):
        fill = "silver"
        if counter % 2 == 1:
            fill = "black"
        canvas.create_rectangle(x - 50, y - 50, x, y, outline="white", fill=fill)
        counter += 1

canvas.pack()


king = tk.PhotoImage(file="images/King.png")
# king_can = tk.Canvas(root, width=king.width(), height=king.height())
# king_can.pack()
king_can = canvas
king_can.create_image(0, 0, image=king)
print(king.width(), king.height())

# need to set variable for image as global bc of grabage collection
def drag(event):
    global king
    king = tk.PhotoImage(file="images/King.png")
    king_can.create_image(event.x_root, event.y_root, image=king)
    # event.widget.place(x=event.x_root, y=event.y_root, anchor=tk.CENTER)

king_can.bind("<B1-Motion>", drag)

root.mainloop()
