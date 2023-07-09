import random



class Umpire:
    def __init__(self,team1,team2):
        self.scores = {f"{team1.name}": 0, f"{team2.name}": 0}
        self.wickets = {f"{team1.name}": 0, f"{team2.name}": 0}
        self.overs = 0
    
    def predict_outcome(self, bowler, batsman, fielders,field):
        batting_prob = batsman.batting * random.uniform(0.8, 1.2)  # Adjusted with some randomness
        bowling_prob = bowler.bowling * random.uniform(0.8, 1.2)
        running_prob = batsman.running * random.uniform(0.8, 1.2)
        fielding_probs = [fielder.fielding for fielder in fielders]
        avg_fielding_prob = sum(fielding_probs) / len(fielding_probs)

        if field.pitch_conditions == "Dry":
            batting_prob *= random.uniform(0.7, 1.0)
            bowling_prob *= random.uniform(0.7, 1.0)
        elif field.pitch_conditions == "Damp":
            batting_prob *= random.uniform(0.8, 1.2)
            bowling_prob *= random.uniform(0.8, 1.2)
        elif field.pitch_conditions == "Grassy":
            batting_prob *= random.uniform(0.9, 1.1)
            bowling_prob *= random.uniform(0.9, 1.1)

        out_prob = (1 - batting_prob) * (1 - avg_fielding_prob) * (1 - bowling_prob)

        runs_prob = batting_prob * running_prob * (1 - avg_fielding_prob) * (1 - bowling_prob)

        outcome = random.choices(
            population=["out", "runs"],
            weights=[out_prob, runs_prob],
            k=1
        )[0]
        
        return outcome

    def update_score(self, team, runs):
        self.scores[team] += runs
    
    def update_wickets(self, team):
        self.wickets[team] += 1
    
    def update_overs(self):
        self.overs += 0.1
        if self.overs>20:
            self.overs = 0