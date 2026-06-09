def view_reports():
    with open ("reports.txt", "r") as f:
        print(f.read())


def save_report(idea_name, score, rating, strength_text, weakness_text):

    report = f"""
    Idea Name : {idea_name}
    Score : {score}
    Rating : {rating}

    Strengths:
    {strength_text}

    Weaknesses:
    {weakness_text}

    ----------------------------------------
    """

    with open("reports.txt", "a") as f:
        f.write(report)

    print("\nReport Saved Successfully!")
    

