import pandas as pd

def main():
    data= {'gender':['a+','b','a','c','b+']}
    df=pd.DataFrame(data)

    replacement_dict = {'a+': 'excellent', 'a': 'very good ', 'b+': 'good','b':'average','c':'poor'}
    print(replacement_dict)
    
if __name__=="__main__":
    main()    