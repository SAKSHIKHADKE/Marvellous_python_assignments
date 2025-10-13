import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def winepredictor(datapath):
    df=pd.read_csv(datapath)

    x=df.drop(columns=['Class','Flavanoids','OD280/OD315 of diluted wines','Nonflavanoid phenols'])
    y=df['Class']

    print(df.head())

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    model=KNeighborsClassifier()

    model.fit(x_train,y_train)

    y_pred=model.predict(x_test)

    accuracy=accuracy_score(y_test,y_pred)

    print("accuracy of score:",accuracy)
    
def main():
    winepredictor("WinePredictor.csv")
if __name__=="__main__":
    main()    