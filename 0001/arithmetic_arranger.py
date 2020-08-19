def arithmetic_arranger(answers=False):
    add_string = []
    while True:
        split_numbs = numbers()
        if type(split_numbs) == int:
            print("Invalid entry")
            continue
        else:
            for number in split_numbs:
                add_string.append(number)
            keep_adding = input("Would you like to add another two numbers?:(y/n) ").strip().lower()
            if keep_adding == 'y':
                continue
            elif keep_adding == 'n':
                break
            else:
                print("Invalid Entry")
                continue



def numbers():
    numbs = input("Which two numbers would you like to add?: ").strip()
    if len(numbs) > 2:
        split_numbs = numbs.split()
        if len(split_numbs) == 2:
            try:
                int(split_numbs[0])
                int(split_numbs[1])
                return split_numbs
            except:
                return 0
        else:
            return 0