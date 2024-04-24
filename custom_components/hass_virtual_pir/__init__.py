import asyncio
import async_timeout
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, CONF_IP_ADDRESS, DEFAULT_TIMEOUT

PLATFORMS = ["binary_sensor"]  

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    ip_address = entry.data[CONF_IP_ADDRESS] 

    forward_entry_setup = hass.config_entries.async_forward_entry_setup(entry, "binary_sensor")
    async_add_entities: AddEntitiesCallback = forward_entry_setup  

    async_add_entities([VirtualPIRSensor(ip_address)], True)
    return True
