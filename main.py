import streamlit as st
import random
from collections import Counter

st.set_page_config(page_title='Sorteador')

st.title("Sorteador de Números")

st.markdown("""

Esse simulador faz automaticamente o sorteio de números a partir dos parâmetros selecionados pelo usuário.

- Valor mínimo e máximo
- Quantos números devem ser sorteados
- Quantas vezes esses números devem ser randomizados
- Quantos sorteios devem ser realizados

Com isso, o simulador irá gerar números aleatórios entre os especificados, realizando uma contagem no final de quantas vezes cada número apareceu no sorteio

No final, serão exibidos os N números mais frequentes de acordo com os filtros selecionados

""")
            
range_values = st.slider(label = "Selecione o valor máximo e mínimo que podem ser sorteados", min_value = 1, max_value = 100, value = (1,50))

n_numbers = st.slider(label = "Selecione a quantidade de números que devem ser sorteados", min_value = 1, max_value = 100, value = 15)

n_iterations = st.slider(label = "Selecione quantas vezes os números devem ser sorteados", min_value = 10000, max_value = 1000000, step = 10000)

n_sorteios = st.slider(label = "Selecione quantos sorteios devem ser realizados", min_value = 1, max_value = 50)

start_check = st.button("Clique aqui para iniciar o sorteio!")

if start_check:

    min_range = range_values[0]

    max_range = range_values[1]

    final_numbers = []

    for _ in range(n_sorteios):

        rand_numbers = []

        for _ in range(n_iterations):

            random_int = random.randint(min_range, max_range)

            rand_numbers.append(random_int)
        
        occurrences = Counter(rand_numbers).most_common(n_numbers)

        raffled_numbers = [number for number, _ in occurrences]

        raffled_numbers.sort()

        final_numbers.append(raffled_numbers)
    
    for number in final_numbers:

        st.text(number)