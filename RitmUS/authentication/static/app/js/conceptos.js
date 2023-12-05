
//alert("este es un mensaje")

//nombre = "elias"
let nombre = "elias"
let edad = 20

if(edad >= 18 && edad <= 64) {
    console.log("mayor de edad")
} else if(edad <= 0 || edad >= 120) {
    console.log("edad incorrecta")
} else if(edad >= 65) {
    console.log("adulto mayor")
} else {
    console.log("menor de edad")
}

let i = 0

while(i < 10) {
    console.log("while: " + i)
    i++
}

for(let i=0; i < 5; i++) {
    console.log("for: " + i)
}

let nombres = ["rodrigo", "matias", "juan"]

console.log(nombres[0])

nombres.forEach(function(item) {
    console.log(item)
})

nombres.forEach((item)=>{
    console.log(item)
})

//JSON

let persona = {
    nombre: "adrian",
    edad: 30,
    estatura: 1.8
}

console.log(persona.nombre)


let estatura = "2"

if(estatura === 2) {
    console.log("ingresa")
}



