import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant

from .const import DOMAIN, CONF_IP_ADDRESS

class VirtualPIRSensorFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        if user_input is not None:  
            return self.async_create_entry(title="Virtual PIR Sensor", data=user_input)

        schema = vol.Schema({vol.Required(CONF_IP_ADDRESS): str})

        return self.async_show_form(step_id="user", data_schema=schema)

