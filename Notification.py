class Notification(object):
	"""docstring for Notification"""
	def __init__(self, idNotificationP, dateNotificationP, stateValidateP, categoryResourceP):
		super(Notification, self).__init__()
		self.idNotification = idNotificationP
		self.dateNotification = dateNotificationP
		self.stateValidate = stateValidateP
		self.categoryResource = categoryResourceP

	def changeStateNotification(self, change):
		self.stateValidate = change

	def getDateNotification(self):
		return self.dateNotification

	def getStateNotification(self):
		return self.stateValidate

	def getIdNotification(self):
		return self.idNotification

	def getCategoryResource(self):
		return self.categoryResource

		
		