# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:58:15 2021

@author: K
"""

###### 세계행복지수 whr 
import pandas as pd 
import numpy as np
whr=pd.read_csv('world-happiness-report.csv')

####positive affectm negative affect 컬럼 제거
whr_ed1=whr.drop(['Positive affect','Negative affect'],axis=1)
whr_ed2=whr_ed1.rename(columns={'Country name':'Country','year':'Year'})
whr_ed2.to_csv('whr.csv',index=False)
whr=pd.read_csv('whr.csv')

###세계행복지수 데이터와 추가데이터간의 나라이름 통일
whr.Country.replace('Czech Republic','Czechia',inplace=True)
whr.Country.replace('Hong Kong S.A.R. of China','Hong Kong',inplace=True)
whr.Country.replace('Taiwan Province of China','Taiwan',inplace=True)
whr.Country.replace('Palestinian Territories','Palestine',inplace=True)
whr.Country.replace("Ivory Coast","Cote d'Ivoire",inplace=True)
whr.Country.replace('Swaziland','Eswatini',inplace=True)
whr_1=whr.set_index('Country')

####데이터가 부족한 나라들 제거 
whr_1.drop\
    (index=['Kosovo','North Cyprus','Somaliland region',\
            'Congo (Brazzaville)','Congo (Kinshasa)'],inplace=True)


whr_1.to_csv('whr22.csv')
whr22=pd.read_csv('whr22.csv')
'''
Somaliland region', 'Kosovo', 'Congo (Brazzaville)',
'Congo (Kinshasa)', 'North Cyprus',
'''

import pandas as pd 
###18,19년도 우울증 환자수 데이터
###컬럼명 변경 및 필요없는 컬럼 제거 
depres=pd.read_csv('depressive disorder 1819.csv')
depres.info()
depres_ed=depres.drop(['age','measure','sex','metric','cause'],axis=1)
depres_ed1=depres_ed.drop(['upper','lower'],axis=1)
depres_ed2=depres_ed1.rename\
    (columns={'location':'Country','val':'depressive disorders','year':'Year'})

dep1=depres_ed2 #우울증 1819년 

###17년도까지의 우울증환자 데이터
###컬럼명 변경 및 필요없는 컬럼 제거 
depre1=pd.read_csv('number-with-depression-by-country.csv')
depre1_ed=depre1.rename\
    (columns={'Prevalence - Depressive disorders - Sex: Both - Age: All Ages (Number)':'depressive disorders'})
del depre1_ed['Code']
depre1_ed_2=depre1_ed.rename(columns={'Entity':'Country'})

dep2=depre1_ed_2
dep2.Country.unique()

#17년도까지데이터와 18,19년도 데이터 합치기 
dep3=pd.concat([dep1,dep2])
dep4=dep3.sort_values(by='Country') # 나라 이름으로 정렬 
dep5=dep4[dep4['Year']>=2005]#2005년 이후 데이터만 추출 
dep5=dep5.sort_values(by=['Country','Year'])
dep5.to_csv('depression.csv',index=False)
depression=pd.read_csv('depression.csv')

#나라와 년도를 기준으로 합치기 
hap=pd.merge(whr22,depression,how='left',on=['Country','Year'])
hap.isnull().sum()

####결측값 앞에년도로 채우기 
###새파일로 저장 
hap=hap.fillna(method='ffill')
hap.to_csv('report1.csv',index=False)

import pandas as pd
report1=pd.read_csv('report1.csv')
report1

#전세계 학업년수 평균 추가 
scho=pd.read_csv('mean-years-of-schooling-1.csv')
scho.columns
scho=\
    scho.rename(columns={'Entity':'Country','Average Total Years of Schooling for Adult Population (Lee-Lee (2016), Barro-Lee (2018) and UNDP (2018))':'schooling'})
    
del scho['Code']
scho
###중간1이랑 합치기 
hap1=pd.merge(report1,scho,on=['Country','Year'],how='left')

#결측값 채우기 
hap1.fillna(method='ffill',inplace=True)
hap1.isnull().sum()
hap1.to_csv('report2.csv',index=False)
report2=pd.read_csv('report2.csv')

#알콜섭취량 # 알콜 x 사망률 
alc=pd.read_csv('death-rates-from-alcohol-use-disorders (1).csv')
alc.columns
del alc['Code']

alc=\
    alc.rename(columns={'Entity':'Country','Deaths - Alcohol use disorders - Sex: Both - Age: Age-standardized (Rate)':'alcohol disorders'})

###합치기
hap_ed5=pd.merge(report2,alc,on=['Country','Year'],how='left')
hap_ed5
#2018년 이후 

#결측값 채우기 
hap_ed5.fillna(method='ffill',inplace=True)
hap_ed5.to_csv('report3.csv',index=False)

report3=pd.read_csv('report3.csv')
report3.isnull().sum()
report3.info()
import pandas as pd 
import numpy as np     

####자살률 추가 
shadea=pd.read_csv('share-deaths-suicide.csv')
del shadea['Code']

##컬럼명 바꾸기 
shadea.rename\
    (columns={'Entity':'Country','Deaths - Self-harm - Sex: Both - Age: All Ages (Percent)':'suicide rates'},inplace=True)

shadea

#합치기 
report3_2=pd.merge(report3,shadea,how='left',on=['Country','Year'])
report3_2.fillna(method='ffill',inplace=True)
##비만률 추가 
obesity=pd.read_csv('share-of-deaths-obesity.csv')
del obesity['Code']

obesity.rename(columns={'Entity':'Country','Obesity (IHME, 2019)':'Obesity'},inplace=True)

report3_3=pd.merge(report3_2,obesity,how='left',on=['Country','Year'])
report3_3.fillna(method='ffill',inplace=True)
report3_3.isnull().sum()
report3_3.to_csv('report3_4.csv',index=False)
report3_4=pd.read_csv('report3_4.csv')
report3_4.set_index('Country',inplace=True)
report3_5=report3_4.drop(index='Hong Kong')
report3_5.to_csv('report3_5.csv')

report3_5.info()


### birth rate
### 출생률 데이터추가 
import pandas as pd 
report3_5=pd.read_csv('report3_5.csv')

br2=pd.read_csv('children-per-woman-UN.csv')
br2.info()
br2.columns
br2.Year.unique().max()
br2.rename\
    (columns={'Entity':'Country','Estimates, 1950 - 2020: Annually interpolated demographic indicators - Total fertility (live births per woman)':'Fertility'},inplace=True)
br2.Fertility.max()  

del br2['Code']

re3=pd.merge(report3_5,br2,how='left',on=['Country','Year'])

re3.to_csv('report3_7.csv',index=False) ###final

########################################################## 0806 ##################################################################
import pandas as pd
report3_7=pd.read_csv('report3_7.csv')
report3_7.info()

###우울증 관련 자료 추가
df1=pd.read_csv('mental-and-substance-use-as-share-of-disease.csv')

##### 컬럼 수정
df1.columns

del df1['Code']

df1.rename\
    (columns={'Entity':'Country','DALYs (Disability-Adjusted Life Years) - Mental and substance use disorders - Sex: Both - Age: All Ages (Percent)':'DALYs Mental disorders'},inplace=True)

####병합
q1=pd.merge(report3_7,df1,how='left',on=['Country','Year'])
q1.isnull().sum()

#앞 년도로 채우기 
q1.fillna(method='ffill',inplace=True)

##새폴더 저장 
q1.to_csv('report3_77.csv',index=False)