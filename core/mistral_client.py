import os
from mistralai import Mistral

class AIClient:
    def __init__(self, api_key):
        self.client = Mistral(api_key=api_key)
        self.model = "mistral-large-latest"
        self.messages = []

    def set_system_prompt(self, prompt):
        self.messages = [{"role": "system", "content": prompt}]

    def chat(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        
        response = self.client.chat.complete(
            model=self.model,
            messages=self.messages
        )
        
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def get_structured_command(self, user_input):
        """
        Enhanced version to specifically ask for a shell command.
        """
        prompt = f"Extract or generate the exact Kali Linux command for this task: {user_input}. Respond ONLY with the command string."
        
        # We don't want to pollute long-term memory with every command extraction, but for now simple append
        temp_messages = self.messages + [{"role": "user", "content": prompt}]
        
        response = self.client.chat.complete(
            model=self.model,
            messages=temp_messages
        )
        
        reply = response.choices[0].message.content.strip().strip('`').strip()
        # Adding to memory so the AI knows what command it suggested for next analysis
        self.messages.append({"role": "assistant", "content": reply})
        return reply
