import numpy as np

RANGE_MIN = 1
RANGE_MAX = 100

BENCHMARK_CYCLES = 1000


def binary_search_guesser(number):
    """Search number in range using binary search

    Args:
        number: int, number to search

    Returns:
        int, count of iterates
    """
    count = 0
    left = RANGE_MIN  # define left border of search range
    right = RANGE_MAX  # define right border of search range
    while left <= right:  # while search range is not collapsed into one number
        count += 1  # increment iterates counter
        mid = (left + right) // 2  # calculate middle of current search range with integer division
        if number == mid:  # if found
            return count  # return count of iterates
        if number < mid:  # if search number is lower than mid-range number
            right = mid - 1  # use left half of current range
        else:  # if search number is higher than mid-range number
            left = mid + 1  # use right half of current range
    raise ValueError('Number %d is not in range'% (number,))

def score_game(guesser_function):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(RANGE_MIN, RANGE_MAX + 1, size=BENCHMARK_CYCLES)
    for number in random_array:
        count_ls.append(guesser_function(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
score_game(binary_search_guesser)
