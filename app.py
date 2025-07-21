from urllib.request import urlopen

for line in urlopen("https://google.com"):
    print(line.decode("utf-8").strip())
