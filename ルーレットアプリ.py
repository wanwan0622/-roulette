# -*- coding: utf-8 -*-
import random

ALL = int(input()) #メンバー全員の人数
name =[] #メンバー全員人の名前（改行区切り）
for i in range(ALL):
    name.append(str(input()))
S = int(input()) #選ぶ人数
N = int(input()) #除外する人数
a=[] #除外する人の名前（改行区切り）
for i in range(N):
    a.append(str(input()))


if ALL <= S + N:
    print("エラー")

else:
    for i in a: #除外する人
        for j in name:
            if i == j:
                name.remove(i)
    #print(len(name), ALL - N)

    number = [ALL+1] * S #選んだ数
    for i in range(S):
        while True:
            tmp = random.randint(0, len(name) - 1)
            if not (tmp in number):
                number[i] = random.randint(0, len(name) - 1)
                break

    for i in range(S - 1):
        print(name[number[i]], end = ' ')
    print(name[number[S-1]])


"""
2020.03.06 問題点はルーレットの結果に重複があること。

テストケース
10
a
b
c
d
e
f
g
h
i
j
3
2
a
b
"""