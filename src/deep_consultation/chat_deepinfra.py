#!/usr/bin/python3

from openai import OpenAI


class ChatDeepInfra:
    def __init__(self, base_url: str, api_key: str, model: str):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
        self.model = model
        self.system_prompt = "You are a helpful assistant."
        self.history = []  # guarda mensagens no formato OpenAI

    # --------------------------------------------------
    # Define ou altera o system prompt
    # --------------------------------------------------
    def set_system_prompt(self, system_prompt: str):
        self.system_prompt = system_prompt

    # --------------------------------------------------
    # Pergunta SEM memória (equivalente ao seu código original)
    # --------------------------------------------------
    def ask_once(self, user_msg: str, stream: bool = False) -> str:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_msg},
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=stream,
        )

        return self._handle_response(response, stream)

    # --------------------------------------------------
    # Pergunta COM memória (usa histórico interno)
    # --------------------------------------------------
    def chat(self, user_msg: str, stream: bool = False, last_turns: int | None = None) -> str:
        messages = [{"role": "system", "content": self.system_prompt}]

        if last_turns is None:
            selected_history = self.history
        else:
            selected_history = self.history[-2 * last_turns:]

        messages.extend(selected_history)
        messages.append({"role": "user", "content": user_msg})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=stream,
        )

        output = self._handle_response(response, stream)
        
        # salva no histórico
        self.history.append({"role": "user", "content": user_msg})
        self.history.append({"role": "assistant", "content": output})

        return output

    # --------------------------------------------------
    # Limpa histórico
    # --------------------------------------------------
    def clear_history(self):
        self.history = []

    def get_history(self):
        return self.history.copy()
    
    # --------------------------------------------------
    # Função interna para tratar streaming ou não
    # --------------------------------------------------
    def _handle_response(self, response, stream: bool) -> str:
        if stream:
            output = ""
            for event in response:
                if event.choices[0].finish_reason:
                    continue
                delta = event.choices[0].delta
                if hasattr(delta, "content") and delta.content:
                    print(delta.content, end="", flush=True)
                    output += delta.content
            print()
            return output
        else:
            return response.choices[0].message.content


if __name__ == "__main__":
    api_key = input("Digite sua API key: ")
    base_url = "https://api.deepinfra.com/v1/openai"
    model = "meta-llama/Meta-Llama-3.1-70B-Instruct"

    cdi = ChatDeepInfra(base_url, api_key, model)

    cdi.set_system_prompt("Você é um assistente acadêmico. Mas vocé não tem papo furado é eficiente quando da respostas. Sua personalidade é espartana e estoica.")

    # Pergunta sem memória
    print("\n--- Pergunta isolada ---")
    
    prompt="Qual é o valor do numero aureo"
    print(">>",prompt)
    print("<<",cdi.ask_once(prompt))

    # Chat com memória
    print("\n--- Chat com memória ---")
    
    prompt="Vou te fazer uma pergunta esteja atento."
    print(">>",prompt)
    print("<<",cdi.chat(prompt))
    
    prompt="quanto é 2+2?"
    print(">>",prompt)
    print("<<",cdi.chat(prompt))

    # Limpar histórico
    cdi.clear_history()
