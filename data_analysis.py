import pandas as pd
import matplotlib.pyplot as plt
import re


data_train = pd.read_csv("train.csv")

plt.figure(num=u'data distribution')
plt.subplot2grid((3,3),(0,0))
gender_x=data_train.Sex.value_counts().sort_index(ascending=True).index.values
gender_s=data_train[data_train.Survived==1].Sex.value_counts().sort_index(ascending=True).values
gender_not_s=data_train[data_train.Survived==0].Sex.value_counts().sort_index(ascending=True).values
plt.bar(gender_x,gender_s,color='dodgerblue')
plt.bar(gender_x,gender_not_s,bottom=gender_s,color='tomato')
for i in range(len(gender_x)):
    plt.text(gender_x[i],gender_s[i]/2-15,str(round(gender_s[i]/(gender_s[i]+gender_not_s[i])*100,2))+'%',
             ha='center',va='bottom')
    plt.text(gender_x[i],gender_s[i]+gender_not_s[i]/2-15,
             str(round(gender_not_s[i]/(gender_s[i]+gender_not_s[i])*100,2))+'%',ha='center',va='bottom')
plt.title(u"gender distribution")
plt.ylabel(u"number")
plt.legend((u'Survived',u'Not Survived'),loc='best')

plt.subplot2grid((3,3),(0,1))
class_x=data_train.Pclass.value_counts().sort_index(ascending=True).index.values
class_s=data_train[data_train.Survived==1].Pclass.value_counts().sort_index(ascending=True).values
class_not_s=data_train[data_train.Survived==0].Pclass.value_counts().sort_index(ascending=True).values
plt.bar(class_x,class_s,color='dodgerblue')
plt.bar(class_x,class_not_s,bottom=class_s,color='tomato')
for i in range(len(class_x)):
    plt.text(class_x[i],class_s[i]/2-15,str(round(class_s[i]/(class_s[i]+class_not_s[i])*100,2))+'%',
             ha='center',va='bottom')
    plt.text(class_x[i],class_s[i]+class_not_s[i]/2-15,
             str(round(class_not_s[i]/(class_s[i]+class_not_s[i])*100,2))+'%',ha='center',va='bottom')
plt.ylabel(u"number")
plt.title(u"class distribution")
plt.legend((u'Survived',u'Not Survived'),loc='best')

plt.subplot2grid((3,3),(0,2))
age_listbins=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,200]
age_listlabel=['0_5','6_10','11_15','16_20','21_25','26_30','31_35','36_40','41_45',
               '46_50','51_55','56_60','61_65','66_70','70+']
age_s=pd.cut(data_train[data_train.Survived==1].Age,age_listbins,labels=age_listlabel).value_counts(sort=False).values
age_not_s=pd.cut(data_train[data_train.Survived==0].Age,age_listbins,labels=age_listlabel).value_counts(sort=False).values
plt.barh(age_listlabel,age_s)
plt.barh(age_listlabel,-age_not_s)
plt.ylabel(u"age")
plt.title(u"age distribution")
plt.legend((u'Survived',u'Not Survived'),loc='best')

plt.subplot2grid((3,3),(1,0))
SibSp_listbins=[-1,0,1,2,3,4,20]
SibSp_listlabel=['0','1','2','3','4','4+']
SibSp_s=pd.cut(data_train[data_train.Survived==1].SibSp,SibSp_listbins,labels=SibSp_listlabel).value_counts(sort=False).values
SibSp_not_s=pd.cut(data_train[data_train.Survived==0].SibSp,SibSp_listbins,labels=SibSp_listlabel).value_counts(sort=False).values
plt.bar(SibSp_listlabel,SibSp_s,color='dodgerblue')
plt.bar(SibSp_listlabel,SibSp_not_s,bottom=SibSp_s,color='tomato')
plt.text('2',400,'Death rate')
for i in range(len(SibSp_listlabel)):
    plt.text(SibSp_listlabel[i],SibSp_s[i]+SibSp_not_s[i]/2-15,
             str(round(SibSp_not_s[i]/(SibSp_s[i]+SibSp_not_s[i])*100,2))+'%',ha='center',va='bottom')
plt.ylabel(u"number")
plt.title(u"SibSp distribution")
plt.legend((u'Survived',u'Not Survived'),loc='best')

plt.subplot2grid((3,3),(1,1))
Parch_listbins=[-1,0,1,2,20]
Parch_listlabel=['0','1','2','2+']
Parch_s=pd.cut(data_train[data_train.Survived==1].Parch,Parch_listbins,labels=Parch_listlabel).value_counts(sort=False).values
Parch_not_s=pd.cut(data_train[data_train.Survived==0].Parch,Parch_listbins,labels=Parch_listlabel).value_counts(sort=False).values
plt.bar(Parch_listlabel,Parch_s,color='dodgerblue')
plt.bar(Parch_listlabel,Parch_not_s,bottom=Parch_s,color='tomato')
plt.text('1',400,'Death rate')
for i in range(len(Parch_listlabel)):
    plt.text(Parch_listlabel[i],Parch_s[i]+Parch_not_s[i]/2-15,
             str(round(Parch_not_s[i]/(Parch_s[i]+Parch_not_s[i])*100,2))+'%',ha='center',va='bottom')
plt.ylabel(u"number")
plt.title(u"Parch distribution")
plt.legend((u'Survived',u'Not Survived'),loc='best')

plt.subplot2grid((3,3),(1,2))
embarked_x=data_train.Embarked.value_counts().sort_index(ascending=True).index.values
embarked_s=data_train[data_train.Survived==1].Embarked.value_counts().sort_index(ascending=True).values
embarked_not_s=data_train[data_train.Survived==0].Embarked.value_counts().sort_index(ascending=True).values
plt.bar(embarked_x,embarked_s,color='dodgerblue')
plt.bar(embarked_x,embarked_not_s,bottom=embarked_s,color='tomato')
for i in range(len(embarked_x)):
    plt.text(embarked_x[i],embarked_s[i]/2-15,str(round(embarked_s[i]/(embarked_s[i]+embarked_not_s[i])*100,2))+'%',
             ha='center',va='bottom')
    plt.text(embarked_x[i],embarked_s[i]+embarked_not_s[i]/2-15,
             str(round(embarked_not_s[i]/(embarked_s[i]+embarked_not_s[i])*100,2))+'%',ha='center',va='bottom')
plt.title(u"embarked")
plt.ylabel(u"number")
plt.legend((u'Survived',u'Not Survived'),loc='best')

plt.subplot2grid((3,3),(2,0))
data_train.Fare[data_train.Pclass==1].plot(kind='kde')
data_train.Fare[data_train.Pclass==2].plot(kind='kde')
data_train.Fare[data_train.Pclass==3].plot(kind='kde')
plt.xlabel(u"fare")
plt.ylabel(u"distribution")
plt.xlim(0,120)
plt.title(u"fare distribution")
plt.legend((u'1st', u'2nd',u'3rd'),loc='best')

plt.subplot2grid((3,3),(2,1))
cabin_x=['Yes','No']
cabin_s=data_train[data_train.Survived==1].Cabin.isna().value_counts(sort=False).values
cabin_not_s=data_train[data_train.Survived==0].Cabin.isna().value_counts(sort=False).values
plt.bar(cabin_x,cabin_s,color='dodgerblue')
plt.bar(cabin_x,cabin_not_s,bottom=cabin_s,color='tomato')
for i in range(len(cabin_x)):
    plt.text(cabin_x[i],cabin_s[i]/2-15,str(round(cabin_s[i]/(cabin_s[i]+cabin_not_s[i])*100,2))+'%',
             ha='center',va='bottom')
    plt.text(cabin_x[i],cabin_s[i]+cabin_not_s[i]/2-15,
             str(round(cabin_not_s[i]/(cabin_s[i]+cabin_not_s[i])*100,2))+'%',ha='center',va='bottom')
plt.xlabel(u"with cabin num or not")
plt.ylabel(u"num")
plt.title(u"cabin num")
plt.legend((u'Survived', u'Not Survived'),loc='best')


plt.figure(num='detailed data')
plt.subplot2grid((2,3),(0,0))
family_size_bin=[0,1,4,20]
family_size_binlabel=['Single','Small','Large']
data_train['family']=data_train.SibSp+data_train.Parch+1
family_size_s=pd.cut(data_train[data_train.Survived==1].family,
                     family_size_bin,labels=family_size_binlabel).value_counts(sort=False).values
family_size_not_s=pd.cut(data_train[data_train.Survived==0].family,
                     family_size_bin,labels=family_size_binlabel).value_counts(sort=False).values
plt.bar(family_size_binlabel,family_size_s,color='dodgerblue')
plt.bar(family_size_binlabel,family_size_not_s,bottom=family_size_s,color='tomato')
for i in range(len(family_size_binlabel)):
    plt.text(family_size_binlabel[i],family_size_s[i]/2-15,str(round(family_size_s[i]/(family_size_s[i]+family_size_not_s[i])*100,2))+'%',
             ha='center',va='bottom')
    plt.text(family_size_binlabel[i],family_size_s[i]+family_size_not_s[i]/2-15,
             str(round(family_size_not_s[i]/(family_size_s[i]+family_size_not_s[i])*100,2))+'%',ha='center',va='bottom')
plt.xlabel(u"family size")
plt.ylabel(u"num")
plt.title(u"Family size")
plt.legend((u'Survived', u'Not Survived'),loc='best')

plt.subplot2grid((2,3),(0,1))
fare_bins=[-1,10,50,100,600]
fare_binlabel=['0_10','11_50','51_100','100+']
fare_s=pd.cut(data_train[data_train.Survived==1].Fare,fare_bins,labels=fare_binlabel).value_counts(sort=False).values
fare_not_s=pd.cut(data_train[data_train.Survived==0].Fare,fare_bins,labels=fare_binlabel).value_counts(sort=False).values
plt.bar(fare_binlabel,fare_s,color='dodgerblue')
plt.bar(fare_binlabel,fare_not_s,bottom=fare_s,color='tomato')
plt.text(fare_binlabel[2],250,'Death rate')
for i in range(len(fare_binlabel)):
    plt.text(fare_binlabel[i],fare_s[i]+fare_not_s[i]/2-15,
             str(round(fare_not_s[i]/(fare_s[i]+fare_not_s[i])*100,2))+'%',ha='center',va='bottom')
plt.ylabel(u"number")
plt.title(u"fare bucket distribution")
plt.legend((u'Survived',u'Not Survived'),loc='best')

plt.subplot2grid((2,3),(0,2))
data_train['Title'] = data_train['Name'].map(lambda x: re.compile(", (.*?)\.").findall(x)[0])
title_Dict = {}
title_Dict.update(dict.fromkeys(['Capt', 'Col', 'Major', 'Dr', 'Rev'], 'Officer'))
title_Dict.update(dict.fromkeys(['Don', 'Sir', 'the Countess', 'Dona', 'Lady'], 'Royalty'))
title_Dict.update(dict.fromkeys(['Mme', 'Ms', 'Mrs'], 'Mrs'))
title_Dict.update(dict.fromkeys(['Mlle', 'Miss'], 'Miss'))
title_Dict.update(dict.fromkeys(['Mr'], 'Mr'))
title_Dict.update(dict.fromkeys(['Master', 'Jonkheer'], 'Master'))
data_train['Title'] = data_train['Title'].map(title_Dict)
title_x=data_train[data_train.Survived==1].Title.value_counts(sort=False).index.values
title_s=data_train[data_train.Survived==1].Title.value_counts(sort=False).values
title_not_s=data_train[data_train.Survived==0].Title.value_counts(sort=False).values
plt.bar(title_x,title_s,color='dodgerblue')
plt.bar(title_x,title_not_s,bottom=title_s,color='tomato')
plt.text(title_x[2],350,'Death rate')
for i in range(len(title_x)):
    plt.text(title_x[i],title_s[i]+title_not_s[i]/2-15,
             str(round(title_not_s[i]/(title_s[i]+title_not_s[i])*100,2))+'%',ha='center',va='bottom')
plt.xlabel('title')
plt.ylabel('num')
plt.title('title distribution')
plt.legend((u'Survived',u'Not survived'),loc='best')

plt.subplot2grid((2,3),(1,0))
data_train.loc[(data_train['Cabin'].isna()),'Cabin']='0'
data_train['Cabin']=data_train['Cabin'].map(lambda x: x.split()[-1])
data_train['Cabin_class']=data_train['Cabin'].map(lambda x: re.compile("[A-Z]").findall(x))
data_train['Cabin_class']=data_train['Cabin_class'].map(lambda x:str(x)[2:-2])
cabin_class_x=data_train['Cabin_class'].value_counts().sort_index(ascending=True).index.drop(['']).values
cabin_class_not_s=data_train[data_train.Survived==0].Cabin_class.value_counts().sort_index(ascending=True).drop(['']).values
cabin_class_s=data_train.Cabin_class.value_counts().sort_index(ascending=True).drop(['']).values-cabin_class_not_s
plt.bar(cabin_class_x,cabin_class_s,color='dodgerblue')
plt.bar(cabin_class_x,cabin_class_not_s,bottom=cabin_class_s,color='tomato')
plt.text(cabin_class_x[3],40,'Death rate')
for i in range(len(cabin_class_x)):
    plt.text(cabin_class_x[i],cabin_class_s[i]+cabin_class_not_s[i]/2,
             str(round(cabin_class_not_s[i]/(cabin_class_s[i]+cabin_class_not_s[i])*100,2))+'%',ha='center',va='bottom')
plt.title('Cabin class distribution')
plt.xlabel('Cabin class')
plt.ylabel('num')
plt.legend((u'Survived',u'Not Survived'),loc='best')

plt.show()