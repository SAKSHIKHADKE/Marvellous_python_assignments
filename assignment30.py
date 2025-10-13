import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score,ConfusionMatrixDisplay,roc_curve

def bank(datapath):
    line='-'*40
    print(line)

    df=pd.read_csv(datapath)

    print(df.head())
    print(line)

    for col in df.select_dtypes(include='object'):
        df[col]=LabelEncoder().fit_transform(df[col])


    print(df.isnull().sum())

    df.dropna()
    df.dropna(axis=1)
    print(df)
    print(df)

    print(line)

    print(df.describe())
  
    print(line)
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(), annot=True, cmap='Blues')
    plt.title('Class Distribution')
    plt.show()

    print(line)

    #df['education']=df['education'].map({'tertiary':0,'secondary':1,'unknown':2})
    #print(df)
    print("+" * 45)

    x=df.drop(columns=['default','campaign','pdays','previous','poutcome','y'])
    y=df['y']

    scaler=StandardScaler()
    x_scaled=scaler.fit_transform(x)
    
    x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,test_size=0.2,random_state=42)

    lr=LogisticRegression()
    knn=KNeighborsClassifier()
    rf=RandomForestClassifier()
    model2=RandomForestClassifier(n_estimators=150,max_depth=10,random_state=42)

    model=lr.fit(x_train,y_train)
    model1=knn.fit(x_train,y_train)
    model3=model2.fit(x_train,y_train)

    model_pred=lr.predict(x_test)
    model1_pred=knn.predict(x_test)
    model3_pred=model2.predict(x_test)

    model_acc=accuracy_score(model_pred, y_test)
    model1_acc=accuracy_score(model1_pred, y_test)
    model3_acc=accuracy_score(model3_pred, y_test)

    print("logistic regression accuracy is:",model_acc)
    print("knn accuracy is:",model1_acc)
    print("random forest accuracy is:",model3_acc)

    model_conf=confusion_matrix(model_pred, y_test)
    model1_conf=confusion_matrix(model1_pred, y_test)
    model3_conf=confusion_matrix(model3_pred, y_test)

    print("logistic regression confusion matrix is:",model_conf)
    print("knn confusion matrix is:",model1_conf)
    print("random forest confusion matrix is:",model3_conf)

    model_cl=classification_report(model_pred, y_test)
    model1_cl=classification_report(model1_pred, y_test)
    model3_cl=classification_report(model3_pred, y_test)

    print("logistic regression classification report is:", model_cl)
    print("knn classification report is:", model1_cl)
    print("random forest classification report is:", model3_cl)

    model_ras=roc_auc_score(model_pred, y_test)
    model1_ras=roc_auc_score(model1_pred, y_test)
    model3_ras=roc_auc_score(model3_pred, y_test)

    print("logistic regression roc auc score is:",model_ras)
    print("knn roc auc score is:",model1_ras)
    print("random forest roc auc score is:",model3_ras)

    model_cd=ConfusionMatrixDisplay(model_conf,display_labels=np.unique(y_test))
    model_cd.plot(cmap="Blues")
    plt.title("confusion matrix of logistic regression algorithm")
    plt.show()

    model_cd=ConfusionMatrixDisplay(model1_conf,display_labels=np.unique(y_test))
    model_cd.plot(cmap="Blues")
    plt.title("confusion matrix of knn algorithm")
    plt.show()

    model_cd=ConfusionMatrixDisplay(model3_conf,display_labels=np.unique(y_test))
    model_cd.plot(cmap="Blues")
    plt.title("confusion matrix of random forest algorithm")
    plt.show()

    lr,trf,_=roc_curve(model_pred,y_test)
    plt.plot(lr,trf,color="black")
    plt.plot([0,1],[0,1],"r--")
    plt.xlabel("false positive rate")
    plt.ylabel("true positive rate")
    plt.title("roc curve of logistic regression")
    plt.grid()
    plt.show()

    knn,trf,_=roc_curve(model1_pred,y_test)
    plt.plot(knn,trf,color="black")
    plt.plot([0,1],[0,1],"r--")
    plt.xlabel("false positive rate")
    plt.ylabel("true positive rate")
    plt.title("roc curve of knn")
    plt.grid()
    plt.show()

    rf,trf,_=roc_curve(model_pred,y_test)
    plt.plot(rf,trf,color="black")
    plt.plot([0,1],[0,1],"r--")
    plt.xlabel("false positive rate")
    plt.ylabel("true positive rate")
    plt.title("roc curve of random forest")
    plt.grid()
    plt.show()

def main():
    bank("bank-full.csv")
if __name__=="__main__":
    main()    

    #confusionmatrix
    #classification_report
    #rocaocscore
    #confusion matrix display
    #roc curve display