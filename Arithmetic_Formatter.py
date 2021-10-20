def arithmetic_arranger(problems, flag = False):

    firstline = ""
    secondline = ""
    lines = ""
    sumx = ""
    count = 0

    for problem in problems:
        firstnumber = problem.split()[0]
        secondnumber = problem.split()[2]
        operator = problem.split()[1]

        operator_flag = False

        if operator == "+":
            operator_flag = True
        elif operator == "-":
            operator_flag = True            
        else:
            operator_flag = False
            return ("Error: Operator must be '+' or '-'.")

        try: 
            firstnumber = int(firstnumber)
            secondnumber = int(secondnumber)
        except:
            return("Error: Numbers must only contain digits.")
        
        if firstnumber > 9999 or secondnumber > 9999:
            return("Error: Numbers cannot be more than four digits.")

        count = count + 1

        sum = ""
        
        if operator =="+":
            sum = firstnumber+secondnumber
        elif operator =="-":
            sum = firstnumber-secondnumber
        
        # print (sum)

        lenght = max(len(str(firstnumber)),len(str(secondnumber))) + 2
        
        top = "" + str(firstnumber).rjust(lenght)
        bottom = operator + str(secondnumber).rjust(lenght-1)
        line = ""
        s = str(sum).rjust(lenght)

        for i in range(lenght):
            line += "-"

        firstline = firstline + top + "    "
        secondline = secondline + bottom + "    "
        lines = lines + line + "    "
        sumx = sumx + s + "    "
    
    if count>5:
        return("Error: Too many problems.")

    if flag:
        solution = firstline.rstrip() + '\n' + secondline.rstrip() + '\n' + lines.rstrip() + '\n' + sumx.rstrip()
        return solution
    else:
        solution = firstline.rstrip() + '\n' + secondline.rstrip() + '\n' + lines.rstrip()
        return solution

        


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
