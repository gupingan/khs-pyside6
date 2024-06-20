# Created by Gu Pingan on 2023/11/21
# GitHub: https://github.com/gupingan
import datetime
import calendar


# 获取当前日期和时间
def get_current_datetime():
    return datetime.datetime.now()


# 格式化日期和时间
def format_datetime(dt: datetime.datetime, format='%Y-%m-%d %H:%M:%S'):
    return dt.strftime(format)


# 获取当前日期
def get_current_date():
    return datetime.date.today()


# 获取当前时间
def get_current_time():
    return datetime.datetime.now().time()


# 获取指定日期的下一天
def get_next_day(date):
    return date + datetime.timedelta(days=1)


# 获取指定日期的前一天
def get_previous_day(date):
    return date - datetime.timedelta(days=1)


# 计算两个日期之间的天数差
def get_days_diff(start_date, end_date):
    return (end_date - start_date).days


# 将字符串解析为日期对象
def parse_date(date_str, format='%Y-%m-%d'):
    return datetime.datetime.strptime(date_str, format).date()


# 将字符串解析为日期时间对象
def parse_datetime(datetime_str, format='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.strptime(datetime_str, format)


# 将时间戳转换为日期时间对象
def timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)


# 将日期时间对象转换为时间戳
def datetime_to_timestamp(dt):
    return dt.timestamp()


# 根据年份和月份获取该月的日历
def get_month_calendar(year, month):
    return calendar.monthcalendar(year, month)


# 获取当前月的日历
def get_current_month_calendar():
    now = datetime.datetime.now()
    return get_month_calendar(now.year, now.month)
