import pandas as pd
df = pd.read_excel("Thu_Lab_dataset_dmw.xlsx")
 

choice=input()
if choice=="a":

    time_slot = input()
    if time_slot == '9am-11am':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '9am-11am']):
                print(df.loc[i,'Class'])
    
    
    elif time_slot == '11am-1pm':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '11am-1pm']):
                print(df.loc[i,'Class'])

    elif time_slot == '2pm-4pm':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '2pm-4pm']):
                print(df.loc[i,'Class'])

    elif time_slot == '3pm-5pm':
        for i in range(0, len(df)):
            if pd.isnull(df.loc[i, '3pm-5pm']):
                print(df.loc[i,'Class'])
    
   
elif choice=="b":
    # print("Enter the room number: ")
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


