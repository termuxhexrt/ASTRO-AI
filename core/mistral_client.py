import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

class AIClient:
    def __init__(self, api_key):
        self.client = MistralClient(api_key=api_key)
        self.model = "mistral-large-latest"
        self.messages = []

    def set_system_prompt(self, prompt):
        self.messages = [ChatMessage(role="system", content=prompt)]

    def chat(self, user_input):
        self.messages.append(ChatMessage(role="user", content=user_input))
        
        # In the future, we will define tools here for function calling
        response = self.client.chat(
            model=self.model,
            messages=self.messages
        )
        
        reply = response.choices[0].message.content
        self.messages.append(ChatMessage(role="assistant", content=reply))
        return reply

    def get_structured_command(self, user_input):
        """
        Enhanced version to specifically ask for a shell command.
        """
        prompt = f"Extract or generate the exact Kali Linux command for this task: {user_input}. Respond ONLY with the command string."
        self.messages.append(ChatMessage(role="user", content=prompt))
        
        response = self.client.chat(
            model=self.model,
            messages=self.messages
        )
        
        reply = response.choices[0].message.content.strip().strip('`')
        self.messages.append(ChatMessage(role="assistant", content=reply))
        return reply
