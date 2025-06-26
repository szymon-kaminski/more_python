def divide(numerator, denominator):
    if denominator == 0:
        return "Not defined"
    elif denominator is None or numerator is None:
        return "Numerator/denominator value is None."
    return int(numerator / denominator)