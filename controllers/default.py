import re
# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():  
    form=auth.login()
    return dict(form=form)


def error():
    return dict()
#auth.add_membership(auth.id_group('Proponentes'))
@auth.requires_login()
def vista_admin():    
    msj= 'Bienvenido %s %s' % (auth.user.first_name,auth.user.last_name)
    if auth.has_membership('Proponentes'):
    	
    	redirect(URL('proponentes'))

    if auth.has_membership('Estudiantes'):
    	redirect(URL('estudiantes'))
    
    form=auth.profile()
    return dict(msj=msj, form=form)
  
'''

'''
def estudiantes():
    def my_form_processing(form):
        if not re.match('\d{2}-\d{5}$', form.vars.f_usbid):
            form.errors.f_usbid = 'El formato válido de carnet es: 00-00000'
        if not re.match('[1-9][0-9]{0,8}$', form.vars.f_cedula):
            form.errors.f_cedula = 'El formato válido de cédula es: 1232382'
        if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', form.vars.f_email):
            form.errors.f_email = 'El formato válido de email es example@example.com'
        if not re.match('\d{7,13}', form.vars.f_telefono):
            form.errors.f_telefono = 'El formato válido de telefono es 08002023223'

    form = SQLFORM(db.t_estudiante,
    	fields = ['f_usbid','f_cedula', 'f_carrera', 'f_sede', 'f_sexo', 'f_telefono', 'f_direccion'])

    user = db.auth_user[auth.user.id]
    form.vars.f_user = user
    form.vars.f_email = auth.user.email
    form.vars.f_nombre = auth.user.first_name
    form.vars.f_apellido = auth.user.last_name
    if request.env.request_method =='POST':
	    if form.process(onvalidation=my_form_processing).accepted:
	        response.flash = 'form accepted'
	        return dict(est=db().select(db.t_estudiante.ALL))
	    elif form.errors:
	        response.flash = 'form has errors'
	    else:
	        response.flash = 'please fill out the form'
    return dict(form=form, est=db().select(db.t_estudiante.ALL))

def proponentes():
    def my_form_processing(form):
        if not re.match('[1-9][0-9]{0,8}$', form.vars.f_cedula):
            form.errors.f_cedula = 'El formato válido de cédula es: 1232382'
        if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', form.vars.f_email):
            form.errors.f_email = 'El formato válido de email es example@example.com'
        if not re.match('\d{7,13}', form.vars.f_telefono):
            form.errors.f_telefono = 'El formato válido de telefono es 08002023223'

    form = SQLFORM(db.t_proponente)
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, proponentes=db().select(db.t_proponente.ALL))

def proponenteDetalles():
    def my_form_processing(form):
        if not re.match('[1-9][0-9]{0,8}$', form.vars.f_cedula):
            form.errors.f_cedula = 'El formato válido de cédula es: 1232382'
        if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', form.vars.f_email):
            form.errors.f_email = 'El formato válido de email es example@example.com'
        if not re.match('\d{7,13}', form.vars.f_telefono):
            form.errors.f_telefono = 'El formato válido de telefono es 08002023223'

    form = SQLFORM(db.t_proponente)
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, proponentes=db().select(db.t_proponente.ALL))


def tutores():
    def my_form_processing(form):
        if form.vars.f_usbid:
            if not re.match('\d{2}-\d{5}$', form.vars.f_usbid) and not re.match('[a-zA-Z0-9_.+-]+', form.vars.f_usbid):
                form.errors.f_usbid = 'usbid invalido'
        if not re.match('[1-9][0-9]{0,8}$', form.vars.f_cedula):
            form.errors.f_cedula = 'El formato válido de cédula es: 1232382'
        if not re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', form.vars.f_email):
            form.errors.f_email = 'El formato válido de email es example@example.com'
        if not re.match('\d{7,13}', form.vars.f_telefono):
            form.errors.f_telefono = 'El formato válido de telefono es 08002023223'
    form = SQLFORM(db.t_tutor)
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, tutores=db().select(db.t_tutor.ALL))


@auth.requires_login()
def estado_manage():
    form = SQLFORM.smartgrid(db.t_estado,onupdate=auth.archive)
    return dict(form=form)

#@auth.requires_login()

def sedes():
    def my_form_processing(form):
        if not re.match('[A-ZÁÉÍÓÚÑ]|[A-ZÁÉÍÓÚÑa]|[a-zñáéíóúäëïöü]*$', form.vars.f_nombre):
            form.errors.f_nombre = 'Sólo puede contener letras'
    form = SQLFORM(db.t_sede)
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'    
    return dict(form=form, sedes=db().select(db.t_sede.ALL))

def areas():
    def my_form_processing(form):
        if not re.match('[A-ZÁÉÍÓÚÑ]|[A-ZÁÉÍÓÚÑa]|[a-zñáéíóúäëïöü]*$', form.vars.f_nombre):
            form.errors.f_nombre = 'Sólo puede contener letras'
    form = SQLFORM(db.t_area,onupdate=auth.archive)
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, areas=db().select(db.t_area.ALL))


def proyectos():
    def my_form_processing(form):
        if not re.match('\d{4}', form.vars.f_codigo):
            form.errors.f_codigo = 'El formato válido del código son 4 dígitos'
        if not re.match('[A-ZÁÉÍÓÚÑ]|[A-ZÁÉÍÓÚÑa]|[a-zñáéíóúäëïöü]*$', form.vars.f_nombre):
            form.errors.f_nombre = 'Sólo puede contener letras'
        if not re.match('[A-ZÁÉÍÓÚÑ]|[A-ZÁÉÍÓÚÑa]|[a-zñáéíóúäëïöü]*$', form.vars.f_descripcion):
            form.errors.f_descripcion = 'Sólo puede contener letras'
        if not re.match('\d{2}', form.vars.f_version):
            form.errors.f_codigo = 'El formato válido de la versión son 2 dígitos'

    form = SQLFORM(db.t_project,onupdate=auth.archive) 
    if form.process(onvalidation=my_form_processing).accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form, proyectos=db().select(db.t_project.ALL))


def sede_manage():
    form = SQLFORM.smartgrid(db.t_sede,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def comunidad_manage():
    form = SQLFORM.smartgrid(db.t_comunidad,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def area_manage():
    form = SQLFORM.smartgrid(db.t_area,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def sexo_manage():
    form = SQLFORM.smartgrid(db.t_sexo,onupdate=auth.archive)
    return locals()

def estudiante_manage():
    form = SQLFORM.smartgrid(db.t_estudiante.id==request.args(0))
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return locals()

@auth.requires_login()
def proponente_manage():
    form = SQLFORM.smartgrid(db.t_proponente,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def tutor_manage():
    form = SQLFORM.smartgrid(db.t_tutor,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def proyecto_manage():
    form = SQLFORM.smartgrid(db.t_proyecto,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def condicion_manage():
    form = SQLFORM.smartgrid(db.t_condicion,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def caracterisicas_manage():
    form = SQLFORM.smartgrid(db.t_caracterisicas,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def cursa_manage():
    form = SQLFORM.smartgrid(db.t_cursa,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def carrera_manage():
    form = SQLFORM.smartgrid(db.t_carrera,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def tipoprop_manage():
    form = SQLFORM.smartgrid(db.t_tipoprop,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def relacionestproy_manage():
    form = SQLFORM.smartgrid(db.t_relacionestproy,onupdate=auth.archive)
    return locals()

def sedesDetalles():
    x = long (request.args[0])
    #return dict(rows = db(db.t_sede.id==x).select())
    record = db.t_sede(request.args[0])
    form = SQLFORM(db.t_sede, record, deletable = True)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    elif not record:
        return dict('La sede ha sido eliminada')
    return dict(form = form,rows = db(db.t_sede.id==x).select())

def estudiantesDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_estudiante.id==x).select())
    
def proponentesDetalles():
    x = long (request.args[0])
    #return dict(rows = db(db.t_sede.id==x).select())
    record = db.t_proponente(request.args[0])
    form = SQLFORM(db.t_proponente, record, deletable = True)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    elif not record:
        return dict('La sede ha sido eliminada')
    return dict(form = form, proyectos = db(db.t_project.f_proponente==record).select())


    
def proyectosDetalles():
    x = long (request.args[0])
    #return dict(rows = db(db.t_sede.id==x).select())
    record = db.t_project(request.args[0])
    form = SQLFORM(db.t_project, record, deletable = True)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    elif not record:
        return dict('La sede ha sido eliminada')
    return dict(form = form)
    
def tutoresDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_tutor.id==x).select())
    
def areasDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_area.id==x).select())
