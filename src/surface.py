import numpy as np
from black_scholes import black_scholes_call
from implied_vol import implied_volatility


def generate_surface(S, r, strikes, maturities):
    K_grid, T_grid = np.meshgrid(strikes, maturities)

    moneyness = np.log(K_grid / S)

    true_vol_surface = (
        0.20
        + 0.80 * moneyness**2
        - 0.35 * moneyness
        + 0.25 * np.exp(-2.0 * T_grid)
        + 0.15 * moneyness**2 * T_grid
    )

    market_prices = black_scholes_call(S, K_grid, T_grid, r, true_vol_surface)

    iv_surface = np.zeros_like(K_grid, dtype=float)

    for j in range(len(maturities)):
        for i in range(len(strikes)):
            iv_surface[j, i] = implied_volatility(
                S, K_grid[j, i], T_grid[j, i], r, market_prices[j, i]
            )

    return K_grid, T_grid, true_vol_surface, market_prices, iv_surface
