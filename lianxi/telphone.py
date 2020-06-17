
#循环输入判断手机号归属地；
while True:
    tel = input('请输入要查询的手机号（回复t退出）')
    typetel = tel[:3]
    if tel!='t':     #判断输入内容是否为t
        if tel.isdigit():     #判断输入内容是否为纯数字
             if len(tel)==11:     #判断手机号是否为11位
                if typetel>=str(130) and typetel<= str(150):
                    print('你查询的手机号为{},该号码属于移动'.format(tel))
                elif typetel>=str(151) and typetel<= str(170):
                    print('你查询的手机号为{},该号码属于联通'.format(tel))
                elif typetel>=str(171) and typetel<= str(199):
                    print('你查询的手机号为{},该号码属于电信'.format(tel))
                else:
                    print('您查询的数据不属于手机号类型，请重新输入')
             else:
                print('查询的手机号位数不正确, 请重新输入')
        else:
            print('查询的手机号格式不正确，含有非数字')
    else:
      break   #跳出循环；

