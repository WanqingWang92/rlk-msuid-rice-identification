import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

lrr_d = ["DUF285", "FBXL18_LRR", "FNIP", "LRR_1", "LRR_10", "LRR_11", "LRR_12", "LRR_2", "LRR_3", "LRR_4", "LRR_5",
         "LRR_6", "LRR_8", "LRR_9", "LRR_RI_capping", "Recep_L_domain", "Transp_inhibit", "TTSSLRR", "LRRNT_2"]

# pkinase clan and Pkinase_C
pkinase_d = ["ABC1", "AceK_kinase", "Act-Frag_cataly", "Alpha_kinase", "APH", "APH_6_hur", "Choline_kinase", "CotH",
             "DUF1679", "DUF2252", "DUF4135", "DUF5898", "EcKL", "Fam20C", "Fructosamin_kin", "FTA2", "Haspin_kinase",
             "HipA_C", "Ins_P5_2-kin", "IPK", "IucA_IucC", "Kdo", "Kinase-like", "Kinase-PolyVal", "KIND", "Pan3_PK",
             "PI3_PI4_kinase", "PIP49_C", "PIP5K", "PK_Tyr_Ser-Thr", "Pkinase", "Pkinase_fungal", "Pox_ser-thr_kin",
             "RIO1", "Seadorna_VP7", "TCAD9", "UL97", "WaaY", "YrbL-PhoP_reg", "YukC", "Pkinase_C"]

l_lectin_d = ["3keto-disac_hyd", "Alginate_lyase2", "ArabFuran-catal", "Arabino_trans_N", "Bac_rhamnosid",
              "Bact_lectin", "bCoV_S1_N", "Calreticulin", "Cleaved_Adhesin", "DUF1349", "DUF1583", "DUF1583_N",
              "DUF1961", "DUF3472", "DUF4975", "DUF6250", "Exotox-A_bind", "Gal-bind_lectin", "GalBD_like", "GH131_N",
              "GH43_C2", "Glyco_hydro_11", "Glyco_hydro_12", "Glyco_hydro_16", "Glyco_hydro_32C", "Glyco_hydro_7",
              "HA1", "Laminin_G_1", "Laminin_G_2", "Laminin_G_3", "Lectin_leg-like", "Lectin_legB", "MAM",
              "Methyltransf_FA", "Neuralized", "Pentaxin", "Peptidase_A4", "Polysacc_lyase", "PRY", "Reoviridae_Vp9",
              "Sial-lect-inser", "Sialidase", "SKN1_KRE6_Sbg1", "SPRY", "TgMIC1", "Toxin_R_bind_N", "TSP_C",
              "VP4_haemagglut", "XET_C", "YJL171C_Tos1_C", "YrpD"]

c_lectin_d = ["Lectin_C"]

g_lectin_b_d = ["B_lectin"]

g_lectin_s_d = ["S_locus_glycop"]

g_lectin_p_d = ["AMA-1", "MANEC", "PAN_1", "PAN_2", "PAN_3", "PAN_4"]

lysm_d = ["gp37_C", "LysM", "OapA", "Phage-Gp8", "Phage_gp53", "Phage_tail_X", "T4_gp9_10"]

pr5k_d = ["Thaumatin"]

tnfr_d = ["BaffR-Tall_bind", "BCMA-Tall_bind", "NCD3G", "stn_TNFRSF12A",
          "TACI-CRD2", "TNFR_c6"]

wak_d = ["WAK", "GUB_WAK_bind", "WAK_assoc"]

malectin_d = ["Malectin", "Malectin_like"]

egf_d = ["cEGF", "CFC", "DSL", "EGF", "EGF_2", "EGF_3", "EGF_alliinase", "EGF_CA", "EGF_MSP1_1", "EGF_Tenascin",
         "Ephrin_rec_like", "Fibrillin_U_N", "FOLN", "FXa_inhibition", "Gla", "hEGF", "I-EGF_1", "Laminin_EGF",
         "Plasmod_Pvs28", "Sushi", "Sushi_2", "Tme5_EGF_like"]

stress_antifung_d = ["Stress-antifung"]

all_d = lrr_d + pkinase_d + l_lectin_d + c_lectin_d + g_lectin_b_d + g_lectin_s_d + g_lectin_p_d + lysm_d +\
pr5k_d + tnfr_d + wak_d + malectin_d + egf_d + stress_antifung_d

almost_all_d = lrr_d + l_lectin_d + c_lectin_d + g_lectin_b_d + g_lectin_s_d + g_lectin_p_d + lysm_d +\
pr5k_d + tnfr_d + wak_d + malectin_d + egf_d + stress_antifung_d

