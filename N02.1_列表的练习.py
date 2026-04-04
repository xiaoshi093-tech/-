#有请出场嘉宾，哈哈哈
guests =["史浩东","史靖东","爱因斯坦"]
for guest in guests:
    print(f"\n尊敬的{guest},诚挚邀请您与我共进晚餐，期待您的到来！")

#利用列表中的替换功能[]，准确的替换人名
print("===嘉宾名单更新===")
print("sorry,史浩东帅哥因行程冲突无法赴约。")
guests[0]="王瑞兵"
print("更新后的邀请：")
for guest in guests:
    print(f"尊敬的{guest},诚挚邀请您与我共进晚餐，期待您的到来！")

# 用guests.insert给名单的准确位置添加了人名，并用append给最后加了人名
print("\n===新增嘉宾邀请===")
print("为了使得宴会更加的热闹，我们将邀请更多的亲朋好友！")
guests.insert(0, "王翠琴")
guests.insert(2, "王晋琴")
guests.append("史利平")
print("完整邀请名单：")
for guest in guests:
    print(f"\n尊敬的{guests},诚挚邀请您与我共进晚餐，期待您的到来！")

# 用while将列表中大于等于2的人名全部删掉，重新生成了名单
print("\n===最终名单调整===")
print("非常抱歉，由于买的饭菜不够，我只能邀请两位朋友了")
while len(guests)>2:
    removed_guest=guests.pop()
    print(f"尊敬的{removed_guest},非常抱歉，由于买的饭菜不够，无法邀请您赴约了。")
print("\n最终保留邀请：")
for guest in guests:
    print(f"尊敬的{guest},您依然在我的邀请名单中，期待与您共进晚餐！")

# 用del删掉了最后俩个人
del guests[0]
del guests[0]
print("\n最终嘉宾名单：",guests)