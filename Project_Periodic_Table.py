from periodictable import elements
import tkinter as tk
import random
correct_ans=0
ans=[]
question=[]
lin_no=0
file=open("Quiz.txt","r")
for line in file:
     line=line.strip()
     lin_no=lin_no+1
     if lin_no%2==0:
          ans.append(line)
     else:
          question.append(line)
print(question ,ans)
n=len(question) #n=length of questions or answers
for i in range(n):
     print(i+1,question[i],ans[i])


# print(file.readline())

random_question=0

def update_label():
     label.config(text=question[random_question])
# Function for  button display
def my_function(element,mass,name,number):
     global random_question
     new_window = tk.Toplevel(main_window)
     tk.Label(new_window, text=f"Element: {element} \n ATOMIC MASS : {mass} \n Element Name: {name} \n ATOMIC NUMBER :{number}").pack()
     
     if number==int(ans[random_question]):
          print("Correct Answer")
     else:
          print("INCORRECT ANSWER")
     random_question=random.randint(0,n-1)
     update_label()
    
main_window = tk.Tk()
main_window.title("Periodic Table")

main_window.configure(bg="black")
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


def get_color(atomic_number):
     if  atomic_number in alkali_metals:
          return "#24bddb"
     elif atomic_number in reactive_nonmetals:
          return "#2e81ff"
     elif atomic_number in noble_gases:
          return "#f8c8d8"
     elif atomic_number in unknown_properties:
          return "#827895"
     elif atomic_number in alkaline_earth_metals:
          return "#ff4967"
     elif atomic_number in Mettaloids:
          return "#f8990e"
     elif atomic_number in Transition_metals:
          return "#6232ec"
     elif atomic_number in Post_Transition_metals:
          return "#57d19f"
     elif atomic_number in Lanthanide:
          return "#7bc6f8"
     elif atomic_number in Actinides:
          return "#ea805d"     
     return "lightblue"

buttons = []
for i in elements:
   # el=elements[i]
    button_color = get_color(i.number)
    # Use lambda to capture the element's symbol
   
    cmd_txt=tk.Text(main_window,width=6,height=2,bg=button_color,relief="solid",cursor="arrow")
    cmd_txt.tag_configure("subscript",offset=-4,font=("Times roman",8))
    cmd_txt.configure(font=("Times New Roman",11))
    cmd_txt.insert("insert",i.symbol,"",i.number,"subscript")
    cmd_txt.configure(state="disabled")
    cmd_txt.bind("<Button-1>",lambda me,name=i.name,number=i.number,elem=i.symbol,ma=i.mass:my_function(elem,ma,name,number))
    buttons.append(cmd_txt)

#     buttons.append(tk.Button(main_window, text=f"{i.symbol}",command=lambda el=i.symbol,name=i.name,number=i.number,ma=i.mass: my_function(el,ma,name,number),width=3, height=1,
#                      bg=button_color, font=("Courier",12), relief="flat"))

atoms = [1,3,11,19,37,55,87]


for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no, column=1)
atoms=[4,12,20,38,56,88]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+1, column=2 )
atoms=[21,39,57,89]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+3, column=3)
atoms=[22,40,72,104,58,90]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+3, column=4 )
atoms=[23,41,73,105,59,91]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+3, column=5)
atoms=[24,42,74,106,60,92]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+3, column=6)
atoms=[25,43,75,107,61,93]
for row_no in range(len(atoms)): 
     buttons[atoms[row_no]-1].grid(row=row_no+3, column=7 )
atoms=[26,44,76,108,62,94]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+3, column=8   )
atoms=[27,45,77,109,63,95]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+3, column=9   )
atoms=[28,46,78,110,64,96]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+3, column=10   )
atoms=[29,47,79,111,65,97]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+3, column=11   )
atoms=[30,48,80,112,66,98]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+3, column=12   )
atoms=[5,13,31,49,81,113,67,99]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+1, column=13   )
atoms=[6,14,32,50,82,114,68,100]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+1, column=14   )
atoms=[7,15,33,51,83,115,69,101]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+1, column=15   )
atoms=[8,16,34,52,84,116,70,102]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+1, column=16  )
atoms=[9,17,35,53,85,117,71,103]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no+1, column=17  )
atoms=[2,10,18,36,54,86,118]
for row_no in range(len(atoms)):
     buttons[atoms[row_no]-1].grid(row=row_no, column=18   )  


label=tk.Label(main_window,text=question[random_question],bg="black",fg="white",font=("Arial", 12) )
label.grid(row=200,column=1,columnspan=18,padx=10,pady=10)

main_window.mainloop()
