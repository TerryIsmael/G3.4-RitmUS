let guardar = document.getElementById("guardar")


guardar.addEventListener("click", function(){
    console.log("boton pinchado")
    let nombre = document.getElementById("nombre").value
    let avisos = document.getElementById("avisos").checked
    console.log(nombre)
    console.log(avisos)
})