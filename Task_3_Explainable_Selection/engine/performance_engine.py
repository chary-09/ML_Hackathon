def analyze_performance(performance, burnout):

    if burnout == "High" and performance > 70:
        return "High performer but overworking"

    elif burnout == "High" and performance < 50:
        return "High burnout with low output → inefficient study"

    elif burnout == "Low" and performance < 50:
        return "Low burnout but low productivity"

    else:
        return "Balanced performance"


def classify_student(performance, burnout):

    if burnout == "High" and performance > 70:
        return "Overworker"

    elif burnout == "High":
        return "Underperformer"

    else:
        return "Balanced Student"