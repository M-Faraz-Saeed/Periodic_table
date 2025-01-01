import tkinter as tk
from PIL import Image, ImageTk
from periodictable import elements
import random
import time

def element_details(symbol,mass,name,number):
    new_window = tk.Toplevel(main_window)
    tk.Label(new_window, text=f"Element: {symbol} \n ATOMIC MASS : {mass} \n Element Name: {name} \n ATOMIC NUMBER :{number}", font=("Arial", 12, "bold"), fg="black", bg="lightblue").pack()
     
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
          list_of_questions.append(line)#odd lin no list_of_questions
n=len(list_of_questions) #n=length of list_of_questionss or list_of_answers

# Creating main window
main_window = tk.Tk()
main_window.title("PERIODIC-TABLE")
main_window.geometry("800x600")
main_window.state("zoomed")

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
quiz_window.state("zoomed")
quiz_window.withdraw()

bg_quiz = tk.Label(quiz_window, image=bg_photo)
bg_quiz.place(x=0, y=0, relwidth=1, relheight=1)


opt_A=0
opt_B=0
opt_C=0
opt_D=0
ans=0
quest_label=tk.Label(quiz_window,text="Q: ",font=("Arial", 22), fg="blue",bg="lightblue")
quest_label.place(x=300,y=150)
a=tk.Button( \
                quiz_window, \
                text=f"A:", \
                font=("Arial",14), \
                fg="black", \
                bg="pink", \
                width=17,\
                command=lambda:option_click(opt_A) \
            )
a.place(x=300,y=300*0.8)
b=tk.Button( \
                quiz_window, \
                text=f"B:", \
                font=("Arial",14), \
                fg="black", \
                bg="pink", \
                width=17,\
                command=lambda:option_click(opt_B) \
                )
b.place(x=300,y=350*0.8)
c=tk.Button( \
                quiz_window, \
                text=f"C:", \
                font=("Arial",14),fg="black", \
                bg="pink", \
                width=17, \
                command=lambda:option_click(opt_C) \
            )
c.place(x=300,y=400*0.8)
d=tk.Button( \
                quiz_window, \
                text=f"D:", \
                font=("Arial",14),fg="black", \
                bg="pink", \
                width=17,\
                command=lambda:option_click(opt_D) \
            )
d.place(x=300,y=450*0.8)
score=0
question_num=0
def display_quiz():
    global opt_A,opt_B,opt_C,opt_D,ans,question_num
    question_num+=1
    if question_num<=10:
        quiz_window.deiconify()
        random_index=random.randint(0,n-1)
        quest=list_of_questions[random_index]
        ans=list_of_ans[random_index]
        opt1=random.randint(1,118)
        opt2=random.randint(1,118)
        opt3=random.randint(1,118)
        list_of_opt=[int(ans),opt1,opt2,opt3]
        random.shuffle(list_of_opt) # for MCQS OPTIONS
        opt_A=list_of_opt[0]
        opt_B=list_of_opt[1]
        opt_C=list_of_opt[2]
        opt_D=list_of_opt[3]
        quest_label.config(text="Q:"+quest)
        a.config(text=f"A:{elements[list_of_opt[0]].name.capitalize()} (Z={elements[list_of_opt[0]].number})")
        b.config(text=f"B:{elements[list_of_opt[1]].name.capitalize()}(Z={elements[list_of_opt[1]].number})")
        c.config(text=f"C:{elements[list_of_opt[2]].name.capitalize()}(Z={elements[list_of_opt[2]].number})")
        d.config(text=f"D:{elements[list_of_opt[3]].name.capitalize()}(Z={elements[list_of_opt[3]].number})")
        quiz_window.update()
    else:
        question_num=0
        quiz_window.withdraw()

correct_label=tk.Label(quiz_window,text="",font=("Arial", 18))
correct_label.place_forget()

def option_click(chk):
        global score,ans,quiz_window
        if chk == int(ans):
            correct_label.config(text="CORRECT",fg="green")
            score+=1
            score_label=tk.Label(quiz_window,text=f"SCORE :{score}",font=("bold",15),bg="lightgreen")
            score_label.place(x=800,y=200)
        else:
            correct_label.config(text="INCORRECT",fg="red")
        correct_label.place(x=525,y=300)
        quiz_window.update()
        time.sleep(0.5)#to display for 0.5 seconds
        correct_label.place_forget()
        quiz_window.update()
        display_quiz()
# Add a button in the main window to open the quiz
quiz_button = tk.Button(main_window, text="Quiz",font=("bold",15),height=2,width=8,bg="lightblue", command=lambda:display_quiz())
quiz_button.place(x=1100,y=50)
#heading of project
heading=tk.Label(main_window,text="PERIODIC-TABLE",font=("bold",30),bg="lightgreen")
heading.place(x=490,y=60)

score_label=tk.Label(quiz_window,text=f"SCORE :0",font=("bold",15),bg="lightgreen")
score_label.place(x=800,y=200)

alkali_metals=tk.Label(main_window,text="ALKALI-METALS",font=("bold",14),bg="#FF6347")
alkali_metals.place(x=15,y=180)

reactive_nonmetals=tk.Label(main_window,text="REACTIVE-NON METALS",font=("bold",14),bg="#98FB98")
reactive_nonmetals.place(x=15,y=215)

noble_gases=tk.Label(main_window,text="NOBLE-GASES",font=("bold",14),bg="#D8BFD8")
noble_gases.place(x=15,y=245)

unknown_properties=tk.Label(main_window,text="UNKNOWN-PROPERTIES",font=("bold",14),bg="#A9A9A9")
unknown_properties.place(x=15,y=275)

alkaline_earth_metals=tk.Label(main_window,text="ALKALINE-EARTH-METALS",font=("bold",14),bg="#FF7F50")
alkaline_earth_metals.place(x=15,y=305)

Mettaloids=tk.Label(main_window,text="METTALOIDS",font=("bold",14),bg="#FFD700")
Mettaloids.place(x=15,y=335)

Transition_metals=tk.Label(main_window,text="TRANSITIONAL-METALS",font=("bold",14),bg="#8A2BE2")
Transition_metals.place(x=15,y=365)

Post_Transition_metals=tk.Label(main_window,text="POST-TRANSITION-METALS",font=("bold",14),bg="#66CDAA")
Post_Transition_metals.place(x=15,y=395)

Lanthanide=tk.Label(main_window,text="LANTHANIDE",font=("bold",14),bg="#ADD8E6")
Lanthanide.place(x=15,y=425)

Actinides=tk.Label(main_window,text="ACTINIDES",font=("bold",14),bg="#FF8C00")
Actinides.place(x=15,y=455)

alkali_metals = [3, 11, 19, 37, 55, 87]
reactive_nonmetals = [1,6,7,8,9,15,16,17,34,35,53]
noble_gases = [2, 10, 18, 36, 54, 86]
unknown_properties=[109,110,111,112,113,114,115,116,117,118]
alkaline_earth_metals=[4,12,20,38,56,88]
Mettaloids=[5,14,32,33,51,52]
Transition_metals=[21,22,23,24,25,26,27,28,29,30,39,40,41,42,43,44,45,46,47,48,72,73,74,75,76,77,78,79,80,104,105,106,107,108]
Post_Transition_metals=[13,31,49,50,81,82,83,84,85]
Lanthanide=[57,58,59,60,61,62,63,64,65,66,67,68,69,70,71]
Actinides=[89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]

def get_color(atm_num):
    if atm_num in alkali_metals:
        return "#FF6347"  # Alkali Metals (Tomato Red)
    elif atm_num in reactive_nonmetals:
        return "#98FB98"  # Reactive Nonmetals (Pale Green)
    elif atm_num in noble_gases:
        return "#D8BFD8"  # Noble Gases (Thistle)
    elif atm_num in unknown_properties:
        return "#A9A9A9"  # Unknown Properties (Dark Gray)
    elif atm_num in alkaline_earth_metals:
        return "#FF7F50"  # Alkaline Earth Metals (Coral)
    elif atm_num in Mettaloids:
        return "#FFD700"  # Metalloids (Gold)
    elif atm_num in Transition_metals:
        return "#8A2BE2"  # Transition Metals (Blue Violet)
    elif atm_num in Post_Transition_metals:
        return "#66CDAA"  # Post-Transition Metals (Medium Aquamarine)
    elif atm_num in Lanthanide:
        return "#ADD8E6"  # Lanthanides (Light Blue)
    elif atm_num in Actinides:
        return "#FF8C00"  # Actinides (Dark Orange)
    return "lightblue"  # Default Color

file=open("elements.txt","r")#reading elements positions from file to adjust positions of buttons
for line in file:
    list=line.split()
    atm_num=int(list[0])
    i =elements[atm_num]
    x=int(list[4])
    y=int(list[5])
    button = tk.Button( \
            main_window, \
            text=list[1], \
            bg=get_color(atm_num), \
            fg="black",width=5,height=2, \
            command=lambda name=i.name,number=i.number,elem=i.symbol,ma=i.mass:element_details(elem,ma,name,number))
    button.place(x=int(x*0.9)+255,y=int(y*0.7)+155)
main_window.mainloop()
