import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS
from .const import DOMAIN

class VirtualPIRFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if user_input is not None:
            # Validate the user input
            ip_address = user_input[CONF_IP_ADDRESS]
            # Check if the IP address is valid (you may want to add more validation here)
            if ip_address:
                # Create the configuration entry
                return self.async_create_entry(title="Virtual PIR Configuration", data={CONF_IP_ADDRESS: ip_address})

        # If no input or invalid input, show the form
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_IP_ADDRESS): str
            })
        )
