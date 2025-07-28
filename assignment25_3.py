import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():
    data={'city':['pune','mumbai','delhi','pune','delhi']}
    
    df=pd.DataFrame(data)
    label_encoder = LabelEncoder()

    df['city_encoded'] = label_encoder.fit_transform(df['city'])
    print(df)
    

if __name__=="__main__":
    main()    