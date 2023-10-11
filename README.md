# Refresh
This container emulates the vulnerable functionality of CVE-2022-1388 in an F5 Router allowing RCE.
CVE-202201388 stems from a complicated relationship between different authentication mechanisms and broxying that stripped Headers allowing improper access to admin endpoints in the webapp.
Competitors must use their bot to send a web request exploiting this flaw.

## Building
```sh
docker build -t refresh .
```

## Running
```sh
docker run -p 80:80 refresh
```

## Exploiting
```sh
python3 exploit.py -u http://localhost -t
```

## References
- https://www.randori.com/blog/vulnerability-analysis-cve-2022-1388/
