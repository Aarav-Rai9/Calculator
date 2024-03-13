import tkinter as tk


def btn_click(item):
    global expression
    expression += str(item)
    entry_field.set(expression)


def btn_clear():
    global expression
    expression = ""
    entry_field.set("")


def btn_equal():
    global expression
    result = str(eval(expression))
    entry_field.set(result)
    expression = ""


expression = ""

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry_field = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_field, font=('Arial', 20, 'bold'), bd=20, insertwidth=4, width=14,
                 justify='right')
entry.grid(row=0, columnspan=4)

# Define the buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+'),
    ('.', '')
]

# Create and place the buttons in the grid
row = 1
for button_row in buttons:
    col = 0
    for button_text in button_row:
        if button_text == '=':
            btn = tk.Button(root, text=button_text, padx=40, pady=20, font=('Arial', 15, 'bold'),
                            command=lambda x=button_text: btn_equal())
        elif button_text == 'C':
            btn = tk.Button(root, text=button_text, padx=40, pady=20, font=('Arial', 15, 'bold'),
                            command=lambda x=button_text: btn_clear())
        else:
            btn = tk.Button(root, text=button_text, padx=40, pady=20, font=('Arial', 15, 'bold'),
                            command=lambda x=button_text: btn_click(x))
        btn.grid(row=row, column=col)
        col += 1
    row += 1

root.mainloop()
