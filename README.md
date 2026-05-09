# Datathon Passos Mágicos - Fase 5 (FIAP)

Este repositório contém a solução analítica para o Datathon da Fase 5 da PosTech FIAP, focado na Associação Passos Mágicos. O objetivo é analisar o impacto educacional e desenvolver modelos preditivos para identificar riscos de defasagem dos alunos.

## 🔗 Links Oficiais da Entrega
- **Aplicação Web (Streamlit):** [https://fiapchallenge5-rm365970.streamlit.app/](https://fiapchallenge5-rm365970.streamlit.app/)
- **Apresentação Gerencial:** `rm365970_passosmagicos_storytelling.pdf` na raiz do projeto.

## 📈 Status do Projeto
- [x] **Fase 1: Limpeza e Preparação de Dados** - Concluída
- [x] **Fase 2: Análise Exploratória (EDA)** - Concluída
- [x] **Fase 3: Modelagem Preditiva** - Concluída
- [x] **Fase 4: Aplicação Streamlit** - Concluída
- [x] **Fase 5: Storytelling e Pitch** - Concluída

## 📁 Estrutura do Repositório
- `notebooks/`: Contém os Notebooks Jupyter das fases do projeto.
- `scripts/`: Scripts Python utilitários.
- `models/`: Modelo de Machine Learning treinado (`.pkl`).
- `app.py` e `requirements.txt`: Arquivos para deploy da aplicação no Streamlit Community Cloud.
- `local_data/`: (Ignorado pelo Git) Contém os dados brutos e playbooks de execução local.

## 🚀 Como Iniciar (Passo a Passo)

### 1. Pré-requisitos
- Python 3.12+
- Ambiente virtual configurado

### 2. Instalação e Configuração do Ambiente
Para instalar todas as bibliotecas e dependências necessárias para a execução completa do projeto, rode os comandos abaixo no seu terminal:

```bash
# Criação e ativação do ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalação das bibliotecas
pip install pandas numpy openpyxl jupyter matplotlib seaborn scikit-learn joblib streamlit weasyprint md2pdf
```

### 3. Execução do Projeto

#### Fase 1: Limpeza de Dados
1. Garanta que a base bruta (`BASE DE DADOS PEDE 2024 - DATATHON.xlsx`) esteja no diretório `local_data/DATATHON/`.
2. Execute o notebook `notebooks/01_data_cleaning.ipynb` ou o script automatizado `scripts/clean_data.py`.
   - Isso gerará o arquivo `local_data/dataset_limpo.csv`.

#### Fase 2: Análise Exploratória (EDA)
1. Certifique-se de que o arquivo limpo `dataset_limpo.csv` foi gerado.
2. Execute o notebook `notebooks/02_eda_e_business.ipynb` para visualizar a resposta às perguntas de negócio.

#### Fase 3: Modelagem Preditiva (Machine Learning)
1. Execute o notebook `notebooks/03_machine_learning.ipynb`.
2. O modelo preditivo Random Forest será treinado e salvo automaticamente na pasta `models/` como `modelo_risco_rf.pkl`.

#### Fase 4: Aplicação Streamlit (Interface Web)
1. Com o modelo treinado salvo em `models/`, inicie a aplicação interativa executando no terminal:
   ```bash
   streamlit run app.py
   ```

#### Fase 5: Geração da Apresentação Executiva (PDF)
1. O relatório técnico com todos os insights e gráficos foi compilado no arquivo `storytelling_academico.md`.
2. Para gerar/atualizar os gráficos e o PDF final da entrega (`rm365970_passosmagicos_storytelling.pdf`), execute:
   ```bash
   python scripts/export_charts.py
   python -c "import markdown, weasyprint; html = markdown.markdown(open('storytelling_academico.md').read()); css = weasyprint.CSS('style.css'); weasyprint.HTML(string=html, base_url='.').write_pdf('rm365970_passosmagicos_storytelling.pdf', stylesheets=[css])"
   ```

## 🛡️ Governança de Dados
A pasta `local_data/` está configurada no `.gitignore` para garantir que dados brutos, incluindo o arquivo Excel original da ONG, não sejam enviados para repositórios públicos, respeitando rigorosamente a privacidade dos dados da Associação Passos Mágicos.
