# ECOR 1041 Lab 4

__author__ = "Ihsan Aydin"
__student_number__ = "101264856"

import math

# =====================================================
# Exercise 1


def area_of_disk(radius: float) -> float:
    """Return the area of a disk with the specified radius.
    
    Precondition: radius >= 0.
    
    >>> area_of_disk(5)
    78.54
    
    >>> area_of_disk(10)
    314.16
    
    >>> area_of_disk(3)
    28.27
    """
    return math.pi * radius ** 2


# =======================================================
# Exercise 2

LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934


def convert_to_litres_per_100_km(mpg: float) -> float:
    """Return the litres per 100 km value depending on the mpg
    
    Precondition: mpg >= 0.
    
    >>>convert_to_litres_per_100_km(32)
    8.83
    
    >>>convert_to_litres_per_100_km(64)
    4.41
    
    >>>convert_to_litres_per_100_km(10)
    28.2
    """
    return LITRES_PER_GALLON / KMS_PER_MILE * 100 / mpg

# =======================================================
# Exercise 3


def accumulated_amount(principal: float, rate: float, n: int, time: int) -> float:
    """Return the accumulated amount depending on the initial amount, rate, number
    of times interest compunded per year and time
    
    Precondition: principal, time, n >= 0.
    
    >>>accumulated_amount(1500,0.043,4,6)
    1938.84
    
    >>>accumulated_amount(0,0.043,4,6)
    0.0
    
    >>>accumulated_amount(1500,0,4,6)
    1500.0
    """
    return principal * (1 + (rate / n)) ** (n * time)

# =======================================================
# Exercise 4


def area_of_cone(height: float, radius: float) -> float:
    """Return the area of a cone by specific height and radius
    
    Precondition: radius, height >= 0.
    
    >>>area_of_cone(5,10)
    351.24
    
    >>>area_of_cone(4,9)
    278.47
    
    >>>area_of_cone(15,32)
    3552.89
    """
    return math.pi * radius * math.sqrt(radius**2 + height**2)

# =======================================================
# Exercise 5


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """Return the distance between two points
    
    >>>distance(1,1,2,2)
    1.41
    
    >>>distance(5,1,3,7)
    6.32
    
    >>>distance(4,0,12,8)
    11.3
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def area_of_circle(xc: int, yc: int, xp: int, yp: int) -> float:
    """Return the area of a circle by calling area_of_disk
    and distance functions
    >>>area_of_circle(1,1,2,2)
    6.28
    
    >>>area_of_circle(0,3,7,4)
    157.1
    
    >>>area_of_circle(16,3,21,9)
    191.6
    """
    return area_of_disk(distance(xc, yc, xp, yp))

