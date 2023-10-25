# ECOR 1041 Lab 6

__author__ = "Ihsan Aydin"
__student_number__ = "101264856"

# ======================================================
# Exercise 1


def parrot_trouble(talking: bool, hour: int) -> bool:
    """Returns if we are in trouble or not depending on the time when the parrot
    talks
    
    Preconditions: Talking == true or false, 0<=hour<=23
    
    Examples:
    >>>parrot_trouble(True,15)
    False
    >>>parrot_trouble(True,6)
    True
    >>>parrot_trouble(False,15)
    False
    """
    return talking and (hour < 7 or hour > 20)


# ======================================================
# Exercise 2
Sun = 0
Mon = 1
Tue = 2
Wed = 3
Thu = 4
Fri = 5
Sat = 6


def alarm_clock(day: int, vacation: bool) -> str:
    """Returns when the alarm will ring depending on the day
    
    Preconditions: Days are written by the first 3 letters and first letter is
    capital, Vacation == True or False
    
    Examples:
    >>>alarm_clock(Sat,False)
    10:00
    >>>alarm_clock(Mon,True)
    10:00
    >>>alarm_clock(Tue,False)
    7:00
    """
    if vacation == True:
        if 1 <= day <= 5:
            ans = print("10:00")
        elif day == 0 or 6:
            ans = print('off')
    elif vacation == False:
        if 1 <= day <= 5:
            ans = print("7:00")
        elif day == 0 or 6:
            ans = print("10:00")
    return ans


# ======================================================
# Exercise 3

def close_far(a: int, b: int, c: int) -> bool:
    """Returns if a is close to b or c but other parameter is not close
    
    Preconditions: a,b,c are integers
    
    Examples:
    >>>close_far(1, 2, 10)
    True
    >>>close_far(1, 2, 3)
    False
    >>>close_far(4, 1, 3)
    True
    """
    if abs(a - c) <= 1 and (abs(b - c) >= 2 and abs(b - a) >= 2):
        ans = True
    elif abs(a - b) <= 1 and (abs(a - c) >= 2 and abs(b - c) >= 2):
        ans = True
    else:
        ans = False
    return ans

# ======================================================
# Exercise 4


def blackjack(a: int, b: int) -> int:
    """Returns the closest value to 21 and returns 0 if both values are over 21
    
    Preconditions: a and b are positive integers
    
    Examples:
    >>>blackjack(20,12)
    20
    >>>blackjack(5,22)
    5
    >>>blackjack(26,32)
    0
    """
    if a > 21:
        a = 0
    if b > 21:
        b = 0
    return max(a, b)

# ======================================================
# Exercise 5


def assistance(income: float, children: int) -> float:
    """Returns the amount of assistance a family will recieve depending on the
    income and children
    
    Precondition: children >= 0, 0<= income <40000
    
    Examples:
    >>>assistance(0,2)
    4000
    >>>assistance(34000,0)
    0
    >>>assistance(25000,5)
    5000
    """
    if 30000 <= income < 40000 and children >= 3:
        money = 1500 * children
    elif 20000 <= income < 30000 and children >= 2:
        money = 1000 * children
    elif income < 20000:
        money = 2000 * children
    else:
        money = 0
    return money

# ======================================================
# Exercise 6


def add_up(n: int) -> float:
    """Returns the floating point number for given integer
    
    Preconditions: n >=0 and integer
    
    Examples:
    >>>add_up(6)
    11.15
    >>>add_up(0)
    0
    >>>add_up(14)
    34.773
    """
    add = 0
    for i in range(n):
        add += ((i + 1) / (n - i))
    return add

# ======================================================
# Exercise 7


def fib(n: int) -> int:
    """Returns fibonacci number depending on given n value.
    
    Preconditions: n>=0 and integer
    
    Examples:
    >>>fib(1)
    1
    >>>fib(4)
    3
    >>>fib(8)
    21
    """
    ans = 0
    fib1 = 1
    fib2 = 1
    for i in range(n - 1):
        ans = fib1 + fib2
        fib1 = fib2
        fib2 = ans
        ans = 0
    return fib1

# ======================================================
# Exercise 8


def years_to_double(initial: float, rate: float) -> int:
    """Returns how many years it takes to double the money with given rate
    
    Preconditions: initial > 0 and  0<rate<100
    
    Examples:
    >>>years_to_double(1000, 5.0)
    15
    >>>years_to_double(1000, 50.0)
    2
    >>>years_to_double(700,100)
    1
    """
    year = 0
    amnt = initial
    while amnt < initial * 2:
        amnt += amnt * (rate / 100)
        year += 1
    return year
