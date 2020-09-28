import random
class Gift:
    def __init__(self, x, n):
        self.remain_size = n
        self.remain_money = x


def getMoney(gift):
    if gift.remain_size == 1:
        return gift.remain_money

    min = 0.01
    max =