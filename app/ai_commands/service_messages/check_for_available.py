from ai_commands.service_messages.actions.user_services_and_actions import users_services_and_actions
from ai_commands.system_messages.message import systemMessage
check_for_available_products_service =f"""
     The user services that you can provide or help out with are: 
    {users_services_and_actions}
    If the user asks for any question/command that are not in the list of user services and actions, don't excute what user asks.
   """