# 这是第二段联系代码，我学到了对于列表数据的添加和删减
motorcycles = ["honda","yamaha","suzuki"]
#对于我上述创建的列表来说第一个单词是honda，但是python语法中规定是从0开始的，接下来我要先尝试删除第一个元素honda，之后尝试删除suzuki。最后我还要添加一个新元素进去
print(motorcycles)
del motorcycles[0]
# 这里我删除了第一个元素honda
print(motorcycles)
del motorcycles[1]
# 这里我删除了第二个元素yamaha
print(motorcycles)
motorcycles.append("shihaodong")
# 这里我添加了自己哈哈哈，其中append是添加到列表的末尾
print(motorcycles)
#到这里我对比了昨天的第一段代码，第一段代码用的是字典｛｝是属于一种无序的排列不能用数字读取，而今天我学到了列表[]是属于一种有序的排列可以按数字读取
motorcycles.insert(0,"duoduo")
# insert是添加到列表的指定位置
print(motorcycles)
motorcycles.remove("yamaha")
#remove 用来固定删除列表中你需要删除的东西
print(motorcycles)

too_expensive="shihaodong"
motorcycles.remove(too_expensive)    #这里我刚开始打了remove（“too_expensive”）这种写法导致了报错。我将shihaodong赋值给了变量too_expensive
print(motorcycles)
print(f"\n{too_expensive.title()} is too expensive for me")
