"""Mix two colors from values stored in farger.json."""

import json
from pathlib import Path


def mix_colors():
    """Mix two colors with a given ratio."""
    with Path('farger.json').open('r', encoding='utf-8') as file:
        data = json.load(file)
        col_a = data['colA']
        col_b = data['colB']
        ratio_b = data['rationB']
    return int(col_a * (1 - ratio_b) + col_b * ratio_b)


print(mix_colors())
