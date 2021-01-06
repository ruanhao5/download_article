import pandas as pd
import numpy as np
import xlwt     # 导入第三方库xlwt，用于写入excel文件
from Article import Article

for citation in range(23):
    # for citationNum in range(24):
    # 读取数据
    data = pd.read_csv(r"citations (%d).csv" % (citation+1))
    data = np.array(data)
    rows = data.shape[0]  # get sheet rows

    # 新建工作簿
    new_workbook = xlwt.Workbook()      
    worksheet = new_workbook.add_sheet('new_test')      # 新建工作表，new_test为工作表名称，无参数默认Sheet1

    rowIndex = 1
    # 写入数据
    for row in range(rows):
        journal = Article(data[row])

        # 写入作者信息
        authors, authorsNum = journal.authorsList()
        for i in range(authorsNum):
            worksheet.write(rowIndex + i, 2, authors[i])
        
        # 写入论文信息
        info = journal.articleInfo()
        worksheet.write_merge(rowIndex, rowIndex+authorsNum-1, 1, 1, info)  # （a,b,c,d,str）从第a行到第b行，第c列到第d列
        
        # 写入序号
        worksheet.write_merge(rowIndex, rowIndex+authorsNum-1, 0, 0, row+1)

        rowIndex = rowIndex + authorsNum + 1

    # 保存工作簿，参数为保存路径
    new_workbook.save(r'C:\Users\RH\Desktop\bug123\test(%d).xls' % (citation+1))       
