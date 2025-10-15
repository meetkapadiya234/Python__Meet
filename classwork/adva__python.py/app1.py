# # f = open("test.txt", "r")
# # data = f.readlines()
# # k = filter(lambda x: 'line' in x, data)
# # print(list(k))
# # f.close() 
# # find a length of a file
# f = open("test.txt", 'w')
# f.write("Hello, World!")
# f.writelines(["\nThis is line 1.", "\nThis is line 2."])
# f.close()
# print(len(open("test.txt").readlines()))

# with open("test.txt", 'r') as f:
#     print(f.tell())
#     f.seek(3)
#     data = f.read()
#     print(f.tell())
#     print(data)

# with open("hello.txt", 'w+') as f:
#     f.write("Hello, World!")
#     f.seek(0)
#     data = f.read()
#     print(data)



