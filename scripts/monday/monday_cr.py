import pandas as pd
import os
df = pd.read_excel("Mon_Cr.xlsx")

choice=input()
if choice=="a":

    time_slot = input()
    if time_slot == '8-9am':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '8-9am']):
                print(df.loc[i,'Class'])
    
    
    elif time_slot == '9-10am':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '9-10am']):
                print(df.loc[i,'Class'])

    elif time_slot == '10-11am':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '10-11am']):
                print(df.loc[i,'Class'])

    elif time_slot == '11:10-12:10pm':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '11:10-12:10pm']):
                print(df.loc[i,'Class'])
    
    elif time_slot=='12:10-1:10pm':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '12:10-1:10pm']):
                print(df.loc[i,'Class'])

    elif time_slot == '2-3pm':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '2-3pm']):
                print(df.loc[i,'Class'])           

    elif time_slot == '3-4pm':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '3-4pm']):
                print(df.loc[i,'Class'])

    elif time_slot == '4-5pm':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '4-5pm']):
                print(df.loc[i,'Class'])

    elif time_slot == '5-6pm':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '5-6pm']):
                print(df.loc[i,'Class'])            

elif choice=="b":
    room = int(input())
    flag = 0
    for i in range(0, len(df)):
        if room == df.iat[i, 0]:
            flag = flag + 1
            break

    # print(flag)
    if flag == 1:
     
        sr=df.iloc[i]
        dd=sr.to_frame()
        invalid_rows = [index for index, row in dd.iterrows() if row.isnull().any()]

        for i in invalid_rows:
            print(i)
    # else:
    #     print("Not found!")


