import base64
import json
import math
import random
import time
import urllib.parse


def _vn(e, t):
    return random.randint(e, t)


def _bn(e):
    t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    values = [t[_vn(0, 61)] for _ in range(e)]
    return ''.join(values)


def get_proof():
    e = time.gmtime()
    t = int(str(int(time.mktime(e)) // 1e3)[:4]) + e.tm_wday + e.tm_hour + e.tm_min + e.tm_mon
    n = {
        "aC": "Mozilla",
        "aN": "Netscape",
        "aV": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "nP": "Win32",
        "uA": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "nL": "en-US", "cE": True, "oS": True, "sW": random.randint(1000, 9999), "sH": random.randint(1000, 9999), "sD": random.randint(1000, 9999), "wW": random.randint(1000, 9999), "wH": random.randint(1000, 9999),
        "cU": "https://vantage.rip/register", "cP": "/register", "cH": "vantage.rip", "cT": "", "cR": "https:",
        "cO": "vantage.rip"
    }

    r = json.dumps({
        "t": int(time.time()),
        "i": n,
    }, separators=(",", ":"))

    a = ''

    for i in range(len(r)):
        a += chr(ord(r[i]) ^ t)

    final = f"{_bn(_vn(50, 150))}.{_bn(math.floor(t % 15) * e.tm_min)}{base64.b64encode(urllib.parse.unquote(a).encode('utf-8')).decode()}"

    return final
