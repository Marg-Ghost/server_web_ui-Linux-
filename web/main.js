////////////////////////////////////////////////
// Server-health
/////////////////////////////////////////////////
async function dashboard() {
    try {
        const response = await fetch('/dashboard');
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();

        document.getElementById('disk_free').textContent = `${data.disk.free} / ${data.disk.total} GiB`;
        document.getElementById('drive_slider').style.width = `${100 - data.disk.used_percent}%`;
        document.getElementById('c_time').textContent = data.timedate.time;
        document.getElementById('c_date').textContent = data.timedate.date;
        document.getElementById('eth').textContent = `${data.network.ethernet.name}: ${data.network.ethernet.status}`;
        document.getElementById('wlan').textContent = `${data.network.wifi.name}: ${data.network.wifi.status}`;
        data.cores.forEach((value, index) => {
            const core = document.getElementById(`core${index + 1}`);
            core.textContent = `${value.toFixed(1)}%`;
            core.style.setProperty('--load', `${value}%`);
        });
        document.getElementById('temp_number').textContent = `${data.cpu_temp.toFixed(1)} °C`;
        document.getElementById('ram_size').textContent = `${data.ram.used} / ${data.ram.total} GiB`;
        document.getElementById('ram_ring').style.setProperty('--ram-load', `${data.ram.used_percent}%`);
    } catch (err) {
        console.error("Refresh Error:", err);
    }
}

setInterval(dashboard, 2000);
dashboard();

