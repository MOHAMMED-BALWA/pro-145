from tkinter import * 
root = Tk()

root.title("DRIVING LICENSE")
root.geometry("450x270")



i = Label(root , bg="red" ,  text="DRIVING LICENSE" , font="35px"  , fg="white"  , width="100",  height="2"   )
i.pack()



n=Label(root)
def add():
    z="ID : 2396445673"
    m["text"]=z
    
    z="NAME : MOHAMMED"
    n["text"]=z
    
    z="DATE OF BIRTH : 22 DECEMBER 2008"
    p["text"]=z
    
    
    z="PIN NO : 400104"
    x["text"]=z
    
    z="ADDRESS : MAHARASHTRA,INDIA"
    v["text"]=z
    
    z="AUTHORISATION TO DRIVE THE FOLLING VEHICLES : TWO FOUR"
    l["text"]=z
    
    
    
m = Label(root   ,  text="ID :"  ,font=('Times', '12', 'bold')  , height="2"  )
m.pack( padx="10",anchor="w")




n = Label(root  ,  text="NAME :" ,font=('Times', '10', 'bold') )
n.pack(padx="10",anchor="w")

p = Label(root  ,  text="DATE OF BIRTH :" , font=('Times', '10', 'bold')  )
p.pack(padx="10",anchor="w")

x = Label(root  ,  text="PIN NO :" ,font=('Times', '10', 'bold')  )
x.pack(padx="10",anchor="w")

v = Label(root  ,  text="ADDRESS :" , font=('Times', '10', 'bold')  )
v.pack(padx="10",anchor="w")

l = Label(root  ,  text="AUTHORISATION TO DRIVE THE FOLLOWING VEHICLES :" , font=('Times', '10', 'bold')   )
l.pack(padx="10",anchor="w")






btn = Button(root , text ="SHOW LICENSE" , command=add , cursor="dot" ,  background="orange" , activebackground="orange" )
btn.pack(pady="20")



root.mainloop()

