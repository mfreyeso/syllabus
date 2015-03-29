import Notification


class Resource:
	"""docstring for ClassName"""
	def __init__(self, nameResourceP, dateResourceP, categoryResourceP, pathFileDataBaseP):
		self.nameResource = nameResourceP
		self.dateResource = dateResourceP
		self.categoryResource = categoryResourceP
		self.pathFileDataBase = pathFileDataBaseP

	def setIdResource(self, idResourceP):
		self.idResource = idResourceP

	def getIdResource(self):
		return self.idResource

	def getNameResource(self):
		return self.nameResource

	def getDateResource(self):
		return self.dateResource

	def getCategoryResource(self):
		return self.categoryResource

	def getPathFileDataBase(self):
		return self.pathFileDataBase

	def getNotification(self):
		return self.notification

	def createNotification(self, dateResourceP, stateValidateP, categoryResourceP):
		response = False
		numNotification = self.getIdResource()
		objectNotification = Notification.Notification(numNotification, dateResourceP, stateValidateP, categoryResourceP)
		self.notification = objectNotification
		response = True
		return response

	def insertNotification(self, notificationObjectP, curConnect):
		response = False
		notificationObject = notificationObjectP
		idNotificationC = notificationObject.getIdNotification()
		dateNotificationC = notificationObject.getDateNotification()
		stateNotificationC = notificationObject.getStateNotification()
		categoryResourceC = notificationObject.getCategoryResource()
		curConnect.execute("INSERT INTO notification VALUES(?, ?, ?, ?)", (idNotificationC, categoryResourceC, stateNotificationC, dateNotificationC))
		response = True
		return response