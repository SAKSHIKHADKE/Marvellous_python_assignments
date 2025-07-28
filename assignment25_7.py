import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def main():
    data={'age':[18,22,25,30,35]}

    df=pd.DataFrame(data)

    maximum = df['age'].max()
    minimum = df['age'].min()

    print("maximum value is : %s \n MInimum value is : %s"%(maximum, minimum))


if __name__=="__main__":
    main()    