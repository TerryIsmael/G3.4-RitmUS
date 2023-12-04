//este es un comentario
//otro cambio  adsf
//validaciones con jquery validate
$.validator.addMethod("terminaCon", function(value, element, parametro) {
    //value-> lo que escribio el usuario en la caja
    //element -> el elemento html
    //parametro -> lo que se le entrega para validar -> duoc.cl

    //true|false

    if(value.endsWith(parametro)) {
        return true;
    }

    return false;
//{0} siempre pasa el parametro recibido por la funcion
}, "Debe terminar con {0}")


$("#formulario_contacto").validate({
    rules:{
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 50
        },
        email: {
            required: true,
            email: true,
            terminaCon: "alumnos.duoc.cl"
            //@duoc.cl
            //number: true
            //min: 3
            //max: 5000
        },
        tipo_solicitud: {
            required: true
        },
        mensaje: {
            required: true,
            minlength: 5,
            maxlength: 200
        }
    },
    messages: {
        nombre: {
            required: "Este campo es requerido",
            minlength: "minimo debe tener 3 caracteres"
        }
    }
})






function cargarTablaContactos() {
    //conectarse con la api, rescatar los registros, crear el html necesario
    //tr -> td -> datos -> pasarle el html creado a la tabla
    let url = "https://api.control-z.cl/api/contacto"

    $.get(url, function(respuesta) {
        

        let htmlTabla = `
           <tr>
            <th>Nombre</th>
            <th>Email</th>
           </tr>
        `

        respuesta.forEach(function(item) {

            htmlTabla += `
                <tr>
                    <td>${item.nombre}</td>
                    <td>${item.email}</td>
                </tr>
            `
        })

        //pasarle el html a la tabla <table>

        $("#tabla_contactos").html(htmlTabla)


    }, "json")

}

cargarTablaContactos()



//let guardar = document.getElementById("guardar")
//addEventListener('click', func)
$("#guardar").click(function() {

    //verificar si todo es valido

    if(!$("#formulario_contacto").valid()) {
        return;
    }


    //console.log("boton pinchado")
    let nombre = $("#nombre").val()
    let email = $("#email").val()
    let tipoSolicitud = $("#tipo_solicitud").val()
    let mensaje = $("#mensaje").val()
    let avisos = $("#avisos").is(":checked")

    //console.log(nombre)???

    let url = "https://api.control-z.cl/api/contacto"


    let data = {
        nombre: nombre,
        email: email,
        tipo_solicitud: tipoSolicitud,
        mensaje: mensaje,
        avisos: avisos?1:0
    }

    $.post(url, data, function(respuesta) {
        console.log(respuesta)
        cargarTablaContactos()
        Swal.fire({
            title: "Felicitaciones",
            text: "Tu mensaje ha sido enviado, te estaremos llamando ;)",
            icon: "success"//error, warning, info y question
        })

    }, "json")
    .fail(function() {
        Swal.fire({
            title: "Ups!",
            text: "Ha ocurrido un error FATAL",
            icon: "error",
            toast: true,
            position: 'top-right',
            timer: 2000,
            timerProgressBar: true
        })
    })

})

