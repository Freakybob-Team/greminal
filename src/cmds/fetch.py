import platform
import os
import distro
import psutil
import datetime
def cmd():
    class c:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        WHITE = '\033[97m'
    print("Fetch - What's My Info?")
    if os.name == "nt":
        print(platform.system())
    if os.name == "posix":
        name = distro.name(pretty=True)
        version = distro.version(pretty=True)
        codename = distro.codename()
        if "Linux Mint" in name:
            print(f"{c.OKGREEN}Linux Mint{c.ENDC} {version} {codename}")
        else:
            print(f"{name} {version} {codename}")
        print(f"Kernal: {platform.release()}")
    cpu = str(psutil.cpu_percent(interval=1))
    ram = psutil.virtual_memory()
    boot_time = psutil.boot_time()
    uptime_seconds = datetime.datetime.now().timestamp() - boot_time
    print(f"CPU Usage: {cpu}%")
    print(f"RAM Usage: {ram.percent}%")
    print(f"Computer Name: {platform.node()}")
    print(f"Uptime (in seconds): {uptime_seconds}")