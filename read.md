# 🔍 Port Scanner

A simple Python-based **port scanner** — this tool helps you identify **open ports** on a given **IP address** or **domain name**. It's useful for those learning about network security or ethical hacking.

## 🛠 Technologies

* Python 3
* `socket` module (for network connections)

## 🚀 How to Run

1. Make sure **Python 3** is installed on your system.
2. Open your terminal or command prompt.
3. Run the script using the following command:

```bash
python port_scanner.py
```

If your script accepts parameters (like target address or port range), you can run it like this:

```bash
python port_scanner.py -t 192.168.1.1 -p 1-1000
```

## 📥 Parameters (optional)

* `-t` or `--target`: Target IP address or domain name
* `-p` or `--ports`: Port range to scan (e.g., `1-1000`)

## 📄 Sample Output

```
[+] Scanning target: 192.168.1.1
[+] Port 22 is open
[+] Port 80 is open
[-] Port 443 is closed
...
Scan complete.
```
