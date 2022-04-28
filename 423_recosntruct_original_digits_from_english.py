class Solution:
    def originalDigits(self, s: str) -> str:
        count = {}
        for i, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
        
        orig = {}
        
        orig['0'] = count.get('z', 0)
        orig['2'] = count.get('w', 0)
        orig['4'] = count.get('u', 0)
        orig['6'] = count.get('x', 0)
        orig['8'] = count.get('g', 0)
        
        orig['3'] = count.get('h', 0) - orig['8']
        orig['5'] = count.get('f', 0) - orig['4']
        orig['7'] = count.get('s', 0) - orig['6']
        orig['9'] = count.get('i', 0) - orig['5'] - orig['6'] - orig['8']
        
        orig['1'] = count.get('o', 0) - orig['2'] - orig['4'] - orig['0']
        
        res = ''
        for key in sorted(orig):
            if orig[key] > 0:
                res += key*orig[key]
        
        return res