const alerta = document.getElementsByClassName("alerta");
const boton = document.querySelector(".boton");

boton.onclick = function () {
    let texto = "";
    for (let i = 0; i < alerta.length; i++) {
        texto += alerta[i].textContent + " ";
    }
    alert(texto.trim());
};
