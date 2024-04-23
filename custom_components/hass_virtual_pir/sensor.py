"""Platform for the Virtual PIR Sensor integration."""
from homeassistant.helpers.entity import Entity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS
from homeassistant.core import HomeAssistant
from datetime import timedelta
from ping3 import ping

SCAN_INTERVAL = timedelta(seconds=10)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Virtual PIR Sensor from a config entry."""
    hass.data.setdefault("virtual_pir", {})
    hass.data["virtual_pir"][entry.entry_id] = VirtualPIRSensor(entry)
    return True

class VirtualPIRSensor(Entity):
    """Representation of a Virtual PIR Sensor."""

    def __init__(self, entry: ConfigEntry):
        """Initialize the sensor."""
        self._entry = entry
        self._ip_address = entry.data.get(CONF_IP_ADDRESS)
        self._state = None

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._entry.title

    @property
    def state(self) -> str:
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
            self._state = None
