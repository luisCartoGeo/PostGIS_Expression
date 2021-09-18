# -*- coding: utf-8 -*-

"""
    ***************************************************************************
    * Plugin name:   PostGIS Expression
    * Plugin type:   QGIS 3 plugin
    * Module:        help variables
    * Description:   Add custom user functions to QGIS Field calculator. 
    * Specific lib:  None
    * First release: 20-09-2021
    * Last release:  ---
    * Copyright:     (C)2021 Luis Eduardo Perez Graterol
    * Email:         luis3176@yahoo.com
    * License:       GPL v3
    ***************************************************************************
"""

# Help docstings
open_expression_pg_doc= """
    Expresión para usuarios avanzados de postgres-postgis, le permitira diseñar y ejecutar su propia
    sentencia SQL, usted es responsable del tipo de datos devuelto por la operación.<BR/>
    Esta expresión, aunque versátil solo maneja resultados alfanumericos o booleanos, provenientes de consultas
    alfanumericas y/o espaciales.<br/>
    Coloque en <b>expresion</b> la sentencia que va delante de una clausula SELECT.<BR/>
    Y en <b>fuente</b>, especifique el FROM de una sentencia SQL, puede agregar otros elementos comunes como
    GROUP BY y ORDER BY.<br/>
    Previamente debe estar activa una conexión a la de Base de Datos.<br/>
    Dependiendo del resultado de la consulta se devolvera un valor unico o una matriz<br/>
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">expression_open_pg(</span>
    <span class="argument">expresion, fuente<span class="functionname">)</span>
    </code></div><br/>
    Para incluir en la sentencia esquemas o capas con mayusculas coloque doble comillas (")<br/>
    Y si desea especificar un texto como comparación de una clausula WHERE utilice \ como comillas simples, una sintaxsis como esta:<br/><br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span>
     
        <h4>Argumentos</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">expresion</td><td>Parte de la sentencia SQL desde el SELECT hasta el FROM. Texto (string)</td></tr>
        <tr><td class="argument">fuente</td><td>Pate de la sentencia delante del FROM. Texto (string)</td></tr>
        <br/>
        </table>
        </code></div>
        <h4>Ejemplos:</h4>
        <!-- Show examples of function.-->
        Determinar el coeficiente de correlación entre la población y el área de los Barrios de Buenos Aires <br/> 
         expression_open_pg('corr(poblacion_,area)','division_administrativa.barrios')<br/>
        <span class="argument">resultado previo</span> 0.770081848773895<br/><br/>
        
        Determinar el coeficiente de correlación entre la población y el área de los Barrios de BA, pero solo de las comunas
        especificadas en la lista<br/>
        expression_open_pg('corr(poblacion_,area)','division_administrativa.barrios where comuna in (10,11,12,14,15)')<br/>
        <span class="argument">resultado previo</span> 0.961284749742084<br/><br/>
        
        Calcula el área acumulada de los barrios agrupados y ordenados por comunas<br/>
        expression_open_pg('sum(st_area(barrios.geom))','division_administrativa.barrios group by comuna order by comuna')<br/>
        <span class="argument">resultado previo</span> [ 0.00170845112089074, 0.000603372178985122, 0.00062766099….] <br/><br/>
        
        Consulta espacial que determina el numero de solicitudes de atención ciudadana (suaci2021) contenidos en los barrios
       que pertenecen a la comuna identificada con el numero 10<br/>
        expression_open_pg('count(*)','division_administrativa.barrios as a,"SUACI".suaci2021 as b where st_intersects(a.geom,b.geom) and a.comuna=10')<br/>
        <span class="argument">resultado previo</span> 32170<br/><br/>
        
        Consulta anterior agrupada y ordenada por comuna<br/>
         expression_open_pg('count(*)','division_administrativa.barrios as a,"SUACI".suaci2021 as b where st_intersects(a.geom,b.geom) group by a.comuna')<br/>
          <span class="argument">resultado previo</span> [ 19322, 21487, 19650, 21154, 17296, 26942, 30545, 11206, … ]
"""


correlation_pg_doc = """
       Devuelve el valor o valores del coeficiente de correlación (R2) entre dos campos numéricos de la 
    una <b>capa</b>  de la base de datos postgreSQL.<br/>
    Deben especificarse los campos sobre el que se realizara el cálculo.<br/>
    Previamente debe estar activa una conexión a la Base de Datos.<br/>
    Opcional se puede definir un <b>filtro</b>, una expresión condicional<br/>
    También puede especificarse una clausula <span class="functionname">group</span>
    <b>opcional</b> para agregar el resultado por un campo<br/>
    Si se aplica <span class="functionname">group</span> el resultado será devuelto
    en una matriz.<br/>
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">correlation_pg(</span>
    <span class="argument">esquema, capa, campo1, campo2,filtro, group<span class="functionname">)</span>
    </code></div><br/>
    El filtro es opcional, es una condicional<br/>
     debe escribirse así:<br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span>
     <p>Si no requiere filtro colocar <span class="functionname">''</span><</p>
     <p>La clausula <b><span class="functionname">group</span></b> es opcional, simplemente escriba
     el campo por el que desea agrupar</p>
    <p>Si no requiere <b><span class="functionname">group</span></b> colocar <span class="functionname">''</span><</p>
     
        <h4>Argumentos</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">esquema</td><td>Nombre del esquema de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">capa</td><td>Nombre de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">campo1</td><td>Nombre del campo numérico por el que se calcular la correlación. Texto (string)</td></tr>
        <tr><td class="argument">campo2</td><td>Nombre del campo numérico que se comparara con el campo1. Texto (string)</td></tr>
        <tr><td class="argument">filtro</td><td>Condicional para filtrar la consulta. Texto (string)</td>
        <br/>
        <br/><b>Las opciones son:</b>
        <br/>'' : no aplicara filtro, consultara todas las entidades de ambas capas
        <br/><span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span> : expresión condicional
        </tr>
        <tr><td class="argument">group</td><td>Nombre del campo por el que desea agrupar. Texto (string)</td></tr>
        </table>
        </code></div>
        <h4>Ejemplos:</h4>
        <!-- Show examples of function.-->
        Determinar el coeficiente de correlación entre la población y el área de los Barrios de Buenos Aires <br/> 
         correlation_pg('division_administrativa','barrios','poblacion_','area','','')<br/>
        <span class="argument">resultado previo</span> 0.770081848773895<br/><br/>
        
        Determinar el coeficiente de correlación entre la población y el área de los Barrios de Buenos Aires agrupado por el campo comunas<br/>
         correlation_pg('division_administrativa','barrios','poblacion_','area','','comuna')<br/>
        <span class="argument">resultado previo</span> [ 0.042736467333633, 0.961366222140714, 0.798900885165583,…,......]<br/><br/>
    """

total_statistics_pg_doc = """
        Devuelve el valor o valores de la estadistica solicitada a un campo de la 
    base de datos postgreSQL.<br/>
    Debe especificarse el campo sobre el que se realizara el cálculo, también el estadistico 
    del listado disponible.<br/>
    Previamente debe estar activa una conexión a la Base de Datos.<br/>
    Opcional se puede definir un <b>filtro</b>, una expresión condicional<br/>
    También puede especificarse una clausula <span class="functionname">group</span>
    <b>opcional</b> para agregar el resultado por un campo<br/>
    Si se aplica <span class="functionname">group</span> el resultado será devuelto
    en una matriz.<br/>
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">total_statitics_pg(</span>
    <span class="argument">esquema, capa, campo, estadistico, filtro, group<span class="functionname">)</span>
    </code></div><br/>
    El filtro es opcional, es una condicional<br/>
     debe escribirse así:<br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span>
     <p>Si no requiere filtro colocar <span class="functionname">''</span><</p>
     <p>La clausula <b><span class="functionname">group</span></b> es opcional, simplemente escriba
     el campo por el que desea agrupar</p>
    <p>Si no requiere <b><span class="functionname">group</span></b> colocar <span class="functionname">''</span><</p>
     
        <h4>Argumentos</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">esquema</td><td>Nombre del esquema de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">capa</td><td>Nombre de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">campo</td><td>Nombre del campo numérico por el que se calculara la estadistica. Texto (string)</td></tr>
        <tr><td class="argument">estadistico</td><td>El estadistico que desea calcular. Texto (string)</td></tr>
        <br/><b>Las opciones son:</b>
        <br/><b>sum</b>:    devuelve la suma de los valores del campo
        <br/><b>avg</b>:    devuelve el promedio de los valores del campo
        <br/><b>max</b>:    devuelve el máximo valor de los valores del campo
        <br/><b>min</b>:    devuelve el mínimo valor de los valores del campo
        <br/><b>count</b>:  devuelve el conteo de todos los registros, o los que cumplen el filtro
        <br/><b>stddev_pop</b>:  devuelve la desviación estandar de la población de los valores del campo
        <br/><b>stddev_samp</b>: devuelve la desviación estandar de la muestra de los valores del campo
        <tr><td class="argument">filtro</td><td> Condicional para filtrar la consulta. Texto (string)</td>
        <br/>
        <br/><b>Las opciones son:</b>
        <br/>'' : no aplicara filtro, consultara todas las entidades de ambas capas
        <br/><span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span> : expresión condicional
        </tr>
        <tr><td class="argument">group</td><td> Nombre del campo por el que desea agrupar. Texto (string)</td></tr>
        </table>
        </code></div>
        <h4>Ejemplos:</h4>
        <!-- Show examples of function.-->
        Determinar el valor mínimo de población del campo poblacion_ de una capa postgis <br/> 
        total_statitics_pg('division_administrativa','barrios','poblacion_','min','','')<br/>
        <span class="argument">resultado previo</span>  6726<br/><br/>
        
        Determinar el valor mínimo de población del campo poblacion_ agrupado por el campo comunas<br/>
        total_statitics_pg('division_administrativa','barrios','poblacion_','min','','comuna')<br/>
        <span class="argument">resultado previo</span>  {6726, 40985, 14084, 176076, 47306, 44132, 51949, 157932,......]<br/><br/>
        
        Determina el valor mínimo de población del campo poblacion_ pero solo de los barrios de la comuna 15<br/> 
         total_statitics_pg('division_administrativa','barrios','poblacion_','min','"comuna"=\\'15\\'','')<br/>
         <span class="argument">resultado previo</span>  13912<br/><br/>
    """

num_intersects_pg_doc = """
        Devuelve el numero de entidades de una capa postgis que intersecta otra
    capa postgis de la misma BD<br/>
    Previamente debe estar activa una conexión a la de Base de Datos.<br/>
    Opcional se puede definir un filtro, una expresión condicional.<br/>
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">num_intersects_pg(</span>
    <span class="argument">esquema1, capa1, esquema2, capa2, filtro<span class="functionname">)</span>
    </code></div><br/>
    El filtro es opcional, es una condicional<br/>
     debe escribirse así:<br/><br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span>
     <p>Si no requiere filtro colocar <span class="functionname">''</span><</p>
     
        <h4>Argumentos</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">esquema1</td><td>Nombre del esquema de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">capa1</td><td>Nombre de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">esquema2</td><td>Nombre del esquema de la capa2. Texto (string)</td></tr>
        <tr><td class="argument">capa2</td><td>Nombre de la capa2. Texto (string)</td></tr>
        <tr><td class="argument">filtro</td><td>Condicional para filtrar la consulta. Texto (string)</td>
        <br/>
        <br/><b>Las opciones son:</b>
        <br/>'' : no aplicara filtro, consultara todas las entidades de ambas capas
        <br/><span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span> : expresión condicional
        </tr>
        </table>
        </code></div>
        <h4>Ejemplos:</h4>
        <!-- Show examples of function.-->
        <p>Determinar el numero de entidades de una capa postgis que intersectan
        todas las entidades de otra capa postgis</p> 
         num_intersects_pg('division_administrativa','barrios','public','parcelas','')<br/>
         <p>Determina el total de entidades de la capa postgis parcelas que intersectan las entidades de la capa
         postgis barrios donde el campo barrio es igual a PALERMO</P>   
        num_intersects_pg('public','parcelas','division_administrativa','barrios','"barrio"=\\'PALERMO\\'')
    """

num_contains_pg_doc="""
    Devuelve el numero de entidades de la <b>capa2</b> postgis que están contenidos
    en la <b>capa1</b> postgis<br/>
    Deben especificarse los parámetros para conectarse a la Base de Datos, 
    los esquemas y capas correspondientes<br/>
    Opcional se puede definir un filtro, una expresión condicional<br/>
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">num_contains_pg(</span>
    <span class="argument">puerto, nombreDB, servidor, usuario, contraseña,
    esquema1, capa1, esquema2, capa2, feature, parent, filtro<span class="functionname">)</span>
    </code></div><br/>
    El filtro es opcional, es una condicional<br/>
     debe escribirse así:<br/><br/>
     <span class="functionname">'"barrios"."barrio"=\'PALERMO\''</span><br/>
     <span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span>
     <p>Si no requiere filtro colocar <span class="functionname">''</span><</p>
     
        <h4>Argumentos</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">puerto</td><td>Numero de puerto de la red. Texto (string) o numero entero</td></tr>
        <tr><td class="argument">nombreDB</td><td>Nombre de la Base de Datos. Texto (string).</td></tr>
        <tr><td class="argument">servidor</td><td>Nombre del servidor (Host). Texto (string)</td></tr>
        <tr><td class="argument">usuario</td><td>Nombre de usuario. Texto (string)</td></tr>
        <tr><td class="argument">contraseña</td><td>contraseña. Texto (string)</td></tr>
        <tr><td class="argument">esquema1</td><td>Nombre del esquema de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">capa1</td><td>Nombre de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">esquema2</td><td>Nombre del esquema de la capa2. Texto (string)</td></tr>
        <tr><td class="argument">capa2</td><td>Nombre de la capa2. Texto (string)</td></tr>
        <tr><td class="argument">filtro</td><td>Condicional para filtrar la consulta. Texto (string)</td>
        <br/>
        <br/><b>Las opciones son:</b>
        <br/>'' : no aplicara filtro, consultara todas las entidades de ambas capas
        <br/><span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span> : expresión condicional
        </tr>
        </table>
        </code></div>
        <h4>Ejemplos:</h4>
        <!-- Show examples of function.-->
        <p>Determinar el numero de entidades de una capa postgis contenidos
        en otra capa postgis</p>
       <p>En el ejemplo se determinan el numero de puntos del Servicio de Atención Ciudadana de
        la Ciudad de Buenos Aires(suaci2021) que estan contenidos en los Barrios de BA</p>
         num_contains_pg(5432,'CABA','localhost','postgres','12345678','division_administrativa','barrios','SUACI','suaci2021','')
         <p>Se aplica un filtro y se evaluan los puntos suaci2021 contenidos en el barrio PALERMO</P>   
        num_contains_pg(5432,'CABA','localhost','postgres','12345678','public','parcelas','SUACI','suaci2021','"barrios"."barrio"=\\'PALERMO\\'')
"""

num_within_pg_doc="""
    Devuelve el numero de entidades de la <b>capa1</b> de postgis que están contenidos
    en la <b>capa2</b> de postgis<br/>
    Previamente debe estar activa una conexión a la de Base de Datos.<br/>
    Opcional se puede definir un filtro, una expresión condicional<br/>
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">num_within_pg(</span>
    <span class="argument">esquema1, capa1, esquema2, capa2, filtro<span class="functionname">)</span>
    </code></div><br/>
    El filtro es opcional, es una condicional<br/>
     debe escribirse así:<br/><br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span>
     <p>Si no requiere filtro colocar <span class="functionname">''</span><</p>
     
        <h4>Argumentos</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">esquema1</td><td>Nombre del esquema de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">capa1</td><td>Nombre de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">esquema2</td><td>Nombre del esquema de la capa2. Texto (string)</td></tr>
        <tr><td class="argument">capa2</td><td>Nombre de la capa2. Texto (string)</td></tr>
        <tr><td class="argument">filtro</td><td>Condicional para filtrar la consulta. Texto (string)</td>
        <br/>
        <br/><b>Las opciones son:</b>
        <br/>'' : no aplicara filtro, consultara todas las entidades de ambas capas
        <br/><span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span> : expresión condicional
        </tr>
        </table>
        </code></div>
        <h4>Ejemplos:</h4>
        <!-- Show examples of function.-->
        <p>Determinar el numero de entidades de una capa postgis dentro de las entidades
        de otra capa postgis</p>
       <<p>En el ejemplo se determinan el numero de puntos del Servicio de Atención Ciudadana de
        la Ciudad de Buenos Aires(suaci2021) que estan contenidos en los Barrios de BA</p><br/>
         num_within_pg('SUACI','suaci2021','division_administrativa','barrios','')<br/>
         <p>Se aplica un filtro y se evaluan los puntos suaci2021 contenidos en el barrio PALERMO</P>   
        num_within_pg('SUACI','suaci2021','division_administrativa','barrios','"barrios"."barrio"=\'PALERMO\'')
"""

num_buffer_intersects_pg_doc="""
       Devuelve el numero de entidades de la <b>capa1</b> postgis que intersecta el area de influencia 
    de las entidades de la <b>capa2</b> postgis de la misma BD<br/>
    Debe especofocarse la distancia en unidades de proyección de las capas.<br/>
    Previamente debe estar activa una conexión a la de Base de Datos.<br/>
    Opcional se puede definir un filtro, una expresión condicional<br/>
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">num_buffer_intersects_pg(</span>
    <span class="argument">esquema1, capa1, esquema2, capa2, distancia, filtro<span class="functionname">)</span>
    </code></div><br/>
    El filtro es opcional, es una condicional<br/>
     debe escribirse así:<br/><br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span>
     <p>Si no requiere filtro colocar <span class="functionname">''</span><</p>
     
        <h4>Argumentos</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">esquema1</td><td>Nombre del esquema de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">capa1</td><td>Nombre de la capa1. Texto (string)</td></tr>
        <tr><td class="argument">esquema2</td><td>Nombre del esquema de la capa2. Texto (string)</td></tr>
        <tr><td class="argument">capa2</td><td>Nombre de la capa2. Texto (string)</td></tr>
        <tr><td class="argument">distancia</td><td>Distancia a considerar para el buffer. Texto (string) o numero</td></tr>
        <tr><td class="argument">filtro</td><td>Condicional para filtrar la consulta. Texto (string)</td>
        <br/>
        <br/><b>Las opciones son:</b>
        <br/>'' : no aplicara filtro, consultara todas las entidades de ambas capas
        <br/><span class="functionname">'"capa"."campo" operador \\'valor del atributo\\''</span> : expresión condicional
        </tr>
        </table>
        </code></div>
        <h4>Ejemplos:</h4>
        <!-- Show examples of function.-->
        Determinar el numero de puntos de la capa suaci2021 que intersectan el area de influencia 
        (distancia 0.001 grados) de las calles tipo CALLE<br/>
         num_buffer_intersects_pg('public','parcelas','public','calles',0.001,'"calles"."tipo_c"=\'CALLE\'')<br/><br/>
         El mismo analisis para una calle especifica, identificada con el id=10<br/>
          num_buffer_intersects_pg('public','parcelas','public','calles',0.001,'"calles"."id"=\'10\'')<br/><br/>
         Determina el total de radios censales que intersectan el area de influencia
         del barrio PALERMO<br/>  
        num_buffer_intersects_pg('division_administrativa','radios_censales','division_administrativa','barrios',0.001,
        '"barrios"."barrio"=\\'PALERMO\\'')<br/>
"""
