import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    distan = math.sqrt((x_1-x_2)(x_1-x_2)+(y_1-y_2)(y_1-y_2))
    return distan