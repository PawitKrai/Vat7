#GUI-Vat.py
from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x600')
GUI.title('Calculated Vat Programming by PAWIT')


#===== Config =====
FONT1 = ('Angsana New',20)



#====== ชองกรอกข้อมูล (ชื่อสินค้า) ======
L = ttk.Label(GUI,text = 'ชื่อสินค้า',font = FONT1).pack()
v_product = StringVar() #เก็บชื่อสินค้า
E1 = ttk.Entry(GUI,textvariable = v_product,font = FONT1)
E1.pack(pady=10)


#====== ชองกรอกข้อมูล (ราคาสินค้า) ======
L = ttk.Label(GUI,text = 'ราคาสินค้าเท่าไหร่',font = FONT1).pack()
v_price = StringVar() #เก็บราคา
E2 = ttk.Entry(GUI,textvariable = v_price,font = FONT1)
E2.pack(pady=10)

#====== ชองกรอกข้อมูล (ราคาสินค้า) ======
L = ttk.Label(GUI,text = 'จำนวน',font = FONT1).pack()
v_quantity = StringVar() #เก็บจำนวน
E3 = ttk.Entry(GUI,textvariable = v_quantity,font = FONT1)
E3.pack(pady=10)


#====== ปุ่มกดเพื่อคำนวน ======
def Calc(event=None):
	# int() คำสั่งแปลข้อความเป็นตัวเลข '2' --> 2
	prduct = v_product.get()
	price = int(v_price.get())
	quantity = int(v_quantity.get())
	total = price*quantity
	
	vat7 = total * (7/107)

	nettotal = total * (100/107)

	print('ราคาก่อน vat: {:.2f} (vat 7%: {:.2f})'.format(nettotal,vat7)) #{:.2f} นับจุดดทศนิยม 2 ตำแหน่ง

	v_result.set('สินค้า: {} {} ชิ้น ทั้งหมด {} บาท ({} บาท/ชิ้น)\nราคาสินค้า: {:.2f}.- VAT7%: {:.2f}.-'.format(prduct,
																							quantity,
																							total,
																							price,
																							nettotal,
																							vat7)) # .set() รับค่าเพื่อส่งต่อไปยัง def อื่นๆ

B1 = ttk.Button(GUI,text = 'Calulate',command = Calc)
B1.pack(ipadx = 20,ipady = 10)

# .bind ต้องใส่ event ใน def ด้วย def f(event=None) ซึ่ง event จะใส่ค่า <Return> เข้าไป
E1.bind('<Return>',Calc)
E2.bind('<Return>',Calc)
E3.bind('<Return>',Calc)


#===== Result =====
v_result = StringVar() #Label ตัวนี้ต้องประกาศ StringVar() เพราะ v_result จะมีการเปลี่ยนค่าตลอดเวลา
v_result.set('<<< Result >>>') #โชว์ข้อมูลเริ่มต้น Defualt


R1 = ttk.Label(GUI,textvariable = v_result,font = FONT1)
R1.pack(ipady=10)

GUI.mainloop()