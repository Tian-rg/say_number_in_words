#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''This pulls together the method of saying number in different language.
'''

__author__ = "Tian"

def __checknumber(number):
       
    number1 = str(number).split(".")[0]
    if number1=="":
        number1 = "0"
        
        if len(number1) > supported_number_length[0]:
            raise NumberTooLargeError("Number is too large to handle")
        
        if len(str(number).split(".")) == 2:
            number2 = str(number).split(".")[1]
            if len(number2) > supported_number_length[1]:
                raise TooManyDecimalDigits("Too many decimal digits to handle")
        
        if str(number).count(".")>=2:
            raise NotCorrectNumberError("Wrong number format")
        elif (len(number1)>1) and (number1.startswith('0')):
            raise NotCorrectNumberError("Wrong number format")
        elif not number1.isnumeric():
            raise NotCorrectNumberError("Wrong number format")
            
class NotCorrectNumberError(Exception):
    pass

class NumberTooLargeError(Exception):
    pass

class TooManyDecimalDigits(Exception):
    pass
            
def __eliminate_leading_zero(num):
    if num == "0":
        return num
    else:
        if num.startswith("0"):
            num = num[1:]
            return __eliminate_leading_zero(num)
        else:
            return num

def __eliminate_trailing_zero(num):
    if num == "0":
        return num
    else:
        if num.endswith("0"):
            num = num[:-1]
            return __eliminate_trailing_zero(num)
        else:
            return num

def sayinchinese(number):
    '''say the number in Chinese
    return: string,
    '''
    
    __checknumber(number)
    # 构造了一个字典，阿拉伯数值和文字数字对应
    aux_dict = dict(zip(list("0123456789."),list("零壹贰叁肆伍陆柒捌玖点")))
    # 此处添加了一个“n”,表示不用读为零的0
    aux_dict["n"] = ''
    
    # 构造一个列表，与数字的位置对应，注意当数字是零时，此表对应的位置将为设置为空
    aux_lst = ["","拾","佰","仟","萬","拾萬","佰萬","仟萬","亿","拾亿","佰亿",
               "仟亿","萬亿","拾萬亿","佰萬亿","仟萬亿","亿亿"][::-1]

    # 将数字按小数点前后分开成两部分，不同的部分不同的处理方法
    number = str(number).split(".")
    
    number_half1 = list(number[0])
    
    aux_lst = aux_lst[-len(number_half1):]
    
    i = len(number_half1) - 1
    while i >= 0 and number_half1[i] == "0":
        number_half1[i] = 'n'
        aux_lst[i] = ''
        i -= 1

    j = 1
    while j <= len(number_half1) - 2:
        if number_half1[j] == '0' and number_half1[j-1] != '0' and number_half1[j+1] == '0':
            number_half1[j] = 'n'
            aux_lst[j] = ''
        if number_half1[j] == '0':
            aux_lst[j] = ''
        j += 1

    # 匹配第一部分，将第一部分的数字变成文字
    number_half1 = [aux_dict[y] for y in number_half1]

    number_half1 = "".join([number_half1[i] + aux_lst[i] for i in range(len(number_half1))])  
    
    if number[0]=='' or number[0] =='0':
        number_half1="零"
    
    number_half1 = ''.join(number_half1.split(" "))
    
    # 以下是对第二部分的处理，
    # 分为两种情况，
    # 情况一：要读的数值中有'.'，且'.'后为不为空。if
    # 情况二：要读的数值中有没有'.'，或，有'.'，但'.'为空
    if len(number) == 2:
        number_half2 = list(number[1])
    
    #去掉末尾的零
        k = len(number_half2) - 1
        while k >= 0 and number_half2[-1] == "0":
            number_half2 = number_half2[:-1]
            k -= 1
        
        #匹配数字与文字
        if number_half2 != "":
            number_half2 = "".join([aux_dict[y] for y in number_half2])
            number_half2 = "点" + number_half2
        else:
            number_half2 = ""
    else:
        number_half2 = ""
    
    return number_half1 + number_half2

def sayinenglish(number):
    '''say the number in english
    return: string,
    '''
    # 将数字按小数点前后分开成两部分，不同的部分不同的处理方法wwwwwwwwwwwwww
    # Nested functions are used here to hide data and DRY principle
    __checknumber(number)
    
    number = str(number).split(".")
    
    def __to_two_digits(input_number, read_zero = False):
        __dct_ttd = {"0":"","1":"One", "2":"Two", "3":"Three",
                     "4":"Four", "5":"Five","6":"Six","7":"Seven",
                     "8":"Eight","9":"Nine","10":"Ten","11":"Eleven",
                     "12":"Twelve","13":"Thirteen", "14":"Fourteen",
                     "15":"Fifteen","16":"Sixteen","17":"Seventeen", 
                     "18":"Eighteen", "19":"Nineteen",
                    "20":"Twenty","30":"Thirty","40":"Fourty",
                    "50":"Fifty","60":"Sixty","70":"Seventy",
                    "80":"Eighty","90":"Ninety"}

        num = __eliminate_leading_zero(input_number)
        
        if num == "0":
            if read_zero == True:
                num = "Zero"
            else:
                num = ""
        elif int(num) >= 1 and int(num) <=19:
            num = __dct_ttd[num]
        else:
            num = " And " + __dct_ttd[num[0]+"0"] + " " + __dct_ttd[num[1]]
        return num

    def __to_three_digits(input_number, read_zero=False):
        num = __eliminate_leading_zero(input_number)
        if len(num) <=2:
            num = __to_two_digits(num,read_zero)
        else:
            num = __to_two_digits(num[0], read_zero) + " Hundred " +  __to_two_digits(num[1:], read_zero = False)
        return num

    def __to_six_digits(input_number, read_zero=False):
        num = __eliminate_leading_zero(input_number)
        if len(num) <= 3:
            num = __to_three_digits(num,read_zero)
        else:
            num = __to_three_digits(num[:-3],read_zero) + " Thousand " +  __to_three_digits(num[-3:],read_zero=False)
        return num

    def __to_nine_digits(input_number, read_zero=False):
        num = __eliminate_leading_zero(input_number)
        if len(num) <= 6:
            num = __to_six_digits(num, read_zero)
        else:   
            num = __to_three_digits(num[:-6],read_zero) + " Million " + __to_six_digits(num[-6:],read_zero=False)
        return num

    def __to_twelve_digits(input_number, read_zero=False):
        num = __eliminate_leading_zero(input_number)
        if len(num) <= 9:
            num = __to_nine_digits(num, read_zero)
        else:   
            num = __to_three_digits(num[:-9],read_zero) + " Billion " + __to_six_digits(num[-9:],read_zero=False)
        return num

    def __more_than_fifteen_digits(input_number, read_zero=False):
        num = __eliminate_leading_zero(input_number)
        if len(num) <= 12:
            num = __to_twelve_digits(num, read_zero)
        else:   
            num = __to_three_digits(num[:-12],read_zero) + " Trillion " +  __to_six_digits(num[-12:],read_zero=False)
        return num
    
    half_one = number[0]
    half_one = __eliminate_leading_zero(half_one)

    half_one = __more_than_fifteen_digits(half_one)
    
    # Handling second half starts here.
    def __read_decimal_digits(input_number):
        __dct_rdd = {"0":"Zero","1":"One", "2":"Two", "3":"Three",
                   "4":"Four", "5":"Five","6":"Six","7":"Seven",
                   "8":"Eight","9":"Nine"}
        num = list(input_number)
        num = [__dct_rdd[x] for x in num]
        num = " ".join(num)
        return num

    if len(number) == 2:
        half_two = number[1]
        
        if half_two == "":
            half_two = ""
        else:
            print (half_two)
            half_two = __eliminate_trailing_zero(half_two)
            print (half_two)
            if half_two == "0":
                half_two = ""
            else:
                print (half_two)
                half_two = " Point " + __read_decimal_digits(half_two)
    else:
        half_two = ""

    return half_one + half_two


def sayinindonesian(number):
    '''say the number in indonesian
    return: string,
    '''    
    # 将数字按小数点前后分开成两部分，不同的部分不同的处理方法wwwwwwwwwwwwww
    # Nested functions are used here to hide data and DRY principle

    __checknumber(number)
    
    def __to_two_digits(input_number, read_zero = False):
        __dct_ttd = {"0":"","1":"Satu", "2":"Dua", "3":"Tiga","4":"Empat", 
                     "5":"Lima","6":"Enam","7":"Tujuh", "8":"Delapan",
                     "9":"Sembilan","10":"Sepuluh","11":"Sebelas",
                     "12":"Dua Belas","13":"Tiga Belas", 
                     "14":"Empat Belas", "15":"Lima Belas",
                     "16":"Enam Belas","17":"Tujuh Belas", 
                     "18":"Delapan Belas", "19":"Sembilan Belas"}

        num = __eliminate_leading_zero(input_number)
        
        if num == "0":
            if read_zero == True:
                num = "Nol"
            else:
                num = ""
        elif int(num) >= 1 and int(num) <=19:
            num = __dct_ttd[num]
        else:
            num = __dct_ttd[num[0]] + " Puluh " + __dct_ttd[num[1]]
        return num

    def __to_three_digits(input_number, read_zero=False):
        num = __eliminate_leading_zero(input_number)
        if len(num) <=2:
            num = __to_two_digits(num,read_zero)
        elif num.startswith("1"):
            num = "Seratus" + " " + __to_two_digits(num[1:], read_zero = False)
        else:
            num = __to_two_digits(num[0], read_zero) + " Ratus " +  __to_two_digits(num[1:], read_zero = False)
        return num

    def __to_six_digits(input_number, read_zero=False):
        num = __eliminate_leading_zero(input_number)
        if len(num) <= 3:
            num = __to_three_digits(num,read_zero)
        elif len(num) == 4 and num.startswith("1"):
            num = "Seribu " + __to_three_digits(num[-3:],read_zero)
        else:
            num = __to_three_digits(num[:-3],read_zero) + " Ribu " +  __to_three_digits(num[-3:],read_zero=False)
        return num

    def __to_nine_digits(input_number, read_zero=False):
        num = __eliminate_leading_zero(input_number)
        if len(num) <= 6:
            num = __to_six_digits(num, read_zero)
        elif len(num) == 7 and num.startswith("1"):
            num = "Sejuta " + __to_six_digits(num[-6:],read_zero=False)
        else:   
            num = __to_three_digits(num[:-6],read_zero) + " Juta " +  __to_six_digits(num[-6:],read_zero=False)
        return num

    def __to_twelve_digits(input_number, read_zero=False):
        num = __eliminate_leading_zero(input_number)
        if len(num) <= 9:
            num = __to_nine_digits(num, read_zero)
        else:   
            num = __to_three_digits(num[:-9],read_zero) + " Milliar " +  __to_six_digits(num[-9:],read_zero=False)
        return num

    def __more_than_fifteen_digits(input_number, read_zero=False):
        num = __eliminate_leading_zero(input_number)
        if len(num) <= 12:
            num = __to_twelve_digits(num, read_zero)
        else:   
            num = __to_three_digits(num[:-12],read_zero) + " Trilium " + __to_six_digits(num[-12:],read_zero=False)
        return num

    def __read_decimal_digits(input_number):
        __dct_rdd = {"0":"Nol","1":"Satu", "2":"Dua", "3":"Tiga",
                   "4":"Empat", "5":"Lima","6":"Enam","7":"Tujuh",
                   "8":"Delapan","9":"Sembilan"}
        num = list(input_number)
        num = [__dct_rdd[x] for x in num]
        num = " ".join(num)
        return num
    
    number = str(number).split(".")
    
    half_one = number[0]
    half_one = __eliminate_leading_zero(half_one)

    half_one = __more_than_fifteen_digits(half_one)

    # Handling second half starts here.
    def __read_decimal_digits(input_number):
        __dct_rdd = {"0":"Nol","1":"Satu", "2":"Dua", "3":"Tiga",
                   "4":"Empat", "5":"Lima","6":"Enam","7":"Tujuh",
                   "8":"Delapan","9":"Sembilan",".":"Koma"}
        num = list(input_number)
        num = [__dct_rdd[x] for x in num]
        num = " ".join(num)
        return num    

    if len(number) == 2:
        half_two = number[1]
        
        if half_two == "":
            half_two = ""
        else:
            half_two = __eliminate_trailing_zero(half_two)
            if half_two == "0":
                half_two = ""
            else:
                half_two = " Koma " + __read_decimal_digits(half_two)
    else:
        half_two = ""
    
    return half_one + half_two

supported_languages = {'Chinese':sayinchinese, 'English':sayinenglish,
                       'Indonesian':sayinindonesian,
                      }
supported_number_length = (17,10)
