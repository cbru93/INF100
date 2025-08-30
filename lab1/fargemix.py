"""Mix two colors from values stored in farger.json."""

import json
from pathlib import Path


def mix_colors():
    """Mix two colors with a given ratio."""
    with Path('farger.json').open('r', encoding='utf-8') as file:
        data = json.load(file)
        col_a = data['colA']
        col_b = data['colB']
        # Accept both the correct key and the common misspelling
        ratio_b = data.get('ratioB', data.get('rationB'))

    def split_rgb(value: int):
        r = value // 1_000_000
        g = (value // 1_000) % 1_000
        b = value % 1_000
        return r, g, b

    def combine_rgb(r: int, g: int, b: int) -> int:
        return r * 1_000_000 + g * 1_000 + b

    r_a, g_a, b_a = split_rgb(col_a)
    r_b, g_b, b_b = split_rgb(col_b)

    r_mix = round(r_a * (1 - ratio_b) + r_b * ratio_b)
    g_mix = round(g_a * (1 - ratio_b) + g_b * ratio_b)
    b_mix = round(b_a * (1 - ratio_b) + b_b * ratio_b)

    return combine_rgb(r_mix, g_mix, b_mix)


print(mix_colors())
