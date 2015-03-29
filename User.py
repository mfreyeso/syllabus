import Resource
import random
import os, string, sys, sqlite3 as lite

class User:

	def __init__(self, identificationP, firstNameP, lastNameP, emailP, usernameP, passwordP, typeUserP):
		self.identification=identificationP
		self.firstName = firstNameP
		self.lastName = lastNameP
		self.email = emailP
		self.username = usernameP
		self.password = passwordP
		self.typeUser = typeUserP
		self.setResources=[]
		
	def getIdentification(self):
		return self.identification

	def getLastName(self):
		return self.lastName

	def getFirstName(self):
		return self.firstName
	
	def getEmail(self):
		return self.email

	def getUsername(self):
		return self.username

	def getPassword(self):
		return self.password

	def getTypeUser(self):
		return self.typeUser

	def getSetResources(self):
		return self.setResources

	def createResource(self, nameResourceP, dateResourceP, categoryResourceP, pathFileP):
		newResource = Resource.Resource(nameResourceP, dateResourceP, categoryResourceP, pathFileP)
		return newResource

	def shareResource(self, objectResourceP, curConnect, statePublicationP):
		response = False
		nameResourceC = objectResourceP.getNameResource()
		dateResourceC = objectResourceP.getDateResource()
		categoryResourceC = objectResourceP.getCategoryResource()
		pathFileC = objectResourceP.getPathFileDataBase()
		identificationUser = self.getIdentification()
		statePublicationC = statePublicationP
		curConnect.execute("INSERT INTO resource('nameResource', 'idCategory', 'datePublication', 'idUser', 'statePublication', 'pathFile') VALUES(?, ?, ?, ?, ?, ?);", (nameResourceC, categoryResourceC, dateResourceC, identificationUser, statePublicationC, pathFileC))
		response=True
		return response

	def searchResource(self, curConnect, categoryResourceP):
		categoryResourceC = categoryResourceP
		curConnect.execute("SELECT * FROM resource WHERE idCategory=? AND statePublication=?", (categoryResourceC, 1))
		resourceCollection = curConnect.fetchall()
		arrayObjectsF = self.formatSearch(resourceCollection)
		return arrayObjectsF

	def formatSearch(self, collectionP):
		arrayObjects =[]
		for resource in collectionP:
			resourceObject = Resource.Resource(resource[1], resource[3], resource[2], resource[6])
			resourceObject.setIdResource(resource[0])
			arrayObjects.append(resourceObject)
		return arrayObjects
	
	def validateResources(self, categoryResourceV, curConnect):
		categoryValidate = categoryResourceV
		curConnect.execute("SELECT * FROM resource WHERE idCategory=? AND statePublication=?", (categoryResourceV, 0))
		result = curConnect.fetchall()
		arrayObjectsF = self.formatSearch(result)
		return arrayObjectsF


			