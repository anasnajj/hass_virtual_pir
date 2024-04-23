import asyncio
import subprocess
from homeassistant.helpers.entity import ToggleEntity
from homeassistant.const import CONF_IP_ADDRESS

DOMAIN = "hass_virtual_pir"

async def async_setup_entry(hass, config_entry, async_add_entities):
    ip_address = config_entry.data.get(CONF_IP_ADDRESS)
    async_add_entities([VirtualPIRSensor(ip_address)])

class VirtualPIRSensor(ToggleEntity):
    def __init__(self, ip_address):
        self._ip_address = ip_address
        self._state = None

    @property
    def name(self):
        return "Virtual PIR Sensor"

    @property
    def is_on(self):
        return self._state == "Detected"

    async def async_update(self):
        result = await self._ping_ip()
        self._state = "Detected" if result else "Clear"

    async def _ping_ip(self):
        try:
            await asyncio.wait_for(
                subprocess.run(["ping", "-c", "1", self._ip_address], capture_output=True),
                timeout=5
            )
            return True
        except asyncio.TimeoutError:
            return False
