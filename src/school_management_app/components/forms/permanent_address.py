import customtkinter as ctk 
from ...utilitis import grid_widget,show_grid
from ...utilitis import heading_text_color,heading_color,text_color
from ...utilitis import bangladesh

class PermanentAddress(ctk.CTkFrame):
    def __init__(self,parent,present_address_component,**kwargs):
        super().__init__(parent,**kwargs)
        
        for i in range(12):
            self.grid_columnconfigure(i,weight=1)
        for i in range(3):
            self.grid_rowconfigure(i,weight=1)  
              
            

        self.divisions=list(bangladesh.keys())
        self.selected_division=None
        
        # variable to hold division value
        self.value_of_permanent_division=ctk.StringVar(value="sylhet")
        
        # variable to hold the value of district
        self.value_of_permanent_district=ctk.StringVar(value=None)
        
        # variable to hold the value of upazila 
        self.value_of_permanent_upazila=ctk.StringVar(value=None)        
        
        # variable to hold the value of address
        self.value_of_permanent_address=ctk.StringVar(value="")  
        
        
        #present_address_component_to_collect_present_address_information   
        self.present_address=present_address_component
        
        self.permanent_address_section_label= ctk.CTkLabel(self,text="Permanent Address",anchor="center",font=("Arial",20),bg_color=heading_color,text_color=heading_text_color)
        grid_widget(entry=self.permanent_address_section_label,c=1,r=0,colspan=8,rowspan=1,direction="we",px=0,py=10)  
        
        # self.permanent_permanent_same_check= ctk.CTkCheckBox(self,text="Same As permanent",font=("Arial",20),text_color=text_color)
        # grid_widget(entry=self.permanent_permanent_same_check,c=5,r=0,colspan=8,rowspan=1,direction="e",px=320,py=10)   
         
        self.student_permanent_division_label= ctk.CTkLabel(self,text="Division:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_division_label,c=0,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_permanent_division_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),variable=self.value_of_permanent_division,command=self.on_division_change,font=("Arial", 18))
        grid_widget(entry=self.student_permanent_division_option,c=1,r=1,colspan=2,rowspan=1,direction="we",px=5,py=10)
        self.student_permanent_division_option.set("Division")
        
        self.student_permanent_district_label= ctk.CTkLabel(self,text="District:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_district_label,c=3,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_permanent_district_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),variable=self.value_of_permanent_district,command=self.on_district_change,font=("Arial", 18),state="disabled")
        grid_widget(entry=self.student_permanent_district_option,c=4,r=1,colspan=2,rowspan=1,direction="we",px=0,py=10)
        self.student_permanent_district_option.set("District")        
        self.student_permanent_upazila_label= ctk.CTkLabel(self,text="Upazila:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_upazila_label,c=6,r=1,colspan=1,rowspan=1,direction="we",px=5,py=10) 
        
        self.student_permanent_upazila_option= ctk.CTkOptionMenu(self,values= self.divisions,dropdown_font=("Arial", 18),command=self.on_upazila_change, font=("Arial", 18),variable=self.value_of_permanent_upazila,state="disabled")
        grid_widget(entry=self.student_permanent_upazila_option,c=7,r=1,colspan=2,rowspan=1,direction="we",px=0,py=10)
        self.student_permanent_upazila_option.set("Upazila")
        
        self.student_permanent_address_label= ctk.CTkLabel(self,text="Address:",anchor="e",font=("Arial",20),text_color=text_color)
        grid_widget(entry=self.student_permanent_address_label,c=0,r=2,colspan=1,rowspan=1,direction="we",px=5,py=10)
        
        self.student_permanent_address_entry= ctk.CTkEntry(self,font=("Arial",20),textvariable=self.value_of_permanent_address)
        grid_widget(entry=self.student_permanent_address_entry,c=1,r=2,colspan=8,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)
        
        self.submit_information=ctk.CTkCheckBox(self,text="Same As Present",command=lambda:self.collect_present_address_info(self.present_address))
        grid_widget(entry=self.submit_information,c=1,r=3,colspan=1,rowspan=1,direction="we",px=0,py=10,ipadx=0,ipady=5)
        
    def on_division_change(self,chosen_division):
        self.selected_division=chosen_division
        self.student_permanent_district_option.set("District")
        self.student_permanent_district_option.configure(values=list(bangladesh[chosen_division].keys()),state="enabled")
        
    def on_district_change(self,chosen_district):
        self.student_permanent_upazila_option.set("Upazila")
        self.student_permanent_upazila_option.configure(values=list(bangladesh[self.selected_division][chosen_district]),state="enabled")    
        
    def on_upazila_change(self,choosen_upazila):
        
        print(choosen_upazila)
        print( self.value_of_permanent_division.get())
        print( self.value_of_permanent_district.get())
        print(self.value_of_permanent_upazila.get())
        
    def collect_present_address_info(self,component):
        print("I am from permanent address",component.present_address_dictionary)
        present_address_info=component.present_address_dictionary
        
        self.student_permanent_division_option.set(present_address_info["present_division"])
        self.student_permanent_division_option.configure(state="disabled")
        
        print(":::::::::",present_address_info["present_district"])
        self.student_permanent_district_option.set(present_address_info["present_district"])
        self.student_permanent_district_option.configure(state="disabled")
        
        self.student_permanent_upazila_option.set(present_address_info["present_upazila"])
        self.student_permanent_upazila_option.configure(state="disabled")
        
        
        self.student_permanent_address_entry.insert(0,present_address_info["present_address"])
        self.student_permanent_address_entry.configure(state="disabled")
        