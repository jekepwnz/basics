from datetime import datetime, timedelta

def date_in_future(integer):
    if type(integer) is not int:
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    else:
        res: str = (datetime.now() + timedelta(days=integer)).strftime('%d-%m-%Y %H:%M:%S')
        return res




# date_in_future([]) # => текущая дата
# date_in_future(2) # => текущая дата + 2 дня

print(date_in_future([])) # => текущая дата
print(date_in_future(2)) # => текущая дата + 2 дня