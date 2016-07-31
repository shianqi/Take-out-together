import math

def weight_cal(welfare_list,take_out_price,take_out_cost):

    take_out_cost = int(take_out_cost)
    take_out_price = int(take_out_price)

    # shop_info.weight = weight
    sum = 0.0
    for welfare in welfare_list:
        sum = sum + (welfare[1]-take_out_cost)/max(welfare[0],take_out_price)
    if len(welfare_list) != 0:
        sum = sum / len(welfare_list)
    else:
        return 0
    return sum





