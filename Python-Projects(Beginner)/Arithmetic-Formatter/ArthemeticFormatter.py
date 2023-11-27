def arithmetic_arranger(problems: str, answers: bool=False) -> str:
    """ Returns the problems arranged vertically and side-by-side. """

    # Error handling
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        problem = problem.split()

        if problem[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        elif not problem[0].isnumeric() or not problem[2].isnumeric():
            return "Error: Numbers must only contain digits."
        elif len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Rearrange functionality
    arranged_problems = ""
    line_one = []
    line_two = []
    line_three = []
    problem_answers = []
    between = " " * 4

    for problem in problems:
        problem = problem.split()

        # Determine what's the largest digit
        largest = ""
        if len(problem[0]) > len(problem[2]):
            largest = problem[0]
        elif len(problem[0]) < len(problem[2]):
            largest = problem[2]
        else:
            largest = problem[0]

        dashes = "-" * (len(largest) + 2)

        # "Space" refers to blank spaces
        spaces_one = ""
        spaces_two = ""
        if largest == problem[0]:
            spaces_one = " " * 2
            spaces_two = " " * (len(largest) - len(problem[2]))
        elif largest != problem[0]:
            spaces_one = " " * ((len(largest) + 2) - len(problem[0]))

        # Line formatting
        line_one.append(f"{spaces_one}{problem[0]}")
        line_two.append(f"{problem[1]} {spaces_two}{problem[2]}")
        line_three.append(f"{dashes}")

        result = eval(f"{problem[0]}{problem[1]}{problem[2]}")
        spaces_three = " " * (len(dashes) - len(str(result)))
        
        problem_answers.append(f"{spaces_three}{result}")

    arranged_problems = (
        f"{between.join(line_one)}\n"
        f"{between.join(line_two)}\n"
        f"{between.join(line_three)}"
    )

    # If `answers` is True, print the answers; otherwise delete the variable
    if answers:
        arranged_problems += f"\n{between.join(problem_answers)}"
    else:
        del problem_answers

    return arranged_problems