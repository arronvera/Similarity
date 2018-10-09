import numpy as np


###编辑距离算法
def distance(labels1, labels2):
    len1 = len(labels1)
    len2 = len(labels2)
    dic = np.zeros((len1 + 1, len2 + 1))
    for i in range(len1):
        dic[i][0] = i
    for j in range(len2):
        dic[0][j] = j
    for i in range(len1 + 1):
        if (i != 0):
            for j in range(len2 + 1):
                if (j != 0):
                    if (labels1[i - 1] == labels2[j - 1]):
                        temp = 0
                    else:
                        temp = 1
                    dic[i][j] = min(dic[i - 1][j - 1] + temp, dic[i][j - 1] + 1, dic[i - 1][j] + 1)

    max = len2
    if (len1 > len2):
        max = len1
    similarity = 1 - dic[len1][len2] / max
    return similarity


if __name__ == '__main__':
    labels1 = ["起亚", "实拍", "汽车", "新闻", "广州车展", "东风", "资讯", "飞机"]
    labels2 = ["广州", "现场", "汽车", "国际车展", "新闻", "首发", "资讯", "现代", "概念", "北京", "飞机"]
    sim = distance(labels1, labels2)
    print(sim)
