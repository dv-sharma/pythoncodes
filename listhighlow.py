def count_low_high(num_list):
    list_high=[]
    list_low=[]
    for num in num_list:
        if num>50 or num%3==0:
            list_high.append(num)
        else:
            list_low.append(num)
    list_new=[len(list_low),len(list_high)]
    if len(list_new)==0:
        return None
    return list_new

""" You must implement the count_low_high() function. Its parameter is a list of numbers.

If a number is greater than 50 or divisible by 3, it will count as a high. If these conditions are not met, the number is considered a low.

At the end of the function, you must return a list that contains the number of lows and highs, in that order.

In case the list is empty, you may return None. """