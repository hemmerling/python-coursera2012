import random

the_players = ["Rolf", "Horst", "Anneliese"]

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        # ???
    return points

def starting_points(players):
    """Returns a list of random points, one for each player."""
#    return [random_point(player) for player in players]

def starting_points2(players):
    """Returns a list of random points, one for each player."""
#    return [random_point for players]

def starting_points3(players):
    """Returns a list of random points, one for each player."""
    return [random_point for player in players]

def starting_points4(players):
    """Returns a list of random points, one for each player."""
    return [random_point() for p in players]

def starting_points5(players):
    """Returns a list of random points, one for each player."""
    return [random_point() for player in players]

def starting_points6(players):
    """Returns a list of random points, one for each player."""
#    print [for player in players: random_point()] 

print starting_points(the_players)
print starting_points2(the_players)
print starting_points3(the_players)
print starting_points4(the_players)
print starting_points5(the_players)
print starting_points6(the_players)