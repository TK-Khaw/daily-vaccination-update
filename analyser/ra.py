#Rolling average

def compute(my_fifo):
    def print(today, yesterday):
        flag = yesterday > today
        return 'Today\'s 7DRA: {:.1f}, {} by ({:.1f}/{:.2f}%)'.format(
            today, 
            'decreased' if flag else 'increased',
            abs(yesterday - today),
            abs(yesterday - today)/yesterday
        )

    def rolling_avg(fifo):
        avg = 0
        for item in fifo:
            avg = avg + int(item['daily'])
        return avg/7

    today = rolling_avg(my_fifo[-7:])
    yesterday = rolling_avg(my_fifo[-8:-1])
    
    return print(today, yesterday)

