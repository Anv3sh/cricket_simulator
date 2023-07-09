import random
from components.field import Field
from components.teams import Teams
from components.player import Player
from components.match import Match


def generate_players(team_name):
    players = []
    for i in range(1, 12):
        player_name = f"Player{team_name}_{i}"
        bowling = round(random.uniform(0.5, 0.9), 2)
        batting = round(random.uniform(0.5, 0.9), 2)
        fielding = round(random.uniform(0.5, 0.9), 2)
        running = round(random.uniform(0.5, 0.9), 2)
        experience = round(random.uniform(0.5, 0.9), 2)

        player = Player(player_name, bowling, batting, fielding, running, experience)
        players.append(player)

    return players

# Generate field data
def generate_field():
    field_size = random.choice(["Small", "Medium", "Large"])
    fan_ratio = round(random.uniform(0.5, 1.5), 2)
    pitch_conditions = random.choice(["Dry", "Damp", "Grassy"])
    home_advantage = round(random.uniform(0.5, 1.5), 2)

    return field_size,fan_ratio,pitch_conditions,home_advantage


# name,bowling,batting,fielding,running,experience
team1_players = generate_players("India")
team2_players = generate_players("Australia")



team1 = Teams("India",team1_players)
team2 = Teams("Australia",team2_players)


field_size,fan_ratio,pitch_conditions,home_advantage = generate_field()

# Create an instance of Field
field = Field(field_size, fan_ratio, pitch_conditions, home_advantage)
home = team1 if random.randint(1,3)== 1 else team2
match = Match(team1,team2,field,home)
match.start()