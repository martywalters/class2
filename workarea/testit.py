import re
s = 'welcome home'
m = re.match(r'(.*)(.*?)', s)
print(m.group())
