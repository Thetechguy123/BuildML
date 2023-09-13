from tkinter import*
import tkinter as tk 
from tkinter.filedialog import askdirectory,askopenfilename
import tkinter.font as TkFont
from ModelDict import Model_Dict
import pandas as pd
root=Tk()

#root.iconbitmap('Construct\Icon.ico')
#root.geometry("700x700")
s1=Frame(root)
s2=Frame(root)
s3=Frame(root)
s4=Frame(root)
s6=Frame(root)
for frame in (s1, s2,s3,s4,s6):
    frame.grid(row=0, column=0,sticky='news')
acspace="                                                                                                                                          "
nspace=acspace+"                                                                                 "
def raise_frame(frame):
    frame.tkraise()
db=pd.DataFrame()
Headings=StringVar()
Headings.set('a')
def s1_s2():
    global db
    db=pd.read_csv(fs)
    print(db.columns)
    Headings.set(str(list(db.columns)))
    print(Headings.get())
    raise_frame(s2)



fs=None
def dbAccess():
    global fs
    fs=askopenfilename()
#    dBlabel=Label(s1,text=fs,bg='white').grid(row=2,column=0)
    dBlabel=Label(s1,text=fs,bg='white').grid(row=2,column=0)
    DBD.set(True)
dir=None
def dirAccess():
    global dir
    dir=askdirectory()
    Label(s1,text=dir,bg='white').grid(row=6,column=0)
    print(DBD.get())
    if DBD.get()==True:
        BTN_S1_S2=Button(s1,text='Next',command=s1_s2).grid(row=31,column=1)
DBD=BooleanVar(root,False)
uploadLabel=Label(s1,text='Upload dataset Here').grid(row=1,column=0)
dBlabel=Label(s1,text=acspace,bg='white').grid(row=2,column=0)    
DBbtn=Button(s1,text="+",command=dbAccess).grid(row=2,column=1)
Label(s1,text="                           ").grid(row=3)
Label(s1,text="                           ").grid(row=4)
Label(s1,text="                           ").grid(row=5)
Label(s1,text="                           ").grid(row=0)

DirLabel=Label(s1,text="Select Directory to store model ").grid(row=5)
Label(s1,text=acspace,bg='white').grid(row=6,column=0)
DIRbtn=Button(s1,text='...',command=dirAccess).grid(row=6,column=1)
for i in range(25):
    Label(s1,text=acspace).grid(row=6+i)
last_label=Label(s1,text=nspace).grid(row=31,column=0)    


#############################################Screen 2


font=TkFont.Font(family="Helvetica",size=36,weight="bold")
font2=TkFont.Font(family="Cooper Std Black",size=18)
Label(s2,text="Type of task ",font=font).grid(row=0, column=0)
Label(s2,text="").grid(row=1)
clf=None
def s2_s3():
    
    global clf
    clf=Model_Dict[model.get()]
    print(clf)
    print(Headings.get())
    raise_frame(s3)
    title_Heading=Headings.get().split(',')
    title_Heading[0]=title_Heading[0][1:]
    title_Heading[-1]=title_Heading[-1][:-1]
    for i in range(len(title_Heading)):
        title_Heading[i]=title_Heading[i][2:-1]
        
    print("AAAHF",title_Heading)
    Features=OptionMenu(s3,FeatureItem,*list(title_Heading)).grid(row=5,column=0)
    Labels=OptionMenu(s3,LabelTitle,*list(title_Heading)).grid(row=10,column=0)
    
def expand():
    print(choose.get())
    if choose.get()=="Regression":
        model.set("Linear Regression")
        OptionMenu(s2,model,"Elastic Net Regression",
        
            "Support Vector Machine(SVR)",
            "Bayesian Ridge Regression",
            "CatBoost Regressor",
            "Kernel Ridge Regression",
            "Linear Regression",
            "GradientBoosting Regressor",
            ).grid(row=3)
    else:
        model.set("Decision Tree")
        OptionMenu(s2,model,"Logistic Regression",
"Support Vector Machine",

"Naive Bayes Multinomial",
"Stochastic Gradient Descent Classifier",

"Decision Tree",
"Random Forest",
"Gradient Boosting Classifier",
).grid(row=3)
    
    btnS2_S3=Button(s2,text="Next",command=s2_s3).grid(row=30,column=1)


    



choose=StringVar()
model=StringVar()
choose.set("Classification")
OptionMenu(s2,choose,"Regression","classification").grid(row=2,column=0)

Button(s2,text="Next",command=expand,font=font2).grid(row=2,column=1)
for i in range(28):
    Label(s2,text='').grid(row=2+i)
S2NLabel=Label(s2,text=nspace).grid(row=30,column=0)    


################################Screen 3

Subfont=TkFont.Font(family="Cooper Std Black",size=30)
FeatureLabel=Label(s3,text="About the data",font=font).grid(row=0)
Label(s3,text="").grid(row=1)
Label(s3,text="").grid(row=2)
from Learning import learn 
Fmodel=None
Enc=None
def S3_S4():
    global Fmodel
    global Enc
    print(clf)
    x=db[FeatureList].values
    labels=db[LabelTitle.get()].values
    print(x)
    print()
    print(labels)
    print(clf)
    Fmodel,Enc=learn(x, labels,clf)
    raise_frame(s4)


def addF():
    global FeatureCount
    global FeatureList
    Label(s3,text=FeatureItem.get()).grid(row=6,column=FeatureCount)
    FeatureCount+=1
    FeatureList.append(FeatureItem.get())    
    AddedF.set(True)
    print(FeatureList)
def addL():
    Label(s3,text=LabelTitle.get()).grid(row=11)

    if AddedF.get()==True:
        Label(s3,text=nspace).grid(row=27,column=0)
        Btn_S3_S4=Button(s3,text='Next',command=S3_S4).grid(row=27,column=1)
    print(LabelTitle.get())

Label(s3,text="Features",font=Subfont).grid(row=3)
Label(s3,text="").grid(row=4)
FeatureList=[]
FeatureItem=StringVar()
FeatureCount=0
AddedF=BooleanVar()
AddedF.set(False)
Val_Heading=Headings
Title_Heading=list(Headings.get())
#Features=OptionMenu(s3,FeatureItem,*Title_Heading).grid(row=5,column=0)
AddBtn=Button(s3,text="+",command=addF).grid(row=5,column=1)
Label(s3,text='').grid(row=7)
Label(s3,text='Label',font=Subfont).grid(row=8)
Label(s3,text='').grid(row=9)
LabelTitle=StringVar()

#Labels=OptionMenu(s3,LabelTitle,Headings.get()).grid(row=10,column=0)
Button_add_Label=Button(s3,text='+',command=addL).grid(row=10,column=1)
for i in range(16):
    Label(s3,text='').grid(row=10+i)



################################Screen 4
import pickle 
import joblib
import os
#from pilot import code_str

'''
def FinishModel(Name):
       # ModelPath=os.path.join(dir,Name+'.sav')
        #EncPath=os.path.join(dir,Name+'_Enc.joblib')
        ModelPath=os.path.join(dir,'A.sav')
        EncPath=os.path.join(dir,'E.joblib')
        pickle.dump(clf,open(ModelPath,'wb'))
        joblib.dump(Enc,open(EncPath,'wb'))

'''
def Appear():
    S4_S5=Button(s4,text='Next',command=FinishModel).grid(row=30)

Label(s4).grid(row=0)
Label(s4,font=font,text="Name of your Model").grid(row=1)
Label(s4).grid(row=2)
Label(s4).grid(row=3)
def FinishModel():

        ModelPath=os.path.join(dir,Name.get()+'.sav')
        EncPath=os.path.join(dir,Name.get()+'_Enc.joblib')
        PilotPath=os.path.join(dir,Name.get()+'_Pilot.py')
        pickle.dump(clf,open(ModelPath,'wb'))
        joblib.dump(Enc,open(EncPath,'wb'))
        code=['import numpy as np']
        code.append('import pickle')
        code.append('import joblib')
        #code.append('fp='+str(dir))
        code.append('enc_fp='+"'"+Name.get()+"_Enc.joblib'")
        code.append("clf=pickle.load(open(%s,'rb'))"%("'"+Name.get()+".sav'"))
        code.append("enc=joblib.load(open(enc_fp,'rb'))")
        code.append('#THIS FUNCTION CAN BE IMPORTED INTO ANY OTHER PROGRAM AND BE USED TO RETURNING THE ORIGINAL LABELS FROM DATASET')
        code.append('def predict(x):      #x should be a list')
        code.append('   pred=clf.predict(np.array([x])) ')
        code.append('   val=enc.inverse_transform(pred)')
        code.append('   return val')
        code_str=''
        for x in code:
            code_str+=x+'\n'
        with open(PilotPath,'w') as f:
            f.write(code_str)
        raise_frame(s6)

Name=StringVar()
Entry(s4,textvariable=Name,width=50,borderwidth=10).grid(row=4,ipady=3,column=0)
ConfButton=Button(s4,text='Yes',command=Appear).grid(row=4,column=1)
for i in range(24):
    Label(s4,text='').grid(row=i+5)

################################Screen 5


Label(s6,text="Your Machine Learning Model Has been constructed",font=font).grid(row=1)
Label(s6,text="Has been constructed",font=font).grid(row=2,column=0)
Label(s6,text="and is available at the selected directory",font=font).grid(row=3,column=0)
Label(s6).grid(row=4)
Label(s6,text="Thank you for using MLBuild",font=Subfont).grid(row=5,column=0)
Label(s6,text="And hope u have a good day",font=Subfont).grid(row=6,column=0)

s1.tkraise()
root.mainloop()