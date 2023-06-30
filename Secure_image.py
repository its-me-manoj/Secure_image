import customtkinter as ctk

class Secure_Image(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x200+50+50')
        self.title("Secure_Image")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        frame = ctk.CTkFrame(self,width=370,height=170)
        frame.grid(padx=15,pady=15,sticky="NSEW")
        
        title_1 = ctk.CTkLabel(frame,text="Secure Image",font=('Arial',20))
        title_1.grid(row=0,column=0,padx=115,pady=10)
        
        btn_img_sel = ctk.CTkButton(frame,text='Choose an Image',command=self.choose)
        btn_img_sel.grid(row=1,column=0,padx=115,pady=10)
        
    def choose(self):
        global fi,keys,file_1
        file_1 = ctk.filedialog.askopenfile(mode='r',filetypes=[('JPG File', '*.jpg'),('PNG File', '*.png')])
        if file_1 is not None:
            img_org = open(file_1.name,'rb')
            fi = img_org.read()
            img_org.close()
            
            new_window = ctk.CTkToplevel(self)
            new_window.title("Encrypt or Decrypt")
            new_window.geometry('350x155')
            new_window.grab_set()
            
            new_label = ctk.CTkLabel(new_window, text="Do you want to encrypt or decrypt?")
            new_label.grid(row=0,column=0,pady=10,padx=35,columnspan=2)
            
            keys = ctk.CTkEntry(new_window,placeholder_text='Enter the key')
            keys.grid(row=1,column=0,padx=35,pady=10,columnspan=2)
            
            btn_en = ctk.CTkButton(new_window,text="Encrypt",command=self.en_or_de)
            btn_en.grid(row=2,column=0,padx=20,pady=10)
            
            btn_en = ctk.CTkButton(new_window,text="Decrypt",command=self.en_or_de)
            btn_en.grid(row=2,column=1,padx=20,pady=10)
            
    def en_or_de(self):
        passwd = int(keys.get())
        img_val = bytearray(fi)
        for i,val in enumerate(fi):
            img_val[i] = val^(passwd % 256)
        enc_img = open(file_1.name,'wb') 
        enc_img.write(img_val)
        enc_img.close()
        
        
            
img = Secure_Image()
img.mainloop()