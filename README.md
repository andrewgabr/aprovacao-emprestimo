# Projeto de Aprovação de Empréstimo

Este projeto tem como objetivo criar um modelo preditivo para aprovação de empréstimos, com foco na identificação de clientes que têm maior probabilidade de não pagar o empréstimo. O modelo utiliza **Random Forest** para prever a inadimplência, sacrificando parte da acurácia para maximizar a identificação de inadimplentes.

## Imagens

Aqui estão as imagens que mostram a previsão de inadimplência para **Aprovado** e **Não Aprovado**:

<div style="display: flex; justify-content: space-between; align-items: flex-start;">
    <img src="https://github.com/andrewgabr/aprovacao-emprestimo-ML/blob/master/imgs/Screenshot%202025-03-30%20184348.png?raw=true" alt="Aprovado" style="width: 48%;"/>
    <img src="https://github.com/andrewgabr/aprovacao-emprestimo-ML/blob/master/imgs/Screenshot%202025-03-30%20184432.png?raw=true" alt="Não Aprovado" style="width: 48%;"/>
</div>

## Descrição

O modelo foi desenvolvido utilizando técnicas de Machine Learning e um fluxo de trabalho de pré-processamento de dados com pipelines. A interface interativa foi criada com **Streamlit**, permitindo a fácil interação com o modelo.

## Objetivo

O principal objetivo é identificar clientes com maior risco de inadimplência, mesmo que isso signifique abrir mão de uma precisão total nas previsões. A acurácia do modelo é **85%**, e esse valor foi ajustado para priorizar a detecção de inadimplentes.

## Tecnologias

- **Python**: Linguagem principal para análise de dados e desenvolvimento do modelo.
- **pandas, numpy**: Para manipulação e análise dos dados.
- **scikit-learn**: Para a implementação do modelo Random Forest e pipelines de pré-processamento.
- **Streamlit**: Para a criação da interface interativa.
- **matplotlib, seaborn**: Para visualizações gráficas dos dados e resultados.

## Processos

### 1. **Coleta e Tratamento dos Dados**
Os dados utilizados no modelo incluem informações financeiras e pessoais de clientes. O tratamento dos dados foi realizado através de pipelines que incluem:

- **Limpeza de Dados**: Preenchimento de valores ausentes e remoção de inconsistências.
- **Codificação de Variáveis Categóricas**: Conversão de variáveis como gênero, tipo de crédito, entre outras, para formato numérico.
- **Escalonamento**: Normalização de variáveis numéricas para garantir que todas as variáveis contribuam igualmente para o modelo.

### 2. **Pipeline para Colunas Categóricas**
As colunas categóricas do dataset foram tratadas utilizando um pipeline específico que envolve a codificação das variáveis em formato numérico.

### 3. **Pipeline para Colunas Numéricas**
As colunas numéricas foram tratadas com escalonamento adequado para que todas as variáveis contribuam igualmente para o modelo.

### 4. **Pipeline Final**
O pipeline final combina as etapas de pré-processamento das colunas categóricas e numéricas, além da implementação do modelo Random Forest.

### 5. **Modelo Preditivo: Random Forest**
O modelo **Random Forest** foi escolhido devido à sua robustez e capacidade de lidar com dados desequilibrados, alcançando **85% de acurácia**. Algumas considerações importantes:

- **Sacrifício de Acurácia**: A acurácia foi ajustada para focar mais na identificação de clientes inadimplentes, mesmo que isso resulte em alguns erros de classificação de clientes que provavelmente pagariam.

### 6. **Interface Interativa com Streamlit**
Foi desenvolvida uma interface com **Streamlit**, onde os usuários podem inserir dados de um novo cliente e obter a previsão da probabilidade de inadimplência, com gráficos de apoio para visualização dos resultados.

#### Exemplo de uso na interface:

- Preencha os dados solicitados para o cliente.
- Veja a previsão do modelo com a probabilidade de inadimplência.

## Imagens

Aqui estão algumas imagens de exemplos dos gráficos e da interface do modelo:

- **Gráfico de importância das variáveis**:
  ![Importância das Variáveis](https://github.com/andrewgabr/aprovacao-emprestimo-ML/blob/master/imgs/feature_importance.png?raw=true)

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/projeto-aprovacao-emprestimo.git
cd projeto-aprovacao-emprestimo
