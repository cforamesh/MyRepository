import tkinter as tk

# ---------------- Window ----------------
window = tk.Tk()
window.title("tk")
window.geometry("400x500")

# ---------------- Entry ----------------
entry = tk.Entry(window, width=30, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=20)


# ---------------- Functions ----------------

def button_click(value):
    entry.insert(tk.END, value)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# ---------------- Row 1 ----------------
tk.Button(window, text="1", width=12,
          command=lambda: button_click("1")).grid(row=1, column=0, padx=5, pady=15)

tk.Button(window, text="2", width=12,
          command=lambda: button_click("2")).grid(row=1, column=1, padx=5, pady=15)

tk.Button(window, text="3", width=12,
          command=lambda: button_click("3")).grid(row=1, column=2, padx=5, pady=15)


# ---------------- Row 2 ----------------
tk.Button(window, text="4", width=12,
          command=lambda: button_click("4")).grid(row=2, column=0, padx=5, pady=15)

tk.Button(window, text="5", width=12,
          command=lambda: button_click("5")).grid(row=2, column=1, padx=5, pady=15)

tk.Button(window, text="6", width=12,
          command=lambda: button_click("6")).grid(row=2, column=2, padx=5, pady=15)


# ---------------- Row 3 ----------------
tk.Button(window, text="7", width=12,
          command=lambda: button_click("7")).grid(row=3, column=0, padx=5, pady=15)

tk.Button(window, text="8", width=12,
          command=lambda: button_click("8")).grid(row=3, column=1, padx=5, pady=15)

tk.Button(window, text="9", width=12,
          command=lambda: button_click("9")).grid(row=3, column=2, padx=5, pady=15)


# ---------------- Row 4 ----------------
tk.Button(window, text="0", width=12,
          command=lambda: button_click("0")).grid(row=4, column=0, padx=5, pady=15)

tk.Button(window, text="+", width=12,
          command=lambda: button_click("+")).grid(row=4, column=1, padx=5, pady=15)

tk.Button(window, text="-", width=12,
          command=lambda: button_click("-")).grid(row=4, column=2, padx=5, pady=15)


# ---------------- Row 5 ----------------
tk.Button(window, text="*", width=12,
          command=lambda: button_click("*")).grid(row=5, column=0, padx=5, pady=15)

tk.Button(window, text="/", width=12,
          command=lambda: button_click("/")).grid(row=5, column=1, padx=5, pady=15)

tk.Button(window, text="=", width=12,
          command=calculate).grid(row=5, column=2, padx=5, pady=15)


# ---------------- Clear Button ----------------
tk.Button(window,
          text="Clear",
          width=15,
          command=clear).grid(row=6, column=0, padx=5, pady=20)


window.mainloop()