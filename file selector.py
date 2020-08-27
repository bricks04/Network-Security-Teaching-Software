import tkinter

while True:
    selection = input("Select string input method('t':text,'f':file)\n>>>")
    if selection.lower() == "f":
        from tkinter.filedialog import askopenfilename
        filename = askopenfilename()
        print(filename)
        #Resolve filename into text
        break
    elif selection.lower() == "t":
      result = input(">>>")
      break