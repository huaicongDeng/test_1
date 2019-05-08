"""
1.学习目标
    熟悉Pandas读取excel表格
2.语法
    2.1 读取表文件
        table = pandas.read_excel(文件路径)
    2.2 读取默认前5行数据
        data = table.head()
    2.3 读取指定的单行，数据会存在列表里面
        table.ix[0].values
3.需求
    
4. 总结
    
"""
# 1.引包
import pandas

# # 读取表文件
# table = pandas.read_excel('./test_data.xlsx')
# # print(table.head())# 默认读取的是前5行的数据,不包括首行
# # print(table.ix[0].values)
# data = []
# for i in table.index.values:
#     data_dict = table.loc[i].to_dict()
#     data.append(data_dict)
# print(data)

class OperationExcel:
    def __init__(self,file_path):
        self.table = pandas.read_excel(file_path)
    def get_data_info(self):
        """获取表格详细信息"""
        data = []
        for i in self.table.index.values:
            data_dict = self.table.loc[i].to_dict()
            data.append(data_dict)
        return data

if __name__ == '__main__':
    operation = OperationExcel('../data/test_data.xlsx')
    print(operation.get_data_info())
