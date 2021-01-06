import pandas as pd
import numpy as np


class Article(object):
    """
    根据 Google scholar 导出的CSV文件，进行提取信息：文章引用、作者
    """
    def __init__(self, data):
        self.Authors = data[0]
        self.Title = data[1]
        self.Publication = data[2]
        self.Volume = data[3]    # number
        self.Number = data[4]    # number
        self.Pages = data[5]     # str
        self.Year = data[6]      # number

    # 论文的引用信息，格式为：标题，期刊，vol(no),pp,year
    def articleInfo(self):
        info = self.Title + ',' + str(self.Publication) + ',' + str(self.Volume) + \
            '(' + str(self.Number) + '),' + str(self.Pages) + ',' + str(self.Year)
        return info

    # 论文的各个作者
    def authorsList(self):
        authors = self.Authors.strip()[0:-1].split(';')     # 人名分开
        authors = [i.strip() for i in authors]     # 去除空格
        authorsNum  = len(authors)
        return authors, authorsNum


if __name__ == "__main__":
    # 读取数据
    data = pd.read_csv("citations.csv")
    data = np.array(data)
    journal = Article(data[1])

    print(journal.articleInfo())
    print(journal.authorsList())