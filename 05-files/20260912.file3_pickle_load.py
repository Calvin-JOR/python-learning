import pickle

with open('mydat.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)