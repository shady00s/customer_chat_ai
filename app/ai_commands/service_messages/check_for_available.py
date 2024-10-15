from ai_commands.service_messages.actions.user_services_and_actions import users_services_and_actions
from ai_commands.system_messages.message import systemMessage
check_for_available_products_service =f"""
     The user services that you can provide or help out with are: 
    {users_services_and_actions}
      after creatinf the JSON Object and validate it, re-validate the filterQuery key with the standerds for PostgresSql to be injected directly to the database.
     
     ** NOTES **
          - if the assistant message answer is in form of question then add it into re-ask and make another friendly message.
          - the assistant message answer must be direct and not contains any vauge words or vauge answers and the re-ask also must be in form of question and not contains any vauge words.
    If the user asks for any question/command that are not in the list of user services and actions, don't excute what user asks.
   """