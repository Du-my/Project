#不停止一直循环输入
while True:
    # 输入语句
    tel=input("请输入手机号：(输入q退出):")
    if tel!="q":#判断是否为q
        if tel.isdigit():#此方法判断该字符串是否为数字组成
            if len(tel)==11:#判断字符串长度是否为11位
                # 使用字符串表达式判断字符串前三位数据区间是否在范围内
                if eval(tel[:3])>=130 and eval(tel[:3])<=150:
                    print("你输入的手机号是{}，属于移动".format(tel))#条件成立输入语句及把输入字符串值赋值format
                elif eval(tel[:3])>=151 and eval(tel[:3])<=170:
                    print("你输入的手机号是{}，属于联通".format(tel))
                elif eval(tel[:3])>=171 and eval(tel[:3])<=199:
                    print("你输入的手机号是{}，属于电信".format(tel))
                else:
                    print("你输入的电话号码是{}，不在号码段内".format(tel))
            else:
                print("你输入的电话号码是{}，长度是{}，位数不对".format(tel,len(tel)))
        else:
            print("你输入的电话号码是{}，输入的含有非数字".format(tel,len(tel)))
    else:
        break
