const list = document.querySelector(".container-clima");
const apiKey = "2a74415905ee49c833cae5377e30ba18";
const inputVal = "Paraná, ar";
  
const url = `https://api.openweathermap.org/data/2.5/weather?q=${inputVal}&appid=${apiKey}&units=metric`;

fetch(url)
.then(response => response.json())
.then(data => {
  console.log(data);
  const { main, name, sys, weather } = data;
  const icon = `https://openweathermap.org/img/wn/${
    weather[0]["icon"]
  }@2x.png`;
  
  let descripcion = weather[0]["description"];

  const div = document.createElement("div");
  div.classList.add("ciudad");
  const cuadro = `
    <fieldset>
    <CENTER>
    <h3 class="nombre-ciudad">
      <span>${name}</span>
      <sup>${sys.country}</sup>
    </h3>
    <div class="temp">${Math.round(main.temp)}<sup>°C</sup></div>
    <figure>
      <img class="icono-tiempo" src="${icon}" alt="${descripcion}">
    </figure>
    <span class="condi">${descripcion}</span>
    <a class="credito" href="https://openweathermap.org/" title="Versión de uso gratuito">
      <i class="fa-solid fa-circle-info"></i>
       OpenWeather 
    </a>
    </CENTER>
    </fieldset>
  `;
  div.innerHTML = cuadro;
  list.appendChild(div);
});