
# from flask import *

# app=Flask(__name__)




# @app.route('/')
# def fun():
#     return "<h1>Welcome to my Flask App</h1>"


# @app.route("/what")
# def hello_world():
#     return "<p<Hello World</p>"



# @app.route("/about")
# def about():
#     return send_file("new.html") # important to link html files to python flask








# if __name__ == '__main__':
#     pass




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from PIL import Imagec



# x=np.array([[2,3,4,5],[34,7,1,5]])
# x=np.sort(x)
# x=x+5



# print(x.shape)
# x=x.reshape(4,2)
# print(x.shape)
# print(x.size)
# x=np.arange(10)
# print(x)
# # print(x.zeros())
# x=np.zeros(5)
# y=np.ones(45)
# print(x)
# print(y)
# x=np.array([[2,3,4,5],[34,7,1,5]])
# # x=np.concatenate((x,y))
# print(np.max(x))
# print(np.mean(x))
# print(np.median(x))
# print(np.argmax(x))
# print(np.argmin(x))

# data={
#     'Name':['Yousaf','Zaman','Maryan'],
#     'Age':[23,34,45],
#     'Country':['Mexico','USA','India']
# }


# d1=pd.DataFrame(data)
# d1.to_csv('blank.csv',index=False)


# d2=pd.read_csv('blank.csv')
# d2['Age'][0]=9999

# print(d2['Age'].values)
# print(d1.head(2))
# # print(d1.describe())
# print("HELLL WORLD")
# print(d1.describe())
# print("WHAT IS THIS ")
# # print(d2.std)
# # print(d2.corr())
# # print(d2.columns)
# # print(d2.index)
# # print(d2.shape)
# # print(d2.size)
# print(d2.dtypes)

df1=pd.DataFrame([[23,3,5,5,6],[1,2,3,4,5]],columns=['date','United','f','4','5'],index=['1','2','3','4','5'])

#based on these values graph them



# I'm using git and github