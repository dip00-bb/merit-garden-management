def check_valid_name(
    field,
    field_name,
    lower_bound,
    upper_bound,
    
    ):
    
    if len(field) < lower_bound:
        print(f"{field_name} Must have {lower_bound} character")
        raise ValueError(
            f"{field_name} Must have {lower_bound} character"
        )
    
    elif len(field) > upper_bound:
        print(f"{field_name} Can not have more than {upper_bound} character")
        raise ValueError(
            f"{field_name} Can not have more than {upper_bound} character"
        )
    
    
    