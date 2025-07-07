import tkinter as tk

def click(event):
    current = str(entry.get())
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

# Button frame
btn_frame = tk.Frame(root)
btn_frame.pack()

buttons=[ 
      ['1','2','3','C'],
      ['4','5','6','+'],
      ['7','8','9','*'],
      ['0','/','-','=']
      ]

for row in buttons:
    r = tk.Frame(btn_frame)
    r.pack(expand=True, fill="both")
    for char in row:
        b = tk.Button(r, text=char, font="Arial 18", relief="groove")
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()
