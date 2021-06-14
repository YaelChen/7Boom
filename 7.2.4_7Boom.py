
def seven_boom(end_number):
    """the function makes a game of "7 Boom" - it replace every number that contains "7" or divides by 7.
    :param end_number: the end number of the game.
    :type end_number: int
    :return all_nums: a list of all numbers in the game.
    :rtype all_nums: list"""
    all_nums = []
    for n in range(1, end_number + 1):
        if n % 7 == 0 or "7" in str(n):
            all_nums.append("Boom")
        else:
            all_nums.append(n)
    return all_nums


print(seven_boom(70))
