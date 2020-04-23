import  random
import string

usename = input('请输入账号:')
passward = input('请输入密码:')
bot = input('请输入你使用的bot(Cyber,EVE,TKS,MEK):')
diqu = input('请输入你想要的地区(US-1,US-2,US-3):')
proxy_num = input('请输入你所需的proxies:')
result = []
i = 0
while i < int(proxy_num):
    ran_str = ''.join(random.sample(string.digits, 8))
    a = diqu+'-1.geosurf.io:8000:'+usename+'+US'+'+'+usename+'-'+ran_str+':'+passward
    result.append(a)
    i += 1
E_path = "E:/test/"
full_path = E_path + bot +'.txt'
file = open(full_path,'w')
file.write(str(result))



#def text_create(name, msg):
    #E_path = "E:/test/"
    #full_path = E_path + name + '.txt'
    #file = open(full_path, 'w')
    #file.write(msg)
#text_create(bot,str(result))
