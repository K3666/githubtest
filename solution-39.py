def my_magnitude_of_a_vector_sample(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    mag = ((x ** 2) + (y ** 2) + (z ** 2)) ** (1/2)
    return mag
