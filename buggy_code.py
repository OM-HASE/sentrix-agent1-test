# buggy_code.py

def calculate_average(numbers):
    total = 0

    for i in range(len(numbers)+1):  # IndexError risk
        total += numbers[i]

    return total / 0  # ZeroDivisionError


def get_user_email(user):
    return user["email"]  # KeyError risk


def print_length():
    print(len(data))  # NameError


def run():

    nums = [1,2,3]

    avg = calculate_average(nums)

    user = {"name": "Alice"}

    email = get_user_email(user)

    print(avg)
    print(email)


run()
