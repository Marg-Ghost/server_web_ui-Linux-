////////////////////////////////////////////////
//Server
/////////////////////////////////////////////////
async function dashboard() {
    const timeElement = document.getElementById("Time");
    const cpuTempElement = document.getElementById("cpu_temp");
    const cpuLoadElement = document.getElementById("cpu_load");
    const diskFreeElement = document.getElementById("disk_free");
    const ramInfoElement = document.getElementById("ram_free");

    // Dummy-Inhalt definieren, da 'content' im Ursprungscode nicht deklariert war
    let currentContent = "Dashboard-Anfrage"; 

    try {
        const response = await fetch('/dashboard', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                data_type: "text",
                content: currentContent
            })
        });
        
        const data = await response.json();
        
        // Daten punktgenau über die Schlüssel ins HTML eintragen
        if(timeElement) timeElement.textContent = "Time: " + data.time;
        if(cpuTempElement) cpuTempElement.textContent = "CPU Temp: " + data.cpu_temp;
        if(cpuLoadElement) cpuLoadElement.textContent = "CPU Load: " + data.cpu_load;
        if(diskFreeElement) diskFreeElement.textContent = "Disk Free: " + data.disk_free;
        if(ramInfoElement) ramInfoElement.textContent = "RAM Info: " + data.ram_info;

    } catch (err) {
        console.error("Refresh Error:", err);
    }
}

// Durchgehende Aktualisierung jede Sekunde (1000ms) oder alle 2 Sekunden (2000ms)
setInterval(dashboard, 2000);

// Direkt beim ersten Laden einmal ausführen
dashboard();