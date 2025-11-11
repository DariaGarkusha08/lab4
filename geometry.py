def area(a, b):
    """
    Calculate the area of a rectangle.
    
    Args:
        a (float): length of the rectangle
        b (float): width of the rectangle
    
    Returns:
        float: area of the rectangle
    
    Raises:
        TypeError: if arguments are not numbers
        ValueError: if arguments are negative
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Arguments must be non-negative")
    return a * b

def perimeter(a, b):
    """
    Calculate the perimeter of a rectangle.
    
    Args:
        a (float): length of the rectangle
        b (float): width of the rectangle
    
    Returns:
        float: perimeter of the rectangle
    
    Raises:
        TypeError: if arguments are not numbers
        ValueError: if arguments are negative
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Arguments must be non-negative")
    return 2 * (a + b)
