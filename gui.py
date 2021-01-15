import tkinter as tk
from tkinter import font
import ieee

def encode_button(number, result):
    if number == "inf" or number == "-inf":
        encoded_val=ieee.encode(number)
        result['text'] = "IEEE-754 Representation: \n" + encoded_val
    else:
        try:
            encoded_val=ieee.encode(float(number))
            result['text'] = "IEEE-754 Representation: \n" + encoded_val
        except:
            result['text'] =  "Not a valid input"
        

def decode_button(number, result):
    try:
        float(number)
        decoded_val=ieee.floatToDecimal(number)
        result['text'] = "Decimal Value: \n" + str(decoded_val)
    except:
        result['text'] =  "Not a valid input"
    
HEIGHT = 300
WIDTH = 500

root = tk.Tk()
root.title("IEEE-754 Encoder/Decoder")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.5, anchor='n')

result = tk.Label(lower_frame, font=('Courier', 12))
result.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.38, relheight=1)

encode = tk.Button(frame, text="Encode", font=40, command=lambda:encode_button(entry.get(), result))
encode.place(relx=0.4, relheight=1, relwidth=0.3)

decode = tk.Button(frame, text="Decode", font=40, command=lambda:decode_button(entry.get(), result))
decode.place(relx=0.7, relheight=1, relwidth=0.3)

root.mainloop()


