def my_unit_vector_sample(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    mag = ((x ** 2) + (y ** 2) + (z ** 2)) ** (1/2)
    new_x = x/mag
    new_y = y/mag
    new_z = z/mag
    unit_vector = [new_x, new_y, new_z]
    return unit_vector
