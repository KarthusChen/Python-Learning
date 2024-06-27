# jgnnq yqtnf, -2 -> hello world
# Gur Mra bs Clguba, 13 -> The Zen of Python

# Importing necessary modules/packages
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase as upper
from string import ascii_lowercase as lower

def decode():
    # Getting text entered and shift value
    text = encoded_text.get('1.0', END)
    n = shift_entry.get()

    # Changing the state of the decoded text box to NORMAL
    # so our program can modify the contents
    # It is usually DISABLED
    decoded_text.config(state=NORMAL)
    decoded_text.delete('1.0', END)  

    # Our program requires an integer to be typed into
    # the shift entry box
    # We use a try/except/else statement to handle invalid
    # input
    try:
        n = int(n)
    except ValueError:
        # Deleting invalid input and displaying pop-up
        # with error info
        shift_entry.delete(0, END)
        messagebox.showinfo("Error!",
                            "Shift must be an integer.")
    else:
        # This is the bulk of the decodingThis.py file we
        # went over a few weeks ago
        char_list = []        
        for char in text:
            if char in upper:
                index = upper.find(char)
                index += n
                index %= 26
                char = upper[index]
                char_list.append(char)
            elif char in lower:
                index = lower.find(char)
                index += n
                index %= 26
                char = lower[index]
                char_list.append(char)
            else:
                char_list.append(char)
        # Add decoded text to decoded text box 
        decoded_text.insert('1.0', ''.join(char_list).rstrip())
    # Disabling the decoded text box once modifications are done
    decoded_text.config(state=DISABLED)

# Creating the root window and adding a title
root = Tk()
root.title('Caesar Cipher Decoder')

# Creating a frame for the encoded label, encoded scrollbar,
# and encoded text box.
# Adding the frame to the root window
encoded_frame = Frame(root)
# Adding the label to the encoded frame with text
encoded_label = Label(encoded_frame, text="Encoded Text:")
# Adding scrollbar to encoded frame
encoded_scrollbar = Scrollbar(encoded_frame)
# Adding text box to encoded frame
# default height of 15 lines, wraps on the word, attaching
# scrollbar above
encoded_text = Text(encoded_frame, height=15, wrap=WORD,
                    yscrollcommand=encoded_scrollbar.set)

shift_frame = Frame(root)
shift_label = Label(shift_frame, text="Shift:")
# Adding entry box to the shift frame
shift_entry = Entry(shift_frame)
# Binding 'Press Enter' event when focus is in the entry
# box to the decode function above
shift_entry.bind('<Return>', lambda _: decode())

decoded_frame = Frame(root)
decoded_label = Label(decoded_frame, text="Decoded Text: ")
decoded_scrollbar = Scrollbar(decoded_frame)
decoded_text = Text(decoded_frame, height=15, wrap=WORD,
                    yscrollcommand=decoded_scrollbar.set)

# Adding button to the root window with text
# Binding button clicking event to the decode function above
button = Button(root, text="Decode", command=decode)
button.bind('<Return>', lambda _: decode())

# Using pack geometry manager
# Packing all the encoded widgets into the encoded frame
encoded_label.pack()
# Scrollbar will be on right and will resize to the height
# of the frame
encoded_scrollbar.pack(side=RIGHT, fill=Y)
# As root window expands the textbox expands to fill space
# in both directions
encoded_text.pack(fill=BOTH, expand=YES)
# Adding desired behavior for scrollbar
encoded_scrollbar.config(command=encoded_text.yview)
# Packing the encoded frame in the root window
encoded_frame.pack(fill=BOTH, expand=YES)

# Using grid geometry manager
# Set location using a grid = columns/rows start at 0
shift_label.grid(row=0, column=0)
shift_entry.grid(row=0, column=1)
# Packing the shift frame in the root window
shift_frame.pack()

decoded_label.pack()
decoded_scrollbar.pack(side=RIGHT, fill=Y)
decoded_text.pack(fill=BOTH, expand=YES)
# Disable the decoded text box
decoded_text.config(state=DISABLED)
decoded_scrollbar.config(command=decoded_text.yview)
decoded_frame.pack(fill=BOTH, expand=YES)

# Packing the button in the root window
button.pack()

# Keep window open until closed
root.mainloop()
