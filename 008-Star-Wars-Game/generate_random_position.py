import random

#Generates random position in the borders of the play area.
def generate_random_position():
    random_positions = []
    r = (280,random.randint(-280,280)) # Right x,y
    l = (-280, random.randint(-280,280)) # Left x,y
    u = (random.randint(-280,280),280) # Up x,y
    d = (random.randint(-280,280),-280) # Down x,y
    random_positions.append(r)
    random_positions.append(l)
    random_positions.append(u)
    random_positions.append(d)
    return random.choice(random_positions) # chooses and returns a random post from r,l,u or d.