class Isbn(object):
    def is_valid(self, num):
        num = num.replace('-', '').replace(' ', '')
        if len(num) != 13:
            return False
        product = (sum(int(ch) for ch in num[::2]) + sum(int(ch) * 3 for ch in num[1::2]))
        return product % 10 == 0