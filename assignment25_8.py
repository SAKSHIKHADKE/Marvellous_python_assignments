import pandas as pd
import numpy as np

def main():
    data={'marks':[85,np.nan,90,np.nan,95]}

    df=pd.DataFrame(data)

    df['marks'] = df['marks'].interpolate(method='linear')
    print(df)



if __name__=="__main__":
    main()    