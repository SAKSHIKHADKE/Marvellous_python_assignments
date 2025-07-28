import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

    #q1
data={'name':['amit','sagar','pooja'],
        'math': [85,90,78],
        'science' : [92,88,80],
        'english' :[75,85,82]}

df=pd.DataFrame(data)
line='_'*40
print(line)
print(df)

maximum = df['math'].max()
minimum = df['math'].min()
print("maximum value is : %s \n MInimum value is : %s"%(maximum, minimum))

print(line)


    #q2
print(line)
df['gender']=['male','male','female']
df_encoded=pd.get_dummies(df,columns=['gender'])
print(df_encoded)
print(line)

#q3
print(line)
average_marks=df.groupby('gender')[['math','science','english']].mean()
print(average_marks)
print(line)

#q4
print(line)
df['gender']=['male','male','female']
df['gender'] = df['gender'].map({'male' : 0, 'female' : 1})
names=df[df['name']=='sagar'].drop(columns='name').squeeze()
plt.pie(names, labels = names.index, colors = ['red', 'blue', 'green'])
plt.title("sagar marks")
plt.show()
print(line)

    #q5

print(line)
df['total']=df['math']+df['science']+df['english']
df['status'] = df['total'].apply(lambda x: 'pass' if x >= 250 else 'fail')

print(df)

print(line)

#q6
print(line)
value_counts = df['status'].value_counts()
print("number of students who passed:",value_counts)
print(line)

#q7
print(line)
df.to_csv('final_dataframe.csv', index=False)
print(df)
print(line)

#q8
print(line)
plt.hist(df['math'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Math Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()
print(line)

#9
print(line)
df.rename(columns={'math': 'mathematics'}, inplace=True)
print(df)
print(line)

#10
print(line)
plt.boxplot(df['english'],patch_artist=True)
plt.title("english marks")
plt.show()
