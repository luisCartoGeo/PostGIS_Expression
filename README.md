# PostGIS_Expression
<table align="center">
    <p align = "center">
      <a href="https://www.linkedin.com/in/luisedpg/"><img alt="LuisGeo" src="https://img.shields.io/badge/AUTOR-Luis%20Eduardo%20Perez%20Graterol-brightgreen"></a>
       <a href="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/readme_en.md"><img alt="LuisGeo" src="https://img.shields.io/badge/ENGLISH-Documentation-lightgrey"></a>
        <a href="https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FluisCartoGeo%2FQGIS_Dashboard%2F"><img alt="Twitter" src="https://img.shields.io/twitter/url?label=TWITTER&style=social&url=https%3A%2F%2Ftwitter.com%2FLuiseperezg"></a>
      </P>
</table>
<img style="text-align:center" src="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/MINI-POSTGIS-EXPRESION.jpg" style="width:10%">
<h2><b>Repositorio del código del complemento para agregar y activar Expresiones PostGIS en QGIS</b></h2><br>

## Indice
- [Introducción](#Introducción)
- [Instalación](#Instalación)

### Introducción

El inicio y desarrollo de <B>QGIS</B> ha estado vinculado con una gran diversidad de tecnologías libres, especialmente <B>PostgreSQL</B>.<BR/><BR/>
<B>PostgreSQL</B> es un sistema de base de datos relacional de código abierto, solida, con más de 30 años de desarrollo, su desempeño iguala y supera 
en algunos casos a sus homólogos comerciales. <B>PostGIS</B> es su poderosa extensión para permitir el manejo de datos espaciales, raster y vectoriales.<BR/>
Si bien, QGIS es una potente y completa aplicación GIS, ciertos temas especializados se apoya en el desarrollo de complementos o en otras tecnologías 
_Open Source_, por ejemplo, para el procesamiento de datos raster cuenta con la integración con _SAGA_ y _Grass_. 
De manera similar QGIS es un cliente ideal y ampliamente utilizado para <i>PostgreSQL-PostGIS</i>.<BR/>
Sin embargo, los usuarios que implementan la solución <b>QGIS/PostGIS</b> manifiestan su interés en una mayor integración, desean contar con la potencia 
del motor de PostGIS dentro de los procesos rutinarios de QGIS.<BR/><BR/>
El complemento <B>PostGIS Expression</B> es una propuesta para lograr esa mayor integración, al brindar expresiones que se ejecutan e implementan el motor de <i>PostgreSQL-PostGIS</i>.

### Instalación

<ul>
<li><b>Procedimiento de instalación:</b> descarga el complemento de este repositorio, luego en QGIS procede a instalarlo utilizando la opción, menú <i>Complementos, 
 > Administrar e instalar complementos > Instalar a partir de ZIP</i>.<br/>
Próximamente estará disponible a través del repositorio de QGIS.<br/></li>
<li><b>Requerimientos:</b> este complemento <b>no</b> requiere bibliotecas adicionales, simplemente instálalo y podrás utilizarlo.<br/>
    Esta <i>específicamente</i> diseñado para consultar Bases de Datos PostgreSQL.<br/>
Las expresiones que realizan consultas espaciales asumen que la extensión PostGIS esta implementada en la Base de Datos.<br/>
Las expresiones que realizan consultas espaciales asumen que el campo con la geometría es <i>geom</i>.<br/></li>
</ul>
<hr></hr>
<h3>Funcionamiento del complemento</h3>
<h4><b>Integridad y seguridad</b></h4>
En esta versión del complemento, solo puede conectarse a una base de datos a la vez, si desea conectarse a otra base de datos debera establecer una nueva conexión lo que removera previas conexiones.<br/>
Como medida de seguridad la conexión a la Base de Datos es de <strong>Solo Lectura</strong>, puede realizar consultas pero no podra modificar la Base de Datos aunque escriba las sentencias para ello.<br/>
<h4><b>Interfaz de usuario</b></h4>
Al activar el complemento se añaden dos botones a la barra de botones, uno para conectar a la base de datos y otro para desconectar.<br/>
Estas herramientas también están disponibles en el menú <i>Complemento</i> > submenú <i>PostGIS Expression</i>.<br/>
<img style="text-align:center" src="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/botones.jpg">
De igual forma si despliega el dialogo de expresiones, notara que se ha agregado la categoría PostGIS con un conjunto de expresiones.<br/>
<img style="text-align:center" src="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/Dialog_expre_postgis.jpg" style="width:10%">
<h4><b>Establecer conexión con la Base de Datos</b></h4>
El primer paso para utilizar las expresiones es establecer conexión con la Base de Datos que desea consultar.<br/> 
Haga clic sobre el botón <i>Nueva conexión</i>, aparecerá una ventana donde podrá introducir los parámetros básicos para establecer la conexión con su Base de Datos:<br/> 
<ol>
    <li><b>Puerto:</b> se coloca por defecto el puerto utilizado por PostgreSQL  (5432) edite este valor si lo requiere.</li>
    <li><b>Nombre de la base de datos:</b> coloque el nombre de la base de datos PostgreSQL con la que desea realizar la instalación.</li>
    <li><b>Usuario:</b> edite el texto y coloque el nombre del usuario.</li>
    <li><b>Contraseña:</b> coloque la contraseña para acceder a la base de datos.</li>
    <li><b>Servidor:</b> coloque el nombre del servidor.</li>
</ol>
<img style="text-align:center" src="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/DIALOGO.jpg" style="width:10%">
Luego de introducir los parámetros requeridos para establecer la conexión pulse el botón <i>Establecer conexión</i>, la ventana mostrara un mensaje si la conexión ha sido exitosa, como se muestra en la imagen, o devolverá un mensaje de error si no puede establecerse la conexión.<br/>
<h4><b>Expresiones</b></h4>
Las expresiones PostGIS permiten hacer consultas alfanuméricas y espaciales, sin embargo, por el momento, el resultado que obtendrá serán valores numéricos o booleanos. Puede obtener como resultado un valor único de una consulta o una lista de valores.<br/>
<ul>
    <li><b>¿Cómo acceder a las expresiones?</b><br/>
Para utilizar las expresiones, despliegue cualquier dialogo de expresiones, por ejemplo con la herramienta <i>seleccionar por atributos</i> o la <i>calculadora de campos</i>.</li><br/>
    <li><b>¿Cómo utilizar las expresiones?</b><br/>
    Al igual que las expresiones propias de QGIS, cada expresión PostGIS cuenta con una ayuda detallada que se muestra al seleccionarla en el Dialogo de Expresiones, incluyendo la sintaxis, parametros de entrada y ejemplos de uso.</li><br/>
    </ul><img style="text-align:center" src="https://github.com/luisCartoGeo/PostGIS_Expression/blob/main/ayuda.jpg" style="width:10%">





