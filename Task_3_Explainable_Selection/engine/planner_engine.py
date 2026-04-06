def generate_daily_plan(data, burnout_score):

    plan = []

    if burnout_score > 65:
        plan.append("Study max 4-5 hours today")
        plan.append("Take breaks every 45 minutes")
        plan.append("Sleep at least 7-8 hours")

    elif burnout_score > 35:
        plan.append("Maintain balanced study schedule")
        plan.append("Revise weak topics")

    else:
        plan.append("Continue current routine")

    return plan