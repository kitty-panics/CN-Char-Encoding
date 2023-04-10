#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# GB18030-2005
#

import re

# Private use characters in GB-to-Unicode mappings
GBK2UniPUA = {'FE50': 'E815', 'FE51': 'E816', 'FE52': 'E817', 'FE53': 'E818', 'FE54': 'E819',
              'FE55': 'E81A', 'FE56': 'E81B', 'FE57': 'E81C', 'FE58': 'E81D', 'FE59': 'E81E',
              'FE5A': 'E81F', 'FE5B': 'E820', 'FE5C': 'E821', 'FE5D': 'E822', 'FE5E': 'E823',
              'FE5F': 'E824', 'FE60': 'E825', 'FE61': 'E826', 'FE62': 'E827', 'FE63': 'E828',
              'FE64': 'E829', 'FE65': 'E82A', 'FE66': 'E82B', 'FE67': 'E82C', 'FE68': 'E82D',
              'FE69': 'E82E', 'FE6A': 'E82F', 'FE6B': 'E830', 'FE6C': 'E831', 'FE6D': 'E832',
              'FE6E': 'E833', 'FE6F': 'E834', 'FE70': 'E835', 'FE71': 'E836', 'FE72': 'E837',
              'FE73': 'E838', 'FE74': 'E839', 'FE75': 'E83A', 'FE76': 'E83B', 'FE77': 'E83C',
              'FE78': 'E83D', 'FE79': 'E83E', 'FE7A': 'E83F', 'FE7B': 'E840', 'FE7C': 'E841',
              'FE7D': 'E842', 'FE7E': 'E843', 'FE80': 'E844', 'FE81': 'E845', 'FE82': 'E846',
              'FE83': 'E847', 'FE84': 'E848', 'FE85': 'E849', 'FE86': 'E84A', 'FE87': 'E84B',
              'FE88': 'E84C', 'FE89': 'E84D', 'FE8A': 'E84E', 'FE8B': 'E84F', 'FE8C': 'E850',
              'FE8D': 'E851', 'FE8E': 'E852', 'FE8F': 'E853', 'FE90': 'E854', 'FE91': 'E855',
              'FE92': 'E856', 'FE93': 'E857', 'FE94': 'E858', 'FE95': 'E859', 'FE96': 'E85A',
              'FE97': 'E85B', 'FE98': 'E85C', 'FE99': 'E85D', 'FE9A': 'E85E', 'FE9B': 'E85F',
              'FE9C': 'E860', 'FE9D': 'E861', 'FE9E': 'E862', 'FE9F': 'E863', 'FEA0': 'E864'}
GBK2UniNonPUA = {'FE50': '2E81', 'FE51': '20087', 'FE52': '20089', 'FE53': '200CC', 'FE54': '2E84',
                 'FE55': '3473', 'FE56': '3447',  'FE57': '2E88',  'FE58': '2E8B',  'FE59': '9FB4',
                 'FE5A': '359E', 'FE5B': '361A',  'FE5C': '360E',  'FE5D': '2E8C',  'FE5E': '2E97',
                 'FE5F': '396E', 'FE60': '3918',  'FE61': '9FB5',  'FE62': '39CF',  'FE63': '39DF',
                 'FE64': '3A73', 'FE65': '39D0',  'FE66': '9FB6',  'FE67': '9FB7',  'FE68': '3B4E',
                 'FE69': '3C6E', 'FE6A': '3CE0',  'FE6B': '2EA7',  'FE6C': '215D7', 'FE6D': '9FB8',
                 'FE6E': '2EAA', 'FE6F': '4056',  'FE70': '415F',  'FE71': '2EAE',  'FE72': '4337',
                 'FE73': '2EB3', 'FE74': '2EB6',  'FE75': '2EB7',  'FE76': '2298F', 'FE77': '43B1',
                 'FE78': '43AC', 'FE79': '2EBB',  'FE7A': '43DD',  'FE7B': '44D6',  'FE7C': '4661',
                 'FE7D': '464C', 'FE7E': '9FB9',  'FE80': '4723',  'FE81': '4729',  'FE82': '477C',
                 'FE83': '478D', 'FE84': '2ECA',  'FE85': '4947',  'FE86': '497A',  'FE87': '497D',
                 'FE88': '4982', 'FE89': '4983',  'FE8A': '4985',  'FE8B': '4986',  'FE8C': '499F',
                 'FE8D': '499B', 'FE8E': '49B7',  'FE8F': '49B6',  'FE90': '9FBA',  'FE91': '241FE',
                 'FE92': '4CA3', 'FE93': '4C9F',  'FE94': '4CA0',  'FE95': '4CA1',  'FE96': '4C77',
                 'FE97': '4CA2', 'FE98': '4D13',  'FE99': '4D14',  'FE9A': '4D15',  'FE9B': '4D16',
                 'FE9C': '4D17', 'FE9D': '4D18',  'FE9E': '4D19',  'FE9F': '4DAE',  'FEA0': '9FBB'}
UniPUA2UniNonPUA = {'E815': '2E81', 'E816': '20087', 'E817': '20089', 'E818': '200CC', 'E819': '2E84',
                    'E81A': '3473', 'E81B': '3447',  'E81C': '2E88',  'E81D': '2E8B',  'E81E': '9FB4',
                    'E81F': '359E', 'E820': '361A',  'E821': '360E',  'E822': '2E8C',  'E823': '2E97',
                    'E824': '396E', 'E825': '3918',  'E826': '9FB5',  'E827': '39CF',  'E828': '39DF',
                    'E829': '3A73', 'E82A': '39D0',  'E82B': '9FB6',  'E82C': '9FB7',  'E82D': '3B4E',
                    'E82E': '3C6E', 'E82F': '3CE0',  'E830': '2EA7',  'E831': '215D7', 'E832': '9FB8',
                    'E833': '2EAA', 'E834': '4056',  'E835': '415F',  'E836': '2EAE',  'E837': '4337',
                    'E838': '2EB3', 'E839': '2EB6',  'E83A': '2EB7',  'E83B': '2298F', 'E83C': '43B1',
                    'E83D': '43AC', 'E83E': '2EBB',  'E83F': '43DD',  'E840': '44D6',  'E841': '4661',
                    'E842': '464C', 'E843': '9FB9',  'E844': '4723',  'E845': '4729',  'E846': '477C',
                    'E847': '478D', 'E848': '2ECA',  'E849': '4947',  'E84A': '497A',  'E84B': '497D',
                    'E84C': '4982', 'E84D': '4983',  'E84E': '4985',  'E84F': '4986',  'E850': '499F',
                    'E851': '499B', 'E852': '49B7',  'E853': '49B6',  'E854': '9FBA',  'E855': '241FE',
                    'E856': '4CA3', 'E857': '4C9F',  'E858': '4CA0',  'E859': '4CA1',  'E85A': '4C77',
                    'E85B': '4CA2', 'E85C': '4D13',  'E85D': '4D14',  'E85E': '4D15',  'E85F': '4D16',
                    'E860': '4D17', 'E861': '4D18',  'E862': '4D19',  'E863': '4DAE',  'E864': '9FBB'}
GBK_CJK_A=['3473', '3447', '359E', '361A', '360E', '396E', '3918', '39CF',
           '39DF', '3A73', '39D0', '3B4E', '3C6E', '3CE0', '4056', '415F',
           '4337', '43B1', '43AC', '43DD', '44D6', '4661', '464C', '4723',
           '4729', '477C', '478D', '4947', '497A', '497D', '4982', '4983',
           '4985', '4986', '499F', '499B', '49B7', '49B6', '4CA3', '4C9F',
           '4CA0', '4CA1', '4C77', '4CA2', '4D13', '4D14', '4D15', '4D16',
           '4D17', '4D18', '4D19', '4DAE']


def convert2char(start1, end1, start2, end2, charset, extra):
    # 遍历第 1 字节
    for i in range(start1, end1 + 1):
        byte1 = hex(i)[2:].upper()
        # 遍历第 2 字节
        for j in range(start2, end2 + 1):
            if extra == '1' and j == 0x7f:
                continue
            else:
                byte2 = hex(j)[2:].upper()
                # 拼接第 1、2 字节为 16 进制
                gbc = f'{byte1}{byte2}'
                # 将 16 进制转换成 int，再 to_bytes()
                b = int(f'0x{gbc}', 16).to_bytes(2, byteorder='big')
                try:
                    char = b.decode(charset)
                    unic = re.sub(r'^..', '', hex(ord(char)).upper())
                    if extra == '1' and unic in UniPUA2UniNonPUA:
                        unicPUA = unic
                        unicNonPUA = UniPUA2UniNonPUA[unic]
                        charPUA = chr(int('0x' + unicPUA, 16))
                        charNonPUA = chr(int('0x' + unicNonPUA, 16))
                        #print(f'0x{gbc}\t{charPUA},{charNonPUA}\tU+{unicPUA},U+{unicNonPUA}')
                        with open('../GB18030-2005.txt', 'a', encoding='utf-8') as f:
                            f.write(f'0x{gbc}\t{charPUA},{charNonPUA}\tU+{unicPUA},U+{unicNonPUA}\n')
                    else:
                        #print(f'0x{gbc}\t{char}\tU+{unic}')
                        with open('../GB18030-2005.txt', 'a', encoding='utf-8') as f:
                            f.write(f'0x{gbc}\t{char}\tU+{unic}\n')
                except UnicodeDecodeError:
                    pass

convert2char(0xB0, 0xF7, 0xA1, 0xFE, 'GB2312',  '0') # GBK/2: B0–F7, A1–FE;              6768/6763
convert2char(0x81, 0xA0, 0x40, 0xFE, 'GB18030', '1') # GBK/3: 81–A0, 40–FE (except: 7F); 6080/6080
convert2char(0xAA, 0xFE, 0x40, 0xA0, 'GB18030', '1') # GBK/4: AA–FE, 40–A0 (except: 7F); 8160/8160


def GBK_in_PUA():
    for k,v in GBK2UniPUA.items():
        gbc = k
        unicPUA = v
        unicNonPUA = UniPUA2UniNonPUA[v]
        charPUA = chr(int('0x' + unicPUA, 16))
        charNonPUA = chr(int('0x' + unicNonPUA, 16))
    
        #print(f'0x{gbc}\t{charPUA},{charNonPUA}\tU+{unicPUA},U+{unicNonPUA}')
        with open('../GB18030-2005.txt', 'a', encoding='utf-8') as f:
            f.write(f'0x{gbc}\t{charPUA},{charNonPUA}\tU+{unicPUA},U+{unicNonPUA}\n')

#GBK_in_PUA()


def Unicode_CJK(start, end):
    for i in range(start, end + 1):
        unic = re.sub(r'^..', '', hex(i).upper())
        if unic in GBK_CJK_A:
            continue
        char = chr(i)
        gbc = char.encode('gb18030').hex()

        #print(f'0x{gbc}\t{char}\tU+{unic}')
        with open('../GB18030-2005.txt', 'a', encoding='utf-8') as f:
            f.write(f'0x{gbc}\t{char}\tU+{unic}\n')

Unicode_CJK(0x3400,  0x4DB5)
Unicode_CJK(0x20000, 0x2A6D6)
