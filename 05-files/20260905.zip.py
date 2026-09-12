f1 = open('20260905/target.zip', 'rb')
f2 = open('20260905/test.jpg', 'ab')

f2.write(f1.read())

f1.close()
f2.close()
print('完成')