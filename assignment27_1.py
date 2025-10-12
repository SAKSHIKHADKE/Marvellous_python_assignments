import pandas as pd
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

def advertising(datapath):
    df=pd.read_csv(datapath)

    x=df.drop(columns=['sales'])
    y=df['sales']

    print(df.head())

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    model=LinearRegression()

    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)

    mse=metrics.mean_squared_error(y_test,y_pred)
    rmse=np.sqrt(mse)
    r2=metrics.r2_score(y_test,y_pred)

    print("mean squared error:",mse)
    print("root mean squared error:",rmse)
    print("r2 squared error:",r2)

def main():
    advertising("Advertising.csv")
if __name__=="__main__":
    main()