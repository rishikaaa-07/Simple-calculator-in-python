import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()

        if op == "+":
            result.set(num1 + num2)
        elif op == "-":
            result.set(num1 - num2)
        elif op == "*":
            result.set(num1 * num2)
        elif op == "/":
            result.set(num1 / num2)
    except ZeroDivisionError:
        result.set("Error: Divide by 0")
    except:
        result.set("Invalid Input")

# Main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x250")

# Variables
result = tk.StringVar()
operator = tk.StringVar(value="+")

# UI Elements
tk.Label(root, text="Number 1").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Number 2").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Operation").pack()
tk.OptionMenu(root, operator, "+", "-", "*", "/").pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

tk.Label(root, text="Result").pack()
tk.Entry(root, textvariable=result).pack()

root.mainloop()