def main():

    score = float(input("Enter score: "))
    print(check_status(score))


def check_status(score):

    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Not good at all, WORK HARD"


main()