try :
    raise ValueError("invalid input")
except ValueError as e :
    e.add_note("please make sure the input is numeric")
    raise