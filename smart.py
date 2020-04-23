import  random

usename = input('请输入账号:')
passward = input('请输入密码:')
bot = input('请输入你使用的bot(Cyber,EVE,TKS,MEK):')
diqu = input('请输入你想要的地区(us,ca,gb,de):')
proxy_num = input('请输入你所需的proxies:')
if (bot == 'Cyber' or bot == 'EVE' or bot =='TKS' or bot == 'MEK') and (diqu == 'us' or diqu == 'ca' or diqu == 'gb' or diqu == 'de'):
    result = []
    i = 0
    while i < int(proxy_num):
        ran_str = random.randint(10000, 99999)
        a = diqu+'.smartproxy.com'+':'+str(ran_str)+':'+usename+':'+passward
        result.append(a)
        i += 1

    E_path = "E:/test/"
    full_path = E_path + bot +'.txt'
    file = open(full_path,'w')
    file.write(str(result))
else:
    E_path = "E:/test/"
    full_path = E_path + bot + '.txt'
    file = open(full_path, 'w')
    file.write('输入信息有误，请重新输入')



#def text_create(name, msg):
    #E_path = "E:/test/"
    #full_path = E_path + name + '.txt'
    #file = open(full_path, 'w')
    #file.write(msg)
#text_create(bot,str(result))
