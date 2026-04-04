import pandas as pd
#第一次运行时,提示没有pandas模块,需要安装，由于我之前用过python安装过pandas，后来检查发现右下角解释器有问题，我换了一个python解释器
#1.现在我是在创建一个简单的表格数据
date = {
    "姓名":["小明","小红","小刚"],
    "年龄":[20,21,19],
    "成绩":[85,92,95]
}
#2.这一部分可以将上述创建的表格数据转化给pandas表格
df = pd.DataFrame(date)
print("完整数据：")
print(df)
print("\n前2行数据:")
print(df.head(2))
print("\n只看成绩列:")
print(df["成绩"])
print("\n成绩平均值:")
print(df["成绩"].mean())
print("\n筛选成绩大于80的同学:")
print(df[df["成绩"]>80])