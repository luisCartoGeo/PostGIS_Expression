# PostGIS_Expression
<table align="center">
    <p align = "center">
      <a href="https://www.linkedin.com/in/luisedpg/"><img alt="LuisGeo" src="https://img.shields.io/badge/AUTOR-Luis%20Eduardo%20Perez%20Graterol-brightgreen"></a>
        <a href="https://twitter.com/Luiseperezg"><img alt="Twitter" src="https://img.shields.io/twitter/url?label=TWITTER&style=social&url=https%3A%2F%2Ftwitter.com%2FLuiseperezg"></a>
      </P>
</table>
<img style="text-align:center" src="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/MINI-POSTGIS-EXPRESION.jpg" style="width:10%">
<h2><b>Plugin code repository for adding and activating PostGIS Expressions in QGIS</b></h2><br>
<h3>Introducción</h3>

The inception and development of <B>QGIS</B> has been linked to a great diversity of free technologies, especially <B>PostgreSQL</B>.<BR/><BR/>
<B>PostgreSQL</B> is an open source, robust, relational database system with over 30 years of development, its performance matches and in some cases surpasses its commercial counterparts. <B>PostGIS</B> is its powerful extension to enable the handling of spatial, raster and vector data.<BR/>
Although QGIS is a powerful and complete GIS application, certain specialized topics are supported by the development of plugins or other _Open Source_ technologies, for example, for raster data processing it has the integration with _SAGA_ and _Grass_.<br/> 
Similarly QGIS is an ideal and widely used client for <i>PostgreSQL-PostGIS</i>.<br/>
However, users implementing the <b>QGIS/PostGIS</b> solution express interest in further integration, they want the power of the PostGIS engine within routine QGIS processes.<BR/><BR/>
The <B>PostGIS Expression</B> plugin is a proposal to achieve this deeper integration by providing expressions that execute and implement the <i>PostgreSQL-PostGIS</i> engine.
<hr></hr>
<h3>Installation</h3>
<ul>
<li><b>Installation procedure:</b> download the plugin from this repository, then in QGIS proceed to install it using the option, menu <i>Plugins > Manage and install plugins > Install from ZIP</i>.<br/>.
It will soon be available through the QGIS repository.<br/></li>
<li><b>Requirements:</b> this add-on <b>does not</b> require additional libraries, just install it and you will be able to use it.<br/>
    It is <i>specifically</i> designed to query PostgreSQL databases.<br/>
Expressions that perform spatial queries assume that the PostGIS extension is implemented in the database.<br/>
Expressions that perform spatial queries assume that the field with the geometry is <i>geom</i>.<br/>
</ul>
<hr></hr>
<h3>Plugin functionality</h3>
<h4><b>Integrity and security</b></h4>
In this version of the plugin, you can only connect to one database at a time, if you want to connect to another database you will have to establish a new connection which will remove previous connections.<br/>
As a security measure the connection to the database is Read Only, you can make queries but you will not be able to modify the database even if you write the statements for it.<br/>
<h4><b>User interface</b></h4>
When the plugin is activated, two buttons are added to the button bar, one to connect to the database and one to disconnect.<br/>
These tools are also available in the menu <i>Complement</i> > submenu <i>PostGIS Expression.</i><br/>
<img style="text-align:center" src="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/botones.jpg">
Likewise, if you display the expressions dialog, you will notice that the PostGIS category has been added with a set of expressions.<br/>
<img style="text-align:center" src="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/Dialog_expre_postgis.jpg" style="width:10%">
<h4><b>Establish connection to the Database</b></h4>
The first step to use the expressions is to establish a connection with the database you want to query.<br/>
Click on the <i>New Connection</i> button, a window will appear where you can enter the basic parameters to establish the connection with your Database:<br/> 
<ol>
    <li><b>Port:</b> the default port used by PostgreSQL (5432) is set by default, edit this value if required.</li>
    <li><b>Database name:</b> enter the name of the PostgreSQL database you want to connect to.</li>
    <li><b>User:</b> edit the text and enter the user's name.</li>
    <li><b>Password:</b> enter the password to access the database.</li>
    <li><b>Host:</b> enter the name of the host.</li>
</ol>
<img style="text-align:center" src="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/DIALOGO.jpg" style="width:10%">
After entering the required parameters to establish the connection click the <i>Establish Connection</i> button, the window will display a message if the connection has been successful, as shown in the image, or will return an error message if the connection cannot be established.<br/>
<h4><b>Expressions</b></h4>
PostGIS expressions allow alphanumeric and spatial queries, however, for the moment, the result you will get will be numeric or Boolean values. You can get as a result a single value from a query or a list of values.<br/>
<ul>
    <li><b>How to access the expressions?</b><br/>
To use expressions, display any expression dialog, for example with the <i>select by attributes</i> tool or the <i>field calculator</i>.</li><br/>
    <li><b>How to use the expressions?</b><br/>
    Like QGIS's own expressions, each PostGIS expression has a detailed help that is displayed when you select it in the Expressions Dialog, including syntax, input parameters and usage examples.</li><br/>
    </ul><img style="text-align:center" src="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/ayuda.jpg" style="width:10%">
