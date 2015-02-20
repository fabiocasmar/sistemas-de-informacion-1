# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

def vista_admin():
	return dict()

def estudiantes():
    form = SQLFORM(db.t_estudiante)
#    return dict(form=form)
#    form = SQLFORM.smartgrid(db.t_estudiante,onupdate=auth.archive)
    return dict(form=form, est=db().select(db.t_estudiante.ALL))

def proponentes():
    form = SQLFORM(db.t_proponente)
#    return dict(form=form)
#    form = SQLFORM.smartgrid(db.t_proponente,onupdate=auth.archive)
    return dict(form=form, proponentes=db().select(db.t_proponente.ALL))

def tutores():
    form = SQLFORM(db.t_tutor)
#    return dict(form=form)
#    form = SQLFORM.smartgrid(db.t_proponente,onupdate=auth.archive)
    return dict(form=form, tutores=db().select(db.t_tutor.ALL))

def proyectos():
    form = SQLFORM(db.t_proyecto)
    return dict(form=form, proyectos=db().select(db.t_proyecto.ALL))

@auth.requires_login()
def estado_manage():
    form = SQLFORM.smartgrid(db.t_estado,onupdate=auth.archive)
    return locals()

#@auth.requires_login()

def sedes():
    form = SQLFORM(db.t_sede)
    return dict(form=form, sedes=db().select(db.t_sede.ALL))

def areas():
    form = SQLFORM(db.t_area,onupdate=auth.archive)
    return dict(form=form, area=db().select(db.t_area.ALL))

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

@auth.requires_login()
def estudiante_manage():
    form = SQLFORM.smartgrid(db.t_estudiante,onupdate=auth.archive)
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
    
#@auth.requires_login()
def sedesDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_sede.id==x).select())
    
def estudiantesDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_estudiante.id==x).select())
    
def proponentesDetalles():
    x = long (request.args[0])
    return dict(rows = db(db.t_proponente.id==x).select())

