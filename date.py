import datetime 
import re

stime = "21:00"
if stime[0] == ":":
    print("あかん")
    exit()

if ":" in stime:
    b = re.split(':', stime)
else: 
    print(":がありません")
    exit()

c = list(map(int,b))#str b[] →int c[]
if(c[0]>=25 or c[1]>=61):
    print("でかすぎぃ！")
    exit()

now = datetime.datetime.now()
hmnow = [now.hour,now.minute]
r = [x - y for (x, y) in zip(c, hmnow)]
print(r[0]*3600+r[1]*60)
