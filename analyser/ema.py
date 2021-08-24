import math 

#Exponential average

SHORT = 3
MID = 7
LONG = 14

def compute(my_fifo):
    def print(short_ema, mid_ema, long_ema):
        d = {
            '{} days'.format(SHORT) : short_ema,
            '{} days'.format(MID) : mid_ema,
            '{} days'.format(LONG) : long_ema,
        }
        order = sorted(
            d,
            key = lambda k : d[k],
            reverse = True
        )
        
        return 'Today\'s Low-Pass: {:.1f} ({} days), {:.1f} ({} days), {:.1f} ({} days),\n\tOrder: {} > {} > {}'.format(
            short_ema,
            SHORT,
            mid_ema,
            MID,
            long_ema,
            LONG,
            order[0],
            order[1],
            order[2],
        )

    def ema(fifo, tc):
        avg = 0
        weight_sum = 0
        for i in range(tc*5):
            weight = math.exp(-i/tc)
            avg = avg + int(fifo[-i-1]['daily'])*weight
            weight_sum = weight_sum + weight
        return avg/weight_sum
    
    short_ema = ema(my_fifo, SHORT)
    mid_ema = ema(my_fifo, MID)
    long_ema = ema(my_fifo, LONG)
    
    return print(short_ema, mid_ema, long_ema)

