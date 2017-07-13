# -*- coding: utf-8 -*-
import jieba

seg_list = jieba.cut("预订明天上午八点的会议室", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))
