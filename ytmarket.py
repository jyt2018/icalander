"""
该程序生成一个包含特定市场活动的 .ics 日历文件。
市场活动基于农历日期，并转换为公历日期。
活动包括 "北陈大集"、"凤凰山大集"、"莱山大集"、"解甲庄大集"、"前七夼早市"、"西轸大集"、"于家滩大集" 和 "院格庄大集"。
"""

from icalendar import Calendar, Event
from datetime import datetime, timedelta
from lunardate import LunarDate

def create_event(summary, start_date):
    """
    创建一个日历事件

    :param summary: 事件的标题
    :param start_date: 事件的开始日期
    :return: icalendar.Event 对象
    """
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', start_date)
    event.add('dtend', start_date + timedelta(days=1))
    return event

cal = Calendar()

# 定义市场活动的日期和标题
market_days = {
    "北陈": [3, 6, 8, 10, 13, 16, 18, 20, 23, 26, 28, 30],
    "凤凰于家滩": [5, 10, 15, 20, 25, 30],
    "莱山西轸": [2, 7, 12, 17, 22, 27],
    "解甲庄": [1, 6, 11, 16, 21, 26],
    "西轸凤凰": [2, 7, 12, 17, 22, 27],
    "院格庄": [4, 9, 14, 19, 24, 29],
    "黄务": [1, 5, 11, 15, 21, 25]
}

for year in range(2025, 2042):
    for month in range(1, 13):
        for summary, days in market_days.items():
            for day in days:
                try:
                    lunar_date = LunarDate(year, month, day) # 创建农历日期对象,比如农历2025年正月十五
                    date = lunar_date.toSolarDate()
                    event = create_event(summary, date)
                    cal.add_component(event)
                except ValueError:
                    # 忽略无效的农历日期
                    continue

# 将日历写入文件
with open("market_events.ics", "wb") as f:
    f.write(cal.to_ical())
