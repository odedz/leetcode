class Solution:
    def romanToInt(self, s: str) -> int:
        special_cases = {'IV': '1',
                         'IX': '2',
                         'XL': '3',
                         'XC': '4',
                         'CD': '5',
                         'CM': '6'}
        special_values = {'1': 4,
                          '2': 9,
                          '3': 40,
                          '4': 90,
                          '5': 400,
                          '6': 900}
        for case in special_cases:
            s = s.replace(case, special_cases[case])
        values = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
        s_values = [(values | special_values)[c] for c in s]
        return sum(s_values)
