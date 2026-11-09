COINS = (50, 25, 10, 5, 2, 1)


def find_coins_greedy(amount: int) -> dict[int, int]:
    result = {}

    for coin in COINS:
        count = amount // coin
        amount %= coin
        if count:
            result[coin] = count

    return result


def find_min_coins(amount: int) -> dict[int, int]:
    min_coins = [0] + [amount + 1] * amount
    last_coin = [0] * (amount + 1)

    for current_amount in range(1, amount + 1):
        for coin in COINS:
            if coin <= current_amount and min_coins[current_amount - coin] + 1 < min_coins[current_amount]:
                min_coins[current_amount] = min_coins[current_amount - coin] + 1
                last_coin[current_amount] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result

if __name__ == "__main__":
    amount_1 = 946546
    print("Amount:", amount_1)
    print("Greedy:", find_coins_greedy(amount_1))
    print("Minimum coins:", find_min_coins(amount_1))
    amount_2 = 123
    print("Amount:", amount_2)
    print("Greedy:", find_coins_greedy(amount_2))
    print("Minimum coins:", find_min_coins(amount_2))