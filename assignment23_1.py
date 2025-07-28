#q1
import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
def data1():
    line='_'*40
    print(line)
    
    data={'name':['amit','sagar','pooja'],
        'math': [85,90,78],
        'science' : [92,88,80],
        'english' :[75,85,82]}
    print(line)

def getinformation(data1):  
    line='_'*40
    print(line)
    df=pd.DataFrame(data1) 
    print("shape of the data:",df.shape)
    print("coumn of the data:",df.columns)
    print("variety of the data:",df.dtypes)
    
    print(line)
    #q2
    print(line)
    print("statistical summary:",df.describe())
    print(line)
    #q3
    print(line)
    df['total'] = df['math'] + df['science'] + df['english']
    print(df)
    print(line)
    #q4
    print(line)
    print(df[df['science']>85])
    print(line)
    #q5
    print(line)
    df['name']=df['name'].replace('pooja','puja')
    print(df)
    print(line)
    #q6
    print(line)
    df.sort_values(by='total', ascending=False, inplace=True)
    print(df)
    print(line)
    #q7
    print(line)
    plt.bar(df['name'],df['total'],color='blue',edgecolor='white')
    plt.title("total marks")
    plt.xlabel("names")
    plt.ylabel("total")
    plt.show()
    print(line)
    
    #q8
    print(line)
    name='amit'
    marks=df[df['name']==name].drop(columns='name').squeeze()
    plt.figure(figsize=(8, 5))
    plt.plot(marks.index,marks.values,color='blue')
    plt.xlabel('amit')
    plt.ylabel('marks')
    plt.grid(True)
    plt.show()
    print(line)

    #9
    print(line)
    data2={'name':['amit','sagar','pooja'],
           'math':[np.nan,76,88],
           'science':[91,np.nan,85]}
    print(line)
    
    df1 = pd.DataFrame(data2)
    df['math'] =df['math'].fillna(df['math'].mean())
    df['science']=df['science'].fillna(df['science'].mean())
    print(df1)
    print(df)
    print(line)

    #10
    print(line)
    df.drop(columns=['english'],inplace=True)
    print(df)
    print(line)

def main():
    line='_'*40
    print(line)
    print(line)
    data={'name':['amit','sagar','pooja'],
        'math': [85,90,78],
        'science' : [92,88,80],
        'english' :[75,85,82]}
    print(line)
  
    print(line)
    getinformation(data)
    data1()

    
if __name__=="__main__":
    main()    


    
