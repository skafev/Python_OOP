class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    @staticmethod
    def divide(*args):
        result = 0
        first_divide = args[0]
        second_divide = args[1]
        result = first_divide / second_divide
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for x in args[1:]:
            result = result - x
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
