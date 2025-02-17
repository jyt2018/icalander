"""
ics_content: 这是 .ics 文件的内容, 包含以下部分: 
BEGIN:VCALENDAR 和 END:VCALENDAR: 表示一个日历对象的开始和结束。
VERSION:2.0: 指定 .ics 文件的版本。
BEGIN:VEVENT 和 END:VEVENT: 表示一个事件的开始和结束。
DTSTART:{event_time.strftime("%Y%m%dT%H%M%S")}: 指定事件的开始时间, 使用 strftime 函数将 datetime 对象格式化为 .ics 所需的字符串格式。
DTSTAMP:{datetime.now().strftime("%Y%m%dT%H%M%S")}: 表示 .ics 文件的创建时间戳。
UID:uid{datetime.now().strftime("%Y%m%d%H%M%S")}@example.com: 为事件生成一个唯一标识符。
DESCRIPTION:{title}的提醒: 描述事件。
SUMMARY:{title}: 事件的标题。
BEGIN:VALARM 和 END:VALARM: 表示一个提醒的开始和结束。
TRIGGER:-PT2H: 设置提醒触发器, -PT2H 表示提前两小时触发提醒。
ACTION:DISPLAY: 指定提醒的动作, 这里是显示提醒。
DESCRIPTION:Reminder: 描述提醒。
"""
from datetime import datetime, timedelta


def create_ics_reminder(event_time_str, title):
    """
    创建一个 .ics 文件的提醒事件

    :param event_time_str: 事件的开始时间，格式为 'yyyy-mm-dd hh:mm'
    :param title: 事件的标题
    """
    # 将输入的年、月、日、时、分转换为 datetime 对象
    event_time = datetime.strptime(event_time_str, "%Y-%m-%d %H:%M")

    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:{event_time.strftime("%Y%m%dT%H%M%S")}
DTSTAMP:{datetime.now().strftime("%Y%m%dT%H%M%S")}
UID:uid{datetime.now().strftime("%Y%m%d%H%M%S")}@example.com
DESCRIPTION:{title}的提醒
SUMMARY:{title}
BEGIN:VALARM
TRIGGER:-PT2H
ACTION:DISPLAY
DESCRIPTION:Reminder
END:VALARM
END:VEVENT
END:VCALENDAR"""

    # 创建一个文件并将 ics 内容写入其中
    with open(f"{title}.ics", "w", encoding="utf-8") as f:
        f.write(ics_content)


if __name__ == "__main__":
    event_time_str = input("请输入年月日时分, 格式为 'yyyy-mm-dd hh:mm': ")
    title = input("请输入标题: ")

    create_ics_reminder(event_time_str, title)
    print(f"已创建名为 {title}.ics 的日历提醒文件。")
