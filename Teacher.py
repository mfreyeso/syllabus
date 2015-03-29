class Teacher(User):

	def loadNotifications(self, arrayNotifications):
		self.notifications=arrayNotifications

	def getNotifications(self):
		return self.notifications
	
		