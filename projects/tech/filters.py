from datetime import datetime

def format_date_zh(value):
    weekdays_en_to_zh = {
        "Monday": "星期一",
        "Tuesday": "星期二",
        "Wednesday": "星期三",
        "Thursday": "星期四",
        "Friday": "星期五",
        "Saturday": "星期六",
        "Sunday": "星期日",
    }
    
    if isinstance(value, datetime):
        weekday_en = value.strftime('%A')
        weekday_zh = weekdays_en_to_zh.get(weekday_en, weekday_en)
        return value.strftime('%Y年%m月%d日 ') + weekday_zh + value.strftime(' %H:%M')
    return value

