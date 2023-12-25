from datetime import datetime

def format_date_zh(value):
    if isinstance(value, datetime):
        return value.strftime('%Y年%m月%d日 %A %H:%M')
    return value
