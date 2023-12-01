

let url = "https://api.control-z.cl/api/feriados"
//let url = "https://mindicador.cl/api"
//ajax
fetch(url)
    .then(function(respuesta) {
        return respuesta.json()
    })
    .then(function(respuesta) {
        /*console.log(respuesta)
        respuesta.forEach(function(feriado) {
            console.log(feriado.nombre)
        })*/

        console.log(respuesta[0].nombre + " " + respuesta[0].fecha)
        let enlaceFeriado = document.getElementById("feriado")

        enlaceFeriado.innerText = respuesta[0].nombre
        //console.log(respuesta.uf.valor)

    })



