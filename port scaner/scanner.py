import asyncio
import json

async def scan_port(host, port, semaphore):
    async with semaphore:
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(host, port),
                timeout=0.5
            )
            banner = await grab_banner(reader)
            writer.close()
            await writer.wait_closed()
            return {"port": port, "status": "open", "banner": banner}
        except:
            return None

async def grab_banner(reader):
    try:
        data = await asyncio.wait_for(reader.read(1024), timeout=0.5)
        return data.decode(errors="ignore").strip()
    except:
        return None

async def run_scanner(host, start_port, end_port, limit):
    semaphore = asyncio.Semaphore(limit)
    tasks = [scan_port(host, port, semaphore) for port in range(start_port, end_port + 1)]
    results = await asyncio.gather(*tasks)
    return [r for r in results if r]

def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
