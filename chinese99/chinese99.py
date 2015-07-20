# -*- coding: utf-8 -*-

def digital_to_chinese(digital_number):
    chinese_number = [u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十']
    return ((chinese_number[digital_number/10] if digital_number >= 20 else '') + chinese_number[10] if digital_number >= 10 else '') + (chinese_number[digital_number%10] if digital_number%10 > 0 else '')

if __name__ == '__main__':
    for i in range(2, 10):
        for j in range(1, 10):
            print u'%s 乘以 %s 等於 %s' % (digital_to_chinese(i), digital_to_chinese(j), digital_to_chinese(i*j))