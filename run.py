import random as r
import matplotlib.pyplot as plt

def gen_data():
    bonus = 10
    start = r.randint(30, 100)
    max_val = r.randint(start, 800)
    scale = max_val/105
    data = list()
    data.append(start)
    while len(data) < 105:
        last = data[-1]
        res = r.randint(1, 105 - len(data)) 
        next_pivot = int(res* scale + r.randint(-bonus, bonus))  # adding some noise
        # next_val = r.randint(100, end)
        s1 = (next_pivot - last)/res
        for i in range(1, res):
            next_val = int(last + i*s1)
            br = r.randint(-bonus, bonus)
            next_val += br
            if len(data) < 105:
                data.append(next_val)
            
        if len(data) < 105: 
            data.append(next_val)
        if len(data) < 105:
            data.append(0)
    # print(data)
    plt.plot(data)
    plt.show()

gen_data()