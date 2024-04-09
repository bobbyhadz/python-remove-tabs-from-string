# Remove the tabs from a String in Python

my_str = 'bobby\thadz\tcom'

result = ' '.join(my_str.split())
print(repr(result))  # 👉️ 'bobby hadz com'

result = ''.join(my_str.split())
print(repr(result))  # 👉️ 'bobbyhadzcom'