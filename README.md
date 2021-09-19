# PostGIS_Expression
<table align="center">
    <p align = "center">
      <a href="https://www.linkedin.com/in/luisedpg/"><img alt="LuisGeo" src="https://img.shields.io/badge/AUTOR-Luis%20Eduardo%20Perez%20Graterol-brightgreen"></a>
       <a href="https://github.com/luisCartoGeo/QGIS_Dashboard/tree/master/"><img alt="LuisGeo" src="https://img.shields.io/badge/ENGLISH-Documentation-lightgrey"></a>
        <a href="https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FluisCartoGeo%2FQGIS_Dashboard%2F"><img alt="Twitter" src="https://img.shields.io/twitter/url?label=TWITTER&style=social&url=https%3A%2F%2Ftwitter.com%2FLuiseperezg"></a>
      </P>
</table>
<h2><b>Repositorio del código del complemento para agregar y activar Expresiones PostGIS en QGIS</b></h2><br>
<h3>Introducción</h3>

El inicio y desarrollo de <B>QGIS</B> ha estado vinculado con una gran diversidad de tecnologías libres, especialmente <B>PostgreSQL</B>.<BR/><BR/>
<B>PostgreSQL</B> es un sistema de base de datos relacional de código abierto, solida, con más de 30 años de desarrollo, su desempeño iguala y supera 
en algunos casos a sus homólogos comerciales. <B>PostGIS</B> es su poderosa extensión para permitir el manejo de datos espaciales, raster y vectoriales.<BR/>
Si bien, QGIS es una potente y completa aplicación GIS, ciertos temas especializados se apoya en el desarrollo de complementos o en otras tecnologías 
Open Source, por ejemplo, para el procesamiento de datos raster cuenta con la integración con SAGA y Grass. 
De manera similar QGIS es un cliente ideal y ampliamente utilizado para PostgreSQL-PostGIS.<BR/>
Sin embargo, los usuarios que implementan la solución <b>QGIS/PostGIS</b> manifiestan su interés en una mayor integración, desean contar con la potencia 
del motor de PostGIS dentro de los procesos rutinarios de QGIS.<BR/><BR/>
El complemento <B>PostGIS Expression</B> es una propuesta para lograr esa mayor integración, al brindar expresiones que se ejecutan e implementan el motor de PostgreSQL-PostGIS.
<hr></hr>
<h3>Instalación</h3>
<ul>
<li><b>Procedimiento de instalación:</b> descarga el complemento de este repositorio, luego en QGIS procede a instalarlo utilizando la opción, menú complementos 
> administrar e instalar complementos > Instalar a partir de ZIP.<br/>
Próximamente estará disponible a través del repositorio de QGIS.<br/></li>
<li><b>Requerimientos:</b> este complemento <b>no</b> requiere instalaciones adicionales, simplemente instálalo y podrás utilizarlo.<br/>
Esta específicamente diseñado para consultar Bases de Datos PostgreSQL.<br/>
Las expresiones que realizan consultas espaciales asumen que la extensión PostGIS esta implementada en la Base de Datos.<br/>
Las expresiones que realizan consultas espaciales asumen que el campo con la geometría es geom.<br/></li>
</ul>
<hr></hr>
<h3>Funcionamiento del complemento</h3>



Agrega nuevas expresiones al Dialogo de Expresiones de QGIS con funciones para realizar consultas a Base de Datos PostGIS utilizando el motor de PostGIS. 
