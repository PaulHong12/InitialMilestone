import os 
import pandas as pd 

df = pd.read_csv('/home/wuyou/workspace/CLAM_balance/RESULT_out/process_list_autogen.csv') # 这个是上一步生成的文件
ids1 = [i[:-4] for i in df.slide_id]
ids2 = [i[:-3] for i in os.listdir('/home/wuyou/workspace/CLAM_balance/RESULT_out/patches')]
df['slide_id'] = ids1
ids = df['slide_id'].isin(ids2)
sum(ids)
df.loc[ids].to_csv('/home/wuyou/workspace/CLAM_balance/RESULT_out/Step_2.csv',index=False)
