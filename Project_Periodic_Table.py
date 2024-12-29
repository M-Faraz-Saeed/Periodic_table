import tkinter as tk
from PIL import Image, ImageTk
import periodictable
from periodictable import elements
import random
import time

def element_details(symbol,mass,name,number):
    # global random_list_of_questions,new_score
    new_window = tk.Toplevel(main_window)
    tk.Label(new_window, text=f"Element: {symbol} \n ATOMIC MASS : {mass} \n Element Name: {name} \n ATOMIC NUMBER :{number}", font=("Arial", 12, "bold"), fg="black", bg="white").pack()
     
list_of_ans=[]
list_of_questions=[]
lin_no=0
file=open("Quiz.txt","r",encoding="utf-8")#readind file for list_of_questions with thier correspondence list_of_answers
for line in file:
     line=line.strip()
     lin_no=lin_no+1
     if lin_no%2==0:#even lin no list_of_answer
          list_of_ans.append(line)
     else:
          list_of_questions.append(line)#odd lin no list_of_questionss

n=len(list_of_questions) #n=length of list_of_questionss or list_of_answers

# Create the main window
main_window = tk.Tk()
main_window.title("PERIODIC-TABLE")
main_window.geometry("800x600") 

# Load the background image
image_path = "image.jpg"  
bg_image = Image.open(image_path)
bg_image = bg_image.resize((1400,1000), Image.LANCZOS) 
bg_photo = ImageTk.PhotoImage(bg_image)

# Label widget for the background image
bg_label = tk.Label(main_window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

quiz_window=tk.Toplevel(main_window)
quiz_window.title("QUIZ WINDOW")
quiz_window.geometry("250x250")
#quiz_window.withdraw()

opt_A=0
opt_B=0
opt_C=0
opt_D=0
ans=0
quest_label=tk.Label(quiz_window,text="Q: ",font=("Arial", 22), fg="blue").pack(pady=20)
a=tk.Button( \
                quiz_window, \
                text=f"A:", \
                font=("Arial",12), \
                fg="black", \
                command=lambda:option_click(opt_A,quiz_window,ans) \
            ).pack(pady=20)
b=tk.Button( \
                quiz_window, \
                text=f"B:", \
                font=("Arial",12), \
                fg="black", \
                command=lambda:option_click(opt_B,quiz_window,ans) \
                ).pack(pady=20)
c=tk.Button( \
                quiz_window, \
                text=f"C:", \
                font=("Arial",12),fg="black", \
                command=lambda:option_click(opt_C,quiz_window,ans) \
            ).pack(pady=20)
d=tk.Button( \
                quiz_window, \
                text=f"D:", \
                font=("Arial",12),fg="black", \
                command=lambda:option_click(opt_D,quiz_window,ans) \
            ).pack(pady=20)
    

def display_quiz():
    quiz_window.deiconify()
    random_index=random.randint(0,n-1)
    quest=list_of_questions[random_index]
    ans=list_of_ans[random_index]
    opt1=random.randint(1,118)
    opt2=random.randint(1,118)
    opt3=random.randint(1,118)
    list_of_opt=[int(ans),opt1,opt2,opt3]
    random.shuffle(list_of_opt) # for MCQS OPTIONS
   #quest_label= tk.Label(quiz_window,text="Q: "+quest,font=("Arial", 22), fg="blue").pack(pady=20)
    quest_label.config(text="Q:"+quest)
    a.config(text=f"A:{elements[list_of_opt[0]].name}")
    b.config(text=f"B:{elements[list_of_opt[1]].name}")
    c.config(text=f"C:{elements[list_of_opt[2]].name}")
    d.config(text=f"D:{elements[list_of_opt[3]].name}")
    quiz_window.update()

def option_click(chk,quiz_window,ans):
        if chk == int(ans):
            tk.Label(quiz_window,text="Correct",font=("Arial", 10), fg="blue").place(x=600,y=200)
        else:
            tk.Label(quiz_window, text="Incorrect",font=("Arial", 10), fg="black").place(x=600,y=400)
        time.sleep(2)
        display_quiz()


# Add a button in the main window to open the quiz
quiz_button = tk.Button(main_window, text="Start Quiz",height=3,width=10, command=lambda:display_quiz())
quiz_button.place(x=650,y=50)

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
file=open("elements.txt","r")#reading elements positions from file to adjust positions of buttons
for line in file:
    list=line.split()
    atm_num=int(list[0])
    i =elements[atm_num]
    x=int(list[4])
    y=int(list[5])
    if len(list)==7:
        if list[6]=="-":
            en=0
        else:
            en=float(list[6])
    else:
        en=0
    button = tk.Button(main_window, text=list[1],bg=rgb_to_hex(int(en*50),0,0),fg="white",width=5,height=2,command=lambda name=i.name,number=i.number,elem=i.symbol,ma=i.mass:element_details(elem,ma,name,number))
    button.place(x=int(x*0.9)+250,y=int(y*0.6)+150)
main_window.mainloop()
