"""The Virtual PIR Sensor integration."""
import logging

from homeassistant.helpers import discovery

# The domain of your integration. Should be equal to the name of your directory.
DOMAIN = "hass_virtual_pir"

# Initialize logger
_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    """Set up the Virtual PIR Sensor component."""
    _LOGGER.info("Setting up the Virtual PIR Sensor component")
    
    # Example: Load platforms
    hass.async_create_task(
        discovery.async_load_platform(hass, "binary_sensor", DOMAIN, {}, config)
    )

    return True
