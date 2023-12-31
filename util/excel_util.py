# -*- coding:utf-8 -*-
# 作者：郭晓华
# 时间：2022/9/29
import xlrd
from xlutils.copy import copy
import time
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = '../config/casedata.xls'
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]


    # 获取excel行数
    def get_lines(self):
        #行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return rows

    # 获取excel列数
    def get_cols(self):
        #列数
        cols = self.table.ncols
        if cols >= 1:
            return cols
        return cols


    # 获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        clos = self.get_cols()
        if rows != None and clos != None:
            for i in range(rows):
                # 拿到数据
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    #获取单元格数据
    def get_col_value(self,row,col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    # # 获取excel中特殊值
    # def get_ctype(self):
    #     rows = self.get_lines()
    #     cols = self.get_cols()
    #     for i in rows:
    #         for j in cols:
    #             data_cy = self.table.cell(i,j).ctype
    #             if data_cy == 0:
    #                 data_cy = data_cy
    #             elif data_cy == 2:
    #                 data_cy = int(data_cy)
    #    return data

    #转化数据-浮点数转化为int
    def get_change_value(self):
        result_data = self.get_data()
        for row in result_data:
            for i in row:
                if type(i) == float:
                    index = row.index(i)
                    i = int(i)
                    row[index] = i
                # elif i == '':
                #     index = row.index(i)
                #     print(index)
                #     i = 0
                #     row[index] = i
        return result_data

    #写入数据
    def write_value(self,row,col,value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,col,value)
        write_data.save(self.excel_path)
        time.sleep(2)


if __name__ == '__main__':
    ex = ExcelUtil()
    # print(ex.get_lines())
    # print(ex.get_data())
    # print(5655788767,ex.get_col_value(0,1))
    # print(ex.write_value(9,1,123456))
    print(ex.get_change_value())