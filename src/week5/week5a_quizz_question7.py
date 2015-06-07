import random

global_players  = ["Rolf", "Horst" "Anneliese"]
def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points1(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        points.append(point)
    return points

def starting_points2(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        points.extend(point)
    return points

def starting_points3(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        #points += point
    return points

print starting_points1(global_players)
print starting_points2(global_players)
#print starting_points3(global_players)
