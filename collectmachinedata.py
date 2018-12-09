#!C:/Users/kundan.KUNDAN/AppData/Local/Programs/Python/Python36/python
from traindata import TrainData
class MachineData:

    def __init__(self,conn):
        train = TrainData(conn)
        self.clf = train.trainData()

    def collectData(self,predictList):
        self.testList=predictList
        # print(df)
        #print(df.shape)
        # print(df.describe())
        # df.hist()
        # plt.show()
        # scatter_matrix(df)
        # plt.show()
        # x=df[:,:-1]
        # y=df[:,len(df[0])-1]
        # print(df.head())
        #print(df.describe())
        out=self.predictData()
        return out
        #print(y_train)
        #print(clf.score(X_train, y_train))
        #print("$%^&*")
    def predictData(self):
        out=self.clf.predict(self.testList)
        return out[0]

