"""Platform for the Virtual PIR Sensor integration."""
from homeassistant.helpers.entity import Entity
from homeassistant.const import STATE_UNKNOWN
from ping3 import ping
from datetime import timedelta

SCAN_INTERVAL = timedelta(seconds=10)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Virtual PIR Sensor from a config entry."""
    async_add_entities([VirtualPIRSensor(entry.data)])

class VirtualPIRSensor(Entity):
    """Representation of a Virtual PIR Sensor."""

    def __init__(self, config):
        """Initialize the sensor."""
        self._name = "Virtual PIR Sensor"
        self._ip_address = config.get(CONF_IP_ADDRESS)
        self._state = STATE_UNKNOWN

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Update the sensor."""
        if self._ip_address:
            if ping(self._ip_address):
                self._state = "Detected"
            else:
                self._state = "Clear"
        else:
            self._state = STATE_UNKNOWN
