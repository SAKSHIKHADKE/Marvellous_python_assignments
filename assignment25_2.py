import pandas as pd
def main():
    line='_'*40
    print(line)
    data={'name':['a','b','c'],'age':[21.0,22.0,23.0]}
    df=pd.DataFrame(data)

    print("Column Data Types:")
    print(df.dtypes)

    df['age']=df['age'].astype(int)
    print(df)
    
if __name__=="__main__":
    main()    
