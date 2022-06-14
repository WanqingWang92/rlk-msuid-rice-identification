##print current dir and change into new working dir

import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#import ath_pfam
ath_nsg_pfam = pd.read_csv('ath_nsg_pfam_parser.csv')
ath_psg_pfam = pd.read_csv('ath_psg_pfam_parser.csv')
print(len(ath_nsg_pfam))
print(len(ath_psg_pfam))
ath_pfam = pd.concat([ath_nsg_pfam, ath_psg_pfam]).reset_index(drop=True)
print(len(ath_pfam))

#domains in arabidopsis
ath_domain = ath_pfam['hmm_name'].unique().astype(str)
ath_domain_list=[]

for index in range(ath_domain.shape[0]):
   domain = ath_domain[index]
   ath_domain_list.append(domain)
ath_domain_list = sorted(ath_domain_list)

#include domains from ath rlk experimentally verified dommains
list1 = pd.read_csv('ath_other_d_rlk_test.csv', names = ['ID'])
#include domains from ath rlk experimentally verified dommains
list2 = pd.read_csv('ath_other_d_rlp_test.csv', names = ['ID'])
ath_rlk_list = pd.concat([list1, list2])
ath_join = pd.merge(ath_rlk_list, ath_pfam, how="inner",left_on='ID',right_on='seq_id')
ath_join_domain = ath_join[['ID',"hmm_name"]]
ath_domain_small = ath_join_domain['hmm_name'].unique().astype(str)

ath_domain_small_list=[]

for index in range(ath_domain_small.shape[0]):
   domain = ath_domain_small[index]
   ath_domain_small_list.append(domain)
ath_domain_small_list = sorted(ath_domain_small_list)

all_d = ["DUF285", "FNIP", "LRR_1", "LRR_2", "LRR_3", "LRR_4", "LRR_5",
         "LRR_6", "LRR_8", "LRR_9", "Recep_L_domain", "LRRNT_2", "ABC1",
         "AceK", "Act-Frag_cataly", "Alpha_kinase", "APH", "APH_6_hur",
         "Choline_kinase", "CotH", "DUF1679", "DUF2252", "DUF4135", "EcKinase",
         "Fam20C", "Fructosamin_kin", "FTA2", "Haspin_kinase", "HipA_C",
         "Ins_P5_2-kin", "IPK", "IucA_IucC", "Kdo", "Kinase-like", "KIND",
         "PI3_PI4_kinase", "PIP49_C", "PIP5K", "Pkinase", "Pkinase_Tyr",
         "Pox_ser-thr_kin", "RIO1", "Seadorna_VP7", "UL97", "WaaY",
         "YrbL-PhoP_reg", "YukC", "Pkinase_C","Alginate_lyase2", "ArabFuran-catal",
         "Bac_rhamnosid", "Calreticulin", "Cleaved_Adhesin", "DUF1080",
         "DUF1349", "DUF1583", "DUF1961", "DUF2401", "DUF3472", "DUF4975",
         "Exotox-A_bind", "Gal-bind_lectin", "Glyco_hydro_11", "Glyco_hydro_12",
         "Glyco_hydro_16", "Glyco_hydro_32C", "Glyco_hydro_7", "Laminin_G_1",
         "Laminin_G_2", "Laminin_G_3", "Lectin_leg-like", "Lectin_legB", "MAM",
         "Methyltransf_FA", "Neuralized", "Pentaxin", "Peptidase_A4",
         "Polysacc_lyase", "PRY", "Reoviridae_Vp9", "Sial-lect-inser",
         "Sialidase", "SKN1", "Spike_NTD", "SPRY", "TgMIC1", "Toxin_R_bind_N",
         "TSP_C", "VP4_haemagglut", "XET_C", "YrpD", "Lectin_C", "B_lectin",
         "S_locus_glycop", "AMA-1", "MANEC", "PAN_1", "PAN_2", "PAN_3", "PAN_4",
         "LysM", "OapA", "Phage_tail_X", "Thaumatin", "BaffR-Tall_bind",
         "BCMA-Tall_bind", "NCD3G", "stn_TNFRSF12A", "TACI-CRD2", "TNFR_c6",
         "WAK", "GUB_WAK_bind", "WAK_assoc","Malectin", "Malectin_like", "cEGF",
         "CFC", "DSL", "EGF", "EGF_2", "EGF_3", "EGF_alliinase", "EGF_CA",
         "EGF_MSP1_1", "FOLN", "FXa_inhibition", "Gla", "hEGF", "Laminin_EGF",
         "Plasmod_Pvs28", "Sushi", "Sushi_2", "Tme5_EGF_like", "Stress-antifung"]
nb_arc_d = ["6PF2K", "AAA", "AAA-ATPase_like", "AAA_10", "AAA_11", "AAA_12",
            "AAA_13", "AAA_14", "AAA_15", "AAA_16", "AAA_17", "AAA_18",
            "AAA_19", "AAA_2", "AAA_21", "AAA_22", "AAA_23", "AAA_24",
            "AAA_25", "AAA_26", "AAA_27", "AAA_28", "AAA_29", "AAA_3", "AAA_30",
            "AAA_31", "AAA_32", "AAA_33", "AAA_34", "AAA_35", "AAA_5", "AAA_6",
            "AAA_7", "AAA_8", "AAA_9", "AAA_PrkA", "ABC_ATPase", "ABC_tran",
            "ABC_tran_Xtn", "Adeno_IVa2", "Adenylsucc_synt", "ADK",
            "AFG1_ATPase", "AIG1", "APS_kinase", "Arf", "ArgK", "ArsA_ATPase",
            "ATP-synt_ab", "ATP_bind_1", "ATP_bind_2", "ATPase", "ATPase_2",
            "Bac_DnaA", "BCA_ABC_TP_C", "Beta-Casp", "Cas_Csn2", "Cas_St_Csn2",
            "CbiA", "CBP_BcsQ", "CDC73_C", "CENP-M", "CFTR_R", "CLP1_P", "CMS1",
            "CoaE", "CobA_CobO_BtuR", "CobU", "cobW", "CPT", "CSM2",
            "CTP_synth_N", "Cytidylate_kin", "Cytidylate_kin2", "DAP3", "DEAD",
            "DEAD_2", "DLIC", "DNA_pack_C", "DNA_pack_N", "DNA_pol3_delta",
            "DNA_pol3_delta2", "DnaB_C", "dNK", "DUF1611", "DUF1726",
            "DUF2075", "DUF2326", "DUF2478", "DUF257", "DUF2791", "DUF2813",
            "DUF3584", "DUF463", "DUF815", "DUF853", "DUF87", "DUF927",
            "Dynamin_N", "Dynein_heavy", "ERCC3_RAD25_C", "Exonuc_V_gamma",
            "FeoB_N", "Fer4_NifH", "Flavi_DEAD", "FTHFS", "FtsK_SpoIIIE",
            "G-alpha", "Gal-3-0_sulfotr", "GBP", "GBP_C", "GTP_EFTU",
            "Gtr1_RagA", "Guanylate_kin", "GvpD", "HDA2-3", "Helicase_C",
            "Helicase_C_2", "Helicase_C_4", "Helicase_RecD", "Herpes_Helicase",
            "Herpes_ori_bp", "Herpes_TK", "Hydin_ADK", "IIGP", "IPPT", "IPT",
            "IstB_IS21", "KAP_NTPase", "KdpD", "Kinesin", "KTI12", "LAP1C",
            "Lon_2", "LpxK", "MCM", "MEDS", "Mg_chelatase", "Microtub_bd",
            "MipZ", "MMR_HSR1", "MMR_HSR1_C", "MobB", "MukB", "MutS_V",
            "Myosin_head", "NACHT", "NB-ARC", "NOG1", "NTPase_1", "NTPase_P4",
            "ORC3_N", "ParA", "Parvo_NS1", "PAXNEB", "PduV-EutP", "PhoH",
            "PIF1", "Podovirus_Gp16", "Polyoma_lg_T_C", "Pox_A32", "PPK2",
            "PPV_E1_C", "PRK", "PSY3", "Rad17", "Rad51", "Ras", "RecA",
            "ResIII", "RHD3", "RHSP", "RNA12", "RNA_helicase", "Roc",
            "RsgA_GTPase", "RuvB_N", "SbcCD_C", "SecA_DEAD", "Septin",
            "Sigma54_activ_2", "Sigma54_activat", "SKI", "SMC_N", "SNF2_N",
            "Spore_IV_A", "SRP54", "SRPRB", "SulA", "Sulfotransfer_1",
            "Sulfotransfer_2", "Sulfotransfer_3", "Sulphotransf", "T2SSE",
            "T4SS-DNA_transf", "Terminase_1", "Terminase_3", "Terminase_6",
            "Terminase_GpA", "Thymidylate_kin", "TIP49", "TK", "TniB", "Torsin",
            "TraG-D_C", "tRNA_lig_kinase", "TrwB_AAD_bind", "TsaE", "UvrB",
            "UvrD-helicase", "UvrD_C", "UvrD_C_2", "Viral_helicase1", "VirC1",
            "VirE", "Zeta_toxin", "Zot"]
target_d = all_d + nb_arc_d
other_d_rlk = ["Aph-1", "RCC1_2", "DUF3403", "Ribonuc_2-5A", "NAF", "DUF3660",
               "Glyco_hydro_18", "RVT_2", "DUF3453", "PP2C", "PRIMA1", "GDPD",
               "rve", "DHHC", "DUF4219", "PB1", "Transposase_21",
               "Transposase_24", "Sec16", "gag_pre-integrs", "PI3Ka",
               "Transpos_assoc", "SCAMP", "S1FA", "2OG-FeII_Oxy_2",
               "RETICULATA-like", "MEKHLA", "HPP", "Methyltransf_29",
               "MlaE", "Clathrin", "EDR1", "zf-HIT", "DUF569", "Herpes_gE",
               "Pep3_Vps18", "Beta-lactamase", "Rio2_N", "F-box", "SHQ1", "FBD",
               "MRP-L27", "HSP20", "Terpene_synth_C", "Nodulin_late",
               "Peptidase_M20", "Ost5", "IQ", "Adeno_E3_CR2", "Amino_oxidase",
               "p450", "EF-hand_7", "EMP70", "TMEM154", "OB_NTP_bind", "MatE",
               "EB", "PQQ", "FAD_binding_4", "WD40", "RVP_2", "E1-E2_ATPase",
               "Hydrolase", "EamA", "LEA_2", "DUF4441", "PMR5N", "H_PPase",
               "Cu_bind_like", "Sugar_tr", "Cupin_1", "Retrotran_gag_3",
               "Glyco_hydro_28", "Aldose_epim", "DHQS", "PRA1", "zf-RING_2",
               "Pyrophosphatase", "JmjN", "JmjC", "Peptidase_M50B", "PGG",
               "Ank_2", "SRF-TF", "FATC", "zf-C5HC2", "K-box", "ATP-synt_A",
               "Retrotran_gag_2", "Tmemb_14", "SLAC1"]
other_d_rlk_should = sorted([x for x in ath_domain_list if x not in target_d])
other_d_rlk_should_small = sorted([x for x in ath_domain_small_list if x not in target_d])
