import datetime
import psutil

class Dashboard:

    def __init__(self):
        self.usr, self.fastf = self.get_fastfetch()

    def get_all_data(self) -> dict:
        return {
            "usr": self.usr,
            "fastf": self.fastf,
            "disk": self.get_drive(),
            "timedate": self.get_time(),
            "network": self.get_network(),
            "cores": self.get_core(),
            "cpu_temp": self.get_cpu_frame(),
            "ram": self.get_ram(),
        }

    def get_fastfetch(self) -> set:
        user = "marg_ghost"
        list_f = []
        return (user, list_f)

    def get_drive(self) -> dict:
        usage = psutil.disk_usage('/')
        to_gib = 1024 ** 3
        return {
            "total": round(usage.total / to_gib, 1),
            "free": round(usage.free / to_gib, 1),
            "used_percent": usage.percent,
        }
    
    def get_time(self) -> dict:
        now = datetime.datetime.now()
        return {
            "time": now.strftime("%H:%M:%S"),
            "date": now.strftime("%d.%m.%Y"),
        }

    def get_network(self) -> dict:
        stats = psutil.net_if_stats()
        interfaces = [name for name in stats if name != "lo"]
        wifi = next((name for name in interfaces if name.startswith(("wl", "wifi"))), None)
        ethernet = next((name for name in interfaces if name != wifi), None)

        def status(name):
            if not name:
                return {"name": "not found", "status": "not found"}
            return {"name": name, "status": "up" if stats[name].isup else "down"}

        return {"ethernet": status(ethernet), "wifi": status(wifi)}

    def get_core(self):
        percentages = psutil.cpu_percent(percpu=True, interval=0.1)
        while len(percentages) < 4:
            percentages.append(0.0)
        return [round(value, 1) for value in percentages[:4]]

    def get_cpu_frame(self):
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                millidegrees = int(f.read().strip())
            return round(millidegrees / 1000, 1)
        except (FileNotFoundError, OSError, ValueError):
            return 0.0

    def get_ram(self) -> dict:
        mem = psutil.virtual_memory()
        used_gb = round(mem.used / (1024**3), 1)
        total_gb = round(mem.total / (1024**3), 1)
        return {"used": used_gb, "total": total_gb, "used_percent": mem.percent}

        