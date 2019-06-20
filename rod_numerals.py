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

if __name__ == '__main__':
    rod = Rod()
    print(rod.int_to_rod(2019))
    print(rod.rod_to_int('L0NI'))
    print(rod.img_text('ARH0'))
