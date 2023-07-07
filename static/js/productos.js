import { Producto } from "./models/Producto.js";
//import productos from "/static/db/productos.json" assert { type: "json" };;

import { parent } from "./config/configProd.js";

/* PRODUCTOS */
const printDatos = (datos, parent) => {
    datos.forEach((produ) => produ.getCardProducto(parent));
};

const cargarDatos = (productos) => {
    let datosObjeto = productos.map(
        (produ) => new Producto(
            produ.nombre, 
            produ.marca, 
            produ.precio,
            produ.stock,
            produ.presentacion, 
            produ.comentario,
            produ.imagen,
            produ.linea
            ),
    );
    
    return datosObjeto;
}

//let datos = cargarDatos();
//printDatos(datos, parent);
let URL = "/static/db/productos.json";
fetch(URL).then(d => d.json()).then(data => {
    let datos = cargarDatos(data);
    printDatos(datos, parent);
});
