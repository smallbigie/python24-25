def calculate_area(length, width):
    """
    Calculate the area of a rectangle

    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns: 
        float: The area of the rectangle
    """
    return length * width
# Example Usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
                     

area = calculate_area(length, width)
print(f"The area of the rectangle is: {area:.2f}")
    
    
    