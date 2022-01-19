from tkinter import *
from newCesarCD import *

def IF_cesarC():
	def generateList(txt):
		num=[]
		for i in range(len(txt)):
			if txt[i].isalpha():
				num.append(random.randint(1,25))
		return num
	userInputText=userText.get("1.0", "end")
	randomList=generateList(userInputText)
	newTextVariable3.set(randomList)
	newTextVariable2.set(cesarC(userInputText, randomList))

def IF_cesarD():
	userInputText=userText.get("1.0", "end")
	userKeyList=keyList.get("1.0", "end")
	cleanKeyList=userKeyList.replace("(", "").replace(")", "")
	newTextVariable.set(cesarD(userInputText, cleanKeyList))
	#newTextVariable.set("Funciona!")

def copyD():
    root.clipboard_clear()
    root.clipboard_append(newTextInvisible.get())

def copyCT():
    root.clipboard_clear()
    root.clipboard_append(newTextInvisible2.get())

def copyCL():
	root.clipboard_clear()
	root.clipboard_append(newTextVariable3.get())

root=Tk()
root.title("Caesar Cipher 1.0")
#root.iconbitmap("encryption.ico")
root.resizable(0,0)
newTextVariable=StringVar()
newTextVariable2=StringVar()
newTextVariable3=StringVar()

#root.config(bg="black")


#root.geometry("1200x700")
#root.resizable(1,1)


frame1=Frame(root, width=400, height=300,)
frame1.pack(side="top", anchor="nw")

labelText=Label(frame1, text="Text:", font=("Comic Sans MS", 25))
labelText.grid(row=0, column=0, sticky="w", padx=25, pady=5)

userText=Text(frame1, width=45, height=15, bd=10, relief="sunken")
userText.grid(row=1, column=0, padx=15, pady=15)

scrollBar=Scrollbar(frame1, command=userText.yview)
scrollBar.grid(row=1, column=0, pady=15, sticky="nse")

userText.config(yscrollcommand=scrollBar.set)

labelText2=Label(frame1, text="Key List:", font=("Comic Sans MS", 25))
labelText2.grid(row=2, column=0, sticky="w", padx=25, pady=5)

keyList=Text(frame1, width=45, height=15, bd=10)
keyList.grid(row=3, column=0, padx=15, pady=15)

scrollBar2=Scrollbar(frame1, command=keyList.yview)
scrollBar2.grid(row=3, column=0, pady=15, sticky="nse")

keyList.config(yscrollcommand=scrollBar2.set)


button=Button(frame1, text="Descifrar", font=("Comic Sans MS", 17), command=lambda:IF_cesarD())
button.grid(row=1, column=3, padx=15, pady=5)

button2=Button(frame1, text="Cifrar", font=("Comic Sans MS", 17), command=lambda:IF_cesarC())
button2.grid(row=3, column=3, padx=15, pady=5)

button3=Button(frame1, text="Copy Text", command=lambda:copyD())
button3.place(x=435, y=85)

button4=Button(frame1, text="Copy Text", command=lambda:copyCT())
button4.place(x=435, y=450)

button5=Button(frame1, text="Copy Key List", command=lambda:copyCL())
button5.place(x=635, y=450)

"""
frame3=Frame(root2, width=400, height=300, bg="blue")
frame3.pack(side="top", anchor="n")
"""

labelText3=Label(frame1, text="El text descifrado es:", font=("Comic Sans MS", 17))
labelText3.grid(row=0, column=1, padx=25, pady=25)

labelText4=Label(frame1, text="El texto cifrado es:", font=("Comic Sans MS", 17))
labelText4.grid(row=2, column=1, padx=25, pady=25)

newText=Label(frame1, textvariable=newTextVariable, wraplength= 500, relief="sunken", bd=5)
newText.grid(row=1, column=1, padx=5, pady=5, )

newTextInvisible=Entry(frame1, textvariable=newTextVariable)
newTextInvisible.grid(row=20, column=0)


newTextInvisible2=Entry(frame1, textvariable=newTextVariable2)
newTextInvisible2.grid(row=20, column=1)

newTextInvisible3=Entry(frame1, textvariable=newTextVariable3)
newTextInvisible3.grid(row=20, column=2)


newText2=Label(frame1, textvariable=newTextVariable2, wraplength= 500, relief="sunken", bd=5)
newText2.grid(row=3, column=1, padx=5, pady=5, )

root.mainloop()