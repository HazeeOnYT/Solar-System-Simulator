function drawPlanet() {
    var planetName = document.getElementById("planetInput").value;
    fetch(`/draw_planet?name=${planetName}`);
}

function spinPlanet() {
    fetch('/spin_planet');
}

function solarSystemPreview() {
    fetch('/solar_system_preview');
}
