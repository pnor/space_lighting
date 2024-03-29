#!/usr/bin/env python3

import light_arrangements_python
import numpy as np

from typing import List
from numpy._typing import NDArray


def polar(
    rho: float, angular_coords: List[float], center: List[float]
) -> NDArray[np.float64]:
    loc = light_arrangements_python.Loc2.polar(rho, angular_coords, center)
    return np.array(loc)


def cylindrical(
    radius: float, theta: float, coords: List[float], center: List[float]
) -> NDArray[np.float64]:
    loc = light_arrangements_python.Loc2.cylindrical(radius, theta, coords, center)
    return np.array(loc)
