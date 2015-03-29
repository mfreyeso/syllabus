import Resource
import User

class Repository(object):
	
	def __init__(self):
		super(Repository, self).__init__()
		self.vectorUsers = []
		self.vectorResources =[]
		self.vectorNotifications = []
		self.categoryResource = ["Socials", "Technology", "Science", "Managment"]

	def loadUserActive(self, userObjectActiveP):
		self.userObjectActive = userObjectActiveP

	def getUserActive(self):
		return self.userObjectActive

	def getUsers(self):
		return self.vectorUsers

	def getResources(self):
		return self.vectorResources

	def getCategoryResources(self):
		return self.categoryResource


	def loadUsers(self, curConnect):
		curConnect.execute("SELECT * FROM user")
		usersLoad = curConnect.fetchall()
		if usersLoad != None:
			for singleUser in usersLoad:
				identificationP = singleUser[0]
				firstNameP = singleUser[1]
				lastNameP = singleUser[2]
				emailP = singleUser[3]
				usernameP = singleUser[4]
				passwordP = singleUser[5]
				typeUserP = singleUser[6]				
				userObject = User.User(identificationP, firstNameP, lastNameP, emailP, usernameP, passwordP, typeUserP)
				self.getUsers().append(userObject)
			return True
		else:
			return False

	def loadResources(self, curConnect, categoryResource):
		curConnect.execute("SELECT * FROM resource WHERE idCategory='"+str(categoryResource)+"' AND statePublication='1'")
		if curConnect.fetchall() != None:

			resourcesLoad = curConnect.fetchall()
			for singleResource in resourcesLoad:
				resourceObject = Resource.Resource(singleResource[0], singleResource[1], singleResource[2], singleResource[3], singleResource[4], singleResource[5])
				getResources().append(resourceObject)

			return True
		else:
			return False

	def validateUserLogin(self, usernameIn, passwordIn):
		response = False
		usersDb =self.getUsers()
		for searchUser in usersDb:
			if searchUser.getUsername() == usernameIn and searchUser.getPassword() == passwordIn :
				response = searchUser
				break
		return response

	def createNewUser(self, identificationP, firstNameP, lastNameP, emailP, usernameP, passwordP, typeUserP, curConnect):
		response = None
		userObjectNew = User.User(identificationP, firstNameP, lastNameP, emailP, usernameP, passwordP, typeUserP)
		print userObjectNew.getUsername()
		curConnect.execute("SELECT * FROM user WHERE identification=? or username=?", (identificationP, usernameP))
		row = curConnect.fetchone()
		if row != None:
			response = False
		else:
			curConnect.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?, ?, ?)", (identificationP, firstNameP, lastNameP, emailP, usernameP, passwordP, typeUserP))
			response = userObjectNew
		return response

		