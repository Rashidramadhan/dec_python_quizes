# a program to convert 12 hour system into 24 hour clock system
# the input is expected to be a date string format
# s = '11:05:45am'
def time_convert(s):
    if s[-2:].upper() == 'PM':
        int_val = int(s[:2]) + 12
        if int_val >= 24:
            int_val = 00
            new_str = s.replace(s[:2], str(int_val))
            print('0' + new_str[:-2])
        else:
            new_str = s.replace(s[:2], str(int_val))
            print(new_str[:-2])
    elif s[-2:].upper() == 'AM':
        hr_val = int(s[:2])
        if hr_val == 12:
            hr_val = 00
            new_str = s.replace(s[:2], str(hr_val))
            print('0' + new_str[:-2])
        else:
            print(s[:-2])
time_convert('12:05:45am')