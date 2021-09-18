from qgis.PyQt.QtCore import Qt, QSettings,  QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QWidget
from qgis.utils import iface, qgsfunction
from qgis.core import QgsProject, QgsMapLayer, QgsFeature, QgsExpression, QgsExpressionContextUtils
import os
from .pg_connect_dialog import pg_connect_dialog
import psycopg2
import decimal

plugin_dir = os.path.dirname(__file__)
locale = QSettings().value('locale/userLocale')[0:2]
if locale == 'es':
    from .postgis_expression_doc_es import *
else:
    from .postgis_expression_doc_en import *
locale_path = os.path.join(
        plugin_dir,
                  'i18n',
                  'postgis_expression_{}.qm'.format(locale))
if os.path.exists(locale_path):
    translator = QTranslator()
    translator.load(locale_path)
    QCoreApplication.installTranslator(translator)

def tr(self, message):
    return QCoreApplication.translate('postgisExpressLoad', message)
    
# Used to add docstring from a variable
def add_doc(value):
    def _doc(func):
        func.__doc__ = value
        return func
    return _doc

@qgsfunction(args='auto', group="PostGIS", register=False, usesgeometry=False, handlesnull=True)
@add_doc(open_expression_pg_doc)
def expression_open_pg(expresion,fuente,feature, parent):
    pry=QgsProject.instance()
    lv=QgsExpressionContextUtils.projectScope(pry).filteredVariableNames ()
    if 'cursor' in lv:
        cursor=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[0]
        connec=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[1]
        
        if connec.info.transaction_status > 2:
            connec.rollback()
        
        sql='select '+expresion+' from '+fuente+';' 
        
        try:
            cursor.execute(sql)
            salida=cursor.fetchall()
            if len(salida)==1:
                if type(salida[0][0])==int or type(salida[0][0])==float:
                    return salida[0][0]
                elif type(salida[0][0])==decimal.Decimal:
                    if str(salida[0][0]).isdigit:
                        salida=int(salida[0][0])
                    else:
                        salida=float(salida[0][0])
                return salida
            else:
                lista=[]
                for i in salida:
                    if type(i[0])==int or type(i[0])==float:
                        lista.append(i[0])
                    elif type(i[0])==decimal.Decimal:
                        if str(i[0]).isdigit():
                            lista.append(int(i[0]))
                        else:
                            lista.append(float(i[0]))
                    elif type(i[0])==bool or type(i[0])==str:
                        lista.append(i)
                    else:
                        lista.append(None)
                return lista
        except Exception as e:
            return str(e) 
    else:
        return "Primero debe crear una conección"

@qgsfunction(args='auto', group="PostGIS", register=False, usesgeometry=False, handlesnull=True)
@add_doc(correlation_pg_doc)
def correlation_pg(esquema,capa,campo1,campo2,filtro,group,feature, parent):
    pry=QgsProject.instance()
    lv=QgsExpressionContextUtils.projectScope(pry).filteredVariableNames ()
    if 'cursor' in lv:
        cursor=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[0]
        connec=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[1]
        
        if connec.info.transaction_status > 2:
            connec.rollback()
        
        if esquema.islower() == False:
            esquema= '"'+esquema+'"'
        if capa.islower() == False:
            capa= '"'+capa+'"'
        if campo1.islower() == False:
            campo1= '"'+campo1+'"'
        if campo2.islower() == False:
            campo2= '"'+campo2+'"'
        esqu=esquema
        
        if filtro=='' and group=='':
            sql='select corr('+campo1+','+campo2+') from '+esqu+'.'+capa+';' 
        elif filtro=='' and group!='':
            sql='select corr('+campo1+','+campo2+') from '+esqu+'.'+capa+'\n'+\
                ' group by '+group+';' 
        elif filtro!='' and group=='':
            sql='select '+estad+'('+campo+') from '+esqu+'.'+capa+'\n'+\
                ' where ('+filtro+');' 
        elif filtro!='' and group!='':
            sql=sql='select corr('+campo1+','+campo2+') from '+esqu+'.'+capa+'\n'+\
                ' where ('+filtro+')'+'\n'+\
                ' group by '+group+';' 
        try:
            cursor.execute(sql)
            salida=cursor.fetchall()
            if len(salida)==1:
                if type(salida[0][0])==int or type(salida[0][0])==float:
                    salida= salida[0][0]
                elif type(salida[0][0])==decimal.Decimal:
                    if str(salida[0][0]).isdigit:
                        salida=int(salida[0][0])
                    else:
                        salida=float(salida[0][0])
                else:
                    salida=None
                return salida
            else:
                lista=[]
                for i in salida:
                    if type(i[0])==int or type(i[0])==float:
                        lista.append(i[0])
                    elif type(i[0])==decimal.Decimal:
                        if str(i[0]).isdigit():
                            lista.append(int(i[0]))
                        else:
                            lista.append(float(i[0]))
                    else:
                        lista.append(None)
                return lista
            
        except Exception as e:
            return str(e) 
    else:
        return "Primero debe crear una conección"
        
@qgsfunction(args='auto', group="PostGIS", register=False, usesgeometry=False, handlesnull=True)
@add_doc(total_statistics_pg_doc)
def total_statistics_pg(esquema,capa,campo,estadistico,filtro,group,feature, parent):
    estad=estadistico
    pry=QgsProject.instance()
    lv=QgsExpressionContextUtils.projectScope(pry).filteredVariableNames ()
    if 'cursor' in lv:
        cursor=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[0]
        connec=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[1]
        
        if connec.info.transaction_status > 2:
            connec.rollback()
        
        if esquema.islower() == False:
            esquema= '"'+esquema+'"'
        if capa.islower() == False:
            capa= '"'+capa+'"'
        esqu=esquema
        
        if filtro=='' and group=='':
            sql='select '+estad+'('+campo+') from '+esqu+'.'+capa+';' 
        elif filtro=='' and group!='':
            sql='select '+estad+'('+campo+') from '+esqu+'.'+capa+'\n'+\
                ' group by '+group+';' 
        elif filtro!='' and group=='':
            sql='select '+estad+'('+campo+') from '+esqu+'.'+capa+'\n'+\
                ' where ('+filtro+');' 
        elif filtro!='' and group!='':
            sql='select '+estad+'('+campo+') from '+esqu+'.'+capa+'\n'+\
                ' where ('+filtro+')'+'\n'+\
                ' group by '+group+';' 
        try:
            cursor.execute(sql)
            salida=cursor.fetchall()
            if len(salida)==1:
                if type(salida[0][0])==int or type(salida[0][0])==float:
                    salida= salida[0][0]
                elif type(salida[0][0])==decimal.Decimal:
                    if str(salida[0][0]).isdigit:
                        salida=int(salida[0][0])
                    else:
                        salida=float(salida[0][0])
                else:
                    salida=None
                return salida
            else:
                lista=[]
                for i in salida:
                    if type(i[0])==int or type(i[0])==float:
                        lista.append(i[0])
                    elif type(i[0])==decimal.Decimal:
                        if str(i[0]).isdigit():
                            lista.append(int(i[0]))
                        else:
                            lista.append(float(i[0]))
                    else:
                        lista.append(None)
                return lista
        except Exception as e:
            return str(e) 
    else:
        return "Primero debe crear una conección"

@qgsfunction(args='auto', group="PostGIS", register=False, usesgeometry=False, handlesnull=True)
@add_doc(num_intersects_pg_doc)
def num_intersects_pg(esquema1,capa1,esquema2,capa2,filtro,feature, parent):
    pry=QgsProject.instance()
    lv=QgsExpressionContextUtils.projectScope(pry).filteredVariableNames ()
    if 'cursor' in lv:
        cursor=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[0]
        connec=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[1]
        
        if connec.info.transaction_status > 2:
            connec.rollback()
                
        if esquema1.islower() == False:
            esquema1= '"'+esquema1+'"'
        if esquema2.islower() == False:
            esquema2= '"'+esquema2+'"'
        if capa1.islower() == False:
            capa1= '"'+capa1+'"'
        if capa2.islower() == False:
            capa2= '"'+capa2+'"'
        if filtro=='':
            sql='select count(*) from '+esquema1+'.'+capa1+' as a,'+'\n'+\
                '(select * from '+esquema2+'.'+capa2+') as b'+'\n'+\
                'WHERE ST_Intersects(a.geom,b.geom);' 
        else:
            #filtro=campo+operador+"'"+valor+"'"
            sql='select count(*) as inters from '+esquema1+'.'+capa1+','+'\n'+\
            esquema2+'.'+capa2+'\n'+\
            'WHERE ST_Intersects('+capa1+'.geom,'+capa2+'.geom)'+'\n'+\
            'And'+'('+filtro+');'
        try:
            cursor.execute(sql)
            salida=cursor.fetchall()
            return salida[0][0]
        except Exception as e:
            return str(e) 
    else:
        return "No existe una conexión con la base de datos"

@qgsfunction(args='auto', group="PostGIS", register=False, usesgeometry=False, handlesnull=True)
@add_doc(num_contains_pg_doc)
def num_contains_pg(esquema1,capa1,esquema2,capa2,filtro,feature, parent):
    pry=QgsProject.instance()
    lv=QgsExpressionContextUtils.projectScope(pry).filteredVariableNames ()
    if 'cursor' in lv:
        cursor=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[0]
        connec=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[1]
        
        if connec.info.transaction_status > 2:
            connec.rollback()
                
        if esquema1.islower() == False:
            esquema1= '"'+esquema1+'"'
        if esquema2.islower() == False:
            esquema2= '"'+esquema2+'"'
        if capa1.islower() == False:
            capa1= '"'+capa1+'"'
        if capa2.islower() == False:
            capa2= '"'+capa2+'"'
        if filtro=='':
            sql='select count(*) from '+esquema1+'.'+capa1+' as a,'+'\n'+\
                '(select * from '+esquema2+'.'+capa2+') as b'+'\n'+\
                'WHERE ST_Contains(a.geom,b.geom);' 
        else:
            #filtro=campo+operador+"'"+valor+"'"
            sql='select count(*) as a from '+esquema1+'.'+capa1+','+'\n'+\
            esquema2+'.'+capa2+'\n'+\
            'WHERE ST_Contains('+capa1+'.geom,'+capa2+'.geom)'+'\n'+\
            'And'+'('+filtro+');'
        try:
            cursor.execute(sql)
            salida=cursor.fetchall()
            return salida[0][0]
        except Exception as e:
            return str(e) 
    else:
        return "No existe una conexión con la base de datos"

@qgsfunction(args='auto', group="PostGIS", register=False, usesgeometry=False, handlesnull=True)
@add_doc(num_within_pg_doc)
def num_within_pg(esquema1,capa1,esquema2,capa2,filtro,feature, parent):
    pry=QgsProject.instance()
    lv=QgsExpressionContextUtils.projectScope(pry).filteredVariableNames ()
    if 'cursor' in lv:
        cursor=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[0]
        connec=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[1]
        
        if connec.info.transaction_status > 2:
            connec.rollback()
                
        if esquema1.islower() == False:
            esquema1= '"'+esquema1+'"'
        if esquema2.islower() == False:
            esquema2= '"'+esquema2+'"'
        if capa1.islower() == False:
            capa1= '"'+capa1+'"'
        if capa2.islower() == False:
            capa2= '"'+capa2+'"'
        if filtro=='':
            sql='select count(*) from '+esquema1+'.'+capa1+' as a,'+'\n'+\
                '(select * from '+esquema2+'.'+capa2+') as b'+'\n'+\
                'WHERE ST_Within(a.geom,b.geom);' 
        else:
            #filtro=campo+operador+"'"+valor+"'"
            sql='select count(*) as a from '+esquema1+'.'+capa1+','+'\n'+\
            esquema2+'.'+capa2+'\n'+\
            'WHERE ST_Within('+capa1+'.geom,'+capa2+'.geom)'+'\n'+\
            'And'+'('+filtro+');'
        try:
            cursor.execute(sql)
            salida=cursor.fetchall()
            return salida[0][0]
        except Exception as e:
            return str(e) 
    else:
        return "No existe una conexión con la base de datos"

@qgsfunction(args='auto', group="PostGIS", register=False, usesgeometry=False, handlesnull=True)
@add_doc(num_buffer_intersects_pg_doc)
def num_buffer_intersects_pg(esquema1,capa1,esquema2,capa2,distancia,filtro,feature, parent):
    pry=QgsProject.instance()
    lv=QgsExpressionContextUtils.projectScope(pry).filteredVariableNames ()
    if 'cursor' in lv:
        cursor=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[0]
        connec=QgsExpressionContextUtils.projectScope(pry).variable('cursor')[1]
        
        if connec.info.transaction_status > 2:
            connec.rollback()
                
        if esquema1.islower() == False:
            esquema1= '"'+esquema1+'"'
        if esquema2.islower() == False:
            esquema2= '"'+esquema2+'"'
        if capa1.islower() == False:
            capa1= '"'+capa1+'"'
        if capa2.islower() == False:
            capa2= '"'+capa2+'"'
        if type(distancia)==str:
            if distancia.isdigit():
                distancia=int(distancia)
            else:
                try:
                    distancia=float(distancia)
                except:
                    return 'Valor de distancia NO valido'
        if filtro=='':
            sql='select count(*) from '+esquema1+'.'+capa1+' as a,'+'\n'+\
                '(select * from '+esquema2+'.'+capa2+') as b'+'\n'+\
                'WHERE ST_Intersects(a.geom,st_buffer(b.geom,'+str(distancia)+'));' 
        else:
            #filtro=campo+operador+"'"+valor+"'"
            sql='select count(*) from '+'\n'+\
           '(select * from '+esquema1+'.'+capa1+') as a ,'+'\n'+\
           esquema2+'.'+capa2+'\n'+\
            ' WHERE ST_Intersects(a.geom,st_buffer('+capa2+'.geom,'+str(distancia)+'))'+'\n'+\
            'And'+'('+filtro+');'
        try:
            cursor.execute(sql)
            salida=cursor.fetchall()
            return salida[0][0]
        except Exception as e:
            return str(e) 
    else:
        return "No existe una conexión con la base de datos"

class postgisExpressLoad:
    def __init__(self, iface):
        self.iface = iface
        # Find plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
#        locale = QSettings().value('locale/userLocale','en')[0:2]
#        locale_path = os.path.join(
#        self.plugin_dir,
#                  'i18n',
#                  'postgis_expression_{}.qm'.format(locale))
#        if os.path.exists(locale_path):
#            self.translator = QTranslator()
#            self.translator.load(locale_path)
#            QCoreApplication.installTranslator(self.translator)
        self.menu= tr(self,u'&PostGIS Expression')
    
    # noinspection PyMethodMayBeStatic
#    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
#        return QCoreApplication.translate('postgis_expression', message)

    def initGui(self):
        QgsExpression.registerFunction(correlation_pg)
        QgsExpression.registerFunction(total_statistics_pg)
        QgsExpression.registerFunction(num_intersects_pg)
        QgsExpression.registerFunction(num_contains_pg)
        QgsExpression.registerFunction(num_within_pg)
        QgsExpression.registerFunction(num_buffer_intersects_pg)
        QgsExpression.registerFunction(expression_open_pg)
        
        # Button and menu to connect to database
        icon_path=os.path.join(self.plugin_dir,"icons/icon.png")
        icon = QIcon(icon_path)
        text=tr(self,u'New connection')
        self.action_conec = QAction(icon, text, self.iface.mainWindow())
        self.action_conec.triggered.connect(self.dlg_connect)
        #action_conec.setEnabled(enabled_flag)
        status_tip=tr(self,u'Establish a connection to the database')
        self.action_conec.setStatusTip(status_tip)
        self.iface.addToolBarIcon(self.action_conec)
        self.iface.addPluginToMenu(
                self.menu,
                self.action_conec)
        icon_path=os.path.join(self.plugin_dir,"icons/disconnect.png")
        icon = QIcon(icon_path)
        text=tr(self,u'Disconnect')
        self.action_disconec = QAction(icon, text, self.iface.mainWindow())
        self.action_disconec.triggered.connect(self.dlg_disconnect)
        status_tip=tr(self,u'Closes the database connection')
        self.action_conec.setStatusTip(status_tip)
        self.iface.addToolBarIcon(self.action_disconec)
        self.iface.addPluginToMenu(
                self.menu,
                self.action_disconec)

    def unload(self):
        QgsExpression.unregisterFunction('correlation_pg')
        QgsExpression.unregisterFunction('total_statistics_pg')
        QgsExpression.unregisterFunction('num_intersects_pg')
        QgsExpression.unregisterFunction('num_contains_pg')
        QgsExpression.unregisterFunction('num_within_pg')
        QgsExpression.unregisterFunction('num_buffer_intersects_pg')
        QgsExpression.unregisterFunction('expression_open_pg')

        self.iface.removePluginMenu(
                tr(self,u'&Postgis Expression'),
                self.action_conec)
        self.iface.removeToolBarIcon(self.action_conec)
        self.iface.removePluginMenu(
                tr(self,u'&Postgis Expression'),
                self.action_disconec)
        self.iface.removeToolBarIcon(self.action_disconec)
    
    def dlg_disconnect(self):
        pry=QgsProject.instance()
        lv=QgsExpressionContextUtils.projectScope(pry).filteredVariableNames ()
        if 'cursor' in lv:
            try:
                cursor=QgsExpressionContextUtils.projectScope(pry).variable('cursor')
                cursor[0].close()
                cursor[1].close()
                QgsExpressionContextUtils.removeProjectVariable(pry,'cursor')
                result_discn=tr(self,"No database connection exists")
                self.iface.messageBar().pushMessage('DB disconnected',\
                result_discn, level=0, duration=7)
            except Exception as e:
                error=str(e)
                self.iface.messageBar().pushMessage('ERROR',\
                error, level=1, duration=7)
        else:
            texte=tr(self,"No database connection exists")
            self.iface.messageBar().pushMessage('ERROR',\
            texte, level=1, duration=7)

    def dlg_connect(self):
        self.dlg = pg_connect_dialog(self.iface)
        # show the dialog
        self.dlg.show()