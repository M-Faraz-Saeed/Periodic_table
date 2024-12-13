from periodictable import elements
import tkinter as tk

# Function to handle button click
def my_function(element,mass,name,number):
    new_window = tk.Toplevel(main_window)
    tk.Label(new_window, text=f"Element: {element} \n ATOMIC MASS : {mass} \n Element Name: {name} \n ATOMIC NUMBER :{number}").pack()

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
   
    cmd_txt=tk.Text(main_window)
    cmd_txt.tag_configure("subscript",offset=-4)
    cmd_txt.insert("insert",i.symbol,"",i.number,"subscript")
    cmd_txt.configure(state="disabled")

    buttons.append(tk.Button(main_window, text=f"{i.symbol}",command=lambda el=i.symbol,name=i.name,number=i.number,ma=i.mass: my_function(el,ma,name,number),width=3, height=1,
                     bg=button_color, font=("Courier",12), relief="flat"))

# Arrange buttons in a grid (example layout for All elements)\
#i=1
# for i in [1,3,11,19,37,55,87]:
#      buttons[i-1].grid(row=i,column=1  )
# atoms = [1,3,11,19,37,55,87]
# for row_no in range(len(atoms)):
#      buttons[atoms[row_no-1]].grid(row=row_no, column=2, padx=5,pady=5)

##
atoms = [1,3,11,19,37,55,87]
# buttons=[tk.Button(main_window,text=elements,width=10,height=2,bg="lightblue",fg="black",font=("Arial",12,"bold"),relief="raised", command=lambda el=i.symbol,name=i.name,number=i.number,ma=i.mass: my_function(el,ma,name,number))
#          for i in range(118)]

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
     buttons[atoms[row_no]-1].grid(row=row_no+1, column=18   )
##

# for i in range(6):
#     buttons[i].grid(row=i, column=1, padx=10, pady=10)
# for i in range(6, 12):
#     buttons[i].grid(row=i-6, column=2, padx=10, pady=10)
# for i in range(12,18):
#      buttons[i].grid(row=i-12, column=3, padx=10, pady=10)
# for i in range(18,24):
#      buttons[i].grid(row=i-18, column=4, padx=10, pady=10)
# for i in range(24,30):
#      buttons[i].grid(row=i-24, column=5, padx=10, pady=10)
# for i in range(30,36):
#      buttons[i].grid(row=i-30, column=6, padx=10, pady=10)
# for i in range(36,42):
#      buttons[i].grid(row=i-36, column=7, padx=10, pady=10)
# for i in range(42,48):
#      buttons[i].grid(row=i-42, column=8, padx=10, pady=10)
# for i in range(48,54):
#      buttons[i].grid(row=i-48, column=9, padx=10, pady=10)
# for i in range(54,60):
#      buttons[i].grid(row=i-54, column=10, padx=10, pady=10)
# for i in range(60,66):
#      buttons[i].grid(row=i-60, column=11, padx=10, pady=10)
# for i in range(66,72):
#      buttons[i].grid(row=i-66, column=12, padx=10, pady=10)
# for i in range(72,80):
#      buttons[i].grid(row=i-72, column=13, padx=10, pady=10)
# for i in range(78,84):
#      buttons[i].grid(row=i-78, column=14, padx=10, pady=10)
# for i in range(84,90):
#      buttons[i].grid(row=i-84, column=15, padx=10, pady=10)
# for i in range(90,96):
#      buttons[i].grid(row=i-90, column=16, padx=10, pady=10)
# for i in range(96,102):
#      buttons[i].grid(row=i-96, column=17, padx=10, pady=10)
# for i in range(102,108):
#      buttons[i].grid(row=i-102, column=18, padx=10, pady=10)
# for i in range(108,114):
#      buttons[i].grid(row=i-108, column=20, padx=10, pady=10)
# for i in range(114,120-2):
#     buttons[i].grid(row=i-114, column=21, padx=10, pady=10)
     
main_window.mainloop()
