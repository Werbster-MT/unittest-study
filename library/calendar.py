from datetime import datetime

def is_weak_day():
    today = datetime.today()
    # 0 is monday and 6 is sunday
    return (0 <= today.weekday() < 5)
