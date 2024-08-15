import asyncio
import logging
from concord4ws import Concord4WSClient

logger = logging.getLogger("concord4ws")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


async def main():
    client = Concord4WSClient("127.0.0.1", 8080)

    if await client.test_connect():
        print("Connected")
    else:
        print("Not Connected")

    def zoneCallback():
        return print(client.state.zones)

    def partitionCallback():
        return print(client.state.partitions)

    await client.connect()

    for zone in client.state.zones.values():
        client.register_callback(zone.callback_id(), zoneCallback)

    for partition in client.state.partitions.values():
        client.register_callback(partition.callback_id(), partitionCallback)

    print(
        f"Connected to panel {client.state.panel.panel_type} with hardware version {client.state.panel.hardware_revision}, software version {client.state.panel.software_revision}, and serial number {client.state.panel.serial_number}"
    )

    print("Ready!")

    await asyncio.futures.Future()


asyncio.run(main())
