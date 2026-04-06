def generate_recommendations(insights, burnout_score):
    rec = []

    if burnout_score > 65:
        rec.append("Take regular breaks")
        rec.append("Reduce workload")

    elif burnout_score > 35:
        rec.append("Maintain balance and improve routine")

    else:
        rec.append("Keep maintaining your current routine")

    for i in insights:
        if "attendance" in i.lower():
            rec.append("Improve attendance consistency")

        if "study hours" in i.lower():
            rec.append("Use Pomodoro technique (25-5 method)")

        if "assignment" in i.lower():
            rec.append("Follow a structured timetable")

        if "performance" in i.lower():
            rec.append("Focus on concept clarity and revision")

    return list(set(rec))