class StartupIdeaValidator:
    def __init__(self, idea):
        self.idea = idea
    
    def calculate_score(self):
        score = 0
        for x in self.idea:

            if x != "budget":
                if self.idea[x]:
                    score += 20
            
        if self.idea["budget"] > 10000:
            score += 20

        return score 

    def get_rating(self, score):

        if score >= 80:
            rating = "Excellent"

        elif score >= 60:
            rating = "Good"

        elif score >= 40:
            rating = "Average"

        else:
            rating = "Weak"

        return rating

    def analyze_idea(self):
        strengths = []
        weaknesses = []

        for key in self.idea:

            if key != "budget":

                if self.idea[key]:

                    if key == "name":
                        strengths.append("Idea name provided")

                    elif key == "problem":
                        strengths.append("Problem clearly defined")

                    elif key == "audience":
                        strengths.append("Target audience identified")

                    elif key == "revenue_model":
                        strengths.append("Revenue model present")

                else:

                    if key == "name":
                        weaknesses.append("Idea name missing")

                    elif key == "problem":
                        weaknesses.append("Problem statement missing")

                    elif key == "audience":
                        weaknesses.append("Target audience missing")

                    elif key == "revenue_model":
                        weaknesses.append("Revenue model missing")
                    
        if self.idea["budget"] > 10000:
            strengths.append("Sufficient budget")
        else:
            weaknesses.append("Budget is too low")

        if len(strengths) == 0:
            strengths.append("None")

        if len(weaknesses) == 0:
            weaknesses.append("None")

        return strengths, weaknesses


