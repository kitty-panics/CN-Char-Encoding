#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# GB2312
#

import re

def convert2char(start, end):
    for i in range(start, end + 1):
        # 将整数转换为对应的字节序列
        b = i.to_bytes(2, byteorder='big')
        # 转换 10 进制得到 GB2312 编码
        gbc = re.sub(r'^..', '0x',hex(i).upper())
        try:
            char = b.decode('gb2312')
            unic = re.sub(r'^..', 'U+', hex(ord(char)).upper())
    
            #print(f'{gbc}\t{char}\t{unic}')
            with open('../GB2312.txt', 'a', encoding='utf-8') as f:
                f.write(f'{gbc}\t{char}\t{unic}\n')
        except UnicodeDecodeError:
            pass

convert2char(0xB0A1, 0xF7FE)
