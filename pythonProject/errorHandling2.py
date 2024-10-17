def vote(age):
    if age<18:
        raise ValueError("Value is error")
    return "he is a voter"
try:
    print(vote(20))
    print(vote(9))
    print(vote(20))

except ValueError as e:
    print(e)