def map(x, in_min, in_max, out_min, out_max):
    """Linear interpolation function.

    Args:
        x (int): original value to be scaled
        in_min (int): minimum input value
        in_max (int): maximum input value
        out_min (int): minimum output value
        out_max (int): maximum output value

    Returns:
        int: output value
    """
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)