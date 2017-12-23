from functools import reduce

class Luhn(object):
    def __init__(self, string):
        self.string = string.strip().replace(" ", "")

    def is_valid(self):
        if (self.string.isdigit()):
            if self.string == "0":
                return False

            num_repr = list(reversed(list(map(int, list(self.string)))))
            num_oper = []
            for i in range(0, len(num_repr)):
                if i % 2 != 0:
                    num = num_repr[i] * 2;
                    if num > 9:
                        num = num - 9
                    num_oper.append(num)
                else:
                    num_oper.append(num_repr[i])

            num_red = reduce(lambda x, y: x+y, num_oper, 0)
            return num_red % 10 == 0
        else:
            return False


print(Luhn("059").is_valid())