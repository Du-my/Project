#循环输入手机号
while True:
    tel= input('请输入要查询的手机号：（输入q退出查询）:')
    if tel!='q':
        if tel.isdecimal():
            if len(tel)==11:
                  if eval(tel[:3])>=130 and eval(tel[:3])<=150:
                      print('您输入的电话为{}，属于移动'.format(tel,len(tel)))
                  elif eval(tel[:3])>=151 and eval(tel[:3])<=170:
                      print('您输入的电话为{}，属于联通'.format(tel,len(tel)))
                  elif eval(tel[:3]) >= 171 and eval(tel[:3]) <= 199:
                      print('您输入的电话为{}，属于电信'.format(tel, len(tel)))
                  else:
                      print('您输入的号码为{}，不在手机号码段内'.format(tel,len(tel)))
            else:
                print('您输入的电话为{}，长度为{}，位数不对')
        else:
            print('您输入的电话为{},输入含有非数字', format(tel, len(tel)))
    else:
        break