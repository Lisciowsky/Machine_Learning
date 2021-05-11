import os
import pandas as pd
import seaborn as sn
import numpy as np


dire = '/home/kuba/Downloads'
os.chdir(dire)

df_Historia_kontaktu = pd.read_excel('Dane_do_zadania_wysylka_walentynkowa.xlsx', sheet_name = 'Historia Kontaktu')
df_Tabela_Transakcji = pd.read_excel('Dane_do_zadania_wysylka_walentynkowa.xlsx', sheet_name = 'Tabela Transakcji')
merged_df = pd.merge(left = df_Historia_kontaktu, right = df_Tabela_Transakcji, how = 'inner').groupby(['id_klienta', 'grupa']).sum().reset_index()
#sorting ascending by date

#plots
sn.histplot(merged_df, x = 'kwota_zakupu', kde = True, element = 'bars', fill = True, hue = 'grupa', stat = 'count')

sn.histplot(merged_df[merged_df['grupa'] == 'Sent'], x = 'kwota_zakupu', kde = True, element = 'bars', fill = True)
sn.histplot(merged_df[merged_df['grupa'] == 'Control'], x = 'kwota_zakupu', kde = True, element = 'bars', fill = False)
sn.histplot(merged_df, x = 'kwota_zakupu', kde = True, element = 'bars', fill = False)

sn.kdeplot(data = merged_df, x = 'kwota_zakupu', hue = 'grupa', multiple = 'stack')


merged_df[merged_df['grupa'] == 'Sent'].kwota_zakupu.describe()
merged_df[merged_df['grupa'] == 'Control'].kwota_zakupu.describe()

len_sent = len(merged_df[merged_df['grupa'] == 'Sent'])
len_control = len(merged_df[merged_df['grupa'] == 'Control'])

sn.lineplot(data = merged_df, x = 'data_zakupu', y = 'kwota_zakupu', hue = 'grupa')


#sorting
merged_df.sort_values(by = 'data_zakupu', ascending = True, inplace = True)
merged_df.index = merged_df['data_zakupu']
merged_df.drop('data_zakupu', axis = 1)
#resampling



# merged_df = merged_df.groupby(['id_klienta', 'grupa']).sum()   # check = merged_df[merged_df.duplicated('id_klienta', keep = False)].groupby('id_klienta')['grupa'].sum()
# merged_df[merged_df.duplicated(subset = ['id_klineta'], keep = False)]
