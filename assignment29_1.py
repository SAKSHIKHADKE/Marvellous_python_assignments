import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,ConfusionMatrixDisplay

def diabetes(datapath):

    line='_'*40
    df=pd.read_csv(datapath)

    x=df.drop(columns=['target'])
    y=df['target']

    print(line)

    print(df.info())
    print(line)
    print(df.isnull().sum())
    print(df.describe())

    print(line)
    df.fillna(df.mean(numeric_only=True))
    print(df)

    print(line)

    scaler=StandardScaler()
    x_scaled=scaler.fit_transform(x)
    
    plt.figure(figsize=(10,6))
    plt.hist(df['target'],color='blue',edgecolor='black')
    plt.xlabel("target value")
    plt.ylabel("frequency")
    plt.title("distribution of target varibale")
    plt.show()
    pairplot(df)
    boxplot(df)

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    
    log_clf=LogisticRegression()
    dt_clf=DecisionTreeClassifier()
    knn_clf=KNeighborsClassifier()

    log_clf.fit(x_train,y_train)
    y_pred=log_clf.predict(x_test)
    log_accuracy=accuracy_score(y_test,y_pred)
    print(log_accuracy*100)

    dt_clf.fit(x_train,y_train)
    y_pred=dt_clf.predict(x_test)
    dt_accuracy=accuracy_score(y_test,y_pred)
    print(dt_accuracy*100)

    knn_clf.fit(x_train,y_train)
    y_pred=knn_clf.predict(x_test)
    knn_accuracy=accuracy_score(y_test,y_pred)
    print(knn_accuracy*100)
    print(line)

    knn_conf=confusion_matrix(y_pred,y_test)
    lr_conf=confusion_matrix(y_pred,y_test)
    dt_conf=confusion_matrix(y_pred,y_test)

    print("KNeighbors confusionmatrix is:",knn_conf)
    print("logisticregression confusin matrix is:",lr_conf)
    print("decision tree confusion matrix is:",dt_clf)

    print(line)

    knn_pres=precision_score(y_pred,y_test)
    lr_pres=precision_score(y_pred,y_test)
    dt_pres=precision_score(y_pred,y_test)

    print("KNeighbors precision score is:",knn_pres)
    print("logisticregression precision score is:",lr_pres)
    print("decision tree precision score is:",dt_pres)

    print(line)

    knn_rec=recall_score(y_pred,y_test)
    lr_rec=recall_score(y_pred,y_test)
    dt_rec=recall_score(y_pred,y_test)

    print("KNeighbors recall_score is:",knn_rec)
    print("logisticregression recall_score is:",lr_rec)
    print("decision tree recall_score is:",dt_rec)

    print(line)

    knn_f=f1_score(y_pred,y_test)
    lr_f=f1_score(y_pred,y_test)
    dt_f=f1_score(y_pred,y_test)

    print("KNeighbors""f1 score  is:",knn_f)
    print("logisticregression f1_score is:",lr_f)
    print("decision tree f1_score is:",dt_f)

    print("visual representation")

    cmdk=ConfusionMatrixDisplay(knn_conf,display_labels=np.unique(y_test))
    cmdk.plot(cmap='Blues')
    plt.title("confusion matrix of kneighbours classifier")
    plt.show()

    cmdl=ConfusionMatrixDisplay(lr_conf,display_labels=np.unique(y_test))
    cmdl.plot(cmap='Greens')
    plt.title("confusion matrix of logistic regression")
    plt.show()

    cmdd=ConfusionMatrixDisplay(dt_conf,display_labels=np.unique(y_test))
    cmdd.plot(cmap='Reds')
    plt.title("confusion matrix of decision tree")
    plt.show()

    print(line)

    df=pd.DataFrame({'metrics':['algrithmns','accuracy','confusion matrix','f1 score','precision','recall'],
                     'value': [LogisticRegression,log_accuracy,lr_conf,lr_f,lr_pres,lr_rec],
                     'value1':[KNeighborsClassifier,knn_accuracy,knn_conf,knn_f,knn_pres,knn_rec],
                     'value2':[DecisionTreeClassifier,dt_accuracy,dt_conf,dt_f,dt_pres,dt_rec]})
    

                    
    print(line)

    df.to_csv("assignemt29_1.csv",index=False)
    print(df)
    
    


def pairplot(df):
    
    sns.pairplot(df)
    plt.title("pairplot")
    plt.xlabel("names")
    plt.ylabel("frequency")
    plt.show()

def boxplot(df):
    plt.boxplot(df['target'],patch_artist=True)
    plt.title("box plot")
    plt.xlabel("names")
    plt.ylabel("frequency")
    plt.show()

   

   
def main():
    diabetes("diabetes.csv")
   
if __name__=="__main__":
    main()
