import pandas as pd
import numpy as np
def main():
    line='_'*40
    print(line)
    data={'salary':[25000,27000,29000,31000,50000,100000]}
    
    df=pd.DataFrame(data)
    Q1 = df['salary'].quantile(0.25)  
    Q3 = df['salary'].quantile(0.75)
    IQR = Q3 - Q1  
    print(IQR)
    print(line)
if __name__=="__main__":
    main()    