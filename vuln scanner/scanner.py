import aiohttp
import asyncio
import os
import json
import socket
import ssl
from tqdm.asyncio import tqdm

if not os.path.exists("results"):
    os.makedirs("results")

# Port scanning
async def scan_ports(host, ports=[80, 443, 8080, 8000]):
    open_ports = []
    for port in ports:
        try:
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.settimeout(1)
            if conn.connect_ex((host, port)) == 0:
                open_ports.append(port)
            conn.close()
        except:
            continue
    return open_ports

# Header & basic vuln check
async def check_url(url):
    result = {'url': url, 'headers': {}, 'tests': {}, 'ports': [], 'https': None}
    # Check headers and HTTPS
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as resp:
                headers = resp.headers
                result['headers'] = {
                    'Server': headers.get('Server'),
                    'X-Frame-Options': headers.get('X-Frame-Options'),
                    'Content-Security-Policy': headers.get('Content-Security-Policy')
                }
        result['https'] = url.startswith('https')
    except Exception as e:
        result['headers'] = {'error': str(e)}
        result['https'] = 'Error'

    # SQLi/XSS simple test
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url + "?id=1'") as resp:
                text = await resp.text()
                result['tests']['sql_injection'] = "Possible vulnerability" if "error" in text else "Not detected"
            async with session.get(url + "?q=<script>alert(1)</script>") as resp:
                text = await resp.text()
                result['tests']['xss'] = "Possible vulnerability" if "<script>alert(1)</script>" in text else "Not detected"
    except:
        result['tests']['sql_injection'] = "Error"
        result['tests']['xss'] = "Error"

    # Port scanning (simple)
    host = url.replace('http://','').replace('https://','').split('/')[0]
    result['ports'] = await scan_ports(host)

    # Save JSON
    filename = f"results/{host.replace(':','_')}.json"
    with open(filename, "w") as f:
        json.dump(result, f, indent=4)

    return result

# Multi-URL scan with progress
async def scan_urls(urls):
    results = []
    for url in tqdm(urls, desc="Scanning URLs"):
        res = await check_url(url)
        results.append(res)
    return results
