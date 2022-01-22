from tkinter import *

root = Tk()
root.title("Do I have a fever?")
root.geometry("600x600")

ihatemylife = Label(root)

q1rb = StringVar(value="0")
q1=Label(root,text="Do you experience shortness of breath during routine activities?")
q1.pack()
q1r=Radiobutton(root, text="yes",variable=q1rb,value="yes")
q1r.pack()
q1r2=Radiobutton(root, text="no",variable=q1rb,value="no")
q1r2.pack()

q2rb = StringVar(value="0")
q2=Label(root,text="Do you experience shortness of breath while at rest/lying down?")
q2.pack()
q2r=Radiobutton(root, text="yes",variable=q2rb,value="yes")
q2r.pack()
q2r2=Radiobutton(root, text="no",variable=q2rb,value="no")
q2r2.pack()

q3rb = StringVar(value="0")
q3=Label(root,text="Do you feel short of breath while lying flat and feel the need to stack multiple pillows to sleep well?")
q3.pack()
q3r=Radiobutton(root, text="yes",variable=q3rb,value="yes")
q3r.pack()
q3r2=Radiobutton(root, text="no",variable=q3rb,value="no")
q3r2.pack()

q4rb = StringVar(value="0")
q4=Label(root,text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?")
q4.pack()
q4r=Radiobutton(root, text="yes",variable=q4rb,value="yes")
q4r.pack()
q4r2=Radiobutton(root, text="no",variable=q4rb,value="no")
q4r2.pack()

q5rb = StringVar(value="0")
q5=Label(root,text="Do you have swelling in the feet/ ankles/legs (shoes feel tighter) or abdomen?")
q5.pack()
q5r=Radiobutton(root, text="yes",variable=q5rb,value="yes")
q5r.pack()
q5r2=Radiobutton(root, text="no",variable=q5rb,value="no")
q5r2.pack()

ihatemylife.pack()

def fever():
    score=0
    if q1rb.get()=="yes":
        score += 1
        print(score)
    else:
        score = score
        print(score)
    if q2rb.get()=="yes":
        score += 1
        print(score)
    else:
        score = score
        print(score)
    if q3rb.get()=="yes":
        score += 1
        print(score)
    else:
        score = score
        print(score)
    if q4rb.get()=="yes":
        score += 1
        print(score)
    else:
        score = score
        print(score)
    if q5rb.get()=="yes":
        score += 1
        print(score)
    else:
        score = score
        print(score)
    
    if score <= 1 and score<3:
        ihatemylife["text"] = "Result: You perhaps want to visit a doctor, just to be safe."
    elif score <= 3 and score <5:
        ihatemylife["text"] = "Result: You should visit a doctor, that is pretty concerning."
    elif score == 5:
        ihatemylife["text"] = "Result: Go visit a doctor, now."
    elif score==0:
        ihatemylife["text"] = "You don't need to visit a doctor."
        
button = Button(root, text="Get Results", command=fever)
button.pack()
root.mainloop()