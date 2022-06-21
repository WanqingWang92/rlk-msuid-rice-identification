import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#import rlk prediction and validified rlk
true_rlk = pd.read_csv('Experimentally_validated_rice_RLK.csv')
predicted_rlk = pd.read_csv('Osa_rlk.csv')

not_predicted = true_rlk[~true_rlk['MSU_ID'].isin(predicted_rlk['ID'])]
