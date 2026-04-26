from black_scholes import black_scholes_call


def implied_volatility(S, K, T, r, market_price):
    low = 0.001
    high = 1.5

    for _ in range(100):
        mid = (low + high) / 2
        price = black_scholes_call(S, K, T, r, mid)

        if price > market_price:
            high = mid
        else:
            low = mid

    return (low + high) / 2
