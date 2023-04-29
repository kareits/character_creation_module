# Тестовые данные.
from typing import List, Tuple

TEST_DATA: List[Tuple[int, str, bool]] = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep, rep_points, buf_effect) -> float:
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


def remove_rep(current_rep, rep_points, debuf_effect) -> float:
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep


def main(duel_res) -> str:
    current_rep: float = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return (f'После {len(duel_res)} поединков, репутация персонажа — '
            f'{current_rep:.3f} очков.')


# Тестовый вызов функции main.
print(main(TEST_DATA))
