class LabelData:
	def __init__(self,PredictList):
		self.currList=PredictList
		self.labelDict()
	def labelDict(self):
		self.dtime = {'not urgent': 1, 'urgent': 2, 'very urgent': 3}
		self.dmotivation = {'Affective': 4, 'cognitive': 1, 'self-assistive': 3, 'social': 3}
		self.dintent = {'fact finding': 1, 'information gathering': 2, 'undirected browsing': 5, 'transaction': 4,'communication(social)': 3, 'info maintenance or update': 6}
		self.dcomplexity = {'single goal': 1, 'multiple goals': 2, 'undirected(no goal)': 3}
		self.dwork = {'Work': 1, 'fun': 2}
		self.dcontinue = {'likely': 1, 'unlikely': 0}
	def labelList(self):
		self.currList[0] = self.dintent[self.currList[0]]
		self.currList[1] = self.dmotivation[self.currList[1]]
		self.currList[2] = self.dcomplexity[self.currList[2]]
		self.currList[3] = self.dwork[self.currList[3]]
		self.currList[4] = self.dtime[self.currList[4]]
		return self.currList