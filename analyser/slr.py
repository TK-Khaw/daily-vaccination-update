import math 

# Simple linear regression

def compute(my_fifo):
    def print(a_now, b_now, r2_now, a_then, b_then, r2_then):
        return 'Today\'s SLR: a = {:.1f}, b = {:.1f}, r2 = {:.1f},\n\tGradient {} by {:.1f} deg. {} linear.'.format(
            a_now,
            b_now,
            r2_now,
            'increased' if b_now > b_then else 'decreased',
            abs(math.atan((b_now - b_then)/(1 + b_now*b_then))) * 180/math.pi,
            'More' if r2_now > r2_then else 'Less',
        )

    def slr(fifo, n = 10):
        s_x = 0
        s_y = 0
        s_xx = 0
        s_xy = 0
        s_yy = 0
        
        for x in range(n):
            y = int(fifo[x]['total_daily'])
            s_x = s_x + x
            s_xx = s_xx + x*x
            s_y = s_y + y
            s_yy = s_yy + y*y
            s_xy = s_xy + x*y

        b = (n*s_xy - s_x*s_y)/(n*s_xx - s_x*s_x)
        a = (s_y - b*s_x)/n
        r2 = b*b*((s_xx - (s_x*s_x)/n)/(s_yy - (s_y*s_y)/n))

        return a,b,r2
    
    a_now, b_now, r2_now = slr(my_fifo[-10:])
    a_then, b_then, r2_then = slr(my_fifo[-11:-1])
    
    return print(a_now, b_now, r2_now, a_then, b_then, r2_then)

