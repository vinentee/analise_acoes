# Análise de Variação de Preços de Ações
Este é um programa em Python que utiliza as bibliotecas Pandas e Matplotlib para analisar a variação dos preços de fechamento e abertura de ações em um determinado período de tempo. Ele carrega dados de um arquivo CSV, filtra os dados para o período desejado e plota gráficos da variação dos preços.

## Requisitos
Python 3.12.2

Bibliotecas Python:

Pandas

Matplotlib

## Uso
Certifique-se de ter um arquivo CSV contendo os dados históricos de preços de ações no formato adequado. O arquivo deve conter colunas para a data ('DATA'), preço de fechamento ('FECHAMENTO') e preço de abertura ('ABERTURA').

Execute o arquivo Python em um ambiente Python.

O programa carregará automaticamente os dados do arquivo CSV especificado.

Os dados serão filtrados para o período desejado. Você pode ajustar o período modificando as datas na variável mask.

Serão exibidos dois gráficos:

Variação do preço de fechamento das ações ao longo do período.

Variação do preço de abertura das ações ao longo do período.

Os gráficos serão exibidos na tela.

## Considerações
Certifique-se de que o arquivo CSV fornecido contém as colunas necessárias ('DATA', 'FECHAMENTO', 'ABERTURA') e que os dados estão no formato correto.

O programa permite ajustar o período desejado alterando as datas na variável mask.

Você pode personalizar os gráficos, como cores, títulos e legendas, modificando os parâmetros passados para as funções de plotagem do Matplotlib.
