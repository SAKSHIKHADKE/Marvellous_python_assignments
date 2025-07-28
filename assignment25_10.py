import pandas as pd 
from sklearn.model_selection import train_test_split

def main():
    data={'age':[25,30,45,35,22],
          'salary':[50000,60000,80000,65000,45000],
          'purchased':[1,0,1,0,1]}
    
    df=pd.DataFrame(data)

    X=df.drop(columns=['age','salary'])
    y=df['purchased']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(X_train, X_test, y_train, y_test)

if __name__=="__main__":
    main()    