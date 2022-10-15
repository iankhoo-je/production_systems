import numpy as np
import matplotlib.pyplot as plt

def equation(process_total, normal_inv, idx, init_inv, t):
    return (process_total* -t) + ((normal_inv * (idx)) + init_inv)

def initial():
# -------------------- User Configurable Variables ------------------------------
    process_total = 10000
    normal_inv = 800
    init_inv = 600
    steps = 100000
# -------------------------------------------------------------------------------
    y_array = []
    t_array = np.linspace(0,1,steps)
    idx = 0   
    
    for t in t_array:
        y  = equation(process_total, normal_inv, idx, init_inv, t)
        y_array.append(y)
        if y<=0:
            idx += 1
            

    print(y_array) # for debugging purpose

    plt.plot(t_array,y_array)
    plt.show()

initial()


def without_init():
    process_total = 10000
    normal_inv = 600

    y_array = []
    t_array = np.linspace(0,1,1001)
    print(t_array)
    idx = 1

    for t in t_array:
        y = (process_total* -t) + (normal_inv * idx)
        y_array.append(y)
        if y == 0:
            idx += 1

    print(y_array)

    plt.plot(t_array,y_array)

    plt.show()
# initialise = True
# for t in t_array:
#     if initialise:
#         y_init = (process_total* -t) + (init_inv)
#         if y_init <= 0:
#             initialise = False
#             y  = equation(process_total, normal_inv, idx, init_inv, t)
#             y_array.append(y)
#         else:       
#             y_array.append(y_init)
#     else:
#         y = equation(process_total, normal_inv, idx, init_inv, t)
#         y_array.append(y)
#         if y <= 0:
#             idx += 1
