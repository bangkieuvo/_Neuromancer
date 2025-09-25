list = "tshngmww.shtml hipykpqu.shtml ztxdhjxn.shtml avpfeoie.shtml fviqpmaw.shtml kqbybdzc.shtml dzrnmzgx.shtml npcsygfl.shtml whqxxojt.shtml ylomcmvu.shtml uhdppswp.shtml gzntiicx.shtml dzwbqiuu.shtml qvzuieng.shtml smcerykh.shtml qjhnmhmq.shtml znodwztr.shtml"

a = list.split(" ")
# probe_paths.py
import requests

base = "https://www.hackthissite.org/missions/basic/8/tmp/"
paths = a
s = requests.Session()
s.headers.update({"User-Agent":"Mozilla/5.0"})

for p in paths:
    url = base + p
    try:
        r = s.get(url, timeout=8)
    except Exception as e:
        print("Err", url, e); continue
    if r.status_code == 200:
        text = r.text.lower()
        print(text)
    else:
        print(r.status_code, url)
