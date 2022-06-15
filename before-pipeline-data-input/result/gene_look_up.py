import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#import rlk prediction and validified rlk
true_rlk = pd.read_csv('Experimentally_validated_rice_RLK.csv')
predicted_rlk = pd.read_csv('Osa_rlk.csv')

#make a list of predicted rlk gene id
rlk_p_list = predicted_rlk[["ID"]].values.tolist()
rlk_is_predicted = rlk_p_list
rlk_not_predicted = true_rlk[~true_rlk.MSU_ID.isin(rlk_is_predicted)]

#it seems like there is no true rlk gene predicted, will look into the