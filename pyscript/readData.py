import os
import pandas as pd

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/978-4-274-22101-9.xlsx')

df1 = pd.read_excel(data_path, sheet_name='概要')
df2 = pd.read_excel(data_path, sheet_name='ID付きPOSデータ（POSデータ）')
df3 = pd.read_excel(data_path, sheet_name='ID付きPOSデータ（IDデータ）', usecols=[0, 1, 2])
df3_ = pd.read_excel(data_path, sheet_name='ID付きPOSデータ（IDデータ）', usecols=[5, 6], skiprows=range(4, 1001))
df4 = pd.read_excel(data_path, sheet_name='アンケート・データ', usecols=range(11))
df4_ = pd.read_excel(data_path, sheet_name='アンケート・データ', usecols=[12, 13, 14], skiprows=range(11, 86)) 
df5 = pd.read_excel(data_path, sheet_name='プロファイル評価データ', usecols=range(9))
df5_ = pd.read_excel(data_path, sheet_name='プロファイル評価データ', usecols=range(11, 17), skiprows=range(9, 17))
df5__ = pd.read_excel(data_path, sheet_name='プロファイル評価データ', usecols=range(11, 17), skiprows=list(range(11))+list(range(14, 17)))
df6 = pd.read_excel(data_path, sheet_name='商品選択データ', usecols=range(9))
df7 = pd.read_excel(data_path, sheet_name='ネットワークデータ', usecols=[0, 1])
df8 = pd.read_excel(data_path, sheet_name='商品クチコミ・データ')
df9 = pd.read_excel(data_path, sheet_name='リピート購買データ')
