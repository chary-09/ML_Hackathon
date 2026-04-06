def generate_insights(data):
    insights = []

    if data["attendance"] < 60:
        insights.append("Low attendance is increasing burnout risk")

    if data["study_hours"] > 8:
        insights.append("Excessive study hours causing fatigue")

    if data["assignment_delay"] > 3:
        insights.append("Frequent assignment delays indicate overload")

    if data["lms_usage"] < 2:
        insights.append("Low LMS engagement affecting learning")

    if data["performance"] < 50:
        insights.append("Low academic performance detected")

    return insights