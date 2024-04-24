import subprocess
import logging

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, CONF_IP_ADDRESS, DEFAULT_TIMEOUT

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    ip_address = entry.data[CONF_IP_ADDRESS]
    async_add_entities([VirtualPIRSensor(ip_address)], True)

class VirtualPIRSensor(BinarySensorEntity):
    def __init__(self, ip_address):
        self._ip_address = ip_address
        self._state = None
        self._device_class = BinarySensorDeviceClass.MOTION

    async def async_update(self):
        try:
            with async_timeout.timeout(DEFAULT_TIMEOUT):
                subprocess.run(["ping", "-c", "1", self._ip_address], check=True)
                self._state = True
        except subprocess.CalledProcessError:
            self._state = False
            _LOGGER.error("Error updating Virtual PIR Sensor state", exc_info=True)
        except asyncio.TimeoutError:
            self._state = False
            _LOGGER.error("Error updating Virtual PIR Sensor state", exc_info=True)

