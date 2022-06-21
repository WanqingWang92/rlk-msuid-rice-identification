
import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#change dir manually

# path = os.getcwd()
# print(path)
# new_path = path + '/heatmap'
# print(new_path)
# os.chdir(new_path)

#transform domain into one column, import deg, rlk and rlp files.
rlk = pd.read_csv('Osa_rlk.csv')
rlp = pd.read_csv('Osa_rlp.csv')

#import RP ad RSC DEG files
rpd1 = pd.read_csv('rice_plant/1d_RB_vs_Moc_DEG.csv')
rpd2 = pd.read_csv('rice_plant/2d_RB_vs_Moc_DEG.csv')
rpd3 = pd.read_csv('rice_plant/3d_RB_vs_Moc_DEG.csv')
rpd=[rpd1, rpd2, rpd3]

rsch1 = pd.read_csv('rice_suspension_cell/1h_chitin_vs_mock_DEG.csv')
rsch3 = pd.read_csv('rice_suspension_cell/3h_chitin_vs_mock_DEG.csv')
rsch6 = pd.read_csv('rice_suspension_cell/6h_chitin_vs_mock_DEG.csv')
rsch12 = pd.read_csv('rice_suspension_cell/12h_chitin_vs_mock_DEG.csv')
rsch=[rsch1, rsch3, rsch6, rsch12]

#for rlk, output deg results
for index, data in enumerate(rpd):
    rlk_deg = rlk.merge(data, how='inner',left_on = 'Isoform_ID', right_on='ID')
    rlk_deg = rlk_deg.drop(columns=['SP','Isoform_ID','baseMean', 'lfcSE', 'stat','pvalue','padj'])
    rlk_deg.to_csv('rlk_rp_'+ str(index) +'.csv', index=False)

for index, data in enumerate(rsch):
    rlk_deg = rlk.merge(data, how='inner',left_on = 'Isoform_ID', right_on='ID')
    rlk_deg = rlk_deg.drop(columns=['SP','Isoform_ID','baseMean', 'lfcSE', 'stat','pvalue','padj'])
    rlk_deg.to_csv('rlk_sc_'+ str(index) +'.csv', index=False)

#for rlp, output deg results
for index, data in enumerate(rpd):
    rlp_deg = rlp.merge(data, how='inner',left_on = 'Isoform_ID', right_on='ID')
    rlp_deg = rlp_deg.drop(columns=['SP','Isoform_ID','baseMean', 'lfcSE', 'stat','pvalue','padj'])
    rlp_deg.to_csv('rlp_rp_'+ str(index) +'.csv', index=False)

for index, data in enumerate(rsch):
    rlp_deg = rlp.merge(data, how='inner',left_on = 'Isoform_ID', right_on='ID')
    rlp_deg = rlp_deg.drop(columns=['SP','Isoform_ID','baseMean', 'lfcSE', 'stat','pvalue','padj'])
    rlp_deg.to_csv('rlp_sc_'+ str(index) +'.csv', index=False)