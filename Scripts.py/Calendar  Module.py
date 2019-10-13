import calendar
n=list(map(int,input().split()))
day=calendar.weekday(n[2],n[0], n[1])
dizionario={0:'MONDAY',1:'TUESDAY',2:'WEDNESDAY',3:'THURSDAY',4:'FRIDAY',5:'SATURDAY','6':'SUNDAY'}
print(dizionario[day])
