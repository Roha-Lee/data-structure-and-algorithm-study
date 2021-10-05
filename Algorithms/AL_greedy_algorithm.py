def coin_problem(value, coin_list):
    coin_list = sorted(coin_list, reverse = True)
    count_coin = [0 for _ in range(len(coin_list))]
    for idx, coin in enumerate(coin_list):
        num_coin = int(value // coin)
        count_coin[idx] = num_coin
        value -= coin * num_coin
    return count_coin

def fractional_knapsack_problem(weights, values, max_weight):
    data_list = [(weight, value) for weight, value in zip(weights, values)]
    data_list = sorted(data_list, reverse = True, key = lambda x: x[1] / x[0])
    amounts = []
    for weight, value in data_list:
        amount = min(max_weight, weight)
        if max_weight - amount >= 0:
            max_weight -= amount
            amounts.append(((weight, value), amount))
    return amounts
    
if __name__ == '__main__':
    print(coin_problem(4720, [500, 100, 50, 1]))
    print(fractional_knapsack_problem(weights = [10,15,20,25,30], values=[10,12,10,8,5], max_weight = 30))
        
