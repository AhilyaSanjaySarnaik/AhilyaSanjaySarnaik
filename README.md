# Hi, I'm Ahilya Sarnaik 👋

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=00F7FF&center=true&vCenter=true&width=800&lines=Cybersecurity+Researcher;AI+Security+%7C+Network+Security;Federated+Learning+%7C+NIDS;Anomaly+Detection+%7C+Security+Research" alt="Typing introduction" />
</p>

<p align="center">
  <a href="https://github.com/AhilyaSanjaySarnaik">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://ahilyasanjaysarnaik.github.io/">
    <img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=firefox&logoColor=00F7FF" alt="Portfolio" />
  </a>
  <a href="https://www.linkedin.com/in/ahilyacyber">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://x.com/Ahi_Cyber">
    <img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X" />
  </a>
  <a href="https://medium.com/@ahilya_Cyber">
    <img src="https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" />
  </a>
  <a href="https://tryhackme.com/p/Clover.Code">
    <img src="https://img.shields.io/badge/TryHackMe-212C42?style=for-the-badge&logo=tryhackme&logoColor=white" alt="TryHackMe" />
  </a>
  <a href="https://profile.hackthebox.com/profile/01a0bed0-1061-72bf-98a1-2bd43baada34">
    <img src="https://img.shields.io/badge/Hack%20The%20Box-111927?style=for-the-badge&logo=hackthebox&logoColor=9FEF00" alt="Hack The Box" />
  </a>
</p>

---

## 🔐 About Me

I'm a **cybersecurity researcher** working at the intersection of security and machine learning, in both directions:

* **Securing AI systems** — building guardrails for LLM agents: prompt-injection detection, MCP tool-poisoning defence, and permission and approval controls for agent tool calls.
* **Using AI for security** — privacy-preserving intrusion detection with **federated learning**, and ML-based phishing detection.

My current research investigates adaptive aggregation for federated Network Intrusion Detection Systems (NIDS) under non-IID data.

---

## 🚀 Featured Projects

| Project | What it does | Stack |
| ------- | ------------ | ----- |
| [**SupervisorGuard AI**](https://github.com/AhilyaSanjaySarnaik/supervisor-ai-chatbot) | Governance layer for AI agents. Every tool call passes a prompt-injection sanitizer, attribute-based access control, and human-in-the-loop approval for high-risk actions before reaching the real GitHub MCP server. | Python, FastAPI, MCP, Docker |
| [**AWS Automated Threat Detection & Response**](https://github.com/AhilyaSanjaySarnaik/aws-detection-response) | Event-driven pipeline that detects and automatically reverses AWS attacks (exposed SSH, S3 backdoors, CloudTrail tampering) with least-privilege Lambda responders. Tested with Stratus Red Team: **every attack reversed in under 9 seconds**. | Terraform, AWS Lambda, EventBridge, Python |
| [**Agentic Firewall & MCP Sanitizing Proxy**](https://github.com/AhilyaSanjaySarnaik/Sanitization_tool) | Multi-layer prompt-injection firewall (regex, heuristics, ML classifier, vector similarity), a scanner for hidden instructions and cross-tool poisoning in MCP tool lists and OpenAPI specs, and a proxy that hides malicious tools from the agent. | Python, Hugging Face, MCP |
| [**Attack Surface Intelligence Platform**](https://github.com/AhilyaSanjaySarnaik/AI_Passive_Reccon_Plaform) | Local LLM workflow for passive recon, asset triage, and VAPT report drafting, protected by PII redaction and injection scoring, with a built-in red-team runner comparing baseline and protected behaviour. | Node.js, Ollama |
| [**Adaptive Gated Aggregation for Federated NIDS**](https://github.com/AhilyaSanjaySarnaik/Adaptive-Gated-Aggregation-in-Federated-Learning-for-Network-Security) | Research on cosine-similarity gating of client updates to handle client drift in federated intrusion detection, evaluated against FedAvg, FedProx, FedAdam, and PerFedHypID. | Python, PyTorch |
| [**AI-Driven Phishing Classifier**](https://github.com/AhilyaSanjaySarnaik/AI-Driven-Phishing-Classifier) | Phishing detection pipeline covering data preparation, training, evaluation, explainability, and an API server. | Python, Jupyter |
| [**AWS Secure Web Infrastructure & IR Lab**](https://github.com/AhilyaSanjaySarnaik/Cloud_Security_AWS-) | Hardened web infrastructure on AWS with an incident response exercise. | AWS |

---

## 🧠 Current Research

### Privacy-Preserving Federated NIDS

Can organisations collaborate on intrusion detection without centralising raw network traffic? Each client trains a local **autoencoder anomaly detector** on its own traffic and shares only model updates.

**Adaptive Gated Aggregation** measures the **cosine similarity** between each client's update and the global model. Updates below a threshold **τ** are excluded; accepted updates are weighted by similarity. This targets **client drift and statistical heterogeneity** without auxiliary labelled data or differential-privacy noise.

| Evaluation | Details |
| ---------- | ------- |
| **Baselines** | FedAvg, FedProx, FedAdam, PerFedHypID |
| **Datasets** | NSL-KDD, UNSW-NB15 |
| **Data partitions** | IID, Non-IID Dirichlet α = 0.5 and α = 0.1 |
| **Metrics** | AUC-ROC, Macro F1, Detection Rate, False Alarm Rate, convergence rounds |
| **Statistics** | Welch's t-test, Cohen's d |

<!-- Once results are final, add one line here, e.g.:
**Result:** Under α = 0.1 on UNSW-NB15, adaptive aggregation improved Macro F1 from X to Y over FedAvg (p < 0.05). -->

**Next:** evaluating the gating mechanism's robustness against malicious clients (model poisoning and backdoor attacks).

---

## 💻 Research Environment

```text
┌─────────────────────────────────────────────────────────────┐
│                 CYBERSECURITY RESEARCH LAB                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Network Traffic                                            │
│       │                                                     │
│       ▼                                                     │
│  ┌─────────────────┐                                        │
│  │ Data Processing │                                        │
│  └────────┬────────┘                                        │
│           │                                                 │
│           ▼                                                 │
│  ┌───────────────────┐                                      │
│  │ Local Autoencoder │                                      │
│  │ Anomaly Detector  │                                      │
│  └─────────┬─────────┘                                      │
│            │                                                │
│            ▼                                                │
│     Federated Learning                                      │
│            │                                                │
│            ▼                                                │
│  ┌──────────────────────┐                                   │
│  │ Adaptive Aggregation │                                   │
│  │ Cosine Similarity    │                                   │
│  └──────────┬───────────┘                                   │
│             │                                               │
│             ▼                                               │
│       Global Model                                          │
│             │                                               │
│             ▼                                               │
│     NIDS Evaluation                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technical Skills

### Cybersecurity

<p>
  <img src="https://img.shields.io/badge/Network%20Security-0D1117?style=for-the-badge&logo=wireshark&logoColor=white" alt="Network Security" />
  <img src="https://img.shields.io/badge/Threat%20Detection-0D1117?style=for-the-badge&logo=virustotal&logoColor=white" alt="Threat Detection" />
  <img src="https://img.shields.io/badge/Incident%20Response-0D1117?style=for-the-badge&logo=thealgorithms&logoColor=white" alt="Incident Response" />
  <img src="https://img.shields.io/badge/Digital%20Forensics-0D1117?style=for-the-badge&logo=bookstack&logoColor=white" alt="Digital Forensics" />
  <img src="https://img.shields.io/badge/SIEM-0D1117?style=for-the-badge&logo=splunk&logoColor=white" alt="SIEM" />
</p>

### AI / Machine Learning

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
</p>

### AI Security & LLM Tooling

<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face" />
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama" />
  <img src="https://img.shields.io/badge/Model%20Context%20Protocol-0D1117?style=for-the-badge&logo=anthropic&logoColor=white" alt="Model Context Protocol" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js" />
</p>

### Development & Infrastructure

<p>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/Kali%20Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Kali Linux" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS" />
  <img src="https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform" />
</p>

---

## 🧪 Hands-On Cybersecurity

* **Network security:** Wireshark traffic analysis, TCP/IP, ARP poisoning and MITM analysis, Cisco Packet Tracer labs
* **Offensive practice:** TryHackMe and Hack The Box labs, OverTheWire Bandit, and my own CTF challenges
* **Tooling:** a Python website enumeration CLI and passive recon automation
* **Cloud:** AWS infrastructure as code with Terraform, automated detection and response, infrastructure hardening, and incident response

---

## 📊 GitHub Statistics

<p align="center">
  <img
    src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=AhilyaSanjaySarnaik&theme=github_dark"
    alt="GitHub Profile Summary"
    width="100%"
  />
</p>

<p align="center">
  <img
    src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=AhilyaSanjaySarnaik&theme=github_dark"
    alt="Repositories per Language"
    width="48%"
  />
  <img
    src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=AhilyaSanjaySarnaik&theme=github_dark"
    alt="Most Commit Language"
    width="48%"
  />
</p>

---

## 🐍 Contribution Activity

<p align="center">
  <img
    src="https://raw.githubusercontent.com/AhilyaSanjaySarnaik/AhilyaSanjaySarnaik/output/github-contribution-grid-snake.svg"
    alt="GitHub Contribution Snake"
    width="100%"
  />
</p>

---

## ✍️ Cybersecurity Writing

I write about cybersecurity, AI security, networking, and practical security concepts.

<p>
  <a href="https://medium.com/@ahilya_Cyber">
    <img src="https://img.shields.io/badge/Medium-Cybersecurity%20Writing-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium Cybersecurity Writing" />
  </a>
</p>

---

## 🌐 Connect With Me

<p align="center">
  <a href="https://ahilyasanjaysarnaik.github.io/">
    <img src="https://img.shields.io/badge/Portfolio-Ahilya%20Sarnaik-000000?style=for-the-badge&logo=firefox&logoColor=00F7FF" alt="Portfolio Website" />
  </a>
  <a href="https://www.linkedin.com/in/ahilyacyber">
    <img src="https://img.shields.io/badge/LinkedIn-Ahilya%20Sarnaik-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/AhilyaSanjaySarnaik">
    <img src="https://img.shields.io/badge/GitHub-AhilyaSanjaySarnaik-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://x.com/Ahi_Cyber">
    <img src="https://img.shields.io/badge/X-@Ahi__Cyber-000000?style=for-the-badge&logo=x&logoColor=white" alt="X" />
  </a>
</p>

<p align="center">
  <a href="https://tryhackme.com/p/Clover.Code">
    <img src="https://img.shields.io/badge/TryHackMe-Clover.Code-212C42?style=for-the-badge&logo=tryhackme&logoColor=white" alt="TryHackMe" />
  </a>
  <a href="https://profile.hackthebox.com/profile/01a0bed0-1061-72bf-98a1-2bd43baada34">
    <img src="https://img.shields.io/badge/Hack%20The%20Box-Profile-111927?style=for-the-badge&logo=hackthebox&logoColor=9FEF00" alt="Hack The Box" />
  </a>
  <a href="https://medium.com/@ahilya_Cyber">
    <img src="https://img.shields.io/badge/Medium-@ahilya__Cyber-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" />
  </a>
</p>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=AhilyaSanjaySarnaik&label=Profile%20Views&color=0e75b6&style=flat" alt="Profile Views" />
</p>

<p align="center">
  <i>Cybersecurity Research • AI Security • Network Defense • Privacy-Preserving ML</i>
</p>
