s="zeroonetwothreefourfivesixseveneightnine"
dic = {}
validChars = ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]

for ch in validChars:
    dic[ch] = 0

l = len(s)

ret = ""
for ch in s:
    dic[ch] = dic[ch] + 1

while l > 0:
    if dic['z'] > 0 and dic['e'] > 0  and dic['r'] > 0 and dic['o'] > 0:
        ret += str(0)
        dic['z'] = dic['z'] - 1
        dic['e'] = dic['e'] - 1
        dic['r'] = dic['r'] - 1
        dic['o'] = dic['o'] - 1
        l = l-4
        continue
    if dic['o'] > 0 and dic['n'] > 0  and dic['e'] > 0:
        ret += str(1)
        dic['o'] = dic['o'] - 1
        dic['n'] = dic['n'] - 1
        dic['e'] = dic['e'] - 1
        l = l-3
        continue
    if dic['t'] > 0 and dic['w'] > 0  and dic['o'] > 0:
        ret += str(2)
        dic['t'] = dic['t'] - 1
        dic['w'] = dic['w'] - 1
        dic['o'] = dic['o'] - 1
        l = l-3
        continue
    if dic['t'] > 0 and dic['h'] > 0  and dic['r'] > 0 and dic['e'] > 0 and dic['e'] > 0:
        ret += str(3)
        dic['t'] = dic['t'] - 1
        dic['h'] = dic['h'] - 1
        dic['r'] = dic['r'] - 1
        dic['e'] = dic['e'] - 1
        dic['e'] = dic['e'] - 1
        l = l-5
        continue
    if dic['f'] > 0 and dic['o'] > 0  and dic['u'] > 0 and dic['r'] > 0:
        ret += str(4)
        dic['f'] = dic['f'] - 1
        dic['o'] = dic['o'] - 1
        dic['u'] = dic['u'] - 1
        dic['r'] = dic['r'] - 1
        l = l-4
        continue
    if dic['f'] > 0 and dic['i'] > 0  and dic['v'] > 0 and dic['e'] > 0:
        ret += str(5)
        dic['f'] = dic['f'] - 1
        dic['i'] = dic['i'] - 1
        dic['v'] = dic['v'] - 1
        dic['e'] = dic['e'] - 1
        l = l-4
        continue
    if dic['s'] > 0 and dic['i'] > 0  and dic['x'] > 0:
        ret += str(6)
        dic['s'] = dic['s'] - 1
        dic['i'] = dic['i'] - 1
        dic['x'] = dic['x'] - 1
        l = l-3
        continue
    if dic['s'] > 0 and dic['e'] > 0  and dic['v'] > 0 and dic['e'] > 0 and dic['n'] > 0:
        ret += str(7)
        dic['s'] = dic['s'] - 1
        dic['e'] = dic['e'] - 1
        dic['v'] = dic['v'] - 1
        dic['e'] = dic['e'] - 1
        dic['n'] = dic['n'] - 1
        l = l-5
        continue
    if dic['e'] > 0 and dic['i'] > 0  and dic['g'] > 0 and dic['h'] > 0 and dic['t'] > 0:
        ret += str(8)
        dic['e'] = dic['e'] - 1
        dic['i'] = dic['i'] - 1
        dic['g'] = dic['g'] - 1
        dic['h'] = dic['h'] - 1
        dic['t'] = dic['t'] - 1
        l = l-5
        continue
    if dic['n'] > 0 and dic['i'] > 0  and dic['n'] > 0 and dic['e'] > 0:
        ret += str(9)
        dic['n'] = dic['n'] - 1
        dic['i'] = dic['i'] - 1
        dic['n'] = dic['n'] - 1
        dic['e'] = dic['e'] - 1
        l = l-4
        continue
print(ret)