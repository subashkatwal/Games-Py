import tkinter as tk

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def perform_operation(operation):
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        result_label.config(text=f"Result is : {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero!")

def exit_program():
    root.destroy()

root = tk.Tk()  #constructor 
root.title("Calculator")

entry1_label = tk.Label(root, text="Enter first number:")
entry1_label.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2_label = tk.Label(root, text="Enter second number:")
entry2_label.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2)

add_button = tk.Button(root, text="Add", command=lambda: perform_operation('add'))
add_button.grid(row=3, column=0)

subtract_button = tk.Button(root, text="Subtract", command=lambda: perform_operation('subtract'))
subtract_button.grid(row=3, column=1)

multiply_button = tk.Button(root, text="Multiply", command=lambda: perform_operation('multiply'))
multiply_button.grid(row=4, column=0)

divide_button = tk.Button(root, text="Divide", command=lambda: perform_operation('divide'))
divide_button.grid(row=4, column=1)

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
