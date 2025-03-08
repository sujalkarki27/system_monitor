function fetchSystemStats() {
    fetch('/system')
        .then(response => response.json())
        .then(data => {
            document.getElementById("cpu").textContent = data.cpu;
            document.getElementById("ram").textContent = data.ram;
            document.getElementById("disk").textContent = data.disk;
        })
        .catch(error => console.error("Error fetching data:", error));
}

setInterval(fetchSystemStats, 1000);
