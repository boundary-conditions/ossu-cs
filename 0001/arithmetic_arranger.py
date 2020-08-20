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
    top_number = []
    operands = []
    bottom_number = []
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
        top_number.append(problem[0])
        operands.append(problem[1])
        bottom_number.append(problem[2])
    
    print(bottom_number)

    for i in range(4):    
        if len(top_number[i]) >= len(bottom_number[i]):
            if i == 0:
                top_number[i] = top_number[i].rjust(len(top_number[i])+2)
                bottom_number[i] = bottom_number[i].rjust(len(top_number[i])-len(bottom_number[i])+1)
            else:
                top_number[i] = top_number[i].rjust(len(top_number[i])+6)
                operands[i] = operands[i].rjust(5)
                bottom_number[i] = bottom_number[i].rjust(len(top_number[i])-len(bottom_number[i])+1)
        elif len(top_number[i]) < len(bottom_number[i]):
            if i == 0:
                top_number[i] = top_number[i].rjust(len(bottom_number[i])-len(top_number[i])+2)
                bottom_number[i] = bottom_number[i].rjust(len(bottom_number[i])+1)
            else:
                top_number[i] = top_number[i].rjust(len(bottom_number[i])-len(top_number[i])+6)
                operands[i] = operands[i].rjust(5)
                bottom_number[i] = bottom_number[i].rjust(len(bottom_number[i])+1)
            

    output = ' '
    for i in top_number:
        output = output + i
    output = output + '\n'
    output = output + operands[0] + bottom_number[0] + f'{operands[1]}' + bottom_number[1]
    
    print(output)
    print(top_number)
    print(bottom_number)
    print(operands)

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])