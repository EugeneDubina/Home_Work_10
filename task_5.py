import subprocess
import chardet

ping_args = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping_element in ping_args:
    ping_process = subprocess.Popen(ping_element, stdout=subprocess.PIPE)
    for line in ping_process.stdout:
        res = chardet.detect(line)
        line = line.decode(res['encoding'])
        print(line)