import customtkinter as ctk
from .....components import ManageFeeTable
class ManageFee(ctk.CTkFrame):
    def __init__(self, parent, student_id,fees_repo, **kwargs):
        super().__init__(parent, bg_color="lightgray", **kwargs)
        self.pack_propagate(False)
        self.student_id = student_id
        self.fees_repo = fees_repo

        fees_information = self.fees_repo.find_fees_information(student_id)
        
        fetched_fees= [dict(fee) for fee in fees_information]
        print(fetched_fees)
        
        for fee in fetched_fees:
            self.manage_fee_table=ManageFeeTable(self,fee=fee)
            self.manage_fee_table.pack(pady=10,padx=20,fill="x")
        print(f"Manage Fee Frame for Student ID: {self.student_id}")
        
        