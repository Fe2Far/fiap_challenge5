# Datathon Passos Mágicos - Fase 5 (FIAP)

Este repositório contém a solução analítica para o Datathon da Fase 5 da PosTech FIAP, focado na Associação Passos Mágicos. O objetivo é analisar o impacto educacional e desenvolver modelos preditivos para identificar riscos de defasagem dos alunos.

## 📈 Status do Projeto
- [x] **Fase 1: Limpeza e Preparação de Dados** - Concluída
- [ ] **Fase 2: Análise Exploratória (EDA)** - Pendente
- [ ] **Fase 3: Modelagem Preditiva** - Pendente
- [ ] **Fase 4: Aplicação Streamlit** - Pendente
- [ ] **Fase 5: Storytelling e Pitch** - Pendente

## 📁 Estrutura do Repositório
- `notebooks/`: Contém os Notebooks Jupyter das fases do projeto.
- `scripts/`: Scripts Python utilitários.
- `local_data/`: (Ignorado pelo Git) Contém os dados brutos e playbooks de execução local.

## 🚀 Como Iniciar

### 1. Pré-requisitos
- Python 3.12+
- Ambiente virtual configurado

### 2. Instalação
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas openpyxl jupyter matplotlib seaborn scikit-learn
```

### 3. Execução
Para reproduzir a limpeza de dados:
1. Garanta que a base bruta (`BASE DE DADOS PEDE 2024 - DATATHON.xlsx`) esteja em `local_data/DATATHON/`.
2. Execute o notebook `notebooks/01_data_cleaning.ipynb`.

## 🛡️ Governança de Dados
A pasta `local_data/` está configurada no `.gitignore` para garantir que dados brutos e arquivos PDF de descrição do projeto não sejam enviados para repositórios públicos, respeitando a privacidade dos dados da associação.
