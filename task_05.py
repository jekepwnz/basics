from datetime import datetime, timedelta

def date_in_future(integer):
    if not isinstance(integer, int):
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    else:
        res: str = (datetime.now() + timedelta(days=integer)).strftime('%d-%m-%Y %H:%M:%S')
        return res

