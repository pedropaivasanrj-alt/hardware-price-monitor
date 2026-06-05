# Hardware Price Monitor

Pipeline de dados para monitoramento diário de preços de peças de reposição de hardware, com foco em apoio à tomada de decisão para compras de suporte técnico.

## Problema

Empresas que fazem manutenção de notebooks e desktops precisam comprar peças como SSDs, memórias RAM e telas. Os preços variam bastante entre lojas e ao longo do tempo, dificultando o orçamento e a reposição.

## Solução

Este projeto coleta preços diariamente, limpa e padroniza os dados, armazena histórico em PostgreSQL e disponibiliza indicadores em um dashboard Power BI.

## Stack

Python, PostgreSQL, Docker, SQL, Power BI, GitHub Actions.

## Arquitetura

Web pages → Python Extractor → Data Cleaning → PostgreSQL → Power BI Dashboard

## Principais métricas

- Menor preço atual
- Variação de preço em 7 e 30 dias
- Histórico por produto
- Loja mais barata por categoria
- Alerta de preço abaixo do alvo

## Como rodar

1. Clone o repositório
2. Configure o `.env`
3. Suba o banco com Docker
4. Execute o pipeline
5. Abra o dashboard