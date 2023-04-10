#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Big5-1984
#

import re

def convert2char(start, end):
    # 遍历范围内的编码
    for i in range(start, end + 1):
        # 将整数转换为对应的字节序列
        b = i.to_bytes(2, byteorder='big')
        # 转换 10 进制得到 Big5 编码
        bigc = re.sub(r'^..', '0x', hex(i).upper())
        try:
            char = b.decode('big5')
            unic = re.sub(r'^..', 'U+', hex(ord(char)).upper())

            #print(f'{bigc}\t{char}\t{unic}')
            with open('../Big5-1984.txt', 'a', encoding='utf-8') as f:
                f.write(f'{bigc}\t{char}\t{unic}\n')
        except UnicodeDecodeError:
            pass

convert2char(0xA259, 0xA261)
convert2char(0xA440, 0xC67F)
convert2char(0xC940, 0xF9D5)
