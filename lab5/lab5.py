# ECOR 1041 Lab 5

__author__ = "Ihsan Aydin"
__student_number__ = "101264856"

#======================================================
# Exercise 1


def tip(dinner_cost: float, satisfactory_level: int) -> float:
    """ Return the value of tip depending on the satistfaction level 
    1= Totally satisfied (20% of dinner cost), 2= Somewhat satisfied (15% of dinner cost), 
    3= Dissatisfied (5% of dinner cost)
    
    Preconditions: 1<= satisfactory_level <= 3.
                    dinner_cost > 0.

    Examples:
    >>>tip(50,1)
    10.0
    >>>tip(100,1)
    20.0
    >>>tip(65,3)
    3.25
    """
    if satisfactory_level == 1:
        tip_paid = dinner_cost * 0.2
    elif satisfactory_level == 2:
        tip_paid = dinner_cost * 0.15
    elif satisfactory_level == 3:
        tip_paid = dinner_cost * 0.05
    return tip_paid

#======================================================
# Exercise 2


def coupon(amount_spent: float) -> float:
    """Return the coupon award depending on how much spent on groceries
    Less than $10 -> no coupon
    Between $10 to $60 -> 8%
    More than $60 to $150 -> 10%
    More than $150 to $210 -> 12%
    More than $210 -> 14%
    
    Preconditions: amount_spent >=0.
    
    Examples
    >>>coupon(5)
    No coupon
    >>>coupon(60.5)
    6.05
    >>>coupon(150)
    15.0
    """
    if amount_spent < 10:
        return print("No coupon")
    elif 10 <= amount_spent <= 60:
        award = amount_spent * 0.08
    elif 60 < amount_spent <= 150:
        award = amount_spent * 0.10
    elif 150 < amount_spent <= 210:
        award = amount_spent * 0.12
    elif amount_spent > 210:
        award = amount_spent * 0.14
    return award

#======================================================
# Exercise 3


weekday = False
weekend = True


def bakers_party(day_type: bool, number_of_pastries: int) -> bool:
    """Returns if the party is succesfull depending on the day type and number
    of pastries eaten.
    
    Precondition: day_type == weekend or day_type == weekend.
    number_of_pastries >= 0.
    
    >>>bakers_party(weekday,80)
    False
    >>>bakers_party(weekday,40)
    True
    >>>bakers_party(weekend,30)
    False
    """
    if day_type == False:
        if 40 <= number_of_pastries <= 60:
            succesful = True
        else:
            succesful = False

    elif day_type == True:
        if number_of_pastries >= 40:
            succesful = True
        else:
            succesful = False
    return succesful


#======================================================
# Exercise 4
summer = True
fall = False
winter = False
spring = False


def squirrel_play(season: bool, temperature: int) -> bool:
    """Return if the squirrels are playing depending on the season and temperature.
    
    Precondition season == summer or season == fall or season == winter or
    season == spring.
    Examples
    >>>squirrel_play(winter,90)
    True
    >>>squirrel_play(spring,10)
    False
    >>>squirrel_play(summer,100)
    True
    """

    if season == True:
        if 60 <= temperature <= 100:
            play = True
        else:
            play = False
    elif season == False:
        if 60 <= temperature <= 90:
            play = True
        else:
            play = False
    return play

#======================================================
# Exercise 5


def great_42(a: int, b: int) -> bool:
    """Returns the result for great 42 game by the given a and b values, and
    determines if it works or not.
    
    Precondition: a and b must be integer
    
    Example
    >>>great_42(45,1)
    False
    >>>great_42(11,31)
    True
    >>>great_42(-50,-8)
    True
    """
    if a == 42 or b == 42:
        answer = True
    elif a + b == 42:
        answer = True
    elif abs(a - b) == 42:
        answer = True
    else:
        answer = False
    return answer

#======================================================
# Exercise 6


def multiply_uniques(a: int, b: int, c: int) -> int:
    """Returns the multiplication of unique values, if the values are same it
    returns 1, if 2 values are same it returns the unique value.
    
    Precondition: a,b,c must be integer.
    
    Example
    >>>multiply_uniques(3,3,3)
    1
    >>>multiply_uniques(2,4,2)
    4
    >>>multiply_uniques(2,6,3)
    36
    """
    if a == b == c:
        answer = 1
    elif a == c:
        answer = b
    elif a == b:
        answer = c
    elif b == c:
        answer = a
    else:
        answer = a * b * c
    return answer
