# 🛡️ Sistema de Detecção de EPI com Aprendizado Federado (DevSecOps)

Este repositório contém o código-fonte e o pipeline de Continuous Integration/Continuous Delivery (CI/CD) para o projeto de detecção de Equipamentos de Proteção Individual (EPI) utilizando **Aprendizado Federado** (Federated Learning - FL).

## 🚀 Arquitetura do Sistema

Nosso sistema é estruturado em três camadas principais, focadas em garantir **privacidade (LGPD)** e **processamento distribuído**:

| Camada | Componentes Chave | Função Principal |
| :--- | :--- | :--- |
| **Edge/Local** | ESP32-S3-CAM, Cliente Flower, YOLO Tiny | Captura de imagem, processamento local de IA, e treino de modelo. **Não envia imagens para a Nuvem.** |
| **Nuvem/AWS** | Flower Server, FIWARE (Orion-LD), MinIO, MongoDB | Agrega os pesos dos modelos treinados localmente (Aprendizado Federado), armazena modelos globais (MinIO) e gerencia dados de contexto (FIWARE). |
| **Apresentação** | Plataforma Web (Dashboard) | Busca dados no FIWARE e exibe alertas e estatísticas de conformidade com EPIs. |



## ⚙️ Pipeline DevSecOps (GitHub Actions)

Implementamos um pipeline DevSecOps para automatizar a entrega de software, garantir a qualidade do código e a segurança das nossas imagens Docker.

O pipeline é composto por três estágios sequenciais: **CI (Integração Contínua)**, **Build & Security** e **CD (Entrega Contínua)**, todos gerenciados pelo **GitHub Actions** na pasta `.github/workflows/`.

| Arquivo (Stage) | Objetivo | Checagens Chave |
| :--- | :--- | :--- |
| **`ci.yml`** | **Continuous Integration** | Valida sintaxe, dependências e executa testes unitários (ou lint) para garantir a saúde do código antes da construção. |
| **`build.yml`** | **Build & Security Check** | Constrói as imagens Docker do `Flower Server` e do `FastAPI Bridge`. Faz um **scan de vulnerabilidades** (prática DevSecOps) e publica no Docker Hub. |
| **`deploy.yml`** | **Continuous Deployment** | Após um `Build` bem-sucedido, conecta-se via SSH à instância **AWS EC2** e executa o `docker-compose pull` e `up -d` para implantar a nova versão do servidor automaticamente. |

### Benefícios do DevSecOps:

1.  **Velocidade e Confiabilidade:** Automação total desde o commit até o deploy em produção.
2.  **Segurança embutida (Shift Left):** A verificação de vulnerabilidades (Scan) ocorre durante o `Build`, antes da implantação.
3.  **Rastreabilidade:** Todas as alterações e implantações são registradas e auditáveis no log do GitHub Actions.
