# -*- coding: utf-8 -*-
__author__ = 'gamefang'

class Rod(object):
    '''
    筹算计数法
    '''
    # 纵、横筹算代码0-9（正数）
    vertical_rod = ['0','a','b','c','d','e','f','g','h','i']
    horizontal_rod = ['0','j','k','l','m','n','o','p','q','r']
    # 图片标签模版
    img_template = '{image=bmpfnt/rod/%s.png}'
    md_template = '![%s](https://raw.githubusercontent.com/gamefang/CountingRod/master/res/%s.png)'
    # 筹算形状字典：{ 筹算代码:(纵向筹数量,横向筹数量)... }
    shape_dic = {
        '0':(0,0),
        'a':(1,0),
        'b':(2,0),
        'c':(3,0),
        'd':(4,0),
        'e':(5,0),
        'f':(1,1),
        'g':(2,1),
        'h':(3,1),
        'i':(4,1),
        'j':(0,1),
        'k':(0,2),
        'l':(0,3),
        'm':(0,4),
        'n':(0,5),
        'o':(1,1),
        'p':(1,2),
        'q':(1,3),
        'r':(1,4),
    }

    def int_to_rod(self,num):
        '''
        整数转化为筹算代码
        @param num: 整数
        @return: 筹算代码
        '''
        rod = ''
        negative = (num < 0)
        for digit,num in enumerate(str(abs(num))[::-1]):
            if digit % 2:   # 奇数位横
                rod = self.horizontal_rod[int(num)] + rod
            else:   # 偶数位纵
                rod = self.vertical_rod[int(num)] + rod
        if negative: rod = rod.upper()
        return rod

    def rod_to_int(self,rod):
        '''
        筹算代码转化为整数
        @param rod: 筹算代码
        @return: 整数或None(当筹算代码不合法时)
        '''
        num = 0
        negative = (rod.lower() != rod)
        for digit,rod in enumerate(rod.lower()[::-1]):
            if digit % 2:   # 奇数位横
                if rod not in self.horizontal_rod: return None
                num += self.horizontal_rod.index(rod) * (10**digit)
            else:   # 偶数位纵
                if rod not in self.vertical_rod: return None
                num += self.vertical_rod.index(rod) * (10**digit)
        if negative: num = -num
        return num

    def img_text(self,num=None,rod=None):
        '''
        输出筹算代码的图型的标记语言，适用于renpy
        @param num: 整数(优先)
        @param rod: 筹算代码
        @return: 图形标记语言
        '''
        if num is not None:
            rod = self.int_to_rod(num)
        result = ''
        negative = (rod.lower() != rod)
        for word in rod:
            result += self.img_template % (word,'_'+word)[negative]
        return result

    def md_text(self,num=None,rod=None):
        '''
        输出筹算代码的markdown标记语言
        @param num: 整数(优先)
        @param rod: 筹算代码
        @return: markdown语言
        '''
        if num is not None:
            rod = self.int_to_rod(num)
        result = ''
        negative = (rod.lower() != rod)
        for word in rod:
            result += self.md_template % ( self.rod_to_int(word) or self.rod_to_int(word+'0')//10, (word,'_'+word)[negative] )
        return result

    def rod_to_shape(self,rod):
        '''
        筹算代码转化为形状模拟
        @param rod: 筹算代码
        @return: [ 是否正数, (第1字纵筹数,第1字横筹数), (第2字纵筹数,第2字横筹数)... ]
        '''
        result = [ self.shape_dic[word] for word in rod.lower() ]
        return [rod.lower() == rod] + result

if __name__ == '__main__':
    rod = Rod()
    print(rod.int_to_rod(2019))
    print(rod.rod_to_int('L0NI'))
    print(rod.img_text(10086))
    print(rod.md_text(10086))
    print(rod.rod_to_shape('mi'))
