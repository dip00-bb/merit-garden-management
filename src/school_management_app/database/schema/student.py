STUDENT_SCHEMA = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- Personal Information
    student_name TEXT NOT NULL,
    mother_name TEXT,
    father_name TEXT,
    date_of_birth TEXT,
    gender TEXT,
    phone_number TEXT,
    whats_app_number TEXT,
    email TEXT,
    blood_group TEXT,
    religion TEXT,

    -- Present Address
    present_division TEXT,
    present_district TEXT,
    present_upazila TEXT,
    present_address TEXT,

    -- Permanent Address
    permanent_division TEXT,
    permanent_district TEXT,
    permanent_upazila TEXT,
    permanent_address TEXT,

    -- Admission Information
    to_admit TEXT,
    group_name TEXT,
    optional_subject TEXT,
    previous_school TEXT,

    -- System Information
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""