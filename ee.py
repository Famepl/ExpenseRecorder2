from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime 


GUI = Tk()
GUI.title('โปรแกมบันทึกค่าใช้จ่าย v.1.0 by Fame')
GUI.geometry('500x700+500+50')


# F1 = Frame(GUI)
# F1.place(x=100,y=50)

############MENU############
menubar = Menu(GUI)
GUI.config(menu=menubar)


filemunu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemunu)
filemunu.add_cascade(label='Import CSV')
filemunu.add_cascade(label='Export to Googlesheet')

def About():
    print('About Menu')
    messagebox.showinfo('About','สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกข้อมูล\nสนใจบริจาคเราไหม? ขอ 1 ก็พอแล้ว\nฺBTC Adderss: abc')



helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_cascade(label='About',command=About)

def Donate():
    messagebox.showinfo('Donate','BTC Address: 21514541652151498546516541')
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_command(label='Donate',command=Donate)
############################


Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

icon_t1 = PhotoImage(file='D:\web\Include\expense.png')
icon_t2 = PhotoImage(file='D:\web\Include\expenselist.png')

Tab.add(T1, text=f'{"ค่าใช้จ่าย":^{30}}',image=icon_t1,compound='top')
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='top')

F1 = Frame(T1)
# F1.place(x=100,y=50)
F1.pack()

days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed:':'พุธ',
        'Thu':'พฦหัสบดี',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์',}

def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    quantity = v_quantity.get()
    
    if expense == '':
        print('No Data')
        messagebox.showwarning('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
        return
    elif price == '':
        messagebox.showwarning('Error','กรุณากรอกข้อมูลราคา')
        return
    elif quantity == '':
        quantity = 1
    

    
    total = float(price) * float(quantity)
    try:
        total = float(price) * float(quantity)

        print('รายการ: {} ราคา: {}'.format(expense,price))
        print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
        text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
        text = text + 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total)
        v_result.set(text)

        v_expense.set('')
        v_price.set('')
        v_quantity.set('')
        
        today = datetime.now().strftime('%a')
        print(today)
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dt = days[today] + '-' + dt
        with open('D:\web\savedata.csv','a',encoding='utf-8',newline='') as f:
            
            
            
            fw = csv.writer(f)
            data = [expense,price,quantity,total]
            fw.writerow(data)


        E1.focus()
        update_tadle()
    except Exception as e:
        print('ERROR',e)
        messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        # messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        # messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')


GUI.bind('<Return>',Save)
    
FONT1 = (None,20)



main_icon = PhotoImage(file='D:\web\Include\icon_money.png')

Mainicon = Label(F1,image=main_icon)
Mainicon.pack()




L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()

E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()


L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()


L = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack()
v_quantity = StringVar()
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()


icon_b1 = PhotoImage(file='D:\web\Include\save.png')

B2 = ttk.Button(F1,text=f'{"Save": >{10}}',image=icon_b1,compound='left',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20)







v_result = StringVar()
v_result.set('----------ผลลัพธ์----------')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='green')

result.pack(pady=20)


#################TAB2###############

def read_csv():
    with open('D:\web\savedata.csv',newline='',encoding='utf-8') as b:
        fr = csv.reader(b)
        data = list(fr)
        rs = data
    return data




L = ttk.Label(T2,text='ตารางแสดงผลลัพท์ทั้งหมด',font=FONT1).pack(pady=20)

header = ['รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=20)
resulttable.pack()

for i in range(len(header)):
    resulttable.heading(header[i],text=header[i])

for h in header:
    resulttable.heading(h,text=h)

headerwidth = [150,170,60,60,60]
for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)

# resulttable.insert('',0,values=['จันทร์','น้ำดื่ม',30,5,150])
# resulttable.insert('','end',values=['จันทร์','น้ำดื่ม',30,5,150])

def update_tadle():
    resulttable.delete(*resulttable.get_children())
    # for c in resulttable.get_children():
    #     resulttable.delete(c)
    data = read_csv()
    for d in data:
        resulttable.insert('',0,values=d)

update_tadle()
print('FET CHILD:',resulttable.get_children())
GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
