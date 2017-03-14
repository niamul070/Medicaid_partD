# coding: utf-8
import pandas as pd
#read data table
df=pd.read_table('PartD_Prescriber_PUF_NPI_14.txt')
df.columns
#q1 avg benifiary
bn=df[df.BENE_COUNT>10]
bn.BENE_COUNT.sum()/len(df.index)
#129.61052267620505

#median of average prc
avg_pr=df.TOTAL_DAY_SUPPLY/df.TOTAL_CLAIM_COUNT

#specialty fraction
by_spcl1=df[(df.BRAND_SUPPRESS_FLAG !='*') &(df.BRAND_SUPPRESS_FLAG !='#')]
spcl2=by_spcl1.groupby('SPECIALTY_DESCRIPTION').sum()
spcl3=spcl2[spcl2.TOTAL_CLAIM_COUNT>1000]
bran_rat=spcl3['BRAND_CLAIM_COUNT']/spcl3['TOTAL_CLAIM_COUNT']
bran_rat[:10]
bran_rat.std()
#0.08806824128592805

#opioid benefit min max ratio diff
opioid_state=df.groupby('NPPES_PROVIDER_STATE').sum()
op_ratio=opioid_state['OPIOID_BENE_COUNT']/opioid_state['ANTIBIOTIC_CLAIM_COUNT']
op_ratio.max()-op_ratio.min()
#0.51833342436324581

#low income and 65 older claim correlation
ge65=df[(df.BENE_COUNT_GE65_SUPPRESS_FLAG !='*') & (df.BENE_COUNT_GE65_SUPPRESS_FLAG !='#')]
ge_rat=ge65['BENE_COUNT_GE65']/ge65['TOTAL_CLAIM_COUNT']
lis=df[(df.LIS_SUPPRESS_FLAG !='*') & (df.LIS_SUPPRESS_FLAG !='#')]
lis_rat=lis['LIS_CLAIM_COUNT']/lis['TOTAL_CLAIM_COUNT']
type(lis_rat)
ge_rat.corr(lis_rat)

#avg inflation rate
df13=pd.read_table('PARTD_PRESCRIBER_PUF_NPI_13.tab',low_memory=False)

cost14=df.TOTAL_DRUG_COST/df.TOTAL_DAY_SUPPLY
cost13=df13.TOTAL_DRUG_COST/df13.TOTAL_DAY_SUPPLY
diff=cost14-cost13
diff.shape
type(diff)
diff.mean()



