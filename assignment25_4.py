from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def main():

    data={'department':['hr','it','finance','hr','it']}
    df=pd.DataFrame(data)

    df['department'] = df['department'].map({'hr' : 0, 'it' : 1, 'finance' : 2})

    print(df)
if __name__=="__main__":
    main()    
