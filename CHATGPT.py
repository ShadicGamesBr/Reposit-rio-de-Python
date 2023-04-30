from transformers import pipeline


# define a tarefa de geração de texto usando o modelo GPT-2
text_generator = pipeline("text-generation", model="gpt2")

# gera um texto com o modelo GPT-2
generated_text = text_generator("O que é inteligência artificial?", max_length=100)[0]["generated_text"]

# imprime o texto gerado
print(generated_text)
