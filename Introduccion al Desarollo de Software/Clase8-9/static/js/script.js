const alerta = document.getElementsByClassName("alerta")

alerta.onclick = function (event) {
    alert(alerta.innerHTML)
}

function randomNumber() {
    return (Math.random() * 256).toFixed(0)
}
