def arithmetic_arranger(problems, show_answer=False):

    # first error for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # dict for operators to find false operators
    ops = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y)}

    # first line for first numbers
    line1 = []
    # second line for operator and second number
    line2 = []
    # third line for dashes
    dashes = []
    # final line for answer
    answers = []

    # a list to separate firstNum, secondNum and operators form the problems list(argument above)
    problem = []
    for i in problems:
        problem.append(i.split())  # split it using spacing in between

    for i in problem:

        # second error for false operators
        if i[1] not in ops.keys():
            return "Error: Operator must be '+' or '-'."

        # third error for numbers containing alphabets
        if not str(i[0]).isnumeric() or not str(i[2]).isnumeric():
            return "Error: Numbers must only contain digits."

        # last error for number with more than 4 digits
        if len(i[0]) > 4 or len(i[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # alignment for all the lines(using firstNum)
        align = len(i[0]) + 2
        # if secondNum is longer
        if len(i[0]) < len(i[2]):
            align = len(i[2]) + 2

        line1.append(str(i[0]).rjust(align))  # first line

        second_line = i[1] + i[2].rjust(align - 1)
        line2.append(str(second_line))  # second line

        dash = align * "-"
        dashes.append(str(dash))  # third line

        ans = ops[i[1]](int(i[0]), int(i[2]))
        answers.append(str(ans).rjust(align))  # final line

    # the spacing between the 4 arithmetic problems
    line1_string = "    ".join(line1)
    line2_string = "    ".join(line2)
    dashes_string = "    ".join(dashes)
    answer_string = "    ".join(answers)

    final = [line1_string, line2_string, dashes_string, answer_string]

    # if second arg is not True don't show the answer
    if not show_answer:
        final.pop()

    # for every line to end in a new line(so that the four line won't print on the same line)
    # makes the arithmetic calculator display vertically
    output = "\n".join(final)

    return output
