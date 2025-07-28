import pandas as pd
from sklearn.model_selection import train_test_split

def main():

    data={'age': [22,25,47,52,46,56], 'purchased':[0,1,1,0,1,0]}
    df=pd.DataFrame(data)

    X = df[['age']]  # Features
    y = df['purchased']  # Target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(X_train, X_test, y_train, y_test )


if __name__=="__main__":
    main()    