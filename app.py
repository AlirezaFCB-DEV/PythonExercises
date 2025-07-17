try : 1 / 0
except ZeroDivisionError as e:
    raise ValueError("Something Went Wrong!!") from e
