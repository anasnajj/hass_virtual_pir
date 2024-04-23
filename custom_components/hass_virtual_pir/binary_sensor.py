import asyncio
from homeassistant.helpers.entity import Entity
from homeassistant.const import STATE_CLEAR, STATE_DETECTED
from subprocess import DEVNULL, PIPE, run

DOMAIN = "hass_virtual_pir"

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([VirtualPIRSensor()])

class VirtualPIRSensor(Entity):
    def __init__(self):
        self._state = STATE_CLEAR

    @property
    def name(self):
        return "Virtual PIR Sensor"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        # Replace "127.0.0.1" with the IP address you want to ping
        result = await self.hass.async_add_executor_job(run, ["ping", "-c", "1", "-W", "1", "127.0.0.1"], stdout=DEVNULL, stderr=PIPE)
        if result.returncode == 0:
            self._state = STATE_DETECTED
        else:
            self._state = STATE_CLEAR
