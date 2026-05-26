# src/geometry.py

import numpy as np


def calculate_angle(a, b, c):
    """
    Calcula el ángulo 3D formado por tres puntos.

    Parámetros:
        a, b, c -> [x, y, z]

    Retorna:
        ángulo en grados
    """

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    norm_ba = np.linalg.norm(ba)
    norm_bc = np.linalg.norm(bc)

    # Evitar división por cero
    if norm_ba == 0 or norm_bc == 0:
        return 0.0

    cosine = np.dot(ba, bc) / (norm_ba * norm_bc)

    cosine = np.clip(cosine, -1.0, 1.0)

    angle = np.degrees(np.arccos(cosine))

    return round(angle, 2)