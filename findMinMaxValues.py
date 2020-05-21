# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:12:38 2020
@author: XeniaLin

5/21 實作練習
宣告一整數串列(大小為5)傳遞給 output(aList)函式
函式由輸入初始化後回傳給主程式並輸出該串列
再由主程式將該串列傳給max(aList)及min(aList)函式
輸出aList之最大值及最小值
(不可使output(list1)用系統函式)
"""
def output(x):
    import random
    for n in range(5):
        randNum = random.randint(1,99)
        x.append(randNum)

def findMax(x):
    maxValue = x[0]
    for n in range(1,len(x)):
        if x[n] > maxValue:
            maxValue = x[n]
    return maxValue

def findMin(x):
    minValue = x[0]
    for n in range(1,len(x)):
        if x[n] < minValue:
            minValue = x[n]
    return minValue

list1 = []
output(list1)
print('List1=', list1)
print('Max Value = %2d' % findMax(list1))
print('Min Value = %2d' % findMin(list1))
