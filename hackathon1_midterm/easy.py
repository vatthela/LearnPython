# 1
import time
import datetime
from datetime import datetime as dt
def day_diff(release_date, code_complete_day):
    date_format_1 = "%d/%m/%Y"
    date_format_2 = "%Y-%d-%m"
    d1 = dt.strptime(release_date, date_format_1)
    d2 = dt.strptime(code_complete_day, date_format_2)
    compare=abs(d1-d2)
    return(compare.days)
# 2
def alpha_num(sentence):
    list = sentence.split()
    list_result = []
    print(list)
    for string in list:
        if (string.isalpha() == False):
            list_result.append(string)
    return (list_result)