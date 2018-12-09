#!C:/Users/kundan.KUNDAN/AppData/Local/Programs/Python/Python36/python
import mysql.connector
import pandas as pd
from sklearn.linear_model import LogisticRegression
class TrainData:
    def __init__(self,conn):
        self.conn=conn#mysql.connector.connect(host='localhost', database='annotation', user='root', password='')
    def trainData(self):
        self.df=pd.read_sql('select intent_type,motivation,complexity,work_fun,continue_not,time_sensitivity from parameters',self.conn)
        self.label()
        self.df.time_sensitivity = [self.dtime[item] for item in self.df.time_sensitivity]
        self.df.intent_type = [self.dintent[item] for item in self.df.intent_type]
        self.df.motivation = [self.dmotivation[item] for item in self.df.motivation]
        self.df.complexity = [self.dcomplexity[item] for item in self.df.complexity]
        self.df.work_fun = [self.dwork[item] for item in self.df.work_fun]
        self.df.continue_not = [self.dcontinue[item] for item in self.df.continue_not]
        self.df.columns = ['intent', 'motivation', 'com', 'w', 'c', 't']
        y = self.df.c
        X = self.df.drop('c', axis=1)
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        clf = LogisticRegression(solver='lbfgs', random_state=1)
        clf.fit(X, y)
        return  clf

    def label(self):
        self.dtime = {'not urgent': 1, 'urgent': 2, 'very urgent': 3}
        self.dmotivation = {'Affective': 4, 'cognitive': 1, 'self-assistive': 3, 'social': 3}
        self.dintent = {'fact finding': 1, 'information gathering': 2, 'undirected browsing': 5, 'transaction': 4,'communication(social)': 3, 'info maintenance or update': 6}
        self.dcomplexity = {'single goal': 1, 'multiple goals': 2, 'undirected(no goal)': 3}
        self.dwork = {'Work': 1, 'fun': 2}
        self.dcontinue = {'likely': 1, 'unlikely': 0}