'''使用pickle保存对象'''
import pickle

data = {
    'Name':'Calvin',
    'Scores':{'语文':85, '数学':90, '英语':95},
    'Info':{'City':'Tokyo', 'Like':'Ting Gu'}
}

with open('mydat.pkl', 'wb') as f:
    pickle.dump(data, f)