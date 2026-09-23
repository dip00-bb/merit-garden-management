STUDENT_FEE="""
CREATE TABLE IF NOT EXISTS student_fee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    
    student_id INTEGER NOT NULL,
    
    admission_fee TEXT,
    monthly_fee TEXT,
    total_fee TEXT,
    paid_fee TEXT DEFAULT '0',
    due_fee TEXT,
    academic_year TEXT,
    
    
    january_fee_status TEXT DEFAULT 'unpaid',
    february_fee_status TEXT DEFAULT 'unpaid',
    march_fee_status TEXT DEFAULT 'unpaid',
    april_fee_status TEXT DEFAULT 'unpaid',
    may_fee_status TEXT DEFAULT 'unpaid',
    june_fee_status TEXT DEFAULT 'unpaid',
    july_fee_status TEXT DEFAULT 'unpaid',
    august_fee_status TEXT DEFAULT 'unpaid',
    september_fee_status TEXT DEFAULT 'unpaid',
    october_fee_status TEXT DEFAULT 'unpaid',
    november_fee_status TEXT DEFAULT 'unpaid',
    december_fee_status TEXT DEFAULT 'unpaid',
    
    first_term_fee_status TEXT DEFAULT 'unpaid',
    half_yearly_fee_status TEXT DEFAULT 'unpaid',
    annual_fee_status TEXT DEFAULT 'unpaid',
    
    
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
    
    
    FOREIGN KEY (student_id) REFERENCES students(student_id) 
    
)
"""