from tkinter import *

#TODO 1: CREATE A DICTIONARY FOR THE MORSE CODE.
MORSE_CODE_DICT = {'A':'.-', 'B':'-...',
                   'C':'-.-.', 'D':'-..', 'E':'.',
                   'F':'..-.', 'G':'--.', 'H':'....',
                   'I':'..', 'J':'.---', 'K':'-.-',
                   'L':'.-..', 'M':'--', 'N':'-.',
                   'O':'---', 'P':'.--.', 'Q':'--.-',
                   'R':'.-.', 'S':'...', 'T':'-',
                   'U':'..-', 'V':'...-', 'W':'.--',
                   'X':'-..-', 'Y':'-.--', 'Z':'--..',
                   '1':'.----', '2':'..---', '3':'...--',
                   '4':'....-', '5':'.....', '6':'-....',
                   '7':'--...', '8':'---..', '9':'----.',
                   '0':'-----', ', ':'--..--', '.':'.-.-.-',
                   '?':'..--..', '/':'-..-.', '-':'-....-',
                   '(':'-.--.', ')':'-.--.-'}


#TODO 2: CREATE A FUNCTION THAT CONVERTS STRINGS TO MORSE CODE
def to_morse():
    code = ''
    outputtxt.delete('1.0', 'end')
    message = inputtxt.get('1.0', 'end-1c')
    for i in message:
        if i != ' ':
            code += MORSE_CODE_DICT[i.upper()] + ' '
        else:
            code += '  '
    return outputtxt.insert('1.0', code.capitalize())


#TODO 3: CREATE A FUNCTION THAT CONVERTS THE MORSE CODE TO READBALE TEXT
def to_text():
    inputtxt.delete('1.0', 'end')
    message = outputtxt.get('1.0', 'end-1c')
    morse = message.split(' ')
    code = ''
    for i in morse:
        if i == '':
            code += ' '
        else:
            for j in MORSE_CODE_DICT:
                if MORSE_CODE_DICT[j] == i:
                    code += j

    return inputtxt.insert('1.0', code)


#TODO 4: CREATE A USER INTERFACE FOR THE PROGRAM


window = Tk()
window.maxsize(750, 700)
window.config(pady=30, padx=30)
window.title("Morse Code Converter")

heading = Label(text="Text to Morse Code Converter", padx=20, fg='black', font=("Times New Roman", 15, "normal"))
heading.grid(column=1, row=0)


canvas = Canvas()
canvas.config(height=96, width=96)
image = PhotoImage(file="morse-code-96.png")
image_item = canvas.create_image(48, 48, image=image)
canvas.grid(column=1, row=1)

text = Label(text="Text", padx=20, fg='black', font=("Times New Roman", 15, "normal"))
text.grid(column=0, row=2)
inputtxt = Text(window, height=10,
                width=25,
                bg="light yellow")
inputtxt.grid(column=0, rowspan=2, row=3)


morse_code = Label(text="Morse Code", padx=20, fg='black', font=("Times New Roman", 15, "normal"))
morse_code.grid(column=2, row=2)
outputtxt = Text(window, height=10,
                width=25,
                bg="light yellow")
outputtxt.grid(column=2, rowspan=2, row=3)

encrypt = Button(text='Encrypt', command=to_morse)
encrypt.grid(column=1, row=3)

decrypt = Button(text='Decrypt', command=to_text)
decrypt.grid(column=1, row=4)

window.mainloop()