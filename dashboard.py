import datetime
import shutil

class Dashboard:
    def __init__(self):
        # self.date = self.time_get()
        # self.system_status = self.get_system_stats()
        pass

    def get_all_data(self) -> dict:
        # Kombiniert Zeit und Hardware in ein einziges JSON-Objekt
        return {
            "time": self.time_get(),
            **self.get_system_stats()
        }

    def time_get(self) -> str:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return time
    
    def get_system_stats(self) -> dict:
        stats = {
            "cpu_temp": "N/A",
            "cpu_load": "N/A",
            "disk_free": "N/A",
            "ram_info": "N/A"
        }

        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                stats["cpu_temp"] = f"{float(f.read()) / 1000.0:.1f} °C"
        except: pass

        try:
            with open("/proc/loadavg", "r") as f:
                stats["cpu_load"] = f.read().split()[0]
        except: pass

        try:
            _, _, free = shutil.disk_usage("/")
            stats["disk_free"] = f"{free / (1024**3):.1f} GB"
        except: pass

        try:
            with open("/proc/meminfo", "r") as f:
                lines = f.readlines()
                total = int(lines[0].split()[1])
                free = int(lines[1].split()[1])
                used_pct = ((total - free) / total) * 100
                stats["ram_info"] = f"{used_pct:.1f} %"
        except: pass

        return stats
