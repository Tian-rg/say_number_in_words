#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Why polymorphism more fit number teller than abstract factory pattern.
# Because before input number, user must know what language they want.
# But for abstract factory pattern, user only know what result they want,
# and does not care what method (or factory) to produce it. 

class __NumberTeller():

    def __init__(self, number):
        self.number = number

    def checknumber(self, number):
        '''Check the number if it exceeds the range that this numtertel-
        ler supports. Check if the number is a valid number.
        '''
        
        num_bef = str(number).split(".")[0]
        
        # When number is like .XXXX, set the number before point to 0
        # When number is '', set the number before point to 0
        if num_bef == "":
            num_bef = "0"
        
        # If the nuber of digits before point is larger than 17, raise
        # error.
        if len(num_bef) > 17:
            raise NumberTooLargeError('''The number is too large, I am
                capable to say!''')
        
        # If the number has point. It will be split into a list contain-
        # ing 2 elements.
        if len(str(number).split(".")) == 2:
            num_af = str(number).split(".")[1]
            if len(num_af) > 10:
                raise TooManyDecimalDigits('''The number has too many
                    digits, You really mean it. Anyway I am capable to
                    say!''')
            elif not num_af.isnumeric():
                raise TypeError("The number is not numeric!")

        # If the number has more than 2 points, raise error.
        if str(num_bef).count(".")>=2:
            raise TypeError("Too many points in it, maybe it's a tyro.")
        # If the number before point is greater than 1 and it startswith
        # 0, raise error.
        elif (len(num_bef)>1) and (num_bef.startswith('0')):
            raise TypeError('''There is zero at the start, maybe it's a 
                tyro''')
        # If the number is not numeric, raise error.
        elif not num_bef.isnumeric():
            raise TypeError("The number is not numeric!!")

    def eliminate_leading_zero(self, num):
        '''This function is to eleminate the leading zero in a string, which
        only contains number character.
        '''
            
        if num == "0":
            return num
        else:
            if num.startswith("0"):
                num = num[1:]
                return self.eliminate_leading_zero(num)
            else:
                return num

    def eliminate_trailing_zero(self, num):
        ''' This funciotn to eleminate the trailing zero in a string, which
        only contains number character.
        '''

        if num == "0":
            return num
        else:
            if num.endswith("0"):
                num = num[:-1]
                return self.eliminate_trailing_zero(num)
            else:
                return num

class NumberToLargeError(Exception):
    pass

class TooManyDecimalDigits(Exception):
    pass

class ChineseNumberTeller(__NumberTeller):

    def __sayinchinese(self):

        number = self.eliminate_leading_zero(self.number)

        # Construct a dict, mapping a single number to words
        # 构造了一个字典，阿拉伯数值和文字数字对应
        aux_dict = dict(zip(list("0123456789."),list('零壹贰叁肆伍陆柒捌玖点')))

        # Add a item to dict, use 'n' to denote 0 which is not said
        # 此处添加了一个“n”,表示不用读为零的0
        aux_dict["n"] = ''

        # 构造一个列表，与数字的位置对应，注意当数字是零时，此表对应的位置将为
        # 设置为空
        aux_lst = ["","拾","佰","仟","萬","拾萬","佰萬","仟萬","亿","拾亿"
        ,"佰亿","仟亿","萬亿","拾萬亿","佰萬亿","仟萬亿","亿亿"][::-1]

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
        number_half1 = [ aux_dict[y] for y in number_half1 ]
        number_half1 = "".join([number_half1[i] + aux_lst[i] for i in range(len(number_half1))])

        if number[0]=='' or number[0] =='0':
            number_half1="零"

        number_half1 = ''.join(number_half1.split(" "))

        if len(number) == 2:
            number_half2 = list(number[1])

            # Elimiate the trailing zeros
            k = len(number_half2) - 1
            while k >= 0 and number_half2[-1] == "0":
                number_half2 = number_half2[:2]

            # Match number and word
            if number_half2 != "":
                number_half2 = "".join([aux_dict[y] for y in number_half2])
                number_half2 = "点" + number_half2
            else:
                number_half2 = ""

        else:
            number_half2 = ""

        return number_half1 + number_half2

    def say(self):
        
        try:
            self.checknumber(self.number)
        except Exception as e:
            return str(e)
        else:
            return self.__sayinchinese()
        finally:
            pass

class EnglishNumberTeller(__NumberTeller):

    def __sayinenglish(self):

        number = self.eliminate_leading_zero(self.number)

        number = str(number).split(".")
        
        def __to_two_digits(input_number, read_zero = False):
            '''Say two-digit number in words!
            '''
            
            __dct_ttd = {"0":"","1":"One", "2":"Two", "3":"Three",
                         "4":"Four", "5":"Five","6":"Six","7":"Seven",
                         "8":"Eight","9":"Nine","10":"Ten","11":"Eleven",
                         "12":"Twelve","13":"Thirteen", "14":"Fourteen",
                         "15":"Fifteen","16":"Sixteen","17":"Seventeen", 
                         "18":"Eighteen", "19":"Nineteen",
                        "20":"Twenty","30":"Thirty","40":"Fourty",
                        "50":"Fifty","60":"Sixty","70":"Seventy",
                        "80":"Eighty","90":"Ninety"}

            num = self.eliminate_leading_zero(input_number)
            
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
            num = self.eliminate_leading_zero(input_number)
            if len(num) <=2:
                num = __to_two_digits(num,read_zero)
            else:
                num = __to_two_digits(num[0], read_zero) + " Hundred " + __to_two_digits(num[1:], read_zero = False)
            return num

        def __to_six_digits(input_number, read_zero=False):
            num = self.eliminate_leading_zero(input_number)
            if len(num) <= 3:
                num = __to_three_digits(num,read_zero)
            else:
                num = __to_three_digits(num[:-3],read_zero) + " Thousand " +  __to_three_digits(num[-3:],read_zero=False)
            return num

        def __to_nine_digits(input_number, read_zero=False):
            num = self.eliminate_leading_zero(input_number)
            if len(num) <= 6:
                num = __to_six_digits(num, read_zero)
            else:   
                num = __to_three_digits(num[:-6],read_zero) + " Million " + __to_six_digits(num[-6:],read_zero=False)
            return num

        def __to_twelve_digits(input_number, read_zero=False):
            num = self.eliminate_leading_zero(input_number)
            if len(num) <= 9:
                num = __to_nine_digits(num, read_zero)
            else:   
                num = __to_three_digits(num[:-9],read_zero) + " Billion " + __to_six_digits(num[-9:],read_zero=False)
            return num

        def __more_than_fifteen_digits(input_number, read_zero=False):
            num = self.eliminate_leading_zero(input_number)
            if len(num) <= 12:
                num = __to_twelve_digits(num, read_zero)
            else:   
                num = __to_three_digits(num[:-12],read_zero) + " Trillion " +  __to_six_digits(num[-12:],read_zero=False)
            return num
    
        half_one = number[0]
        half_one = self.eliminate_leading_zero(half_one)

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
                half_two = self.eliminate_trailing_zero(half_two)
                print (half_two)
                if half_two == "0":
                    half_two = ""
                else:
                    print (half_two)
                    half_two = " Point " + __read_decimal_digits(half_two)
        else:
            half_two = ""

        return half_one + half_two


    def say(self):

        try:
            self.checknumber(self.number)
        except Exception as e:
            return str(e)
        else:
            return self.__sayinenglish()
        finally:
            pass

class IndonesianNumberTeller(__NumberTeller):

    def __sayinindonesian(self):

        def __to_two_digits(input_number, read_zero = False):

            __dct_ttd = {"0":"","1":"Satu", "2":"Dua", "3":"Tiga","4":"Empat", 
                         "5":"Lima","6":"Enam","7":"Tujuh", "8":"Delapan",
                         "9":"Sembilan","10":"Sepuluh","11":"Sebelas",
                         "12":"Dua Belas","13":"Tiga Belas", 
                         "14":"Empat Belas", "15":"Lima Belas",
                         "16":"Enam Belas","17":"Tujuh Belas", 
                         "18":"Delapan Belas", "19":"Sembilan Belas"}

            num = self.eliminate_leading_zero(input_number)
        
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
            num = self.eliminate_leading_zero(input_number)
            if len(num) <=2:
                num = __to_two_digits(num,read_zero)
            elif num.startswith("1"):
                num = "Seratus" + " " + __to_two_digits(num[1:], read_zero = False)
            else:
                num = __to_two_digits(num[0], read_zero) + " Ratus " +  __to_two_digits(num[1:], read_zero = False)
            return num

        def __to_six_digits(input_number, read_zero=False):
            num = self.eliminate_leading_zero(input_number)
            if len(num) <= 3:
                num = __to_three_digits(num,read_zero)
            elif len(num) == 4 and num.startswith("1"):
                num = "Seribu " + __to_three_digits(num[-3:],read_zero)
            else:
                num = __to_three_digits(num[:-3],read_zero) + " Ribu " +  __to_three_digits(num[-3:],read_zero=False)
            return num

        def __to_nine_digits(input_number, read_zero=False):
            num = self.eliminate_leading_zero(input_number)
            if len(num) <= 6:
                num = __to_six_digits(num, read_zero)
            elif len(num) == 7 and num.startswith("1"):
                num = "Sejuta " + __to_six_digits(num[-6:],read_zero=False)
            else:   
                num = __to_three_digits(num[:-6],read_zero) + " Juta " +  __to_six_digits(num[-6:],read_zero=False)
            return num

        def __to_twelve_digits(input_number, read_zero=False):
            num = self.eliminate_leading_zero(input_number)
            if len(num) <= 9:
                num = __to_nine_digits(num, read_zero)
            else:   
                num = __to_three_digits(num[:-9],read_zero) + " Milliar " +  __to_six_digits(num[-9:],read_zero=False)
            return num

        def __more_than_fifteen_digits(input_number, read_zero=False):
            num = self.eliminate_leading_zero(input_number)
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
    
        number = str(self.number).split(".")
    
        half_one = number[0]
        half_one = self.eliminate_leading_zero(half_one)

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
                half_two = self.eliminate_trailing_zero(half_two)
                if half_two == "0":
                    half_two = ""
                else:
                    half_two = " Koma " + __read_decimal_digits(half_two)
        else:
            half_two = ""

        return half_one + half_two    

    def say(self):
        try:
            self.checknumber(self.number)
        except Exception as e:
            return str(e)
        else:
            return self.__sayinindonesian()
        finally:
            pass
