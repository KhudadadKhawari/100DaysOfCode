import random

def generate_random_position():
    random_positions = []
    r = (280,random.randint(-280,280))
    l = (-280, random.randint(-280,280))
    u = (random.randint(-280,280),280)
    d = (random.randint(-280,280),-280)
    random_positions.append(r)
    random_positions.append(l)
    random_positions.append(u)
    random_positions.append(d)
    return random.choice(random_positions)