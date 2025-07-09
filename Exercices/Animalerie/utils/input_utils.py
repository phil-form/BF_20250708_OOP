from datetime import datetime

def read_int(msg):
    ret_val = None
    while not ret_val:
        try:
            ret_val = int(input(msg))
        except:
            print("ENter an integer")

    return ret_val

def read_str(msg):
    return input(msg)

def read_bool(msg):
    print(msg)
    choice = input("Entrez O/N")

    if(choice in ["O", "N", "o", "n"]):
        return True if choice == "O" or choice == "o" else False
    else:
        return read_bool(msg)

def read_date(msg):
    try:
        return datetime.strptime(input(msg + " (au format dd/mm/yyyy)"), "%d/%m/%y")
    except:
        return read_date(msg)
