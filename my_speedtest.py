import csv
import time
from datetime import datetime
import speedtest

def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {power_labels[n]+'b'}"

def test_speed():
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    servers = []
    test = speedtest.Speedtest()
    test.get_servers(servers)
    test.get_best_server()

    test.download()
    test.upload()

    res = test.results.dict()

    data = [
        current_time,
        res['client']['isp'],
        format_bytes(res['download']),
        format_bytes(res['upload'])
    ]

    with open(f"results_{datetime.now().strftime('%d_%m_%Y')}.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)

while True:
    try:
        test_speed()
        time.sleep(180)
    except Exception:
        data = [
            datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "No data",
            "No data",
            "No data"
        ]
        with open(f"results_{datetime.now().strftime('%d_%m_%Y')}.csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)

        time.sleep(15)
