from zwpython import*
from zwpy.pywebio_zw import 输入框,输出表格,输出文本
from zwpy.openpyxl_zw import 电子表格
文件1=电子表格('万载2024年4月工资明细.xlsx')
表1=文件1[0]
用户输入=输入框('请输入名字单量:')
for 行 in 范围(2,表1.最大行+1):
    if 字符串(表1.单元格(行,1).值)==用户输入:
     输出表格([表1[1].所有值,表1[行].所有值])
