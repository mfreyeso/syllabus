import os, string, sys, sqlite3 as lite
import os
from bottle import route, run, debug, template, request, static_file, error, get, post
import Repository
from bottle import default_app

objectRepository = Repository.Repository()
#Connect to Database
con = lite.connect('databaseapp.sqlite')
cur = con.cursor()

#Loading the users
if objectRepository.loadUsers(cur):
	print "The users was found succsefully"

else:
	print "Error in loading the users"


@route('/validateUser', method='GET')
def validateUser():
	if request.GET.get('login', '').strip():
		usernameText = request.GET.get('usernameText', '').strip()
		passwordText = request.GET.get('passwordText', '').strip()
		userDefault = objectRepository.validateUserLogin(usernameText, passwordText)
		if userDefault != None:
			objectRepository.loadUserActive(userDefault)
			if objectRepository.getUserActive().getTypeUser() == 1:
				return template('menu.tpl')
			else:
				return template('menuS.tpl')
		else:
			return template('errorLogin.tpl')

@route('/newUser', method='POST')
def createNewUser():
	identification = request.forms.identification
	firstname = request.forms.firstname
	lastname = request.forms.lastname
	email = request.forms.email
	username = request.forms.username
	password = request.forms.password
	typeUser = request.forms.typeuser
	userDefault = objectRepository.createNewUser(identification, firstname, lastname, email, username, password, typeUser, cur)
	if userDefault != None:
		con.commit()
		objectRepository.loadUserActive(userDefault)
		if objectRepository.getUserActive().getTypeUser() == 1:
			return template('menu.tpl')
		else:
			return template('menu.tpl')
	else:
		return template('errorLogin.tpl')



@route('/insertResourceB', method='POST')
def createNewResource():
	nameResource = request.forms.nameResource
	dateResource = request.forms.dateResource
	categoryResource = request.forms.categorytype
	dataResource = request.files.get('dataResource')
	pathOne = os.getcwd()
	pathTwo='resources'
	pathFinal = os.path.join(pathOne, pathTwo)
	dataResource.save(pathFinal)
	pathDataBase = os.path.join(pathFinal, dataResource.filename)
	resourceCreated = objectRepository.getUserActive().createResource(nameResource, dateResource, categoryResource, pathDataBase)
	if resourceCreated != None:
		if objectRepository.getUserActive().getTypeUser() < 1:
			statePublication = 0
			if objectRepository.getUserActive().shareResource(resourceCreated, cur, 0):
				con.commit()
				idLastResource = cur.lastrowid
				resourceCreated.setIdResource(idLastResource)
				if resourceCreated.createNotification(dateResource, 0, categoryResource):
					notificationCreated = resourceCreated.getNotification()
					if resourceCreated.insertNotification(notificationCreated, cur):
						con.commit()
						print "El recurso fue creado satisfactoriamente"
						return template('notification.tpl')
					else:
						print "No se ingreso en la Base de Datos la Notification"
						return template('error.tpl')
				else:
					print "No se creo el objeto notification"
					return template('error.tpl')
			else:
				"El recurso fue creado y validado con exito"
				return template('error.tpl')
		else:
			print "El recurso no pudo ser compartido en el sistema"
			return template('error.tpl')
	else:
		print "El objeto recurso no pudo ser creado"
		return template('error.tpl')


@route('/insertResource', method='GET')
def formNewResource():
	return template('newResource.tpl')

@route('/viewResources', method='GET')
def viewResources():
	return template('searchResource.tpl')

@route('/searchResources', method='POST')
def searchResources():
	categoryResourceS = request.forms.get('categoryType')
	setResult = objectRepository.getUserActive().searchResource(cur, categoryResourceS)
	if setResult != None:
		categorySearch = objectRepository.getCategoryResources()[0]
		return template('tableResources.tpl', setFound=setResult, category=categorySearch)
	else:
		print "No hay nada"
		return template('error.tpl')

@route('/validateResources', method='GET')
def viewValidateResources():
	return template('selViewResources.tpl')

@route('/validateResourcesF', method='POST')
def viewValidateResources():
	categoryResourceV = request.forms.get('categoryResource')
	print categoryResourceV
	if objectRepository.getUserActive().getTypeUser() == 1:
		resourceObjectsV = objectRepository.getUserActive().validateResources(categoryResourceV, cur)
		if resourceObjectsV != None:
			return template('viewResourcesVal.tpl', setFound=resourceObjectsV)
		else:
			print "No entre al template"
			return template('error.tpl')

@route('/menu')
def signUpUser():
	return template('menu.tpl')

@route('/notification')
def signUpUser():
	return template('notification.tpl')

@route('/error')
def signUpUser():
	return template('error.tpl')

@route('/pruebacss')
def pruebacss():
	return template('template.tpl')

@route('/')
def index():
	return template('index.tpl')

@route('/static/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/changeState/<identificacionResource>')
def changeStateResource(identificacionResource):
	idResourceP = identificacionResource
	cur.execute("UPDATE resource SET statePublication=1 WHERE idResource=?", idResourceP)
	con.commit()
	return template('menu.tpl')

@route('/resourcesV/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./resources/')

@route('/resources/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./resources/', download=True)

run(host='localhost', port=8080)


