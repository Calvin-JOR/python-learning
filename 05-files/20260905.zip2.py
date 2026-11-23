with open('target.zip', 'rb') as f1, open('test.jpg', 'ab') as f2:
    f2.write(f1.read())
print('完成')