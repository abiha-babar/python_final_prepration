class MyFactory:
    @staticmethod
    def get_max(*args, **kwargs):
        print(kwargs)
        return max(args)


# YOU ARE ABOUT TO WRITE A UTILITY CLASS MyFactory which provide me various methods
# NOTE THAT UTILITY CLASS IS THAT WHICH CAN NOT BE INSTANTIATED.

# 1. Write a method that takes two arguments and returns the maximum of the two.

print(MyFactory.get_max(100, 50, 1, d=100, a=10, b=20))  # 100
