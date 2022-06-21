import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#change dir manually

# path = os.getcwd()
# print(path)
# new_path = path + '/heatmap'
# print(new_path)
# os.chdir(new_path)

#import rlk rp degs
rlk_rp_d1 = pd.read_csv('rlk_deg/rlk_rp_d1.csv')
rlk_rp_d2 = pd.read_csv('rlk_deg/rlk_rp_d2.csv')
rlk_rp_d3 = pd.read_csv('rlk_deg/rlk_rp_d3.csv')

rlk_rp_d12 = rlk_rp_d1.merge(rlk_rp_d2, how='outer',on = 'ID', suffixes=("_d1","_d2"))
rlk_rp_d123 = rlk_rp_d12.merge(rlk_rp_d3, how='outer',on = 'ID')
rlk_rp_d123.to_csv('rlk_rp_deg.csv', index=False)

#import rlk rsc degs
rlk_sc_h1 = pd.read_csv('rlk_deg/rlk_sc_h1.csv')
rlk_sc_h3 = pd.read_csv('rlk_deg/rlk_sc_h3.csv')
rlk_sc_h6 = pd.read_csv('rlk_deg/rlk_sc_h6.csv')
rlk_sc_h12 = pd.read_csv('rlk_deg/rlk_sc_h12.csv')

rlk_sc_h13 = rlk_sc_h1.merge(rlk_sc_h3, how='outer',on = 'ID', suffixes=("_h1","_h3"))
rlk_sc_h136 = rlk_sc_h13.merge(rlk_sc_h6, how='outer',on = 'ID')
rlk_sc_h13612 = rlk_sc_h136.merge(rlk_sc_h12, how='outer',on = 'ID', suffixes=("_h6","_h12"))
rlk_sc_h13612.to_csv('rlk_sc_deg.csv', index=False)

#import rlp rp degs
rlp_rp_d1 = pd.read_csv('rlp_deg/rlp_rp_d1.csv')
rlp_rp_d2 = pd.read_csv('rlp_deg/rlp_rp_d2.csv')
rlp_rp_d3 = pd.read_csv('rlp_deg/rlp_rp_d3.csv')

rlp_rp_d12 = rlp_rp_d1.merge(rlp_rp_d2, how='outer',on = 'ID', suffixes=("_d1","_d2"))
rlp_rp_d123 = rlp_rp_d12.merge(rlp_rp_d3, how='outer',on = 'ID')
rlp_rp_d123.to_csv('rlp_rp_deg.csv', index=False)

#import rlp rsc degs
rlp_sc_h1 = pd.read_csv('rlp_deg/rlp_sc_h1.csv')
rlp_sc_h3 = pd.read_csv('rlp_deg/rlp_sc_h3.csv')
rlp_sc_h6 = pd.read_csv('rlp_deg/rlp_sc_h6.csv')
rlp_sc_h12 = pd.read_csv('rlp_deg/rlp_sc_h12.csv')

rlp_sc_h13 = rlp_sc_h1.merge(rlp_sc_h3, how='outer',on = 'ID', suffixes=("_h1","_h3"))
rlp_sc_h136 = rlp_sc_h13.merge(rlp_sc_h6, how='outer',on = 'ID')
rlp_sc_h13612 = rlp_sc_h136.merge(rlp_sc_h12, how='outer',on = 'ID', suffixes=("_h6","_h12"))
rlp_sc_h13612.to_csv('rlp_sc_deg.csv', index=False)