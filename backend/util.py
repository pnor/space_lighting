#!/usr/bin/env python3

""" Convenience functions"""

import colour
import copy
from typing import Union, List, Tuple
import numpy as np
from numba import jit

from backend.backend_types import RGB


def hex_to_rgb(hex_str: str) -> RGB:
    color_obj = colour.Color(hex_str)
    rgb = color_obj.rgb
    rgb = [int(x * 255) for x in rgb]
    return rgb


def hex_to_color_obj(hex_str: str) -> colour.Color:
    return colour.Color(hex_str)


def color_obj_to_rgb(color_obj: colour.Color) -> RGB:
    rgb = color_obj.rgb
    rgb = [int(x * 255) for x in rgb]
    return rgb


def color_format_to_obj(color: Union[RGB, str, colour.Color]) -> colour.Color:
    if type(color) is list or type(color) is tuple:
        assert len(color) >= 3
        return colour.Color(rgb=tuple(np.array(color) / 255))
    else:
        return colour.Color(color)


def set_color_luminance(color: Union[RGB, str, colour.Color], luminance: float) -> RGB:
    """Returns `color` with its luminance set to `luminance` as a rgb tuple"""
    c = color_format_to_obj(color)
    c.set_luminance(luminance)
    return c.rgb


def dim_color(color: Union[RGB, str, colour.Color]) -> RGB:
    """Returns an extremely dimmed version of `color`
    `color` can be a hex string or rgb tuple"""
    return set_color_luminance(0.01)


def color_range(
    color_start: Union[RGB, str, colour.Color],
    color_end: Union[RGB, str, colour.Color],
    number: int,
) -> List[RGB]:
    """Returns `number` colors spanning the range from `color_start` to `color_end`"""
    c1 = color_format_to_obj(color_start)
    c2 = color_format_to_obj(color_end)
    colors_spanning = list(c1.range_to(c2, number))
    return [color_obj_to_rgb(c) for c in colors_spanning]


@jit
def clamp(num, min_value, max_value):
    num = max(min(num, max_value), min_value)
    return num


@jit
def sigmoid(x: float) -> float:
    return 1 / (1 + np.exp(-x))


@jit
def distance_formula(x1: float, y1: float, x2: float, y2: float):
    return np.sqrt(np.power(x2 - x1, 2) + np.power(y2 - y1, 2))


@jit
def polar_to_cartesian(r: float, theta: float) -> Tuple[float, float]:
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


@jit
def transform_unit_circle_to_origin(
    x: float, y: float, orig_x: float, orig_y: float
) -> Tuple[float, float]:
    """
    Transforms coordinates in x: (-1..1), y: (-1..1) to box with width and height 1 centered on
    `(orig_x, orig_y)`.
    Mostly for converting the unit circle results in `polar_to_cartesian` to the space used to
    locate LEDs in 2D space.
    """
    x = (x / 2) + orig_x
    y = (y / 2) + orig_y
    return x, y