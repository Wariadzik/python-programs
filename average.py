def get_average(*numbers):
    try:
        return sum(numbers)/len(numbers)
    except:
        return "Wrong data"
print(get_average(2,4,7,4))