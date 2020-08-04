from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import cx_Oracle 
import bs4
import requests
import socket
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

root = Tk()
root.geometry('550x550+400-100')
root.title("Student Management System")
root.iconbitmap('D:\demo\python\project\stu.ico')
root['bg'] = '#93cdfa'

#function of each button event

def f1():   #add window
	root.withdraw()
	adst.deiconify()
	adst['bg'] = '#93cdfa'

def f2():   #add function
	try:
		con = None
		con = cx_Oracle.connect('username/password')
		rno = int(er.get())
		sname = en.get()
		smarks = int(em.get())
		if rno<1:
			messagebox.showerror("warning","be +ve roll no should start from 1")
			er.delete(0,END)
			en.delete(0,END)
			em.delete(0,END)
			er.focus()
		elif len(sname)==0:
			messagebox.showerror("warning","name cannot be empty!")
			er.delete(0,END)
			em.delete(0,END)
			er.focus()
		elif sname.isdigit():
			messagebox.showerror("warning","name cannot be a number")
			er.delete(0,END)
			en.delete(0,END)
			em.delete(0,END)
			er.focus()
		elif len(sname)<2:
			messagebox.showerror("warning","length of name should be minimum 2 characters")
			er.delete(0,END)
			en.delete(0,END)
			em.delete(0,END)
			er.focus()
		elif smarks>100 or smarks<0:
			messagebox.showerror("warning","marks should be between 0-100")
			er.delete(0,END)
			en.delete(0,END)
			em.delete(0,END)
			er.focus()
		else:
			if sname.isalpha():
				cursor = con.cursor()
				cursor = con.cursor()
				sql ="insert into student values('%d','%s','%d')"
				args = (rno,sname,smarks)
				cursor.execute(sql % args)
				con.commit()
				#print("successfully added")
				messagebox.showinfo("success","record inserted ")
				er.delete(0,END)
				en.delete(0,END)
				em.delete(0,END)
				er.focus()
			else:
				messagebox.showerror("warning","name cannot be special character")
				er.delete(0,END)
				en.delete(0,END)
				em.delete(0,END)
				er.focus()
	
	except ValueError:
		messagebox.showerror("warning","ValueError")
		er.delete(0,END)
		en.delete(0,END)
		em.delete(0,END)
		er.focus()
	except cx_Oracle.IntegrityError:
		messagebox.showerror("issue ", "Roll no. " + str(rno) + "  already exists")
		er.delete(0,END)
		en.delete(0,END)
		em.delete(0,END)
		er.focus()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue ",""+e)
	finally:
		if con is not None:
			con.close()
			#print("disconnectd")

def f3():  #add window close
	adst.withdraw()
	root.deiconify()


def f4():
	root.withdraw()
	vw.deiconify()
	vw['bg'] = '#93cdfa'
	stdata.delete(1.0,END)
	con = None
	try:
		con = cx_Oracle.connect('username/password')
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + "rno=" + str(d[0]) + " sname=" + str(d[1]) + " smarks=" + str(d[2]) + "\n"
		stdata.insert(INSERT,msg)
	except cx_Oracle.DatabaseError as e:
		#print("issue",e)
		messagebox.showerror("issue ",""+e)
	finally:
		if con is not None:
			con.close()

def f5():
	vw.withdraw()             #view(back button)
	root.deiconify()

def f6():  #mainFrame upadte button 
	
	root.withdraw()     
	updst.deiconify()
	updst['bg'] = '#93cdfa'

def f7():   #update code 
	con = None
	try:
		con = cx_Oracle.connect('username/password')	
		rno = int(uer.get())
		sname = uen.get()
		smarks =int(uem.get())
		if rno<1:
			messagebox.showerror("warning","be +ve roll no should start from 1")
			uer.delete(0,END)
			uen.delete(0,END)
			uem.delete(0,END)
			uer.focus()
		elif len(sname)==0:
			messagebox.showerror("warning","name cannot be empty!")
			uer.delete(0,END)
			uen.delete(0,END)
			uem.delete(0,END)
			uer.focus()
		elif sname.isdigit():
			messagebox.showerror("warning","name cannot be a number")
			uer.delete(0,END)
			uen.delete(0,END)
			uem.delete(0,END)
			uer.focus()
		elif len(sname)<2:
			messagebox.showerror("warning","length of name should be minimum 2 characters")
			uen.delete(0,END)
			uer.delete(0,END)
			uem.delete(0,END)
			uer.focus()
		elif smarks>100 or smarks<0:
			messagebox.showerror("warning","marks should be between 0-100")
			uen.delete(0,END)
			uer.delete(0,END)
			uem.delete(0,END)
			uer.focus()
		else:
			if sname.isalpha():
				cursor = con.cursor()
				sql = "update student set sname = '%s',smarks = '%d' where rno = '%d'"
				args = (sname,smarks,rno)
				cursor.execute(sql % args)
				con.commit()
				#print(cursor.rowcount, " record updated ")
				messagebox.showinfo("success",str(cursor.rowcount) + " record updated ")
				uer.delete(0,END)
				uen.delete(0,END)
				uem.delete(0,END)
				uer.focus()
			else:
				messagebox.showerror("warning","Proper name required")
				uer.delete(0,END)
				uen.delete(0,END)
				uem.delete(0,END)
	except ValueError:
		messagebox.showerror("warning","ValueError")
		uer.delete(0,END)
		uen.delete(0,END)
		uem.delete(0,END)
		uer.focus()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		#print("issue ",e)
		messagebox.showerror("issue ",""+e)
	finally:
		if con is not None:
			con.close()



def f8():                             #update (back button)
	updst.withdraw()                  
	root.deiconify()
	
def f9():                             #delete (main frame button)
	root.withdraw()
	dst.deiconify()
	dst['bg'] = '#93cdfa'

def f10():				#delete (delete window delete button)
	try:
		con = cx_Oracle.connect('username/password') #enter your username and password 
		#print("connected")
		rno = int(der.get())
		if rno>=1:
			cursor = con.cursor()
			sql = "delete from student where rno = '%d'"
			args =(rno)
			cursor.execute(sql % args)
			con.commit()
			#print("record deleted ")
			#print(cursor.rowcount, " record deleted ")
			messagebox.showinfo("success",str(cursor.rowcount) + " record deleted ")
			der.delete(0,END)
			der.focus()
	except ValueError:
		messagebox.showerror("warning","ValueError")
		der.delete(0,END)
		der.focus()
		 
	except cx_Oracle.DatabseError as e:
		con.rollback()
		messagebox.showerror("issue ",""+e)
		
	finally:
		if con is not None:
			con.close()
			#print("disconnected")

def f11():
	dst.withdraw()                  
	root.deiconify()

def f12(): #graph

	con = cx_Oracle.connect('username/password')
	cursor = con.cursor()
	sql = "select * from student"
	cursor.execute(sql)


	name = []
	smarks = []
	for result in cursor:
		name.append(result[1])
		smarks.append(result[2])

	y_pos = np.arange(len(name))
	plt.bar(y_pos,smarks,align="center",label='Marks',width=0.25)
	plt.xticks(y_pos,name)
	plt.title("Student Analysis")


	plt.xlabel("Student Name")
	plt.ylabel("Student Marks")

	plt.legend()
	plt.grid()
	con.close()
	plt.show()

	



#main frame 
btnA = Button(root,text='Add',font=('Comic Sans MS',15,'italic'),width=10,command = f1,bg = "#e1f4fa")
btnV = Button(root,text='View',font=('Comic Sans MS',15,'italic'),width=10,command = f4,bg = "#e1f4fa")
btnU = Button(root,text='Update',font=('Comic Sans MS',15,'italic'),width=10,command = f6,bg = "#e1f4fa")
btnD = Button(root,text='Delete',font=('Comic Sans MS',15,'italic'),width=10,command = f9,bg = "#e1f4fa")
btnG = Button(root,text='Graph',font=('Comic Sans MS',15,'italic'),width=10,command = f12,bg = "#e1f4fa")

lcity = Label(root,text="City",font=('Comic Sans MS',15,'italic'),width=10)
ecity = Entry(root,font=('Comic Sans MS',15,'italic'),width = 8,bd=5)

ltemp = Label(root,text="Temperature",font=('Comic Sans MS',15,'italic'),width=10)
etemp = Entry(root,font=('Comic Sans MS',15,'italic'),width=8,bd=5)

lqotd = Label(root,text="QOTD",font=('Comic Sans MS',15,'italic'),width=10)
eqotd = Entry(root,font=('Comic Sans MS',15,'italic'),width = 31,bd=5)

btnA.place(x=180,y=30)
btnV.place(x=180,y=90)
btnU.place(x=180,y=150)
btnD.place(x=180,y=210)
btnG.place(x=180,y=270)
lcity.place(x=0,y=350)
ltemp.place(x=240,y=350)
lqotd.place(x=0,y=420)
ecity.place(x=110,y=350)
etemp.place(x=380,y=350)
eqotd.place(x=110,y=420)

#city extraction

try:
	socket.create_connection(("www.google.com",80))
	res = requests.get("https://ipinfo.io")
	print(res)
	data = res.json()
	#print(data)
	city = data['city']
	ecity.insert(0,city)
except OSError :
	print("check network")



#temperature extraction

try:
	socket.create_connection(("www.google.com",80))
	res=requests.get("https://ipinfo.io")
	data=res.json()
	city=data['city']
       	
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address=a1+a2+a3
	res=requests.get(api_address)
	data=res.json()
	#print(data)
	temp=data['main']['temp']
	#print("City: ", city, "Temperature :",temp)
	etemp.insert(0,temp)

except OSError :
	print("check network") 

#quote extraction in entry

res = requests.get("https://www.brainyquote.com/quote_of_the_day.html")
soup = bs4.BeautifulSoup(res.text,'lxml')
quote = soup.find('img',{"class":"p-qotd"})
msg = quote['alt']
eqotd.insert(0,msg)


#addstudent
adst = Toplevel(root)
adst.title("Add Students ")
adst.geometry('550x550+400-100')



lr = Label(adst,text="Enter rno",font=('comic sans ms',16,'bold'),bg="#e1f4fa")
er = Entry(adst,bd=5,font=('comic sans ms',16,'bold'),bg = "#e1f4fa")

ln = Label(adst,text="Enter name",font=('comic sans ms',16,'bold'),bg="#e1f4fa")
en = Entry(adst,bd=5,font=('comic sans ms',16,'bold'),bg = "#e1f4fa")

lm = Label(adst,text="Enter Marks",font=('comic sans ms',16,'bold'),bg="#e1f4fa")
em = Entry(adst,bd=5,font=('comic sans ms',16,'bold'),bg = "#e1f4fa")

bas = Button(adst, text = "Save",font=('comic sans ms',16,'bold'),command = f2,bg = "#e1f4fa")
bab = Button(adst, text = "Back",font=('comic sans ms',16,'bold'),command = f3,bg = "#e1f4fa")

lr.pack(pady=10)
er.pack(pady=10)
ln.pack(pady=10)
en.pack(pady=10)
lm.pack(pady=10)
em.pack(pady=10)
bas.pack(pady=10)
bab.pack(pady=10)

adst.withdraw()

#viewStudent

vw = Toplevel(root)
vw.title("View Students ")
vw.geometry('550x550+400-100')

stdata = scrolledtext.ScrolledText(vw,width=30,height=20)
btnViewBack = Button(vw,text="Back",font=('comic sans ms',16,'bold'),command = f5,bg = "#e1f4fa")

stdata.pack(pady=10)
btnViewBack.pack(pady=10)

vw.withdraw()


#updateStudnt

updst = Toplevel(root)
updst.title("Update Students ")
updst.geometry('550x550+400-100')

ulr = Label(updst,text="Enter rno",font=('comic sans ms',16,'bold'),bg = "#e1f4fa")
uer = Entry(updst,bd=5,font=('comic sans ms',16,'bold'),bg = "#e1f4fa")

uln = Label(updst,text="Enter name",font=('comic sans ms',16,'bold'),bg = "#e1f4fa")
uen = Entry(updst,bd=5,font=('comic sans ms',16,'bold'),bg = "#e1f4fa")

ulm = Label(updst,text="Enter Marks",font=('comic sans ms',16,'bold'),bg ="#e1f4fa")
uem = Entry(updst,bd=5,font=('comic sans ms',16,'bold'),bg = "#e1f4fa")

ubas = Button(updst, text = "Save",font=('comic sans ms',16,'bold'),command = f7,bg = "#e1f4fa")
ubab = Button(updst, text = "Back",font=('comic sans ms',16,'bold'),command = f8,bg = "#e1f4fa")

ulr.pack(pady=10)
uer.pack(pady=10)
uln.pack(pady=10)
uen.pack(pady=10)
ulm.pack(pady=10)
uem.pack(pady=10)
ubas.pack(pady=10)
ubab.pack(pady=10)

updst.withdraw()

#DeleteStudent

dst = Toplevel(root)
dst.title("Delete Students ")
dst.geometry('550x550+400-100')

dlr = Label(dst,text="Enter rno",font=('comic sans ms',16,'bold'),bg = "#e1f4fa")
der = Entry(dst,bd=5,font=('comic sans ms',16,'bold'),bg = "#e1f4fa")

dbas = Button(dst, text = "Save",font=('comic sans ms',16,'bold'),command = f10,bg = "#e1f4fa")
dbab = Button(dst, text = "Back",font=('comic sans ms',16,'bold'),command = f11,bg = "#e1f4fa")

dlr.pack(pady=10)
der.pack(pady=10)
dbas.pack(pady=10)
dbab.pack(pady=10)

dst.withdraw()

root.mainloop()
