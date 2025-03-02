import datetime
def datecount(start, step):
    step = step.lower()
    while True:
        yield start
        
        if step == "daily":
            start += datetime.timedelta(days=1)
        elif step == "weekly":
            start += datetime.timedelta(weeks=1)
        elif step == "alternative":
            start += datetime.timedelta(days=2)
        elif step == "monthly":
            year = start.year
            month = start.month + 1 
            if month > 12:
                month = 1  
                year = year + 1
            start = start.replace(year=year, month=month)  
        elif step == "quarterly":
            year = start.year
            month = start.month + 3 
            if month > 12:
                month =month -12  
                year =year + 1
            start = start.replace(year=year, month=month) 
        elif step == "yearly":
            start = start.replace(year=start.year + 1)
        else:
            return "Invalid"

start = datetime.date.today()
step = input("Enter the step from the list ['alternative', 'daily', 'weekly', 'monthly', 'quarterly', 'yearly']:")
result = datecount(start, step)
for i in range(10):
    print(next(result))