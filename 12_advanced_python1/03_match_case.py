def http_status(status):
    match status:
        case 200:
            return "ok"
        case 400:
            return "Not Found"
        case 568:
            return "Error"
        case _:
            return "Unknown Status"
        
print(http_status(333))


# merge

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged)