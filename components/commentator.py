

class Commentator:
    def __init__(self, umpire):
        self.umpire = umpire


    def provide_commentary(self,bowler, batsman, fielders, field, outcome,runs):
        bowler_name = bowler.name
        batsman_name = batsman.name

        if outcome == "out":
            commentary = f"{bowler_name} takes a wicket! {batsman_name} is out."
        elif outcome == "runs":

            commentary = f"{batsman_name} scores {runs} runs."

        self.display_commentary(commentary)

    def display_commentary(self, commentary):
        print(commentary)