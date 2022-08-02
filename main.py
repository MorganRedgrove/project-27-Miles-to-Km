import tkinter

window = tkinter.Tk()
window.title("Miles to Km Calculator")
window.minsize(width=500, height=300)

#label
my_label_1 = tkinter.Label(text="miles", font=("Tahoma", 24, "bold"))
my_label_1.grid(column=3, row=1, padx=10, pady=10)

my_label_2 = tkinter.Label(text="is equal to", font=("Tahoma", 24, "bold"))
my_label_2.grid(column=1, row=2)

my_label_3 = tkinter.Label(text="0", font=("Tahoma", 24, "bold"))
my_label_3.grid(column=2, row=2, padx=10, pady=10)

my_label_4 = tkinter.Label(text="Km", font=("Tahoma", 24, "bold"))
my_label_4.grid(column=3, row=2, padx=10, pady=10)
#button

def button_clicked():
    conversion = int(input.get())*1.609
    my_label_3["text"] = int(conversion)

button = tkinter.Button(text="calculate", command=button_clicked)
button.grid(column=2, row=3, padx=10, pady=10)

#entry
input = tkinter.Entry()
input.insert(-1, "0")
input.grid(column=2, row=1, padx=10, pady=10)
input["width"] = 10



window.mainloop()