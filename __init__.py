# -*- coding: utf-8 -*-
"""
    ***************************************************************************
    * Plugin name:   PostGIS_Expression
    * Plugin type:   QGIS 3 plugin
    * Module:        Initialization
    * Description:   Adds customs expressions for querying PostgreSQL-PostGIS Databases. 
    * Specific lib:  None
    * First release: 2021-08-10
    * Last release:  -------
    * Copyright:     (C)2021 Luis Eduardo Pérez G.
    * Email:         luisepg3176@gmail.com
    * License:       GPL v3
    ***************************************************************************

    This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load postgisExpressLoad class from file PostGIS_expression_functions
    from .PostGIS_expression_functions import postgisExpressLoad
    return postgisExpressLoad(iface)
