from qgis.PyQt import uic
import os
import psycopg2
from qgis import PyQt
from qgis.PyQt.QtGui import QIcon,QPixmap
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtWidgets import QLineEdit, QDialog, QPushButton
from qgis.core import QgsProject, QgsExpressionContextUtils, QgsExpressionContextScope

DialogUi, DialogType=uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'pg_connect_dlg.ui'))

class pg_connect_dialog(DialogUi, DialogType):
    """Allows the connection to the database to be established"""
    def __init__(self,iface):
        """Constructor.

        :param Port: default is 5432
        :type Port: str or number
        :param Database name
        :type Database name: str
        :param Password
        :type Password: str
        :param User: default postgres
        :type User: str
        :param host name
        :type hos: str
        """
        super().__init__()
        self.setupUi(self)   #initializes everything done in QtDesigner
        self.dir = os.path.dirname(__file__)
        self.iface=iface
        icon= QPixmap(os.path.join(self.dir,'icons/plugin_image'))
        self.licon.setPixmap(icon.scaledToHeight(180,0))
        self.bconnect.clicked.connect(self.connection)
        #EVENTS BUTTONS ACCEP CANCEL
        self.accepted.connect(self.aceptar)
        self.rejected.connect(self.cancelar)
    
    def connection(self):
        puerto = self.lport.text()
        dbname = self.ldbname.text()
        servidor = self.lhost.text()
        usuario= self.luser.text()
        cont= self.lpass.text()
        
        try:
            conn = psycopg2.connect(dbname=dbname, 
                                    port=puerto, 
                                    user=usuario,
                                    password=cont, 
                                    host=servidor)
            conn.set_session(readonly=True)
            cur = conn.cursor()
            self.label_result.setText('Successful connection')
            pry=QgsProject.instance()
            QgsExpressionContextUtils.setProjectVariable(pry,'cursor',[cur,conn])
        except Exception as e:
            self.label_result.setText('Failed connection check supply parameters')
            self.iface.messageBar().pushMessage('ERROR',\
            str(e), level=1, duration=7)
    
    def aceptar(self):
        pry=QgsProject.instance()
        lv=QgsExpressionContextUtils.projectScope(pry).filteredVariableNames()
        if 'cursor' in lv==False:
            self.connection()
        self.close()
    
    def cancelar(self):
        self.close()