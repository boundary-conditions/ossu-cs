def arithmetic_arranger(str, answers=False):
    add_string = []
    numbs = input("Which two numbers would you like to add?: ").strip()
    if len(numbs) > 2:
        split_numbs = numbs.split()
        if len(split_numbs) == 2:
            for number in split_numbs:
                add_string.append(number)
        else:
            print("Invalid entry")
            return