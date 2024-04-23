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
    """Add a Virtual PIR sensor based on a config entry."""
    ip_address = entry.data[CONF_IP_ADDRESS]
    async_add_entities([VirtualPIRSensor(ip_address)], True)

class VirtualPIRSensor(BinarySensorEntity):
    def __init__(self, ip_address):
        """Initialize the sensor."""
        self._ip_address = ip_address
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Virtual PIR Sensor ({self._ip_address})"

    @property
    def unique_id(self):
        return self._ip_address

    @property
    def device_class(self):
        """Return the class of this sensor."""
        return BinarySensorDeviceClass.MOTION

    @property
    def is_on(self):
        """Return True if the sensor is activated."""
        return self._state

    async def async_update(self):
        """Check if the device is reachable."""
        try:
            with async_timeout.timeout(DEFAULT_TIMEOUT):
                result = subprocess.run(
                    ["ping", "-c", "1", "-W", "2", self._ip_address],
                    stdout=subprocess.DEVNULL,
                )
                self._state = result.returncode == 0
        except asyncio.TimeoutError:
            self._state = None
            _LOGGER.error("Timeout checking status for %s", self._ip_address)
