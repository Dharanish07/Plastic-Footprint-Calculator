import tkinter as tk
from tkinter import ttk
from functools import partial  


LARGEFONT =("Circular", 35)

class tkinterApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		# Create A Canvas
		my_canvas = tk.Canvas()
		my_canvas.pack(side='left', fill='both', expand=True)
		# Add A Scrollbar To The Canvas
		my_scrollbar = ttk.Scrollbar(container, orient='vertical', command=my_canvas.yview)
		my_scrollbar.pack(side='left', fill='y')
		# Configure The Canvas
		my_canvas.configure(yscrollcommand=my_scrollbar.set)
		my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
		# Create ANOTHER Frame INSIDE the Canvas
		second_frame = tk.Frame(my_canvas)
		my_canvas.create_window((0,0), window=second_frame, anchor="ne")

		
		container.pack(side = "top", fill = "both",expand=True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		
		self.frames = {}
		for F in [PFC, PFC1_1, PFC1_2,PFC1_3,PFC2,PFC3,PFC4,PFC5,Dash]:
			frame = F(second_frame, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")
		self.show_frame(PFC)
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
		
class PFC(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Plastic Footprint Calculator", font = "Circular" )
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		label = ttk.Label(self, text ="General Information", font = "Circular" )
		label.grid(row = 2, column = 4, padx = 10, pady = 10)

		label2 = ttk.Label(self, text ="Company Name:")
		label2.grid(row = 3, column = 1,padx = 5, pady = 5,sticky='W')

		self.comp = tk.StringVar() 
		en00 = tk.Entry(self, textvariable=self.comp,width=26).grid(row=3, column=2,sticky='W')

		label2 = ttk.Label(self, text ="Plastic Reduction Scope:")
		label2.grid(row = 4, column = 1,padx = 5, pady = 5,sticky='W')

		self.se = tk.StringVar()
		mo = ttk.Combobox(self, textvariable=self.se,width=23)
		mo['values'] = ["Plastic Neutral","Plastic Negative"]
		mo['state'] = 'readonly'
		mo.grid(row = 4, column = 2,sticky='W')

		

		label2 = ttk.Label(self, text ="Plastic Footprint Scope")
		label2.grid(row = 5, column = 1,padx = 5, pady = 5,sticky='W')

		self.se1 = tk.StringVar()
		mo1 = ttk.Combobox(self, textvariable=self.se1,width=23)
		mo1['values'] = ["Product","Brand","Service","Company"]
		mo1['state'] = 'readonly'
		mo1.grid(row = 5, column = 2,sticky='W')


		label2 = ttk.Label(self, text ="Period of Data Used for Calculator")
		label2.grid(row = 6, column = 1,padx = 5, pady = 5,sticky='W')

		self.mon = tk.StringVar() 
		en00 = tk.Entry(self, textvariable=self.mon,width=26).grid(row=6, column=2,sticky='W')


		
		button1 = ttk.Button(self, text ="Next",command = lambda : controller.show_frame(PFC1_1))
		button1.grid(row = 10, column = 2, padx = 10, pady = 10)
		button2 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(PFC))
		button2.grid(row = 10, column = 1, padx = 10, pady = 10)
	def abc(self):
			self.info = [self.comp.get(),self.se.get(),self.se1.get(),self.mon.get()]
			return self.info
			

class PFC1_1(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="1A | Plastic Inputs to Production of Goods", font = "Circular",foreground="white",background="green")
		label.grid(row = 0, column =2, padx = 5, pady = 5)
		#A.Product
		label2 = ttk.Label(self, text ="A. PRODUCT \n\nThese are plastic raw materials that go directly into the product that is being made.\nExamples include vinyl, resin, glue, polypropylene plastic, polycarbonate, and \nplastics that go into toys and appliances")
		label2.grid(row = 1, column = 0,padx = 5, pady = 5,sticky='W')
		
		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 2, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 2, column = 2,padx = 5, pady = 5)
		
		se = tk.StringVar()
		mo = ttk.Combobox(self, textvariable=se)
		mo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo['state'] = 'normal'
		mo.grid(row = 3, column = 0,padx = 5, pady = 5,sticky='W')
		self.n0 = tk.StringVar()
		self.n0.set("0")
		en0 = tk.Entry(self, textvariable=self.n0).grid(row=3, column=1)
		n00 = tk.StringVar() 
		en00 = tk.Entry(self, textvariable=n00).grid(row=3, column=2)

		se1 = tk.StringVar()
		mo1 = ttk.Combobox(self, textvariable=se1)
		mo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo1['state'] = 'normal'
		mo1.grid(row = 4, column = 0,padx = 5, pady = 5,sticky='W')
		self.n1 = tk.StringVar()
		self.n1.set("0")
		en1 = tk.Entry(self, textvariable=self.n1).grid(row=4, column=1)
		n10 = tk.StringVar() 
		en10 = tk.Entry(self, textvariable=n10).grid(row=4, column=2)

		se2 = tk.StringVar()
		mo2 = ttk.Combobox(self, textvariable=se2)
		mo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo2['state'] = 'normal'
		mo2.grid(row = 5, column = 0,padx = 5, pady = 5,sticky='W')
		self.n2 = tk.StringVar()
		self.n2.set("0")
		en2 = tk.Entry(self, textvariable=self.n2).grid(row=5, column=1)
		n20 = tk.StringVar() 
		en20 = tk.Entry(self, textvariable=n20).grid(row=5, column=2)

		se3 = tk.StringVar()
		mo3 = ttk.Combobox(self, textvariable=se3)
		mo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo3['state'] = 'normal'
		mo3.grid(row = 6, column = 0,padx = 5, pady = 5,sticky='W')
		self.n3 = tk.StringVar()
		self.n3.set("0")
		en3 = tk.Entry(self, textvariable=self.n3).grid(row=6, column=1)
		n30 = tk.StringVar() 
		en30 = tk.Entry(self, textvariable=n30).grid(row=6, column=2)

		se4 = tk.StringVar()
		mo4 = ttk.Combobox(self, textvariable=se4)
		mo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo4['state'] = 'normal'
		mo4.grid(row = 7, column = 0,padx = 5, pady = 5,sticky='W')
		self.n4 = tk.StringVar()
		self.n4.set("0")
		en4 = tk.Entry(self, textvariable=self.n4).grid(row=7, column=1)
		n40 = tk.StringVar() 
		en40 = tk.Entry(self, textvariable=n40).grid(row=7, column=2)

		#B.Packaging

		label3 = ttk.Label(self, text ="B. PACKAGING \n\nThese are plastic materials that are used in the primary, secondary, or tertiary product \npackaging of the product. Examples include wrappers, bottles, caps, laminated boxes,\nand labels.")
		label3.grid(row = 8, column = 0,padx = 5, pady = 5)

		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 9, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 9, column = 2,padx = 5, pady = 5)
		
		bse = tk.StringVar()
		bmo = ttk.Combobox(self, textvariable=bse)
		bmo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo['state'] = 'normal'
		bmo.grid(row = 10, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn0 = tk.StringVar()
		self.bn0.set("0")
		ben0 = tk.Entry(self, textvariable=self.bn0).grid(row=10, column=1)
		bn00 = tk.StringVar() 
		ben00 = tk.Entry(self, textvariable=bn00).grid(row=10, column=2)

		bse1 = tk.StringVar()
		bmo1 = ttk.Combobox(self, textvariable=bse1)
		bmo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo1['state'] = 'normal'
		bmo1.grid(row = 11, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn1 = tk.StringVar()
		self.bn1.set("0")
		ben1 = tk.Entry(self, textvariable=self.bn1).grid(row=11, column=1)
		bn10 = tk.StringVar() 
		ben10 = tk.Entry(self, textvariable=bn10).grid(row=11, column=2)

		bse2 = tk.StringVar()
		bmo2 = ttk.Combobox(self, textvariable=bse2)
		bmo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo2['state'] = 'normal'
		bmo2.grid(row = 12, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn2 = tk.StringVar()
		self.bn2.set("0")
		ben2 = tk.Entry(self, textvariable=self.bn2).grid(row=12, column=1)
		bn20 = tk.StringVar() 
		ben20 = tk.Entry(self, textvariable=bn20).grid(row=12, column=2)

		bse3 = tk.StringVar()
		bmo3 = ttk.Combobox(self, textvariable=bse3)
		bmo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo3['state'] = 'normal'
		bmo3.grid(row = 13, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn3 = tk.StringVar()
		self.bn3.set("0")
		ben3 = tk.Entry(self, textvariable=self.bn3).grid(row=13, column=1)
		bn30 = tk.StringVar() 
		ben30 = tk.Entry(self, textvariable=bn30).grid(row=13, column=2)

		bse4 = tk.StringVar()
		bmo4 = ttk.Combobox(self, textvariable=bse4)
		bmo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo4['state'] = 'normal'
		bmo4.grid(row = 14, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn4 = tk.StringVar()
		self.bn4.set("0")
		ben4 = tk.Entry(self, textvariable=self.bn4).grid(row=14, column=1)
		bn40 = tk.StringVar() 
		ben40 = tk.Entry(self, textvariable=bn40).grid(row=14, column=2)

		#C.Processing

		label3 = ttk.Label(self, text ="C. PROCESSING/MANUFACTURING \n\nThese are plastic materials that are used anywhere in the manufacturing \nprocess of the product. Examples include plastic equipment, safety goggles, hairnets, \npackaging for cleaning implements and other fluids, and plastic pallets in the plant.")
		label3.grid(row = 15, column = 0,padx = 5, pady = 5)

		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 16, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 16, column = 2,padx = 5, pady = 5)
		
		cse = tk.StringVar()
		cmo = ttk.Combobox(self, textvariable=cse)
		cmo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo['state'] = 'normal'
		cmo.grid(row = 17, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn0 = tk.StringVar()
		self.cn0.set("0")
		cen0 = tk.Entry(self, textvariable=self.cn0).grid(row=17, column=1)
		cn00 = tk.StringVar() 
		cen00 = tk.Entry(self, textvariable=cn00).grid(row=17, column=2)

		cse1 = tk.StringVar()
		cmo1 = ttk.Combobox(self, textvariable=cse1)
		cmo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo1['state'] = 'normal'
		cmo1.grid(row = 18, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn1 = tk.StringVar()
		self.cn1.set("0")
		cen1 = tk.Entry(self, textvariable=self.cn1).grid(row=18, column=1)
		cn10 = tk.StringVar() 
		cen10 = tk.Entry(self, textvariable=cn10).grid(row=18, column=2)

		cse2 = tk.StringVar()
		cmo2 = ttk.Combobox(self, textvariable=cse2)
		cmo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo2['state'] = 'normal'
		cmo2.grid(row = 19, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn2 = tk.StringVar()
		self.cn2.set("0")
		cen2 = tk.Entry(self, textvariable=self.cn2).grid(row=19, column=1)
		cn20 = tk.StringVar() 
		cen20 = tk.Entry(self, textvariable=cn20).grid(row=19, column=2)

		cse3 = tk.StringVar()
		cmo3 = ttk.Combobox(self, textvariable=cse3)
		cmo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo3['state'] = 'normal'
		cmo3.grid(row = 20, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn3 = tk.StringVar()
		self.cn3.set("0")
		cen3 = tk.Entry(self, textvariable=self.cn3).grid(row=20, column=1)
		cn30 = tk.StringVar() 
		cen30 = tk.Entry(self, textvariable=cn30).grid(row=20, column=2)

		cse4 = tk.StringVar()
		cmo4 = ttk.Combobox(self, textvariable=cse4)
		cmo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo4['state'] = 'normal'
		cmo4.grid(row = 21, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn4= tk.StringVar()
		self.cn4.set("0")
		cen4 = tk.Entry(self, textvariable=self.cn4).grid(row=21, column=1)
		cn40 = tk.StringVar() 
		cen40 = tk.Entry(self, textvariable=cn40).grid(row=21, column=2)
		def call_result(label_result, n0, n1,n2,n3,n4,bn0,bn1,bn2,bn3,bn4,cn0,cn1,cn2,cn3,cn4):
					result_1_a = int(n0.get())+int(n1.get())+int(n2.get())+int(n3.get())+int(n4.get())+int(bn0.get())+int(bn1.get())+int(bn2.get())+int(bn3.get())+int(bn4.get())+int(cn0.get())+int(cn1.get())+int(cn2.get())+int(cn3.get())+int(cn4.get())
					label_result.config(text="Result = %d" % result_1_a)
					return
						

		labelResult = tk.Label(self)
		labelResult.grid(row=22, column=1)
		call_result = partial(call_result, labelResult, self.n0,self.n1,self.n2,self.n3,self.n4,self.bn0,self.bn1,self.bn2,self.bn3,self.bn4,self.cn0,self.cn1,self.cn2,self.cn3,self.cn4)
		buttonCal = tk.Button(self, text="Calculate SUBTOTAL(KG)", command=call_result).grid(row = 22, column = 0,padx = 5, pady = 5,sticky='E')

		label = ttk.Label(self, text ="1B | Plastic Inputs to Rendering Services for Service Companies", font = "Circular",foreground="white",background="green")
		label.grid(row = 24, column =2, padx = 5, pady = 5)
		
		#A.SERVICE

		label2 = ttk.Label(self, text ="A. SERVICE\n\nThese are plastic materials that are used in order to render any service.\nExamples include plastic utensils, straws, shower caps, medical equipment, \nand disposable razors.")
		label2.grid(row = 25, column = 0,padx = 5, pady = 5,sticky='W')
		
		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 26, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 26, column = 2,padx = 5, pady = 5)
		
		ba_se = tk.StringVar()
		ba_mo = ttk.Combobox(self, textvariable=ba_se)
		ba_mo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		ba_mo['state'] = 'normal'
		ba_mo.grid(row = 27, column = 0,padx = 5, pady = 5,sticky='W')
		self.ba_n0 = tk.StringVar()
		self.ba_n0.set("0")
		ba_en0 = tk.Entry(self, textvariable=self.ba_n0).grid(row=27, column=1)
		ba_n00 = tk.StringVar() 
		ba_en00 = tk.Entry(self, textvariable=ba_n00).grid(row=27, column=2)

		ba_se1 = tk.StringVar()
		ba_mo1 = ttk.Combobox(self, textvariable=ba_se1)
		ba_mo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		ba_mo1['state'] = 'normal'
		ba_mo1.grid(row = 28, column = 0,padx = 5, pady = 5,sticky='W')
		self.ba_n1 = tk.StringVar()
		self.ba_n1.set("0")
		ba_en1 = tk.Entry(self, textvariable=self.ba_n1).grid(row=28, column=1)
		ba_n10 = tk.StringVar() 
		ba_en10 = tk.Entry(self, textvariable=ba_n10).grid(row=28, column=2)

		ba_se2 = tk.StringVar()
		ba_mo2 = ttk.Combobox(self, textvariable=ba_se2)
		ba_mo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		ba_mo2['state'] = 'normal'
		ba_mo2.grid(row = 29, column = 0,padx = 5, pady = 5,sticky='W')
		self.ba_n2 = tk.StringVar()
		self.ba_n2.set("0")
		ba_en2 = tk.Entry(self, textvariable=self.ba_n2).grid(row=29, column=1)
		ba_n20 = tk.StringVar() 
		ba_en20 = tk.Entry(self, textvariable=ba_n20).grid(row=29, column=2)

		ba_se3 = tk.StringVar()
		ba_mo3 = ttk.Combobox(self, textvariable=ba_se3)
		ba_mo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		ba_mo3['state'] = 'normal'
		ba_mo3.grid(row = 30, column = 0,padx = 5, pady = 5,sticky='W')
		self.ba_n3 = tk.StringVar()
		self.ba_n3.set("0")
		ba_en3 = tk.Entry(self, textvariable=self.ba_n3).grid(row=30, column=1)
		ba_n30 = tk.StringVar() 
		ba_en30 = tk.Entry(self, textvariable=ba_n30).grid(row=30, column=2)

		ba_se4 = tk.StringVar()
		ba_mo4 = ttk.Combobox(self, textvariable=ba_se4)
		ba_mo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		ba_mo4['state'] = 'normal'
		ba_mo4.grid(row = 31, column = 0,padx = 5, pady = 5,sticky='W')
		self.ba_n4 = tk.StringVar()
		self.ba_n4.set("0")
		ba_en4 = tk.Entry(self, textvariable=self.ba_n4).grid(row=31, column=1)
		ba_n40 = tk.StringVar() 
		ba_en40 = tk.Entry(self, textvariable=ba_n40).grid(row=31, column=2)
		def call_result2(labelresult2,ba_n0, ba_n1,ba_n2,ba_n3,ba_n4):
					result_1_b = int(ba_n0.get())+int(ba_n1.get())+int(ba_n2.get())+int(ba_n3.get())+int(ba_n4.get())
					labelresult2.config(text="Result = %d" % result_1_b)
					return 
						

		labelresult2 = tk.Label(self)
		labelresult2.grid(row=32, column=1)
		callres2 = partial(call_result2, labelresult2, self.ba_n0,self.ba_n1,self.ba_n2,self.ba_n3,self.ba_n4)

		

		buttonCal2 = tk.Button(self, text="Calculate SUBTOTAL(KG)",command=callres2 ).grid(row = 32, column = 0,padx = 5, pady = 5,sticky='E')

		def call_result3(labelresult3, n0, n1,n2,n3,n4,bn0,bn1,bn2,bn3,bn4,cn0,cn1,cn2,cn3,cn4,ba_n0, ba_n1,ba_n2,ba_n3,ba_n4):
					result_1_c = int(n0.get())+int(n1.get())+int(n2.get())+int(n3.get())+int(n4.get())+int(bn0.get())+int(bn1.get())+int(bn2.get())+int(bn3.get())+int(bn4.get())+int(cn0.get())+int(cn1.get())+int(cn2.get())+int(cn3.get())+int(cn4.get())+int(ba_n0.get())+int(ba_n1.get())+int(ba_n2.get())+int(ba_n3.get())+int(ba_n4.get())
					labelresult3.config(text="Result = %d" % result_1_c)
					return 
						

		labelresult3 = tk.Label(self)
		labelresult3.grid(row=34, column=1)
		callres3 = partial(call_result3, labelresult3, self.n0, self.n1,self.n2,self.n3,self.n4,self.bn0,self.bn1,self.bn2,self.bn3,self.bn4,self.cn0,self.cn1,self.cn2,self.cn3,self.cn4, self.ba_n0,self.ba_n1,self.ba_n2,self.ba_n3,self.ba_n4)


		buttonCal3 = tk.Button(self, text="Calculate TOTAL PLASTIC INPUTS IN PRODUCTS/SERVICE (KG)",command=callres3 ).grid(row = 34, column = 0,padx = 5, pady = 5,sticky='E')

		

		
		button1 = ttk.Button(self, text ="Next",command = lambda : controller.show_frame(PFC2))
		button1.grid(row = 35, column = 2, padx = 10, pady = 10)
		button2 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(PFC))
		button2.grid(row = 35, column = 1, padx = 10, pady = 10)
		
	def abc(self):
			self.result_ttl = int(self.n0.get())+int(self.n1.get())+int(self.n2.get())+int(self.n3.get())+int(self.n4.get())+int(self.bn0.get())+int(self.bn1.get())+int(self.bn2.get())+int(self.bn3.get())+int(self.bn4.get())+int(self.cn0.get())+int(self.cn1.get())+int(self.cn2.get())+int(self.cn3.get())+int(self.cn4.get())+int(self.ba_n0.get())+int(self.ba_n1.get())+int(self.ba_n2.get())+int(self.ba_n3.get())+int(self.ba_n4.get())
			return self.result_ttl
			
			
			
		
		

class PFC1_2(tk.Frame,):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="PFC1.2", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)
		label2 = tk.Label(self)
		label2.grid(row = 5, column = 4, padx = 10, pady = 10)
		
		def call_res(label2):
					

					label2.config(text=controller.frames[PFC1_1].abc())
					return

		
		
		#def tkraise(self, aboveThis=None):
					
		#                       start_page = self.controller.frames[PFC1_1]
					
		#                       self.label2.configure(text=start_page.abc())
		#                       super().tkraise(aboveThis)

					
		
		#label = ttk.Label(self, text =tex, font = LARGEFONT)
		#label.grid(row = 4, column = 4, padx = 10, pady = 10)

		changelbl=partial(call_res,label2)
		button1 = ttk.Button(self, text ="Next",command = lambda : controller.show_frame(PFC1_3))
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)
		button2 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(PFC1_1))
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
		button3 = ttk.Button(self, text ="Change",command = changelbl)
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)

		
class PFC1_3(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="PFC1.3", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)
		button1 = ttk.Button(self, text ="Next",command = lambda : controller.show_frame(PFC2))
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)
		button2 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(PFC1_2))
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

class PFC2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="2| Plastics Used in Logistics & Shipping", font = "Circular",foreground="white",background="green")
		label.grid(row = 0, column =2, padx = 5, pady = 5)
		
		#A.PLASTIC USED IN PACKING AND TRANSPORTING FROM MANUFACTURING TO WAREHOUSE
		
		label2 = ttk.Label(self, text ="A. PLASTIC USED IN PACKING AND TRANSPORTING FROM MANUFACTURING\nTO WAREHOUSE\n\nExamples include plastic pallets used in truck, stretch wrap, and bubble wrap.")
		label2.grid(row = 1, column = 0,padx = 5, pady = 5,sticky='W')
		
		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 2, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 2, column = 2,padx = 5, pady = 5)
		
		se = tk.StringVar()
		mo = ttk.Combobox(self, textvariable=se)
		mo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo['state'] = 'normal'
		mo.grid(row = 3, column = 0,padx = 5, pady = 5,sticky='W')
		self.n0= tk.StringVar()
		self.n0.set("0")
		en0 = tk.Entry(self, textvariable=self.n0).grid(row=3, column=1)
		n00 = tk.StringVar()
		en00 = tk.Entry(self, textvariable=n00).grid(row=3, column=2)

		se1 = tk.StringVar()
		mo1 = ttk.Combobox(self, textvariable=se1)
		mo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo1['state'] = 'normal'
		mo1.grid(row = 4, column = 0,padx = 5, pady = 5,sticky='W')
		self.n1 = tk.StringVar()
		self.n1.set("0")
		en1 = tk.Entry(self, textvariable=self.n1).grid(row=4, column=1)
		n10 = tk.StringVar()
		en10 = tk.Entry(self, textvariable=n10).grid(row=4, column=2)
		
		se2 = tk.StringVar()
		mo2 = ttk.Combobox(self, textvariable=se2)
		mo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo2['state'] = 'normal'
		mo2.grid(row = 5, column = 0,padx = 5, pady = 5,sticky='W')
		self.n2 = tk.StringVar()
		self.n2.set("0")
		en2 = tk.Entry(self, textvariable=self.n2).grid(row=5, column=1)
		n20 = tk.StringVar()
		en20 = tk.Entry(self, textvariable=n20).grid(row=5, column=2)

		se3 = tk.StringVar()
		mo3 = ttk.Combobox(self, textvariable=se3)
		mo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo3['state'] = 'normal'
		mo3.grid(row = 6, column = 0,padx = 5, pady = 5,sticky='W')
		self.n3 = tk.StringVar()
		self.n3.set("0")
		en3 = tk.Entry(self, textvariable=self.n3).grid(row=6, column=1)
		n30 = tk.StringVar()
		en30 = tk.Entry(self, textvariable=n30).grid(row=6, column=2)

		se4 = tk.StringVar()
		mo4 = ttk.Combobox(self, textvariable=se4)
		mo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo4['state'] = 'normal'
		mo4.grid(row = 7, column = 0,padx = 5, pady = 5,sticky='W')
		self.n4= tk.StringVar()
		self.n4.set("0")
		en4 = tk.Entry(self, textvariable=self.n4).grid(row=7, column=1)
		n40 = tk.StringVar()
		en40 = tk.Entry(self, textvariable=n40).grid(row=7, column=2)

		#B.PLASTIC USED IN PACKING AND TRANSPORTING FROM WAREHOUSE TO RETAILER

		label3 = ttk.Label(self, text ="B. PLASTIC USED IN PACKING AND TRANSPORTING FROM WAREHOUSE TO RETAILER\n\nExamples include nylon, adhesives, and plastic twine.")
		label3.grid(row = 8, column = 0,padx = 5, pady = 5)

		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 9, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 9, column = 2,padx = 5, pady = 5)
		
		bse = tk.StringVar()
		bmo = ttk.Combobox(self, textvariable=bse)
		bmo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo['state'] = 'normal'
		bmo.grid(row = 10, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn0= tk.StringVar()
		self.bn0.set("0") 
		ben0 = tk.Entry(self, textvariable=self.bn0).grid(row=10, column=1)
		bn00 = tk.StringVar() 
		ben00 = tk.Entry(self, textvariable=bn00).grid(row=10, column=2)

		bse1 = tk.StringVar()
		bmo1 = ttk.Combobox(self, textvariable=bse1)
		bmo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo1['state'] = 'normal'
		bmo1.grid(row = 11, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn1= tk.StringVar()
		self.bn1.set("0") 
		ben1 = tk.Entry(self, textvariable=self.bn1).grid(row=11, column=1)
		bn10 = tk.StringVar() 
		ben10 = tk.Entry(self, textvariable=bn10).grid(row=11, column=2)

		bse2 = tk.StringVar()
		bmo2 = ttk.Combobox(self, textvariable=bse2)
		bmo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo2['state'] = 'normal'
		bmo2.grid(row = 12, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn2= tk.StringVar()
		self.bn2.set("0")
		ben2 = tk.Entry(self, textvariable=self.bn2).grid(row=12, column=1)
		bn20 = tk.StringVar() 
		ben20 = tk.Entry(self, textvariable=bn20).grid(row=12, column=2)

		bse3 = tk.StringVar()
		bmo3 = ttk.Combobox(self, textvariable=bse3)
		bmo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo3['state'] = 'normal'
		bmo3.grid(row = 13, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn3 = tk.StringVar()
		self.bn3.set("0") 
		ben3 = tk.Entry(self, textvariable=self.bn3).grid(row=13, column=1)
		bn30 = tk.StringVar() 
		ben30 = tk.Entry(self, textvariable=bn30).grid(row=13, column=2)

		bse4 = tk.StringVar()
		bmo4 = ttk.Combobox(self, textvariable=bse4)
		bmo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo4['state'] = 'normal'
		bmo4.grid(row = 14, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn4= tk.StringVar()
		self.bn4.set("0") 
		ben4 = tk.Entry(self, textvariable=self.bn4).grid(row=14, column=1)
		bn40 = tk.StringVar() 
		ben40 = tk.Entry(self, textvariable=bn40).grid(row=14, column=2)

				#C.PLASTICS USED IN PACKING AND TRANSPORTING FROM WAREHOUSE DIRECTO TO CONSUMER
		
		label3 = ttk.Label(self, text ="C. PLASTICS USED IN PACKING AND TRANSPORTING FROM WAREHOUSE DIRECTO TO\nCONSUMER (I.E. ONLINE SALES, DIRECT SALES, ETC.)\n\nExamples include delivery sleeves, shipping and return bags, and plastic tags.")
		label3.grid(row = 15, column = 0,padx = 5, pady = 5)

		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 16, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 16, column = 2,padx = 5, pady = 5)
		
		cse = tk.StringVar()
		cmo = ttk.Combobox(self, textvariable=cse)
		cmo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo['state'] = 'normal'
		cmo.grid(row = 17, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn0= tk.StringVar()
		self.cn0.set("0") 
		cen0 = tk.Entry(self, textvariable=self.cn0).grid(row=17, column=1)
		cn00 = tk.StringVar() 
		cen00 = tk.Entry(self, textvariable=cn00).grid(row=17, column=2)

		cse1 = tk.StringVar()
		cmo1 = ttk.Combobox(self, textvariable=cse1)
		cmo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo1['state'] = 'normal'
		cmo1.grid(row = 18, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn1= tk.StringVar()
		self.cn1.set("0") 
		cen1 = tk.Entry(self, textvariable=self.cn1).grid(row=18, column=1)
		cn10 = tk.StringVar() 
		cen10 = tk.Entry(self, textvariable=cn10).grid(row=18, column=2)

		cse2 = tk.StringVar()
		cmo2 = ttk.Combobox(self, textvariable=cse2)
		cmo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo2['state'] = 'normal'
		cmo2.grid(row = 19, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn2 = tk.StringVar()
		self.cn2.set("0") 
		cen2 = tk.Entry(self, textvariable=self.cn2).grid(row=19, column=1)
		cn20 = tk.StringVar() 
		cen20 = tk.Entry(self, textvariable=cn20).grid(row=19, column=2)

		cse3 = tk.StringVar()
		cmo3 = ttk.Combobox(self, textvariable=cse3)
		cmo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo3['state'] = 'normal'
		cmo3.grid(row = 20, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn3 = tk.StringVar()
		self.cn3.set("0") 
		cen3 = tk.Entry(self, textvariable=self.cn3).grid(row=20, column=1)
		cn30 = tk.StringVar() 
		cen30 = tk.Entry(self, textvariable=cn30).grid(row=20, column=2)

		cse4 = tk.StringVar()
		cmo4 = ttk.Combobox(self, textvariable=cse4)
		cmo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo4['state'] = 'normal'
		cmo4.grid(row = 21, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn4= tk.StringVar()
		self.cn4.set("0") 
		cen4 = tk.Entry(self, textvariable=self.cn4).grid(row=21, column=1)
		cn40 = tk.StringVar() 
		cen40 = tk.Entry(self, textvariable=cn40).grid(row=21, column=2)


		def call_result_2(label_result_2, n0, n1,n2,n3,n4,bn0,bn1,bn2,bn3,bn4,cn0,cn1,cn2,cn3,cn4):
					result_2 = int(n0.get())+int(n1.get())+int(n2.get())+int(n3.get())+int(n4.get())+int(bn0.get())+int(bn1.get())+int(bn2.get())+int(bn3.get())+int(bn4.get())+int(cn0.get())+int(cn1.get())+int(cn2.get())+int(cn3.get())+int(cn4.get())
					label_result_2.config(text="Result = %d" % result_2)
					return
						

		labelresult_2 = tk.Label(self)
		labelresult_2.grid(row=22, column=1)
		call_result_2 = partial(call_result_2, labelresult_2, self.n0,self.n1,self.n2,self.n3,self.n4,self.bn0,self.bn1,self.bn2,self.bn3,self.bn4,self.cn0,self.cn1,self.cn2,self.cn3,self.cn4)


		buttonCal = tk.Button(self, text="Calculate SUBTOTAL(KG)",command=call_result_2).grid(row = 22, column = 0,padx = 5, pady = 5,sticky='E')
		
		button1 = ttk.Button(self, text ="Next",command = lambda : controller.show_frame(PFC3))
		button1.grid(row = 24, column = 2, padx = 10, pady = 10)
		button2 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(PFC1))
		button2.grid(row = 24, column = 1, padx = 10, pady = 10)

	def abc(self):
	    self.result_ttl = int(self.n0.get())+int(self.n1.get())+int(self.n2.get())+int(self.n3.get())+int(self.n4.get())+int(self.bn0.get())+int(self.bn1.get())+int(self.bn2.get())+int(self.bn3.get())+int(self.bn4.get())+int(self.cn0.get())+int(self.cn1.get())+int(self.cn2.get())+int(self.cn3.get())+int(self.cn4.get())
	    return self.result_ttl
		
class PFC3(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="3| Plastics Used Directly for Advertising, Promotions & Merchandising", font = "Circular",foreground="white",background="green")
		label.grid(row = 0, column =2, padx = 5, pady = 5)
		#A.PLASTICS USED IN ADVERTISING
		label2 = ttk.Label(self, text ="A. PLASTICS USED IN ADVERTISING\nExamples include billboard tarpaulins, point-of-sale displays, laminated brochures, \nPVC banners, and signages.")
		label2.grid(row = 1, column = 0,padx = 5, pady = 5,sticky='W')
		
		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 2, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 2, column = 2,padx = 5, pady = 5)
		
		se = tk.StringVar()
		mo = ttk.Combobox(self, textvariable=se)
		mo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo['state'] = 'normal'
		mo.grid(row = 3, column = 0,padx = 5, pady = 5,sticky='W')
		self.n0= tk.StringVar()
		self.n0.set("0")
		en0 = tk.Entry(self, textvariable=self.n0).grid(row=3, column=1)
		n00 = tk.StringVar()
		en00 = tk.Entry(self, textvariable=n00).grid(row=3, column=2)

		se1 = tk.StringVar()
		mo1 = ttk.Combobox(self, textvariable=se1)
		mo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo1['state'] = 'normal'
		mo1.grid(row = 4, column = 0,padx = 5, pady = 5,sticky='W')
		self.n1 = tk.StringVar()
		self.n1.set("0")
		en1 = tk.Entry(self, textvariable=self.n1).grid(row=4, column=1)
		n10 = tk.StringVar()
		en10 = tk.Entry(self, textvariable=n10).grid(row=4, column=2)
		
		se2 = tk.StringVar()
		mo2 = ttk.Combobox(self, textvariable=se2)
		mo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo2['state'] = 'normal'
		mo2.grid(row = 5, column = 0,padx = 5, pady = 5,sticky='W')
		self.n2 = tk.StringVar()
		self.n2.set("0")
		en2 = tk.Entry(self, textvariable=self.n2).grid(row=5, column=1)
		n20 = tk.StringVar()
		en20 = tk.Entry(self, textvariable=n20).grid(row=5, column=2)

		se3 = tk.StringVar()
		mo3 = ttk.Combobox(self, textvariable=se3)
		mo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo3['state'] = 'normal'
		mo3.grid(row = 6, column = 0,padx = 5, pady = 5,sticky='W')
		self.n3 = tk.StringVar()
		self.n3.set("0")
		en3 = tk.Entry(self, textvariable=self.n3).grid(row=6, column=1)
		n30 = tk.StringVar()
		en30 = tk.Entry(self, textvariable=n30).grid(row=6, column=2)

		se4 = tk.StringVar()
		mo4 = ttk.Combobox(self, textvariable=se4)
		mo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo4['state'] = 'normal'
		mo4.grid(row = 7, column = 0,padx = 5, pady = 5,sticky='W')
		self.n4= tk.StringVar()
		self.n4.set("0")
		en4 = tk.Entry(self, textvariable=self.n4).grid(row=7, column=1)
		n40 = tk.StringVar()
		en40 = tk.Entry(self, textvariable=n40).grid(row=7, column=2)

		#B.PLASTICS USED IN EVENTS AND ACTIVATIONS

		label3 = ttk.Label(self, text ="B. PLASTICS USED IN EVENTS AND ACTIVATIONS\nExamples include plastic booths, snack and beverage packaging, and various fit-outs and decorations.")
		label3.grid(row = 8, column = 0,padx = 5, pady = 5)

		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 9, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 9, column = 2,padx = 5, pady = 5)
		
		bse = tk.StringVar()
		bmo = ttk.Combobox(self, textvariable=bse)
		bmo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo['state'] = 'normal'
		bmo.grid(row = 10, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn0= tk.StringVar()
		self.bn0.set("0") 
		ben0 = tk.Entry(self, textvariable=self.bn0).grid(row=10, column=1)
		bn00 = tk.StringVar() 
		ben00 = tk.Entry(self, textvariable=bn00).grid(row=10, column=2)

		bse1 = tk.StringVar()
		bmo1 = ttk.Combobox(self, textvariable=bse1)
		bmo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo1['state'] = 'normal'
		bmo1.grid(row = 11, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn1= tk.StringVar()
		self.bn1.set("0") 
		ben1 = tk.Entry(self, textvariable=self.bn1).grid(row=11, column=1)
		bn10 = tk.StringVar() 
		ben10 = tk.Entry(self, textvariable=bn10).grid(row=11, column=2)

		bse2 = tk.StringVar()
		bmo2 = ttk.Combobox(self, textvariable=bse2)
		bmo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo2['state'] = 'normal'
		bmo2.grid(row = 12, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn2= tk.StringVar()
		self.bn2.set("0") 
		ben2 = tk.Entry(self, textvariable=self.bn2).grid(row=12, column=1)
		bn20 = tk.StringVar() 
		ben20 = tk.Entry(self, textvariable=bn20).grid(row=12, column=2)

		bse3 = tk.StringVar()
		bmo3 = ttk.Combobox(self, textvariable=bse3)
		bmo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo3['state'] = 'normal'
		bmo3.grid(row = 13, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn3 = tk.StringVar()
		self.bn3.set("0") 
		ben3 = tk.Entry(self, textvariable=self.bn3).grid(row=13, column=1)
		bn30 = tk.StringVar() 
		ben30 = tk.Entry(self, textvariable=bn30).grid(row=13, column=2)

		bse4 = tk.StringVar()
		bmo4 = ttk.Combobox(self, textvariable=bse4)
		bmo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo4['state'] = 'normal'
		bmo4.grid(row = 14, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn4= tk.StringVar()
		self.bn4.set("0") 
		ben4 = tk.Entry(self, textvariable=self.bn4).grid(row=14, column=1)
		bn40 = tk.StringVar() 
		ben40 = tk.Entry(self, textvariable=bn40).grid(row=14, column=2)

		def call_result_3(label_result3, n0, n1,n2,n3,n4,bn0,bn1,bn2,bn3,bn4):
					result_3 = int(n0.get())+int(n1.get())+int(n2.get())+int(n3.get())+int(n4.get())+int(bn0.get())+int(bn1.get())+int(bn2.get())+int(bn3.get())+int(bn4.get())
					label_result3.config(text="Result = %d" % result_3)
					return
						

		labelResult3 = tk.Label(self)
		labelResult3.grid(row=15, column=1)
		call_result3 = partial(call_result_3, labelResult3, self.n0,self.n1,self.n2,self.n3,self.n4,self.bn0,self.bn1,self.bn2,self.bn3,self.bn4)
		

		buttonCal = tk.Button(self, text="Calculate SUBTOTAL(KG)",command=call_result3 ).grid(row = 15, column = 0,padx = 5, pady = 5,sticky='E')
		
		button1 = ttk.Button(self, text ="Next",command = lambda : controller.show_frame(PFC4))
		button1.grid(row = 17, column = 2, padx = 10, pady = 10)
		button2 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(PFC2))
		button2.grid(row = 17, column = 1, padx = 10, pady = 10)

	def abc(self):
	    self.result_ttl = int(self.n0.get())+int(self.n1.get())+int(self.n2.get())+int(self.n3.get())+int(self.n4.get())+int(self.bn0.get())+int(self.bn1.get())+int(self.bn2.get())+int(self.bn3.get())+int(self.bn4.get())
	    return self.result_ttl

		

class PFC4(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="4| Plastics Used for General & Administrative Activities", font = "Circular",foreground="white",background="green")
		label.grid(row = 0, column =2, padx = 5, pady = 5)
		#A.PLASTICS USED IN OFFICE FURNITURE AND EQUIPMENT
		label2 = ttk.Label(self, text ="A. PLASTICS USED IN OFFICE FURNITURE AND EQUIPMENT\n\nExamples include plastic components in laptops, printers, A/C units, \nstorage bins, and furniture.")
		label2.grid(row = 1, column = 0,padx = 5, pady = 5,sticky='W')
		
		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 2, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 2, column = 2,padx = 5, pady = 5)
		
		se = tk.StringVar()
		mo = ttk.Combobox(self, textvariable=se)
		mo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo['state'] = 'normal'
		mo.grid(row = 3, column = 0,padx = 5, pady = 5,sticky='W')
		self.n0 = tk.StringVar()
		self.n0.set("0")
		en0 = tk.Entry(self, textvariable=self.n0).grid(row=3, column=1)
		n00 = tk.StringVar() 
		en00 = tk.Entry(self, textvariable=n00).grid(row=3, column=2)

		se1 = tk.StringVar()
		mo1 = ttk.Combobox(self, textvariable=se1)
		mo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo1['state'] = 'normal'
		mo1.grid(row = 4, column = 0,padx = 5, pady = 5,sticky='W')
		self.n1 = tk.StringVar()
		self.n1.set("0") 
		en1 = tk.Entry(self, textvariable=self.n1).grid(row=4, column=1)
		n10 = tk.StringVar() 
		en10 = tk.Entry(self, textvariable=n10).grid(row=4, column=2)

		se2 = tk.StringVar()
		mo2 = ttk.Combobox(self, textvariable=se2)
		mo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo2['state'] = 'normal'
		mo2.grid(row = 5, column = 0,padx = 5, pady = 5,sticky='W')
		self.n2 = tk.StringVar()
		self.n2.set("0") 
		en2 = tk.Entry(self, textvariable=self.n2).grid(row=5, column=1)
		n20 = tk.StringVar() 
		en20 = tk.Entry(self, textvariable=n20).grid(row=5, column=2)

		se3 = tk.StringVar()
		mo3 = ttk.Combobox(self, textvariable=se3)
		mo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo3['state'] = 'normal'
		mo3.grid(row = 6, column = 0,padx = 5, pady = 5,sticky='W')
		self.n3 = tk.StringVar()
		self.n3.set("0") 
		en3 = tk.Entry(self, textvariable=self.n3).grid(row=6, column=1)
		n30 = tk.StringVar() 
		en30 = tk.Entry(self, textvariable=n30).grid(row=6, column=2)

		se4 = tk.StringVar()
		mo4 = ttk.Combobox(self, textvariable=se4)
		mo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo4['state'] = 'normal'
		mo4.grid(row = 7, column = 0,padx = 5, pady = 5,sticky='W')
		self.n4= tk.StringVar()
		self.n4.set("0") 
		en4 = tk.Entry(self, textvariable=self.n4).grid(row=7, column=1)
		n40 = tk.StringVar() 
		en40 = tk.Entry(self, textvariable=n40).grid(row=7, column=2)

		#B.PLASTICS USED IN OFFICE SUPPLIES

		label3 = ttk.Label(self, text ="B. PLASTICS USED IN OFFICE SUPPLIES\n\nExamples include plastic components and packaging of plastic fasteners, \nbinder clips paper reams, snacks, and cleaning supplies.")
		label3.grid(row = 8, column = 0,padx = 5, pady = 5,sticky='W')

		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 9, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 9, column = 2,padx = 5, pady = 5)
		
		bse = tk.StringVar()
		bmo = ttk.Combobox(self, textvariable=bse)
		bmo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo['state'] = 'normal'
		bmo.grid(row = 10, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn0= tk.StringVar()
		self.bn0.set("0") 
		ben0 = tk.Entry(self, textvariable=self.bn0).grid(row=10, column=1)
		bn00 = tk.StringVar() 
		ben00 = tk.Entry(self, textvariable=bn00).grid(row=10, column=2)

		bse1 = tk.StringVar()
		bmo1 = ttk.Combobox(self, textvariable=bse1)
		bmo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo1['state'] = 'normal'
		bmo1.grid(row = 11, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn1= tk.StringVar()
		self.bn1.set("0") 
		ben1 = tk.Entry(self, textvariable=self.bn1).grid(row=11, column=1)
		bn10 = tk.StringVar() 
		ben10 = tk.Entry(self, textvariable=bn10).grid(row=11, column=2)

		bse2 = tk.StringVar()
		bmo2 = ttk.Combobox(self, textvariable=bse2)
		bmo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo2['state'] = 'normal'
		bmo2.grid(row = 12, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn2= tk.StringVar()
		self.bn2.set("0") 
		ben2 = tk.Entry(self, textvariable=self.bn2).grid(row=12, column=1)
		bn20 = tk.StringVar() 
		ben20 = tk.Entry(self, textvariable=bn20).grid(row=12, column=2)

		bse3 = tk.StringVar()
		bmo3 = ttk.Combobox(self, textvariable=bse3)
		bmo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo3['state'] = 'normal'
		bmo3.grid(row = 13, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn3 = tk.StringVar()
		self.bn3.set("0") 
		ben3 = tk.Entry(self, textvariable=self.bn3).grid(row=13, column=1)
		bn30 = tk.StringVar() 
		ben30 = tk.Entry(self, textvariable=bn30).grid(row=13, column=2)

		bse4 = tk.StringVar()
		bmo4 = ttk.Combobox(self, textvariable=bse4)
		bmo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo4['state'] = 'normal'
		bmo4.grid(row = 14, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn4= tk.StringVar()
		self.bn4.set("0") 
		ben4 = tk.Entry(self, textvariable=self.bn4).grid(row=14, column=1)
		bn40 = tk.StringVar() 
		ben40 = tk.Entry(self, textvariable=bn40).grid(row=14, column=2)

				#C.Processing

		label3 = ttk.Label(self, text ="C. PLASTICS USED IN COMPANY EVENTS\n\nExamples include plastic used at company birthdays, luncheons, and \nparties; e.g. plastic utensils, decor, takeout packaging, and acrylic nameplates.")
		label3.grid(row = 15, column = 0,padx = 5, pady = 5,sticky='W')

		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 16, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 16, column = 2,padx = 5, pady = 5)
		
		cse = tk.StringVar()
		cmo = ttk.Combobox(self, textvariable=cse)
		cmo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo['state'] = 'normal'
		cmo.grid(row = 17, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn0= tk.StringVar()
		self.cn0.set("0") 
		cen0 = tk.Entry(self, textvariable=self.cn0).grid(row=17, column=1)
		cn00 = tk.StringVar() 
		cen00 = tk.Entry(self, textvariable=cn00).grid(row=17, column=2)

		cse1 = tk.StringVar()
		cmo1 = ttk.Combobox(self, textvariable=cse1)
		cmo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo1['state'] = 'normal'
		cmo1.grid(row = 18, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn1= tk.StringVar()
		self.cn1.set("0") 
		cen1 = tk.Entry(self, textvariable=self.cn1).grid(row=18, column=1)
		cn10 = tk.StringVar() 
		cen10 = tk.Entry(self, textvariable=cn10).grid(row=18, column=2)

		cse2 = tk.StringVar()
		cmo2 = ttk.Combobox(self, textvariable=cse2)
		cmo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo2['state'] = 'normal'
		cmo2.grid(row = 19, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn2 = tk.StringVar()
		self.cn2.set("0") 
		cen2 = tk.Entry(self, textvariable=self.cn2).grid(row=19, column=1)
		cn20 = tk.StringVar() 
		cen20 = tk.Entry(self, textvariable=cn20).grid(row=19, column=2)

		cse3 = tk.StringVar()
		cmo3 = ttk.Combobox(self, textvariable=cse3)
		cmo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo3['state'] = 'normal'
		cmo3.grid(row = 20, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn3 = tk.StringVar()
		self.cn3.set("0") 
		cen3 = tk.Entry(self, textvariable=self.cn3).grid(row=20, column=1)
		cn30 = tk.StringVar() 
		cen30 = tk.Entry(self, textvariable=cn30).grid(row=20, column=2)

		cse4 = tk.StringVar()
		cmo4 = ttk.Combobox(self, textvariable=cse4)
		cmo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo4['state'] = 'normal'
		cmo4.grid(row = 21, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn4= tk.StringVar()
		self.cn4.set("0") 
		cen4 = tk.Entry(self, textvariable=self.cn4).grid(row=21, column=1)
		cn40 = tk.StringVar() 
		cen40 = tk.Entry(self, textvariable=cn40).grid(row=21, column=2)

		#D.Processing

		label3 = ttk.Label(self, text ="D. PLASTICS USED IN RESEARCH AND DEVELOPMENT\n\nThese are plastic materials used in new product or service innovations. Examples include \nplastic raw materials, packaging components, tools, and equipment.")
		label3.grid(row = 22, column = 0,padx = 5, pady = 5)

		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 23, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 23, column = 2,padx = 5, pady = 5)
		
		dse = tk.StringVar()
		dmo = ttk.Combobox(self, textvariable=dse)
		dmo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		dmo['state'] = 'normal'
		dmo.grid(row = 24, column = 0,padx = 5, pady = 5,sticky='W')
		self.dn0 = tk.StringVar()
		self.dn0.set("0")
		den0 = tk.Entry(self, textvariable=self.dn0).grid(row=24, column=1)
		dn00 = tk.StringVar() 
		den00 = tk.Entry(self, textvariable=dn00).grid(row=24, column=2)

		dse1 = tk.StringVar()
		dmo1 = ttk.Combobox(self, textvariable=dse1)
		dmo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		dmo1['state'] = 'normal'
		dmo1.grid(row = 25, column = 0,padx = 5, pady = 5,sticky='W')
		self.dn1 = tk.StringVar()
		self.dn1.set("0")
		den1 = tk.Entry(self, textvariable=self.dn1).grid(row=25, column=1)
		dn10 = tk.StringVar() 
		den10 = tk.Entry(self, textvariable=dn10).grid(row=25, column=2)

		dse2 = tk.StringVar()
		dmo2 = ttk.Combobox(self, textvariable=dse2)
		dmo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		dmo2['state'] = 'normal'
		dmo2.grid(row = 26, column = 0,padx = 5, pady = 5,sticky='W')
		self.dn2 = tk.StringVar()
		self.dn2.set("0")
		den2 = tk.Entry(self, textvariable=self.dn2).grid(row=26, column=1)
		dn20 = tk.StringVar() 
		den20 = tk.Entry(self, textvariable=dn20).grid(row=26, column=2)

		dse3 = tk.StringVar()
		dmo3 = ttk.Combobox(self, textvariable=dse3)
		dmo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		dmo3['state'] = 'normal'
		dmo3.grid(row = 27, column = 0,padx = 5, pady = 5,sticky='W')
		self.dn3 = tk.StringVar()
		self.dn3.set("0") 
		den3 = tk.Entry(self, textvariable=self.dn3).grid(row=27, column=1)
		dn30 = tk.StringVar() 
		den30 = tk.Entry(self, textvariable=dn30).grid(row=27, column=2)

		dse4 = tk.StringVar()
		dmo4 = ttk.Combobox(self, textvariable=cse4)
		dmo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		dmo4['state'] = 'normal'
		dmo4.grid(row = 28, column = 0,padx = 5, pady = 5,sticky='W')
		self.dn4= tk.StringVar()
		self.dn4.set("0") 
		den4 = tk.Entry(self, textvariable=self.dn4).grid(row=28, column=1)
		dn40 = tk.StringVar() 
		den40 = tk.Entry(self, textvariable=dn40).grid(row=28, column=2)

		def call_result4(label_result4, n0, n1,n2,n3,n4,bn0,bn1,bn2,bn3,bn4,cn0,cn1,cn2,cn3,cn4,dn0,dn1,dn2,dn3,dn4):
					result_4 = int(n0.get())+int(n1.get())+int(n2.get())+int(n3.get())+int(n4.get())+int(bn0.get())+int(bn1.get())+int(bn2.get())+int(bn3.get())+int(bn4.get())+int(cn0.get())+int(cn1.get())+int(cn2.get())+int(cn3.get())+int(cn4.get())+int(dn0.get())+int(dn1.get())+int(dn2.get())+int(dn3.get())+int(dn4.get())
					label_result4.config(text="Result = %d" % result_4)
					return
				
						

		labelResult4 = tk.Label(self)
		labelResult4.grid(row=29, column=1)
		call_result4 = partial(call_result4, labelResult4, self.n0,self.n1,self.n2,self.n3,self.n4,self.bn0,self.bn1,self.bn2,self.bn3,self.bn4,self.cn0,self.cn1,self.cn2,self.cn3,self.cn4,self.dn0,self.dn1,self.dn2,self.dn3,self.dn4)


		buttonCal = tk.Button(self, text="Calculate SUBTOTAL(KG)",command=call_result4 ).grid(row = 29, column = 0,padx = 5, pady = 5,sticky='E')

		def call_result_ttl(label_result_ttl, n0, n1,n2,n3,n4,bn0,bn1,bn2,bn3,bn4,cn0,cn1,cn2,cn3,cn4,dn0,dn1,dn2,dn3,dn4):
					result_ttl = int(n0.get())+int(n1.get())+int(n2.get())+int(n3.get())+int(n4.get())+int(bn0.get())+int(bn1.get())+int(bn2.get())+int(bn3.get())+int(bn4.get())+int(cn0.get())+int(cn1.get())+int(cn2.get())+int(cn3.get())+int(cn4.get())+int(dn0.get())+int(dn1.get())+int(dn2.get())+int(dn3.get())+int(dn4.get())
					result_ttl=(result_ttl+controller.frames[PFC1_1].abc()+controller.frames[PFC2].abc()+controller.frames[PFC3].abc())/1000
					label_result_ttl.config(text="Result = %d" % result_ttl)
					return
		
		
		labelResult_ttl = tk.Label(self)
		labelResult_ttl.grid(row=30, column=1)
		call_result_ttl = partial(call_result_ttl, labelResult_ttl, self.n0,self.n1,self.n2,self.n3,self.n4,self.bn0,self.bn1,self.bn2,self.bn3,self.bn4,self.cn0,self.cn1,self.cn2,self.cn3,self.cn4,self.dn0,self.dn1,self.dn2,self.dn3,self.dn4)
		buttonCal2 = tk.Button(self, text="TOTAL GROSS PLASTIC FOOTPRINT (MT)",command=call_result_ttl ).grid(row = 30, column = 0,padx = 5, pady = 5,sticky='E')

		button1 = ttk.Button(self, text ="Next",command = lambda : controller.show_frame(PFC5))
		button1.grid(row = 32, column = 2, padx = 10, pady = 10)
		button2 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(PFC3))
		button2.grid(row = 32, column = 1, padx = 10, pady = 10)

	def abc(self):
	    self.result_ttl = int(self.n0.get())+int(self.n1.get())+int(self.n2.get())+int(self.n3.get())+int(self.n4.get())+int(self.bn0.get())+int(self.bn1.get())+int(self.bn2.get())+int(self.bn3.get())+int(self.bn4.get())+int(self.cn0.get())+int(self.cn1.get())+int(self.cn2.get())+int(self.cn3.get())+int(self.cn4.get())+int(self.dn0.get())+int(self.dn1.get())+int(self.dn2.get())+int(self.dn3.get())+int(self.dn4.get())
	    return self.result_ttl
		
class PFC5(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Plastics Reused / Recycled / Composted", font = "Circular",foreground="white",background="green")
		label.grid(row = 0, column =2, padx = 5, pady = 5)
		
		#A.REUSE/REUSED PACKAGING
		label2 = ttk.Label(self, text ="A. REUSE/REUSED PACKAGING\n\nOperation by which packaging is refilled or used for the same purpose for which it was conceived,\nwith or without the support of auxiliary products present on the market, \nenabling the packaging to be refilled. ")
		label2.grid(row = 1, column = 0,padx = 5, pady = 5,sticky='W')
		
		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 2, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 2, column = 2,padx = 5, pady = 5)
		
		se = tk.StringVar()
		mo = ttk.Combobox(self, textvariable=se)
		mo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo['state'] = 'normal'
		mo.grid(row = 3, column = 0,padx = 5, pady = 5,sticky='W')
		self.n0 = tk.StringVar()
		self.n0.set("0")
		en0 = tk.Entry(self, textvariable=self.n0).grid(row=3, column=1)
		n00 = tk.StringVar() 
		en00 = tk.Entry(self, textvariable=n00).grid(row=3, column=2)

		se1 = tk.StringVar()
		mo1 = ttk.Combobox(self, textvariable=se1)
		mo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo1['state'] = 'normal'
		mo1.grid(row = 4, column = 0,padx = 5, pady = 5,sticky='W')
		self.n1 = tk.StringVar()
		self.n1.set("0") 
		en1 = tk.Entry(self, textvariable=self.n1).grid(row=4, column=1)
		n10 = tk.StringVar() 
		en10 = tk.Entry(self, textvariable=n10).grid(row=4, column=2)

		se2 = tk.StringVar()
		mo2 = ttk.Combobox(self, textvariable=se2)
		mo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo2['state'] = 'normal'
		mo2.grid(row = 5, column = 0,padx = 5, pady = 5,sticky='W')
		self.n2 = tk.StringVar()
		self.n2.set("0") 
		en2 = tk.Entry(self, textvariable=self.n2).grid(row=5, column=1)
		n20 = tk.StringVar() 
		en20 = tk.Entry(self, textvariable=n20).grid(row=5, column=2)

		se3 = tk.StringVar()
		mo3 = ttk.Combobox(self, textvariable=se3)
		mo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo3['state'] = 'normal'
		mo3.grid(row = 6, column = 0,padx = 5, pady = 5,sticky='W')
		self.n3 = tk.StringVar()
		self.n3.set("0") 
		en3 = tk.Entry(self, textvariable=self.n3).grid(row=6, column=1)
		n30 = tk.StringVar() 
		en30 = tk.Entry(self, textvariable=n30).grid(row=6, column=2)

		se4 = tk.StringVar()
		mo4 = ttk.Combobox(self, textvariable=se4)
		mo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		mo4['state'] = 'normal'
		mo4.grid(row = 7, column = 0,padx = 5, pady = 5,sticky='W')
		self.n4= tk.StringVar()
		self.n4.set("0") 
		en4 = tk.Entry(self, textvariable=self.n4).grid(row=7, column=1)
		n40 = tk.StringVar() 
		en40 = tk.Entry(self, textvariable=n40).grid(row=7, column=2)

		def call_result_5_a(label_result_5_a, n0, n1,n2,n3,n4):
					result_5_a = int(n0.get())+int(n1.get())+int(n2.get())+int(n3.get())+int(n4.get())
					label_result_5_a.config(text="Result = %d" % result_5_a)
					return
						

		labelResult_5_a = tk.Label(self)
		labelResult_5_a.grid(row=8, column=1)
		call_result_5_a = partial(call_result_5_a, labelResult_5_a, self.n0,self.n1,self.n2,self.n3,self.n4)

		buttonCal = tk.Button(self, text="Calculate SUBTOTAL(KG)",command=call_result_5_a).grid(row = 8, column = 0,padx = 5, pady = 5,sticky='E')

		#B RECYCLED PACKAGING (POST-CONSUMER)

		label3 = ttk.Label(self, text ="B. RECYCLED PACKAGING (POST-CONSUMER)\n\nProduct, packaging, or associated component that can be diverted from the waste stream \nthrough available processes and programmes and can be collected, processed, and \nreturned to use in the form of raw materials or products.")
		label3.grid(row = 9, column = 0,padx = 5, pady = 5,sticky='W')

		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 10, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 10, column = 2,padx = 5, pady = 5)
		
		bse = tk.StringVar()
		bmo = ttk.Combobox(self, textvariable=bse)
		bmo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo['state'] = 'normal'
		bmo.grid(row = 11, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn0= tk.StringVar()
		self.bn0.set("0") 
		ben0 = tk.Entry(self, textvariable=self.bn0).grid(row=11, column=1)
		bn00 = tk.StringVar() 
		ben00 = tk.Entry(self, textvariable=bn00).grid(row=11, column=2)

		bse1 = tk.StringVar()
		bmo1 = ttk.Combobox(self, textvariable=bse1)
		bmo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo1['state'] = 'normal'
		bmo1.grid(row = 12, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn1= tk.StringVar()
		self.bn1.set("0") 
		ben1 = tk.Entry(self, textvariable=self.bn1).grid(row=12, column=1)
		bn10 = tk.StringVar() 
		ben10 = tk.Entry(self, textvariable=bn10).grid(row=12, column=2)

		bse2 = tk.StringVar()
		bmo2 = ttk.Combobox(self, textvariable=bse2)
		bmo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo2['state'] = 'normal'
		bmo2.grid(row = 13, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn2= tk.StringVar()
		self.bn2.set("0") 
		ben2 = tk.Entry(self, textvariable=self.bn2).grid(row=13, column=1)
		bn20 = tk.StringVar() 
		ben20 = tk.Entry(self, textvariable=bn20).grid(row=13, column=2)

		bse3 = tk.StringVar()
		bmo3 = ttk.Combobox(self, textvariable=bse3)
		bmo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo3['state'] = 'normal'
		bmo3.grid(row = 14, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn3 = tk.StringVar()
		self.bn3.set("0") 
		ben3 = tk.Entry(self, textvariable=self.bn3).grid(row=14, column=1)
		bn30 = tk.StringVar() 
		ben30 = tk.Entry(self, textvariable=bn30).grid(row=14, column=2)

		bse4 = tk.StringVar()
		bmo4 = ttk.Combobox(self, textvariable=bse4)
		bmo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		bmo4['state'] = 'normal'
		bmo4.grid(row = 15, column = 0,padx = 5, pady = 5,sticky='W')
		self.bn4= tk.StringVar()
		self.bn4.set("0") 
		ben4 = tk.Entry(self, textvariable=self.bn4).grid(row=15, column=1)
		bn40 = tk.StringVar() 
		ben40 = tk.Entry(self, textvariable=bn40).grid(row=15, column=2)

		def call_result_5_b(label_result_5_b,bn0,bn1,bn2,bn3,bn4):
					result_5_b = int(bn0.get())+int(bn1.get())+int(bn2.get())+int(bn3.get())+int(bn4.get())
					label_result_5_b.config(text="Result = %d" % result_5_b)
					return
						

		labelResult_5_b = tk.Label(self)
		labelResult_5_b.grid(row=16, column=1)
		call_result_5_b = partial(call_result_5_b, labelResult_5_b, self.bn0,self.bn1,self.bn2,self.bn3,self.bn4)

		buttonCal = tk.Button(self, text="Calculate SUBTOTAL(KG)",command=call_result_5_b ).grid(row = 16, column = 0,padx = 5, pady = 5,sticky='E')

		#C.Processing

		label3 = ttk.Label(self, text ="C. PLASTICS COMPOSTED\n\nA packaging or packaging component (1) is compostable if it is in compliance with relevant international compostability \nstandards (2) and if its successful post-consumer (3) collection, (sorting), and \ncomposting is proven to work in practice and at scale (4). See glossary for more info.")
		label3.grid(row = 17, column = 0,padx = 5, pady = 5,sticky='W')

		label2 = ttk.Label(self, text ="Weight(KG)")
		label2.grid(row = 18, column = 1,padx = 5, pady = 5)
		label3 = ttk.Label(self, text ="Source/Assumptions")
		label3.grid(row = 18, column = 2,padx = 5, pady = 5)
		
		cse = tk.StringVar()
		cmo = ttk.Combobox(self, textvariable=cse)
		cmo['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo['state'] = 'normal'
		cmo.grid(row = 19, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn0= tk.StringVar()
		self.cn0.set("0") 
		cen0 = tk.Entry(self, textvariable=self.cn0).grid(row=19, column=1)
		cn00 = tk.StringVar() 
		cen00 = tk.Entry(self, textvariable=cn00).grid(row=19, column=2)

		cse1 = tk.StringVar()
		cmo1 = ttk.Combobox(self, textvariable=cse1)
		cmo1['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo1['state'] = 'normal'
		cmo1.grid(row = 20, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn1= tk.StringVar()
		self.cn1.set("0") 
		cen1 = tk.Entry(self, textvariable=self.cn1).grid(row=20, column=1)
		cn10 = tk.StringVar() 
		cen10 = tk.Entry(self, textvariable=cn10).grid(row=20, column=2)

		cse2 = tk.StringVar()
		cmo2 = ttk.Combobox(self, textvariable=cse2)
		cmo2['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo2['state'] = 'normal'
		cmo2.grid(row = 21, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn2 = tk.StringVar()
		self.cn2.set("0") 
		cen2 = tk.Entry(self, textvariable=self.cn2).grid(row=21, column=1)
		cn20 = tk.StringVar() 
		cen20 = tk.Entry(self, textvariable=cn20).grid(row=21, column=2)

		cse3 = tk.StringVar()
		cmo3 = ttk.Combobox(self, textvariable=cse3)
		cmo3['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo3['state'] = 'normal'
		cmo3.grid(row = 22, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn3 = tk.StringVar()
		self.cn3.set("0") 
		cen3 = tk.Entry(self, textvariable=self.cn3).grid(row=22, column=1)
		cn30 = tk.StringVar() 
		cen30 = tk.Entry(self, textvariable=cn30).grid(row=22, column=2)

		cse4 = tk.StringVar()
		cmo4 = ttk.Combobox(self, textvariable=cse4)
		cmo4['values'] = ["Polyethylene Terephthalate (PET/PETE)","High-Density Polyethylene (HDPE)","Polyvinyl Chloride (PVC/Vinyl)","Low-Density Polyethylene (LDPE)","Polypropylene (PP)","Polystyrene (PS/Styrofoam)","others"]
		cmo4['state'] = 'normal'
		cmo4.grid(row = 22, column = 0,padx = 5, pady = 5,sticky='W')
		self.cn4= tk.StringVar()
		self.cn4.set("0")    
		cen4 = tk.Entry(self, textvariable=self.cn4).grid(row=23, column=1)
		cn40 = tk.StringVar() 
		cen40 = tk.Entry(self, textvariable=cn40).grid(row=23, column=2)

		def call_result_5_c(label_result_5_c, cn0,cn1,cn2,cn3,cn4):
					result_5_c = int(cn0.get())+int(cn1.get())+int(cn2.get())+int(cn3.get())+int(cn4.get())
					label_result_5_c.config(text="Result = %d" % result_5_c)
					return
						

		labelResult_5_c = tk.Label(self)
		labelResult_5_c.grid(row=24, column=1)
		call_result_5_c = partial(call_result_5_c, labelResult_5_c, self.cn0,self.cn1,self.cn2,self.cn3,self.cn4)

		buttonCal = tk.Button(self, text="Calculate SUBTOTAL(KG)",command=call_result_5_c ).grid(row = 24, column = 0,padx = 5, pady = 5,sticky='E')

		def call_result_5_d(label_result_5_d, n0, n1,n2,n3,n4,bn0,bn1,bn2,bn3,bn4,cn0,cn1,cn2,cn3,cn4):
					result_5_d = (int(n0.get())+int(n1.get())+int(n2.get())+int(n3.get())+int(n4.get())+int(bn0.get())+int(bn1.get())+int(bn2.get())+int(bn3.get())+int(bn4.get())+int(cn0.get())+int(cn1.get())+int(cn2.get())+int(cn3.get())+int(cn4.get()))/1000
					label_result_5_d.config(text="Result = %d" % result_5_d)
					return
						

		labelResult_5_d = tk.Label(self)
		labelResult_5_d.grid(row=25, column=1)
		call_result_5_d = partial(call_result_5_d, labelResult_5_d, self.n0,self.n1,self.n2,self.n3,self.n4,self.bn0,self.bn1,self.bn2,self.bn3,self.bn4,self.cn0,self.cn1,self.cn2,self.cn3,self.cn4)


		

		totrec = tk.Button(self, text="Calculate TOTAL REUSED/RECYCLED/COMPOSTED (MT)",command=call_result_5_d ).grid(row = 25, column = 0,padx = 5, pady = 5,sticky='E')

		def call_result_5_net(label_result_5_net, n0, n1,n2,n3,n4,bn0,bn1,bn2,bn3,bn4,cn0,cn1,cn2,cn3,cn4):
					result_5_net= (int(n0.get())+int(n1.get())+int(n2.get())+int(n3.get())+int(n4.get())+int(bn0.get())+int(bn1.get())+int(bn2.get())+int(bn3.get())+int(bn4.get())+int(cn0.get())+int(cn1.get())+int(cn2.get())+int(cn3.get())+int(cn4.get()))/1000
					plas=(controller.frames[PFC1_1].abc()+controller.frames[PFC2].abc()+controller.frames[PFC3].abc()+controller.frames[PFC4].abc())/1000

					result_5_net=plas-result_5_net
					label_result_5_net.config(text="Result = %d" % result_5_net)
					return

		

		labelResult_5_net= tk.Label(self)
		labelResult_5_net.grid(row=26, column=1)
		call_result_5_net = partial(call_result_5_net, labelResult_5_net, self.n0,self.n1,self.n2,self.n3,self.n4,self.bn0,self.bn1,self.bn2,self.bn3,self.bn4,self.cn0,self.cn1,self.cn2,self.cn3,self.cn4)


		plastnet = tk.Button(self, text="PLASTIC FOOTPRINT NET OF REUSED/RECYCLED PLASTIC (MT)  =  ", command=call_result_5_net).grid(row = 26, column = 0,padx = 5, pady = 5,sticky='E')

		button1 = ttk.Button(self, text ="Next",command = lambda : controller.show_frame(Dash))
		button1.grid(row = 27, column = 2, padx = 10, pady = 10)
		button2 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(PFC4))
		button2.grid(row = 27, column = 1, padx = 10, pady = 10)


	def abc(self):
	    self.result_ttl = int(self.n0.get())+int(self.n1.get())+int(self.n2.get())+int(self.n3.get())+int(self.n4.get())+int(self.bn0.get())+int(self.bn1.get())+int(self.bn2.get())+int(self.bn3.get())+int(self.bn4.get())+int(self.cn0.get())+int(self.cn1.get())+int(self.cn2.get())+int(self.cn3.get())+int(self.cn4.get())
	    return self.result_ttl

class Dash(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="DASHBOARD", font = "Circular",foreground="white",background="green")
		label.grid(row = 0, column =4, padx = 10, pady = 10)

		label = ttk.Label(self, text ="Plastic Input to Production of \nGoods/Rendering Services", font = "Circular")
		label.grid(row = 2, column =1, padx = 10, pady = 10)

		label = ttk.Label(self, text ="Plastics Used in\nLogistics/Shipping", font = "Circular")
		label.grid(row = 2, column =2, padx = 10, pady = 10)

		label = ttk.Label(self, text ="Plastic Used Directly for \nAdvertising & Promotions", font = "Circular")
		label.grid(row = 2, column =3, padx = 10, pady = 10)

		label = ttk.Label(self, text ="Plastic Used for \nGeneral & Administrative Activities", font = "Circular")
		label.grid(row = 2, column =4, padx = 10, pady = 10)

		label = ttk.Label(self, text ="Plastic Reused/ Recycled/Composted", font = "Circular")
		label.grid(row = 2, column =5, padx = 10, pady = 10)

		def gen_rep(labelp1,labelp2,labelp3,labelp4,labelpr,labelrep,labelrep2):
					labelp1.config(text="= %d KG" %controller.frames[PFC1_1].abc() )
					labelp2.config(text="= %d KG" %controller.frames[PFC2].abc() )
					labelp3.config(text="= %d KG" %controller.frames[PFC3].abc() )
					labelp4.config(text="= %d KG" %controller.frames[PFC4].abc() )
					labelpr.config(text="= %d KG" %controller.frames[PFC5].abc() )
					ttlplas=(controller.frames[PFC1_1].abc()+controller.frames[PFC2].abc()+controller.frames[PFC3].abc()+controller.frames[PFC4].abc())/1000
					ttlrec=controller.frames[PFC5].abc()/1000
					net=ttlplas-ttlrec
					lis=controller.frames[PFC].abc()
					labelrep2.config(text="The GROSS Plastic Footprint for "+lis[0]+" is\n"+str(ttlplas)+" MT.\n\n The NET Footprint for "+lis[0]+" is\n"+str(net)+" MT.\n\n For the duration "+lis[3])
					if lis[1]=="Plastic Negative":
						net=net*2
					labelrep.config(text= lis[0]+" will need "+ str(net)+" MT of Plastic Credits to be "+ lis[1]+"."  )
					return

		


		labelp1 = tk.Label(self)
		labelp1.grid(row = 3, column = 1, padx = 10, pady = 10)

		labelp2 = tk.Label(self)
		labelp2.grid(row = 3, column = 2, padx = 10, pady = 10)

		labelp3 = tk.Label(self)
		labelp3.grid(row = 3, column = 3, padx = 10, pady = 10)

		labelp4 = tk.Label(self)
		labelp4.grid(row = 3, column = 4, padx = 10, pady = 10)
		
		labelpr = tk.Label(self)
		labelpr.grid(row = 3, column = 5, padx = 10, pady = 10)

		labelrep2 = tk.Label(self,foreground="white",background="green")
		labelrep2.grid(row = 4, column = 3,sticky='W')

		labelrep = tk.Label(self,foreground="white",background="green")
		labelrep.grid(row = 5, column = 3, sticky='S')
		
		button1 = ttk.Button(self, text ="Back",command = lambda : controller.show_frame(PFC5))
		button1.grid(row = 7, column = 1, padx = 10, pady = 10)

		gen_rep=partial(gen_rep,labelp1,labelp2,labelp3,labelp4,labelpr,labelrep,labelrep2)

		button2 = ttk.Button(self, text ="Generate Report",command = gen_rep)
		button2.grid(row = 1, column = 4, padx = 10, pady = 10)



# Driver Code
app = tkinterApp()
app.title("Plastic Footprint Calculator")
app.mainloop()
