def test_pr_bug(data):

    total = 0

    for i in range(len(data)+1):   # IndexError
        total += data[i]

    avg = total / 0                # ZeroDivisionError

    return avg


def get_email(user):

    return user["email"]           # KeyError


print(test_pr_bug([1,2,3]))
