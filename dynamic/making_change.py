# Calculates the minimum amount of coins to make a certain change for a set of coins

coins = [1, 2, 5, 7]

minimum_amount_of_coins_for = [None for x in range(1000)]


def smallest_change_count_for(change):
    if change < 0:
        return -1
    if change is 0:
        return 0

    if minimum_amount_of_coins_for[change] is not None:
        return minimum_amount_of_coins_for[change]

    coin_count = change

    for this_coin in coins:
        if change >= this_coin:
            coin_count = min(coin_count, 1 + smallest_change_count_for(change - this_coin))

    minimum_amount_of_coins_for[change] = coin_count
    return coin_count


print smallest_change_count_for(-1) == -1
print smallest_change_count_for(0) == 0
print smallest_change_count_for(1) == 1
print smallest_change_count_for(2) == 1
print smallest_change_count_for(5) == 1
print smallest_change_count_for(7) == 1
print smallest_change_count_for(10) == 2
print smallest_change_count_for(20) == 4
print smallest_change_count_for(50) == 8
