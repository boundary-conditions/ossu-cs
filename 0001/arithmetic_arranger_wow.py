"""
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
**If there are too many problems supplied to the function. The limit is five, anything more will return:
**Error: Too many problems.
**The appropriate operators the function will accept are addition and subtraction. Multiplication and division **will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error **returned will be:
**Error: Operator must be '+' or '-'.
**Each number (operand) should only contain digits. Otherwise, the function will return:
**Error: Numbers must only contain digits.
**Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error **string returned will be:
**Error: Numbers cannot be more than four digits.
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
Development
Write your code in arithmetic_arranger.py. For development, you can use main.py to test your arithmetic_arranger() function. Click the "run" button and main.py will run.

Testing
The unit tests for this project are in test_module.py. We imported the tests from test_module.py to main.py for your convenience. The tests will run automatically whenever you hit the "run" button.
"""
#["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]



def arithmetic_arranger(problems_list, answers=False):
    output_list = []
    top_numbers = []
    operands = []
    bottom_numbers = []
    adjusted_top_numbers = []
    adjusted_operands = []
    adjusted_bottom_numbers =[]
    answers_list = []
    if len(problems_list) > 5:
        return "Error: too many problems"
    for problem in problems_list:
        problem = problem.split()
        try:
            int(problem[0])   
            int(problem[2])    
        except:
            return "Error: Numbers must only contain digits"
        if len(problem) != 3 or len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits"
        elif problem[1] != '+' and problem[1] != '-':
            return "Error: Operator must be '+' or '-'"
        #end of error checking

        output_list.append(problem[0])
        output_list.append(problem[1])
        output_list.append(problem[2])
        top_numbers.append(problem[0])
        operands.append(problem[1])
        bottom_numbers.append(problem[2])

    number_of_problems = int(len(output_list) / 3)

    #define answers and store in list

    i = 0
    while i < number_of_problems:
        x = int(output_list.pop(0))
        op = output_list.pop(0)
        y = int(output_list.pop(0))
        if op == '+':
            answer = x + y
        else:
            answer = x - y
        answers_list.append(answer)
        i += 1

    #Operand spacing

    for i in range(number_of_problems):
        if i == 0:
            adjusted_operands.append(operands[i])
            continue
        adjusted_operand = operands[i].rjust(5)
        adjusted_operands.append(adjusted_operand)
    
    #spacing for top numbers

    for i in range(number_of_problems):
        top_length = len(top_numbers[i])
        bottom_length = len(bottom_numbers[i])
        if i == 0:
            if top_length < bottom_length:
                adjusted_top_number = top_numbers[i].rjust(bottom_length + 2)
                adjusted_top_numbers.append(adjusted_top_number)
            elif top_length >= bottom_length:
                adjusted_top_number = top_numbers[i].rjust(top_length + 2) #check
        else:
            if top_length < bottom_length: #check
                adjusted_top_number = top_numbers[i].rjust(bottom_length + 6)
                adjusted_top_numbers.append(adjusted_top_number)
            elif top_length >= bottom_length:
                adjusted_top_number = top_numbers[i].rjust(top_length + 6) #check
                adjusted_top_numbers.append(adjusted_top_number)

    #spacing the bottom numbers, could combine with top numbers

    for i in range(number_of_problems):
        top_length = len(top_numbers[i])
        bottom_length = len(bottom_numbers[i])
        if top_length <= bottom_length:
            adjusted_bottom_number = bottom_numbers[i].rjust(bottom_length + 1)
            adjusted_bottom_numbers.append(adjusted_bottom_number)
        elif top_length > bottom_length:
            adjusted_bottom_number = bottom_numbers[i].rjust(top_length + 1)
            adjusted_bottom_numbers.append(adjusted_bottom_number)  

    bottom_line = []
    for i in range(number_of_problems):
        bottom_line.append(adjusted_operands[i])
        bottom_line.append(adjusted_bottom_numbers[i])

    #final print statements are long long long
    if answers == False:
        if number_of_problems == 5:
            print(f"{adjusted_top_numbers[0]}{adjusted_top_numbers[1]}{adjusted_top_numbers[2]}{adjusted_top_numbers[3]}{adjusted_top_numbers[4]}\n{bottom_line[0]}{bottom_line[1]}{bottom_line[2]}{bottom_line[3]}{bottom_line[4]}{bottom_line[5]}{bottom_line[6]}{bottom_line[7]}{bottom_line[8]}{bottom_line[9]}\n{len(bottom_line[0] + bottom_line[1])*'-'}    -{len(bottom_line[3])*'-'}    -{len(bottom_line[5])*'-'}    -{len(bottom_line[7])*'-'}    -{len(bottom_line[9])*'-'}")
        elif number_of_problems == 4:
            print(f"{adjusted_top_numbers[0]}{adjusted_top_numbers[1]}{adjusted_top_numbers[2]}{adjusted_top_numbers[3]}\n{bottom_line[0]}{bottom_line[1]}{bottom_line[2]}{bottom_line[3]}{bottom_line[4]}{bottom_line[5]}{bottom_line[6]}{bottom_line[7]}\n{len(bottom_line[0] + bottom_line[1])*'-'}    -{len(bottom_line[3])*'-'}    -{len(bottom_line[5])*'-'}    -{len(bottom_line[7])*'-'}")
        elif number_of_problems == 3:
            print(f"{adjusted_top_numbers[0]}{adjusted_top_numbers[1]}{adjusted_top_numbers[2]}\n{bottom_line[0]}{bottom_line[1]}{bottom_line[2]}{bottom_line[3]}{bottom_line[4]}{bottom_line[5]}\n{len(bottom_line[0] + bottom_line[1])*'-'}    -{len(bottom_line[3])*'-'}    -{len(bottom_line[5])*'-'}")
        elif number_of_problems == 2:
            print(f"{adjusted_top_numbers[0]}{adjusted_top_numbers[1]}\n{bottom_line[0]}{bottom_line[1]}{bottom_line[2]}{bottom_line[3]}\n{len(bottom_line[0] + bottom_line[1])*'-'}    -{len(bottom_line[3])*'-'}")
        elif number_of_problems == 1:
            print(f"{adjusted_top_numbers[0]}\n{bottom_line[0]}{bottom_line[1]}\n{len(bottom_line[0] + bottom_line[1])*'-'}")
    else:
        if number_of_problems == 5:
            print(f"{adjusted_top_numbers[0]}{adjusted_top_numbers[1]}{adjusted_top_numbers[2]}{adjusted_top_numbers[3]}{adjusted_top_numbers[4]}\n{bottom_line[0]}{bottom_line[1]}{bottom_line[2]}{bottom_line[3]}{bottom_line[4]}{bottom_line[5]}{bottom_line[6]}{bottom_line[7]}{bottom_line[8]}{bottom_line[9]}\n{len(bottom_line[0] + bottom_line[1])*'-'}    -{len(bottom_line[3])*'-'}    -{len(bottom_line[5])*'-'}    -{len(bottom_line[7])*'-'}    -{len(bottom_line[9])*'-'}")

    
    
    


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 430", "123 + 49", "4567 + 1"])
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 430", "123 + 49"])
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 430"])
arithmetic_arranger(["32 + 698", "3801 - 2"])
arithmetic_arranger(["32 + 698"])

