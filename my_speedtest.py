import csv
import time
from datetime import datetime
import speedtest
import os

def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {power_labels[n]+'b'}"


def check_directory():
    path = current_time.strftime('%m_%Y')
    if not os.path.exists(path):
        os.mkdir(path) 



def test_speed():
    servers = []
    test = speedtest.Speedtest()
    test.get_servers(servers)
    test.get_best_server()

    test.download()
    test.upload()

    res = test.results.dict()

    data = [
        current_time.strftime("%d/%m/%Y %H:%M:%S"),
        res['client']['isp'],
        format_bytes(res['download']),
        format_bytes(res['upload'])
    ]

    with open(f"{current_time.strftime('%m_%Y')}/results_{current_time.strftime('%d_%m_%Y')}.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)

while True:
    current_time = datetime.now()
    check_directory()

    try:


        test_speed()

        time.sleep(180)
    except Exception:
        data = [
            current_time.strftime("%d/%m/%Y %H:%M:%S"),
            "No data",
            "No data",
            "No data"
        ]
        with open(f"{current_time.strftime('%m_%Y')}/results_{current_time.strftime('%d_%m_%Y')}.csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerow(data)

        time.sleep(15)
