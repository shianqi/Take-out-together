import math

def weight_cal(shop_info):
    take_out_cost = int(shop_info.take_out_cost)
    take_out_price = int(shop_info.take_out_price)
    welfare = shop_info.welfare


    weight = 0.0
    m = 0.0
    for i in range(int(len(welfare)/2)):
        m = m + max(take_out_price,welfare[i*2])


    for i in range(int(len(welfare)/2)):
        weight = weight + math.sqrt((max(take_out_price,welfare[2*i]))/m)*100*(1-(max(take_out_price,welfare[i*2])-welfare[i*2+1]+take_out_cost)/(max(welfare[i*2],take_out_price)+take_out_cost))
    # shop_info.weight = weight
    return weight





