import pandas as pd

def main():
    data={'marks':[45,67,88,32,76]}

    df=pd.DataFrame(data)

    df['marks'] = df['marks'].where(df['marks'] >= 50, "Fail")
    print(df)
    
if __name__=="__main__":
    main()    