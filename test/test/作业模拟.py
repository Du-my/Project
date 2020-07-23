#618作业模拟

# sreStr = 'A old lady come in, the name is Mary, level 94454'
# def getName(fileName):
#     res = fileName.split('the name is')[1].split(',')[0]
#     print(res)
# getName(sreStr)


#619作业模拟第一题
# infoStudent = input('')
# temp = infoStudent.split(';')
# for one in temp:
#     if ',' not in one:
#         continue
#     name,age =one.split(',')
#     name = name.strip()
#     age = age.strip()
#
#     if not age.isdigit():
#         continue
#     age = int(age)
#     print(f'{name:20}:{age:02}')


#619作业模拟第二题
# log = '''
# f20180111014341/i_51a7hC3W.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156063244230469	image/jpeg	0
# f20180111014341/j_R0Hpl4EG.json	1036	ForGzwzV3e-uR3_UzvppJs1VgfQG	15156064773253144	application/json	0
# f20180111020739/i_0TDKs0rD.jpeg	169472	FrITJxleSP7wUD-MWw-phL_KP6Eu	15156076847077556	image/jpeg	0
# f20180111090619/i_1BwNksbL.jpg	49634	FtXBGmipcDha-67WQgGQR5shEBu2	15156329458714950	image/jpeg	0
# f20180111090619/j_i1K74768.json	3042	Fl5PpDw1TsZXMuhoq1RUrOeGZ6br	15156335067090003	application/json	0
# f20180111095839/i_Q7KMKeda.png	518522	Fl-yB1_ruL2uxZN9k7DjB62h9dYH	15156359599713253	image/png	0
# f20180111100442/i_No8kToIV.jpg	48975	Fu1cw3f--5Vpz9kLGeJfvljhCtyZ	15156364349642377	image/jpeg	0
# f20180111142119/i_s83iZ2GR.png	92278	Fns8tdh3JCkRmfE_COYEu4o8w03E	15156517082371259	image/png	0
# f20180111144306/i_yE5TC84E.png	139230	Fjf61ymabEnEvnr5ZMHFjXGCrYlP	15156530038824150	image/png	0
# f20180111144306/j_OF4WVtSH.json	159	FqwkKcxfo8jd0jFUyuH4X2CrnE9q	15156530083419530	application/json	0
# f20180111150230/i_KtnER4g3.png	120044	FuwOWdrqzcr2-UScem-LzEMgMezs	15156541734892258	image/png	0
# f20180111150230/j_xMSUEejY.json	158	FjJr_4deMqFphGaptm-2Pa6wwRP2	15156541771989216	application/json	0
# f20180111151741/i_JuSWztB3.jpg	92506	FrIjRevHSi6xv4-NQa2wrHu5a1zQ	15156550875370965	image/jpeg	0
# f20180111153550/i_9wWzVenl.gif	769872	FvslKY9JUaCQm-lu02E34tvAP_oG	15156561674621628	image/gif	0
# '''
# relist=[]
# lines = log.split('\n')
# del lines[0],lines[-1]
# for line in lines:
#     temp = line.split('\t')
#     fileType = temp[0].split('.')[-1].strip()
#     fileSize = int(temp[1].strip())
#     inFlage = False
#     for one in relist:
#         if one[0] == fileType:
#             one[1]+=fileSize
#             inFlage =True
#             break
#     if inFlage==False:
#         relist.append([fileType,fileSize])
#
# print(relist)


#621作业模拟第一题
inList= [1,2,5,7,8,0,766,444,6776,242,999,-1,-75,888]
def mySort(inList):
    newList = []
    while len(inList)>0:
        minData = min(inList)
        newList.append(minData)
        inList.remove(minData)
    return newList
print(mySort(inList))






