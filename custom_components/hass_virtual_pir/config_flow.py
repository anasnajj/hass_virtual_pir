"""Config flow for Virtual PIR Sensor integration."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS

class VirtualPIRConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Virtual PIR Sensor."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(
                title="Virtual PIR Sensor", data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_IP_ADDRESS): str,
                }
            ),
        )
