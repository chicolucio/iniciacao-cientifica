GRAVITY = 9.8  # m/s**2


def height(initial_height, initial_speed, time):
    return initial_height + initial_speed * time - (1/2) * GRAVITY * time**2
