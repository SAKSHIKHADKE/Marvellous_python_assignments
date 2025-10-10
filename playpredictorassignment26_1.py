import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def playpredictor(datapath):
    df=pd.read_csv(datapath)


   
    df['Whether']=df['Whether'].map({'Sunny':0,'Overcast':1,'Rainy':2})
    df['Temperature']=df['Temperature'].map({'Hot':0,'Mild':1,'Cool':2})
    df['Play']=df['Play'].map({'Yes':0,'No':1})

    print(df.head())
    print(df.shape)

    x=df.drop(columns='Play')
    y=df['Play']

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    model=KNeighborsClassifier(n_neighbors=5)

    model.fit(x_train,y_train)
    
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)

    print("accuracy score is :",accuracy)

   
def main():
    playpredictor("PlayPredictor.csv")
if __name__=="__main__":
    main()   