# # l = [10,20,30,40,50,"hello","a",True,5.6]
# # l1 = list((10,20,30,40,50))
# # print(l)
# # print(type(l))
# # print(len(l))

# # x = list((1,2,3,4,5))
# # print(x)

# # print(l1)
# # print(l[-1])
# # print(l[1:4])
# # print(l[1:])
# # print(l[:4])
# # print(l[:])
# # print(l[::2])
# # print(l[::-1])
# # print(l1[::2])
# # print((l[2:5:2]))
# # print(l1[-1:-6:-1])
# # print(l[::-1])

# # x[1] = "sql"
# # x.insert(2,"python")
# # x.append("java")
# # x.extend(["c","c++","html"])
# # print(x)
# # x.remove("sql")
# # x.pop()
# # x.pop(2)
# # x.clear()
# # # del x
# # # print(x)
# # x[2:4] = [100,200,300]
# # print(x)

# # for i in l:
# #     print(i)

# # for i in range(len(l)):
# #     print(l[i])

# # i = 0
# # while i < len(l):
# #     print(l[i])
# #     i += 1

# # # listcomprehension

x = ["python","java","java","c","c++","html","css","js"]
# # y = [i for i in x if "c" in i]
# # print(y)    

# # for i in x:
# #     if "p" in i:
# #         y.append(i)

# # # y = [i for i in x if 'a' in i]
# # y = ["abc"   for i in x]
# # print(y)

# x.sort
# x.sort(reverse=1)
# x.reverse()
# print(x)

y = x.copy()
y = x.count("java")
y = x.index("c++")
print(y)
