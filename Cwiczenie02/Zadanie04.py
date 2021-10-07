def celc_to_other(temp, temp_type):
    if temp_type == "F":
        return (9 * temp) / 5 + 32
    elif temp_type == "K":
        return temp + 273
    elif temp_type == "R":
        return (temp + 273.15) * 1.8
    else:
        return None
