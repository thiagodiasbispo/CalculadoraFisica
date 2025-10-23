# Calculadora Física

Aplicação educativa em Python + Streamlit que reúne calculadoras de fórmulas físicas organizadas por ramos (cada ramo em um módulo dentro do pacote `calculadora`). A página principal lista os ramos e suas sub-áreas; cada sub-área abre uma página própria com conteúdo didático (coluna esquerda) e formulário (coluna direita). Os resultados são calculados automaticamente quando as variáveis necessárias são preenchidas.

Como rodar:
1. Crie e ative um ambiente virtual (recomendado).
2. Instale dependências:
   pip install -r requirements.txt
3. Execute:
   streamlit run app.py

Estrutura:
- app.py : App principal e roteamento por query params.
- calculadora/ : pacote com módulos por ramo.
  - eletromagnetismo.py : implementa "Calculadora de Watts" e utilitários.
  - eletronica.py : módulo placeholder para sub-áreas de eletrônica.
  - energia.py : módulo placeholder para energia, trabalho e potência.
