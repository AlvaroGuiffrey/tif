# tif
Codo a Codo - Trabajo Integrador Final - Comisión 23030 - Grupo 10

INTEGRACION DE DJANGO BACKEND

Realizamos la integración en Django del FrontEnd del TPO - Proyecto: "Alma Bichera" - Tienda de mascotas; teniendo en cuenta las observaciones realizadas en la devolución del Profesor.

Nota: en cuanto a los colores y las imágenes utilizadas corresponden a las del emprendimiento. Por ahi no son los colores más atractivos pero son los que las propietarias utilizan, al igual que el logo y las fotos no tienen la calidad deseada pero son los que utilizan en las redes sociales. 

Consta de cuatro páginas que observan el concepto de diseño web responsivo: Inicio (Landing Page), Productos, Conocenos y Contacto.

Mantiene el mismo header, nav y footer en todas las páginas, con las siguientes particularidades:
1) Header: la banda azul, en la parte superior derecha, donde se muestra el cambio de los domicilios de los locales, cuando estamos utilizando un dispositivo de pantalla pequeña o reducimos el tamaño del navegador, solo se muestra ek teléfono de contacto;
2) Nav: cuando estamos utilizando un dispositivo de pantalla pequeña o reducimos el tamaño del navegador, se muestra a la derecha el ícono de "Menú hanburguesa"; y
3) Footer: los íconos nos conectan a las redes sociales de "Alma Bichera".

PAGINA DE INICIO:
Tiene dos sectores bien destacados, la sección principal con un banner para suscribirse a una "PROMO" y un carrousel con fotos de mascotas amigas; a la derecha un aside que en la parte superior ofrece datos del "CLIMA" en Paraná, Entre Ríos consumidos desde la api de "OpenWeather" versión gratuita y más abajo opiniones de clientes que las tomamos de un json (experiencias.json) ubicado en la carpeta Static/DB.  
Haciendo clik en el botón "REGISTRATE" del banner de la promo, nos muestra un formulario del tipo "modal" que nos permite ingresar los datos, los que son validados con JS y los mismos persisten en SheetDB (https://sheetdb.io/api/v1/mnulmpy28bm64).

PAGINA PRODUCTOS:
Tiene una sección principal, donde podemos ver los productos (alimentos para mascotas) que se ofrecen. En la parte superior de cada producto se muestra una etiqueta si el mismo es de la línea "premiun" o "económica" y se coloca una transparencia con un mensaje si no tuviera stock disponible. 
Los datos los consumimos de un json (productos.json) ubicado en la carpeta Static/DB.

PAGINA CONOCENOS:
Tiene tres secciones bien definidas: la primera (superior) es una reseña del emprendimiento; la segunda contiene la info de las propietarias, donde se observa el boton "Contacto" que al clicker nos muestra la info y modifica su contenido para ocultar la información si hacemos clik nuevamente, si pasamos el mouse sobre el QR de WS este cambia su dimención para poder realizar un correcto escaneo en caso pantallas pequeñas; y en la última parte muestra las fotos y un mapa de la ubicación de los locales en un iframe, la info se obtiene de Google Maps.

PAGINA CONTACTO:
En el sector izquierdo hay un formulario para enviar un mail y a la derecha otros medios para contactarse, incluso repite un mapa del local principal donde desarrollan la actividad. Para el envío utilizamos el servicio gratuito de FORMSUBMIT 



