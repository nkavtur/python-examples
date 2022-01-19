from collections import defaultdict


def fruits_into_baskets1(fruits):
    basket1, basket2 = [], []
    basket1_type, basket2_type = None, None

    max_basket1, max_basket2 = [], []
    index = 0

    while index < len(fruits):
        current_fruit = fruits[index]

        if not basket1_type:
            basket1_type = current_fruit

        if basket1_type == current_fruit:
            basket1.append(current_fruit)
            index += 1
            if len(basket1) + len(basket2) > len(max_basket1) + len(max_basket2):
                max_basket1, max_basket2 = basket1, basket2
            continue

        if not basket2_type:
            basket2_type = current_fruit

        if basket2_type == current_fruit:
            basket2.append(current_fruit)
            index += 1
            if len(basket1) + len(basket2) > len(max_basket1) + len(max_basket2):
                max_basket1, max_basket2 = basket1, basket2
            continue

        if basket1_type != current_fruit and basket2_type != current_fruit:
            basket1, basket2 = [], []
            basket1_type, basket2_type = None, None
            index -= 1

    return len(max_basket1) + len(max_basket2)


assert fruits_into_baskets1(['A', 'B', 'C', 'A', 'C']) == 3
assert fruits_into_baskets1(['A', 'B', 'C', 'B', 'B', 'C']) == 5


def fruits_into_baskets2(fruits):
    window_start = 0
    baskets, total_number = set(), 0

    for window_end in range(len(fruits)):
        baskets.add(fruits[window_end])
        total_number += 1

        if len(baskets) > 2:
            baskets.remove(fruits[window_start])
            window_start += 1
            total_number -= 1

    return total_number


assert fruits_into_baskets2(['A', 'B', 'C', 'A', 'C']) == 3
assert fruits_into_baskets2(['A', 'B', 'C', 'B', 'B', 'C']) == 5
