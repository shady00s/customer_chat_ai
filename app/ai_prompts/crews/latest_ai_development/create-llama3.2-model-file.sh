model_name='llama3.2'
custom_model_name='crewai-llama-3.2'

ollama pull $model_name
ollama create $custom_model_name -f ./Llama3.2Modelfile