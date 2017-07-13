# -*- coding: utf-8 -*-

## 1: meeting reservation
# components = [
#   ['订', '定', '预订', '预订', '帮我订下', '订下', '帮我预定', '帮我预订'],
#   ['', '明天', '后天', '周一', '周二', '周三', '周四', '周五', '周六', '周日', '下周'],
#   ['', '下午', '上午'],
#   ['一点', '两点', '三点', '四点', '五点', '六点', '七点', '八点', '九点', '十点', '十一点', '十二点'],
#   ['101号会议室', '203号会议室', '的会议室', '的教室', '的办公室', '的会议']
# ]
# label = 1
# path = './data.nosync/1_meeting_reservation.txt'

# # 7: meeting room cancellation
# components = [
#   ['取消', '取消预订', '取消掉', '帮我取消', '请取消'],
#   ['', '明天', '后天', '周一', '周二', '周三', '周四', '周五', '周六', '周日', '下周'],
#   ['', '下午', '上午'],
#   ['', '一点', '两点', '三点', '四点', '五点', '六点', '七点', '八点', '九点', '十点', '十一点', '十二点'],
#   ['的会议室', '预订的会议室']
# ]
# label = 7
# path = './data.nosync/7_meeting_room_cancellation.txt'

# # 2: alarm clock
# components = [
#   ['订', '预订', '帮我订下', '订下', '帮我订', '设置', '设定'],
#   ['', '明天', '后天', '周一', '周二', '周三', '周四', '周五', '周六', '周日'],
#   ['', '下午', '上午'],
#   ['一点', '两点', '三点', '四点', '五点', '六点', '七点', '八点', '九点', '十点', '十一点', '十二点'],
#   ['', '半', '十', '二十', '三十', '四十', '五十'],
#   ['', '分'],
#   ['的闹钟', '的提醒']
# ]
# label = 2
# path = './data.nosync/2_alarm_clock_set.txt'

# # 3: phone
# components = [
#   ['请', ''],
#   ['拨打', '查询', '查找', '打', '呼叫'],
#   ['杨佳颖', '周曼坤', '叶钰婷', '郭竹裕', '袁世伟', '林山珠', '李俊德', '许嘉辉', '李宜旺', '赵秋义', '陈洁铭', '苏佳玲', '李惠美', '刘大钧', '陈慧娟', '周素禾', '蔡志其', '王信宏', '陈淑慧', '张函霞', '刘伟诚', '宗嘉祥', '罗乃育', '刘聿兴', '黎美娟', '郑伊忠', '陈琇顺', '傅美云', '张伟', '王伟', '王芳', '李伟', '李娜', '张敏', '李静', '王静', '刘伟', '王秀英'],
#   ['的手机', '的电话', '的座机', '的号码', '的微信']
# ]
# label = 3
# path = './data.nosync/3_phone.txt'

# # 4: weather
# components = [
#   ['查询', ''],
#   ['', '明天', '后天', '周一', '周二', '周三', '周四', '周五', '周六', '周日', '下周一', '下周二', '下周三', '下周四', '下周五', '下周六', '下周日', '下周'],
#   ['中国', '广州', '北京', '上海', '深圳', '长沙', '旧金山', '匹兹堡', '纽约', ''],
#   ['的天气', '下雨吗', '天气怎样']
# ]
# label = 4
# path = './data.nosync/4_weather.txt'

# # 5: train
# components = [
#   ['订', '定', '预订', '帮我订下', '订下', '帮我订'],
#   ['', '明天', '后天', '周一', '周日'],
#   ['', '下午', '上午'],
#   ['一点', '三点', '六点', '十二点'],
#   ['', '半'],
#   ['', '从'],
#   ['广州', '深圳', '香港', '北京', '上海', '长沙', '纽约', '旧金山', '巴黎', '匹兹堡'],
#   ['到', '去'],
#   ['广州', '深圳', '香港', '北京', '上海', '长沙', '纽约', '旧金山', '巴黎', '匹兹堡'],
#   ['的火车', '的高铁', '的火车票', '的动车']
# ]
# label = 5
# path = './data.nosync/5_train_reservation.txt'

# # 6: plane
# components = [
#   ['订', '定', '预订', '帮我订下', '订下', '帮我订'],
#   ['', '明天', '后天', '周一', '周日'],
#   ['', '下午', '上午'],
#   ['一点', '三点', '六点', '十二点'],
#   ['', '半'],
#   ['', '从'],
#   ['广州', '深圳', '香港', '北京', '上海', '长沙', '纽约', '旧金山', '巴黎', '匹兹堡'],
#   ['飞', '去'],
#   ['广州', '深圳', '香港', '北京', '上海', '长沙', '纽约', '旧金山', '巴黎', '匹兹堡'],
#   ['的机票', '的飞机', '的飞机票']
# ]
# label = 6
# path = './data.nosync/6_plane_reservation.txt'

# # 8: reminder
# components = [
#   ['提醒', '告诉'],
#   ['', '我'],
#   ['', '明天', '后天', '周一', '周二', '周三', '周四', '周五', '周六', '周日', '下周'],
#   ['', '下午', '上午'],
#   ['一点', '两点', '三点', '四点', '五点', '六点', '七点', '八点', '九点', '十点', '十一点', '十二点'],
#   ['去上班', '去学校', '起床']
# ]
# label = 8
# path = './data.nosync/8_reminder.txt'

with open(path, 'w') as f:
  def s(si, sf):
    if si == len(components):
      f.write(sf + ' ' + str(label) + '\n')
    else:
      for comp in components[si]:
        s(si + 1, sf + comp)

  s(0, '')