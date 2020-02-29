'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''
THOUSAND = 1000
MILLION = 1000000
BILLION = 1000000000

class Solution:
    def numberToWords(self, num: int) -> str:
        def less_than_10(num):
            map_ = {
                1: 'One', 2: 'Two', 3: 'Three',
                4: 'Four', 5: 'Five', 6: 'Six', 
                7: 'Seven', 8: 'Eight', 9:'Nine',
                0: 'Zero'
            }
            return map_[num]
        
        def less_than_20(num):
            if num < 10:
                return less_than_10(num)
            
            map_ = {
                10: 'Ten', 11: 'Eleven', 12: 'Twelve',
                13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                19: 'Nineteen',
            }
            return map_[num]
        
        def less_than_100(num):
            if num < 20:
                return less_than_20(num)

            map_ = {
                2: 'Twenty', 3: 'Thirty', 4: 'Forty',
                5: 'Fifty', 6: 'Sixty', 7: 'Seventy',
                8: 'Eighty', 9: 'Ninety',
            }
            
            tens = num // 10
            units = num % 10 
            if units == 0:
                return map_[tens]
            
            return map_[tens] + ' ' + less_than_10(units)
            
        def less_than_1000(num):
            '''convert 3 digit number to str'''
            if num < 100:
                return less_than_100(num)
            
            hundreds = num // 100
            remainder = num % 100
            
            result = less_than_10(hundreds) + ' ' + 'Hundred'
            if remainder == 0:
                return result 
            
            return result + ' ' + less_than_100(remainder)
        
        def less_than_million(num):
            if num < THOUSAND:
                return less_than_1000(num)
            
            thousands = num // THOUSAND
            remainder = num % THOUSAND
            
            result = less_than_1000(thousands) + ' ' + 'Thousand'
            
            if remainder == 0:
                return result
        
            return result + ' ' + less_than_1000(remainder)

        def less_than_billion(num):
            if num < MILLION:
                return less_than_million(num)
            
            millions = num // MILLION
            remainder = num % MILLION
            result = less_than_1000(millions) + ' ' + 'Million'
            if remainder == 0:
                return result
            
            return result + ' ' + less_than_million(remainder)
         
        def less_than_trillion(num):
            if num < BILLION:
                return less_than_billion(num)
            
            billions = num // BILLION
            remainder = num % BILLION
            result = less_than_1000(billions) + ' ' + 'Billion'
            if remainder == 0:
                return result
            
            return result + ' ' + less_than_billion(remainder)
        
        return less_than_trillion(num)
