import asyncio
import async_timeout
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, CONF_IP_ADDRESS, DEFAULT_TIMEOUT

PLATFORMS = ["binary_sensor"]  # Include the binary_sensor platform

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the platform from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Retrieve the IP address entered by the user
    ip_address = entry.data[CONF_IP_ADDRESS]

    forward_entry_setup = hass.config_entries.async_forward_entry_setup(entry, "binary_sensor")
    async_add_entities: AddEntitiesCallback = forward_entry_setup

    async_add_entities([VirtualPIRSensor(ip_address)], True)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_forward_entry_unload(
        entry, "binary_sensor"
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
