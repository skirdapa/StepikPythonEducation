import re

link = '''
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">
'''
link_pattern = r'\w+\.\w+\.\w+|\w+\.\w+'
r = sorted(re.findall(link_pattern, link))
print(r)

aset = {1,2,3,4,5}
bset = {2,3,33,44,55}

aset.update(bset)
print(sorted(aset))