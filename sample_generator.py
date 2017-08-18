# -*- coding: utf-8 -*-

import os

from config import Config

common_names = ['杨佳颖', '周曼坤', '叶钰婷', '郭竹裕', '袁世伟', '林山珠', '李俊德', '许嘉辉', '李宜旺', '赵秋义', '陈洁铭', '苏佳玲', '李惠美', '刘大钧', '陈慧娟', '周素禾', '蔡志其', '王信宏', '陈淑慧', '张函霞', '刘伟诚', '宗嘉祥', '罗乃育', '刘聿兴', '黎美娟', '郑伊忠', '陈琇顺', '傅美云', '张伟', '王伟', '王芳', '李伟', '李娜', '张敏', '李静', '王静', '刘伟', '王秀英']

data = [
  {
    'label' : 0,
    'description' : 'voice_output_on_off',
    'components' : [
      ['关闭', '打开'],
      ['语音', '语音播报', '播报']
    ]
  },
  {
    'label' : 1,
    'description' : 'phone_call',
    'components' : [
      ['请', ''],
      ['拨打', '查询', '查找', '打', '呼叫', '打给', '打电话给'],
      common_names,
      ['的', ''],
      ['手机', '电话', '座机', '号码']
    ]
  },
  {
    'label' : 2,
    'description' : 'send_message',
    'components' : [
      ['给', '向'],
      common_names,
      ['发信息', '发短信', '短信', '发简讯']
    ]
  },
  {
    'label' : 3,
    'description' : 'send_email',
    'components' : [
      ['给', '向'],
      common_names,
      ['发邮件', '写邮件', '发email', 'email', '写email']
    ]
  },
  {
    'label' : 4,
    'description' : 'navigation',
    'components' : [
      ['去', '导航', '到'],
      ['深圳', '广州', '上海', '长沙', ''],
      ['路', '街', '街道', '大道', ''],
      ['怎么走', '', '去怎么走', '的路线']
    ]
  },
  {
    'label' : 5,
    'description' : 'performance_dismissal',
    'components' : [
      ['查', '查询', '调出', ''],
      ['近期', ''],
      ['有', '', '有没有'],
      ['离职倾向员工', '哪些员工可能离职', '哪些员工可能会离职', '哪些员工有离职倾向']
    ]
  },
  {
    'label' : 6,
    'description' : 'performance_kpi',
    'components' : [
      ['查', '查询', '调出', ''],
      common_names + ['我'],
      ['的', ''],
      ['工作饱和度', '饱和度', 'kpi']
    ]
  },
  {
    'label' : 7,
    'description' : 'visit_website',
    'components' : [
      ['打开', '访问', '搜索', '上'],
      ['百度', '天猫', '淘宝', '新浪', '网易', '优酷', '爱奇艺', '京东'],
      ['网站', '的网站', '网址', '的网址', '网', '']
    ]
  },
  {
    'label' : 8,
    'description' : 'meeting_room_reservation',
    'components' : [
      ['订', '定', '预订', '预订', '帮我订下', '订下', '帮我预定', '帮我预订'],
      ['', '明天', '后天', '周一', '周二', '周三', '周四', '周五', '周六', '周日', '下周'],
      ['', '下午', '上午'],
      ['一点', '两点', '三点', '四点', '五点', '六点', '七点', '八点', '九点', '十点', '十一点', '十二点'],
      ['一人', '两人', '三人'],
      ['101号会议室', '203号会议室', '的会议室', '的教室', '的办公室', '的会议'],
      ['一', '两', '三'],
      ['个小时', '小时']
    ]
  },
  {
    'label' : 9,
    'description' : 'reminder',
    'components' : [
      ['提醒', '告诉'],
      ['', '我'],
      ['', '明天', '后天', '周一', '周二', '周三', '周四', '周五', '周六', '周日', '下周'],
      ['', '下午', '上午'],
      ['一点', '两点', '三点', '四点', '五点', '六点', '七点', '八点', '九点', '十点', '十一点', '十二点'],
      ['去上班', '去学校', '起床', '开会']
    ]
  },
  {
    'label' : 10,
    'description' : 'reminder_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['今天', '明天', '这周', '下周'],
      ['的日常', '日程', '日程安排', '我的日程']
    ]
  },
  {
    'label' : 11,
    'description' : 'meeting_reservation_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['今天', '明天', '这周', '下周'],
      ['的会议', '会议', '会议安排', '我的会议安排', '的会议安排']
    ]
  },
  {
    'label' : 12,
    'description' : 'meeting_room_reservation_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['会议室安排', '会议室安排情况', '会议室订阅情况', '会议室']
    ]
  },
  {
    'label' : 13,
    'description' : 'task_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['月度工作任务', '工作任务', '本月工作任务']
    ]
  },
  {
    'label' : 14,
    'description' : 'task_completion_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['月度工作任务', '工作任务', '本月工作任务'],
      ['完成情况', '的完成情况', '完成的如何', '做完了吗']
    ]
  },
  {
    'label' : 15,
    'description' : 'budget_execution_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['月度预算执行情况', '预算执行情况', '本月预算执行情况'],
      ['如何', '怎样']
    ]
  },
  {
    'label' : 16,
    'description' : 'reimbursement_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['本月', '当月', '这个月', '月度', ''],
      ['费用报销', '报销'],
      ['情况', '']
    ]
  },
  {
    'label' : 17,
    'description' : 'loan_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['本月', '当月', '这个月', '月度', ''],
      ['借款'],
      ['情况', '']
    ]
  },
  {
    'label' : 18,
    'description' : 'fee_receive_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['本月', '当月', '这个月', '月度', ''],
      ['应收款', '收款'],
      ['情况', '']
    ]
  },
  {
    'label' : 19,
    'description' : 'fee_payment_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['本月', '当月', '这个月', '月度', ''],
      ['应付款', '付款'],
      ['情况', '']
    ]
  },
  {
    'label' : 20,
    'description' : 'attendance_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['本月', '当月', '这个月', '月度', ''],
      common_names + [''],
      ['考勤', '考勤情况', '出勤', '的考勤', '的出勤率', '的考勤率', '考勤率', '出勤率']
    ]
  },
  {
    'label' : 21,
    'description' : 'business_trip_query',
    'components' : [
      ['查询', '查', '调出', ''],
      ['本月', '当月', '这个月', '月度', ''],
      common_names + [''],
      ['出差', '出差情况', '的出差情况']
    ]
  },
  {
    'label' : 22,
    'description' : 'weather',
    'components' : [
      ['查询', ''],
      ['', '明天', '后天', '周一', '周二', '周三', '周四', '周五', '周六', '周日', '下周一', '下周二', '下周三', '下周四', '下周五', '下周六', '下周日', '下周'],
      ['中国', '广州', '北京', '上海', '深圳', '长沙', '旧金山', '匹兹堡', '纽约', ''],
      ['的天气', '下雨吗', '天气怎样']
    ]
  },
  {
    'label' : 23,
    'description' : 'stock',
    'components' : [
      ['查询', '查', ''],
      ['花样年'],
      ['的股价', '股价', '股票', '股票情况']
    ]
  },
  {
    'label' : 24,
    'description' : 'joke',
    'components' : [
      ['讲个笑话', '给我讲个笑话', '请给我讲个笑话', '说个笑话', '说笑话'],
      ['听听', '来听听', '']
    ]
  },
  {
    'label' : 25,
    'description' : 'story',
    'components' : [
      ['讲个故事', '给我讲个故事', '请给我讲个故事', '说个故事', '说故事'],
      ['听听', '来听听', '']
    ]
  },
  {
    'label' : 26,
    'description' : 'news',
    'components' : [
      ['看新闻', '讲个新闻', '给我讲个新闻', '请给我讲个新闻', '说个新闻', '说新闻', '播报新闻', '播放新闻', '讲新闻'],
      ['听听', '来听听', '']
    ]
  },
  {
    'label' : 27,
    'description' : 'plane',
    'components' : [
      ['订', '定', '预订', '帮我订下', '订下', '帮我订'],
      ['', '明天', '后天', '周一', '周日'],
      ['', '下午', '上午'],
      ['一点', '三点', '六点', '十二点'],
      ['', '半'],
      ['', '从'],
      ['广州', '深圳', '香港', '北京', '上海', '长沙', '纽约', '旧金山', '巴黎', '匹兹堡'],
      ['飞', '去'],
      ['广州', '深圳', '香港', '北京', '上海', '长沙', '纽约', '旧金山', '巴黎', '匹兹堡'],
      ['的机票', '的飞机', '的飞机票', '的航班']
    ]
  },
  {
    'label' : 28,
    'description' : 'train',
    'components' : [
      ['订', '定', '预订', '帮我订下', '订下', '帮我订'],
      ['', '明天', '后天', '周一', '周日'],
      ['', '下午', '上午'],
      ['一点', '三点', '六点', '十二点'],
      ['', '半'],
      ['', '从'],
      ['广州', '深圳', '香港', '北京', '上海', '长沙', '纽约', '旧金山', '巴黎', '匹兹堡'],
      ['到', '去'],
      ['广州', '深圳', '香港', '北京', '上海', '长沙', '纽约', '旧金山', '巴黎', '匹兹堡'],
      ['的火车', '的高铁', '的火车票', '的动车']
    ]
  }
]


if __name__ == '__main__':
  dir_path = os.path.dirname(os.path.realpath(__file__))
  model_base_path = os.path.join(dir_path, Config.CURRENT_MODEL_BASE_PATH, 'data.nosync')
  if not os.path.exists(model_base_path):
    os.makedirs(model_base_path)

  count = 0
  for i, d in enumerate(data):
    label = int(d['label'])
    if i != label:
      print('Format error on {}'.format(i))
      assert i == label
    description = d['description']
    components = d['components']
    with open(os.path.join(model_base_path, '{}_{}.txt'.format(label, description)), 'w') as f:
      def s(si, sf):
        if si == len(components):
          f.write(sf + ' ' + str(label) + '\n')
        else:
          for comp in components[si]:
            s(si + 1, sf + comp)

      s(0, '')
