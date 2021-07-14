import math 

#Max Min

WEEK = 7
MONTH = 30
HUNDRED = 100

def compute(my_fifo):
    def print(max_week, min_week, max_month, min_month, max_hundred, min_hundred):
        
        return 'Today\'s Min-Max: Min: {} ({}) Max: {} ({}) ({} days)\n\t\tMin: {} ({}) Max: {} ({}) ({} days)\n\t\tMin: {} ({}) Max: {} ({}) ({} days)'.format(
            min_week['total_daily'],
            min_week['date'],
            max_week['total_daily'],
            max_week['date'],
            WEEK,
            min_month['total_daily'],
            min_month['date'],
            max_month['total_daily'],
            max_month['date'],
            MONTH,
            min_hundred['total_daily'],
            min_hundred['date'],
            max_hundred['total_daily'],
            max_hundred['date'],
            HUNDRED,
        )

    def maxmin(fifo):
        max_row = max(fifo, key = lambda k: int(k['total_daily']))
        min_row = min(fifo, key = lambda k: int(k['total_daily']))
        return max_row, min_row
    
    max_week, min_week = maxmin(my_fifo[-WEEK:])
    max_month, min_month = maxmin(my_fifo[-MONTH:])
    max_hundred, min_hundred = maxmin(my_fifo[-HUNDRED:])

    return print(max_week, min_week, max_month, min_month, max_hundred, min_hundred)

