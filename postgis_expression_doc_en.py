# -*- coding: utf-8 -*-

"""
    ***************************************************************************
    * Plugin name:   PostGIS Expression
    * Plugin type:   QGIS 3 plugin
    * Module:        help variables
    * Description:   Add custom user functions to QGIS Field calculator. 
    * Specific lib:  None
    * First release: 2021
    * Last release:  ---
    * Copyright:     (C)2021 Luis Eduardo Perez Graterol
    * Email:         luis3176@yahoo.com
    * License:       GPL v3
    ***************************************************************************
"""

# Help docstings
open_expression_pg_doc= """
    Expression for advanced users of postgres-postgis, will allow you to design and run your own
    SQL statement, you are responsible for the type of data returned by the operation.<BR/>
    This expression, although versatile, only handles alphanumeric or boolean results, 
    coming from alphanumeric and/or spatial queries.<br/>
    Place in <b>expression</b> the statement that goes in front of a SELECT clause.<BR/>
    And in <b>source</b>, specify the FROM of a SQL statement, you can add other common elements such as
    GROUP BY and ORDER BY.<br/>
    Previously a connection to the database must be active.<br/>
    Depending on the result of the query, a single value or an array will be returned.<br/>
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">expression_open_pg(</span>
    <span class="argument">expresion, source<span class="functionname">)</span>
    </code></div><br/>
    To include outlines or layers in the sentence with capital letters, use double quotation marks (")<br/>
   And if you want to specify a text as a comparison of a WHERE clause use \ as single quotes, a syntax like this:<br/><br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"capa"."campo" operator \\'value of attribute\\''</span>
     
        <h4>Argumentos</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">expresion</td><td>Part of the SQL statement from the SELECT to the FROM. Text (string)</td></tr>
        <tr><td class="argument">source</td><td>Sentence part in front of the FROM. Text(string)</td></tr>
        <br/>
        </table>
        </code></div>
        <h4>Examples:</h4>
        <!-- Show examples of function.-->
        Determine the correlation coefficient between the population and the area of the neighborhoods of Buenos Aires <br/> 
         expression_open_pg('corr(poblacion_,area)','division_administrativa.barrios')<br/>
        <span class="argument">previous result</span> 0.770081848773895<br/><br/>
        
        Determine the correlation coefficient between the population and the area of the BA Neighborhoods, but only of the communes
        specified in the list<br/>
        expression_open_pg('corr(poblacion_,area)','division_administrativa.barrios where comuna in (10,11,12,14,15)')<br/>
        <span class="argument">previous result</span> 0.961284749742084<br/><br/>
        
        Calculates the cumulative area of the neighborhoods grouped and sorted by communes.<br/>
        expression_open_pg('sum(st_area(barrios.geom))','division_administrativa.barrios group by comuna order by comuna')<br/>
        <span class="argument">previous result</span> [ 0.00170845112089074, 0.000603372178985122, 0.00062766099….] <br/><br/>
        
        Spatial query that determines the number of citizen service requests (suaci2021) that are contained in the neighborhoods
       that belong to the commune identified with the number 10<br/>
        expression_open_pg('count(*)','division_administrativa.barrios as a,"SUACI".suaci2021 as b where st_intersects(a.geom,b.geom) and a.comuna=10')<br/>
        <span class="argument">previous result</span> 32170<br/><br/>
        
        Previous query grouped and sorted by commune<br/>
         expression_open_pg('count(*)','division_administrativa.barrios as a,"SUACI".suaci2021 as b where st_intersects(a.geom,b.geom) group by a.comuna')<br/>
          <span class="argument">previous result</span> [ 19322, 21487, 19650, 21154, 17296, 26942, 30545, 11206, … ]
    """

correlation_pg_doc = """
       Returns the value(s) of the correlation coefficient (R2) between two numeric fields of a 
    <b>layer</b> of the postgreSQL database.<br/>
    The fields on which the calculation will be performed must be specified.
    Previously a connection to the database must be active.
    Optionally you can define a <b>filter</b>, a conditional expression<br/>.
    You can also specify an clause <span class="functionname">group</span>
    <b>optional</b> to aggregate the result by a field.<br/>
    If <span class="functionname">group</span> is applied the result will be returned in an array.<br/>
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">correlation_pg(</span>
    <span class="argument">schema, layer, field1, field2, filter, group<span class="functionname">)</span>
    </code></div><br/>
    The filter is optional, it is a conditional<br/>
     it must be written like this::<br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span>
     <p>If no filter is required, place <span class="functionname">''</span><</p>
     <p>The  clause<b><span class="functionname">group</span></b> is optional, simply type the field you want to group by</p>
    <p>If you do not require <b><span class="functionname">group</span></b> write <span class="functionname">''</span><</p>
     
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">schema</td><td>Name of the schema. String</td></tr>
        <tr><td class="argument">layer</td><td>Name of the layer. string</td></tr>
        <tr><td class="argument">field1</td><td>Name of the numeric field by which the correlation is to be calculated. string</td></tr>
        <tr><td class="argument">field2</td><td>Name of the numeric field to be compared with field1. string</td></tr>
        <tr><td class="argument">filter</td><td>Conditional to filter the query. string</td>
        <br/>
        <br/><b>The options are:</b>
        <br/>'' will not apply filter, it will query all entities of both layers.
        <br/><span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span> : conditional expression
        </tr>
        <tr><td class="argument">group</td><td>Name of the field you want to group by. string</td></tr>
        </table>
        </code></div>
        <h4>Examples:</h4>
        <!-- Show examples of function.-->
        Determine the correlation coefficient between the population and the area of the neighborhoods of Buenos Aires.<br/> 
         correlation_pg('division_administrativa','barrios','poblacion_','area','','')<br/>
        <span class="argument">previous result</span> 0.770081848773895<br/><br/>
        
        Determine the correlation coefficient between the population and the area of Buenos Aires neighborhoods grouped 
        by the commune field.<br/>
         correlation_pg('division_administrativa','barrios','poblacion_','area','','comuna')<br/>
        <span class="argument">previous result</span> [ 0.042736467333633, 0.961366222140714, 0.798900885165583,…,......]<br/><br/>
    """

total_statistics_pg_doc = """
        Returns the value or values of the requested statistic to a field in the postgreSQL database. 
    postgreSQL database.<br/>
    The field on which the calculation will be performed must be specified, 
    as well as the statistic of the available list.<br/>
    Previously a connection to the database must be active.
    Optionally you can define a <b>filter</b>, a conditional expression<br/>.
    You can also specify an clause <span class="functionname">group</span>
    <b>optional</b> to aggregate the result by a field.<br/>
    If <span class="functionname">group</span> is applied the result will be returned in an array.<br/>
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">total_statitics_pg(</span>
    <span class="argument">schema, layer, field, statistic, filter, group<span class="functionname">)</span>
    </code></div><br/>
    The filter is optional, it is a conditional<br/>
     it must be written like this:<br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span>
     <p>If no filter is required, place <span class="functionname">''</span></p>
     <p>The  clause<b><span class="functionname">group</span></b> is optional, simply type the field you want to group by</p>
    <p>If you do not require <b><span class="functionname">group</span></b> write <span class="functionname">''</span><</p>
     
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">schema</td><td>Name of the schema. String</td></tr>
        <tr><td class="argument">layer</td><td>Name of the layer. string</td></tr>
        <tr><td class="argument">field</td><td>Name of the numeric field by which the statistic will be calculated. string</td></tr>
        <tr><td class="argument">statitic</td><td>The statistic you want to calculate. string</td></tr>
        <br/><b>The options are:</b>
        <br/><b>sum</b>: returns the sum of the values of the field
        <br/><b>avg</b>: returns the average of field values
        <br/><b>max</b>: returns the maximum value of the values in the field
        <br/><b>min</b>: returns the minimum value of the values in the field
        <br/><b>count</b>: returns the count of all the records, or those that satisfy the filter
        <br/><b>stddev_pop</b>: returns the standard deviation of the population of the values in the field
        <br/><b>stddev_samp</b>: returns the sample standard deviation of the field values.
        <tr><td class="argument">filter</td><td>Conditional to filter the query. string</td>
        <br/>
        <br/><b>The options are:</b>
        <br/>'' will not apply filter, it will query all entities of both layers.
        <br/><span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span> : conditional expression
        </tr>
        <tr><td class="argument">group</td><td>Name of the field you want to group by. string</td></tr>
        </table>
        </code></div>
        <h4>Examples:</h4>
        <!-- Show examples of function.-->
        Determine the minimum population value of the population_ field of a postgis layer:<br/> 
        total_statitics_pg('division_administrativa','barrios','poblacion_','min','','')<br/>
        <span class="argument">previous result</span>  6726<br/><br/>
        
        Determine the minimum population value of the population_ field grouped by the commune field.<br/>
        total_statitics_pg('division_administrativa','barrios','poblacion_','min','','comuna')<br/>
        <span class="argument">previous result</span>  {6726, 40985, 14084, 176076, 47306, 44132, 51949, 157932,......]<br/><br/>
        
        Determine the minimum population value of the population_ field, but only for the neighborhoods of commune 15.<br/> 
         total_statitics_pg('division_administrativa','barrios','poblacion_','min','"comuna"=\\'15\\'','')<br/>
         <span class="argument">previous result</span>  13912<br/><br/>
    """

num_intersects_pg_doc = """
    Returns the number of entities of a postgis layer intersecting another 
    postgis layer of the same DB.<br/>
    Previously a connection to the database must be active.
    Optionally you can define a <b>filter</b>, a conditional expression<br/>.
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">num_intersects_pg(</span>
    <span class="argument">schema1, layer1, schema2, layer2, filter<span class="functionname">)</span>
    </code></div><br/>
    The filter is optional, it is a conditional<br/>
     it must be written like this:<br/><br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span>
     <p>If no filter is required, place <span class="functionname">''</span></p>
     
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">schema1</td><td>Name of the schema of layer1. string</td></tr>
        <tr><td class="argument">layer1</td><td>Name of the layer1. string</td></tr>
        <tr><td class="argument">schema2</td><td>Name of the schema of layer2. string</td></tr>
        <tr><td class="argument">layer2</td><td>Name of the layer2. string</td></tr>
        <tr><td class="argument">filter</td><td>Conditional to filter the query. string</td>
        <br/>
        <br/><b>The options are:</b>
        <br/>'' will not apply filter, it will query all entities of both layers.
        <br/><span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span> : conditional expression
        </tr>
        </table>
        </code></div>
        <h4>Examples:</h4>
        <!-- Show examples of function.-->
        Determine the number of entities of a postgis layer that intersect 
         all entities of another postgis layer.<br/> 
         num_intersects_pg('division_administrativa','barrios','public','parcelas','')<br/><br/>
         Determines the total number of entities of the postgis layer parcels that intersect the entities of the postgis layer neighborhoods               where the field neighborhood is equal to PALERMO.<br/>  
        num_intersects_pg('public','parcelas','division_administrativa','barrios','"barrio"=\\'PALERMO\\'')
    """

num_contains_pg_doc="""
    Returns the number of entities of the postgis <b>layer2</b> which are contained in 
    the postgis <b>layer1</b> <br/>
    Previously a connection to the database must be active.
    Optionally you can define a <b>filter</b>, a conditional expression<br/>.
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">num_contains_pg(</span>
    <span class="argument">schema1, layer1, schema2, layer2, filter, feature, parent<span class="functionname">)</span>
    </code></div><br/>
    The filter is optional, it is a conditional<br/>
     it must be written like this:<br/><br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span>
     <p>If no filter is required, place <span class="functionname">''</span></p>
     
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">schema1</td><td>Name of the schema of layer1. string</td></tr>
        <tr><td class="argument">layer1</td><td>Name of the layer1. String</td></tr>
        <tr><td class="argument">schema2</td><td>Name of the schema of layer2. string</td></tr>
        <tr><td class="argument">layer2</td><td>Name of the layer1. String</td></tr>
        <tr><td class="argument">filter</td><td>Conditional to filter the query. string</td>
        <br/>
        <br/><b>The options are:</b>
        <br/>'' will not apply filter, it will query all entities of both layers.
        <br/><span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span> : conditional expression
        </tr>
        </table>
        </code></div>
        <h4>Examples:</h4>
        <!-- Show examples of function.-->
        Determine the number of entities of a postgis layer contained in another postgis layer.  in another postgis layer<br/>
        In the example we determine the number of points of the Citizen Attention Service (suaci2021) of the City of 
        the City of Buenos Aires(BA) that are contained in the Neighborhoods of BA<br/><br/>
         num_contains_pg(5432,'CABA','localhost','postgres','12345678','division_administrativa','barrios','SUACI','suaci2021','')<br/> 
        A filter is applied and the suaci2021 points contained in the PALERMO neighborhood are evaluated.<br/>  
        num_contains_pg(5432,'CABA','localhost','postgres','12345678','public','parcelas','SUACI','suaci2021','"barrios"."barrio"=\\'PALERMO\\'')
"""

num_within_pg_doc="""
    Returns the number of entities of the postgis <b>layer1</b> that are contained in the postgis <b>layer2</b><br/>
    Previously a connection to the database must be active.
    Optionally you can define a <b>filter</b>, a conditional expression<br/>.
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">num_within_pg(</span>
    <span class="argument">schema1, layer1, schema2, layer2, filter<span class="functionname">)</span>
    </code></div><br/>
    The filter is optional, it is a conditional<br/>
     it must be written like this:<br/><br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span>
     <p>If no filter is required, place <span class="functionname">''</span></p>
     
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">schema1</td><td>Name of the schema of layer1. string</td></tr>
        <tr><td class="argument">layer1</td><td>Name of the layer1. String</td></tr>
        <tr><td class="argument">schema2</td><td>Name of the schema of layer2. string</td></tr>
        <tr><td class="argument">layer2</td><td>Name of the layer1. String</td></tr>
        <tr><td class="argument">filter</td><td>Conditional to filter the query. string</td>
        <br/>
        <br/><b>The options are:</b>
        <br/>'' will not apply filter, it will query all entities of both layers.
        <br/><span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span> : conditional expression
        </tr>
        </tr>
        </table>
        </code></div>
        <h4>Examples:</h4>
        <!-- Show examples of function.-->
        Determine the number of entities of a postgis layer within the entities of another postgis layer. <br/>
      The example shows the number of points of the Citizen Attention Service of the City of Buenos Aires (suaci2021) 
      that are contained in the of the City of Buenos Aires (BA)<br/>
         num_within_pg('SUACI','suaci2021','division_administrativa','barrios','')<br/><br/>
         A filter is applied and the suaci2021 points contained in the PALERMO neighborhood are evaluated.<br/>   
        num_within_pg('SUACI','suaci2021','division_administrativa','barrios','"barrios"."barrio"=\'PALERMO\'')
"""

num_buffer_intersects_pg_doc="""
     Returns the number of entities of the postgis <b>layer1</b> that intersect 
    the area of influence of the entities in the postgis <b>layer2</b><br/>
    The distance in projection units of the layers must be specified.<br/>
     Previously a connection to the database must be active.
    Optionally you can define a <b>filter</b>, a conditional expression<br/>.
    <h4>Sintaxis</h4>
    <div class="syntax"><code>
    <span class="functionname">num_buffer_intersects_pg(</span>
    <span class="argument">schema1, layer1, schema2, layer2, distance, filter<span class="functionname">)</span>
    </code></div><br/>
    The filter is optional, it is a conditional<br/>
     it must be written like this:<br/><br/>
     <span class="functionname">'"barrios"."barrio"=\\'PALERMO\\''</span><br/>
     <span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span>
     <p>If no filter is required, place <span class="functionname">''</span></p>
     
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">schema1</td><td>Name of the schema of layer1. string</td></tr>
        <tr><td class="argument">layer1</td><td>Name of the layer1. String</td></tr>
        <tr><td class="argument">schema2</td><td>Name of the schema of layer2. string</td></tr>
        <tr><td class="argument">layer2</td><td>Name of the layer1. String</td></tr>
        <tr><td class="argument">distance</td><td>Distance to consider for the buffer. Text (string) or number</td></tr>
        <tr><td class="argument">filter</td><td>Conditional to filter the query. string</td>
        <br/>
        <br/><b>The options are:</b>
        <br/>'' will not apply filter, it will query all entities of both layers.
        <br/><span class="functionname">'"layer"."field" operator \\'value of attribute\\''</span> : conditional expression
        </tr>
        </table>
        </code></div>
        <h4>Examples:</h4>
        <!-- Show examples of function.-->
        Determine the number of points in the suaci2021 layer intersecting the area 
        of influence (distance 0.001 degrees) of the streets of type STREET.<br/>
         num_buffer_intersects_pg('public','parcelas','public','calles',0.001,'"calles"."tipo_c"=\'CALLE\'')<br/><br/>
         The same analysis for a specific street, identified with the id=10<br/>
          num_buffer_intersects_pg('public','parcelas','public','calles',0.001,'"calles"."id"=\'10\'')<br/><br/>
         Determines the total number of census radius intersecting the area of influence of the PALERMO<br/>  
        num_buffer_intersects_pg('division_administrativa','radios_censales','division_administrativa','barrios',0.001,
        '"barrios"."barrio"=\\'PALERMO\\'')<br/>
"""
