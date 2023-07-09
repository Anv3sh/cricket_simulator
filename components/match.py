import random
from .umpire import Umpire
from .commentator import Commentator


class Match:
    
    def __init__(self, team1, team2, field,home):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.home = home
        self.innings = 1
        self.change_innings = False
        self.end_match = False
        self.umpire = Umpire(team1,team2)
        self.commentator = Commentator(self.umpire)

    def start(self):
        # Perform toss and decide batting/bowling order
        self.toss_winner = random.choice([self.team1, self.team2])
        self.toss_decision = random.choice(["bat", "bowl"])

        if self.toss_decision == "bat":
            batting_team = self.toss_winner
            bowling_team = self.team1 if self.toss_winner == self.team2 else self.team2
        else:
            batting_team = self.team1 if self.toss_winner == self.team2 else self.team2
            bowling_team = self.toss_winner

        # Select captains
        batting_team.select_captain(random.randint(0, len(batting_team.players)-1))
        bowling_team.select_captain(random.randint(0, len(bowling_team.players)-1))

        # Set batting and bowling order
        batting_order_team1=[]
        bowling_order_team1=[]
        batting_order_team2=[]
        bowling_order_team2=[]
        while len(batting_order_team1)==0:
            batting_order_team1 = random.sample(range(len(batting_team.players)), len(batting_team.players))
        while len(bowling_order_team1)==0:
            bowling_order_team1 = random.sample(range(len(batting_team.players)), len(batting_team.players))

        while len(batting_order_team2)==0:
            batting_order_team2 = random.sample(range(len(bowling_team.players)), len(bowling_team.players))
        while len(bowling_order_team2)==0:
            bowling_order_team2 = random.sample(range(len(bowling_team.players)), len(bowling_team.players))

        batting_team.set_batting_order(batting_order_team1)
        batting_team.set_bowling_order(bowling_order_team1)

        bowling_team.set_batting_order(batting_order_team2)
        bowling_team.set_bowling_order(bowling_order_team2)
        
        # Print match details
        print("Match Details:")
        print(f"Toss Winner: {self.toss_winner.name}")
        print(f"Decision: {self.toss_decision}")
        print(f"Batting Team: {batting_team.name}")
        print(f"Bowling Team: {bowling_team.name}")
        print(f"{batting_team.name} Captain: {batting_team.captain.name}")
        print(f"{bowling_team.name} Captain: {bowling_team.captain.name}")

        # Start the match simulation
        self.simulate_match()
        return

    def simulate_match(self):
        while True:
            self.simulate_ball()
            # Check if the innings should be changed or the match should end
            if self.should_change_innings():
                self.changing_innings()
            elif self.should_end_match():
                self.match_end_stats()
                break
        return
    
    def should_change_innings(self):
        return self.change_innings
    
    def should_end_match(self):
        return self.end_match
    
    def changing_innings(self):
        self.innings = 2

    def match_end_stats(self):
        # Calculate and display the final result of the match
        if (self.toss_decision == "bat" and self.toss_winner == self.team1) or (self.toss_decision == "bowl" and self.toss_winner == self.team2):
            print(f"{self.team1} scored {self.umpire.scores[self.team1.name]}/{self.umpire.wickets[self.team1.name]}")
            print(f"{self.team2} scored {self.umpire.scores[self.team2.name]}/{self.umpire.wickets[self.team2.name]}")
            if self.umpire.scores[self.team1.name] > self.umpire.scores[self.team2.name]:
            
                print(f"{self.team1.name} won by",self.umpire.scores[self.team1.name]-self.umpire.scores[self.team2.name],"runs")

            else:
                print(f"{self.team2.name} with",11-self.umpire.wickets[self.team2.name],"wickets remaining")
        else:
            print(f"{self.team2} scored {self.umpire.scores[self.team2.name]}/{self.umpire.wickets[self.team2.name]}")
            print(f"{self.team1} scored {self.umpire.scores[self.team1.name]}/{self.umpire.wickets[self.team1.name]}")

            if self.umpire.scores[self.team2.name] > self.umpire.scores[self.team1.name]:
                print(f"{self.team2.name} won by",self.umpire.scores[self.team2.name]-self.umpire.scores[self.team1.name],"runs")

            else:
                print(f"{self.team1.name} with",11-self.umpire.wickets[self.team1.name],"wickets remaining")

        return
    
    def check_all_out(self,batting_team):
        return self.umpire.wickets[batting_team] == 10

    def simulate_ball(self):
        if self.innings == 1:
            batting_team = self.team1
            bowling_team = self.team2
        else:
            batting_team = self.team2
            bowling_team = self.team1
        batsman = batting_team.get_next_batsman()
        for i in range(20):
            bowler,fielders = bowling_team.get_next_bowler()
            
            
            for j in range(6):
                outcome = self.umpire.predict_outcome(bowler, batsman,fielders,self.field)
                runs=0
                if outcome == "out":
                    self.umpire.update_wickets(batting_team.name)
                    if self.check_all_out(batting_team.name):
                        self.end_match = True
                        break
                    batsman = batting_team.get_next_batsman()
                else:
                    runs = random.randint(0, 6)
                    self.umpire.update_score(batting_team.name, runs)
                    # Handle scoring runs
                self.commentator.provide_commentary(bowler,batsman,fielders,self.field,outcome,runs)

                self.umpire.update_overs()
        if self.innings == 1 and not self.end_match:
            self.change_innings = True
        else:
            self.end_match = True
        return
        