# Hi, I'm Ahilya Sarnaik 👋

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=00F7FF&center=true&vCenter=true&width=800&lines=Cybersecurity+Researcher;AI+Security+%7C+Network+Security;Federated+Learning+%7C+NIDS;Anomaly+Detection+%7C+Security+Research" alt="Typing introduction" />
</p>

<p align="center">
  <a href="https://github.com/ahilyasavali12-prog">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://ahilyasavali12-prog.github.io/ahilyasarnaik.github.io/">
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

I am a **Cybersecurity Researcher** interested in applying machine learning and distributed computing to practical security problems.

My current research focuses on **privacy-preserving Network Intrusion Detection Systems (NIDS)** using **Federated Learning**, with particular interest in anomaly detection, client heterogeneity, model aggregation, and network security.

I am especially interested in:

* 🔐 Network Security & Intrusion Detection
* 🤖 AI / Machine Learning for Cybersecurity
* 🧠 Anomaly Detection
* 🔄 Federated Learning
* 🛡️ Privacy-Preserving Security
* 📊 Security Analytics
* 🔬 Cybersecurity Research & Experimentation

---

## 🔬 Research & Technical Focus

| Area                   | Focus                                                  |
| ---------------------- | ------------------------------------------------------ |
| **Federated Learning** | Privacy-preserving collaborative model training        |
| **Network Security**   | Network Intrusion Detection Systems                    |
| **Anomaly Detection**  | Autoencoder-based detection of abnormal traffic        |
| **AI Security**        | Machine learning applications in cybersecurity         |
| **Model Aggregation**  | Adaptive aggregation under statistical heterogeneity   |
| **Security Datasets**  | NSL-KDD and UNSW-NB15                                  |
| **Evaluation**         | AUC-ROC, Macro F1, Detection Rate, FAR and convergence |

---

## 🧠 Current Research

### Privacy-Preserving Federated NIDS

My research investigates whether **Federated Learning** can improve privacy in collaborative network intrusion detection without requiring organisations to centralise raw network traffic.

The research uses locally trained **autoencoder anomaly detectors**, where clients train on their own network data and share model updates rather than raw traffic.

### Proposed Adaptive Aggregation

The proposed approach uses **cosine similarity** to measure the geometric alignment between a client's model update and the current global model.

Clients whose updates fall below a similarity threshold **τ** are excluded from aggregation, while accepted updates receive weights proportional to their similarity.

The approach is designed to address **client drift and statistical heterogeneity** while avoiding the need for auxiliary labelled data or differential-privacy noise.

### Experimental Evaluation

The current evaluation compares:

* **FedAvg**
* **FedProx**
* **FedAdam**
* **Adaptive Aggregation**
* **PerFedHypID**

Across:

* IID data
* Non-IID α = 0.5
* Non-IID α = 0.1

Using:

* **NSL-KDD**
* **UNSW-NB15**

Evaluation metrics include:

* AUC-ROC
* Macro F1
* Detection Rate (DR)
* False Alarm Rate (FAR)
* Convergence rounds
* Welch's t-test
* Cohen's d

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

### Development & Infrastructure

<p>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
  <img src="https://img.shields.io/badge/Kali%20Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Kali Linux" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS" />
</p>

---

## 🧪 Hands-On Cybersecurity

I regularly work with practical cybersecurity concepts including:

* Network traffic analysis
* Wireshark packet analysis
* TCP/IP and network protocols
* ARP poisoning and MITM analysis
* Vulnerability assessment
* SIEM and security monitoring
* Incident response
* Digital forensics
* Threat intelligence
* Linux security environments
* Cybersecurity labs and CTF platforms

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
│  ┌───────────────┐                                          │
│  │ Data Processing│                                         │
│  └───────┬───────┘                                          │
│          │                                                  │
│          ▼                                                  │
│  ┌───────────────────┐                                      │
│  │ Local Autoencoder │                                      │
│  │ Anomaly Detector  │                                      │
│  └─────────┬─────────┘                                      │
│            │                                                │
│            ▼                                                │
│     Federated Learning                                      │                                                           │
│            ▼                                                │
│  ┌─────────────────────┐                                    │
│  │ Adaptive Aggregation │                                   │
│  │ Cosine Similarity    │                                   │
│  └──────────┬──────────┘                                    │
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

## 📊 GitHub Statistics

<p align="center">
  <img
    src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=ahilyasavali12-prog&theme=github_dark"
    alt="GitHub Profile Summary"
    width="100%"
  />
</p>

<p align="center">
  <img
    src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=ahilyasavali12-prog&theme=github_dark"
    alt="Repositories per Language"
    width="48%"
  />
  <img
    src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=ahilyasavali12-prog&theme=github_dark"
    alt="Most Commit Language"
    width="48%"
  />
</p>

---

## 🐍 Contribution Activity

<p align="center">
  <img
    src="https://raw.githubusercontent.com/ahilyasavali12-prog/Ahilya-Sarnaik/output/github-contribution-grid-snake.svg"
    alt="GitHub Contribution Snake"
    width="100%"
  />
</p>

---

## ✍️ Cybersecurity Writing

I write about cybersecurity, security research, networking, and practical security concepts.

<p>
  <a href="https://medium.com/@ahilya_Cyber">
    <img src="https://img.shields.io/badge/Medium-Cybersecurity%20Writing-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium Cybersecurity Writing" />
  </a>
</p>

---

## 🌐 Connect With Me

<p align="center">
  <a href="https://ahilyasavali12-prog.github.io/ahilyasarnaik.github.io/">
    <img src="https://img.shields.io/badge/Portfolio-Ahilya%20Sarnaik-000000?style=for-the-badge&logo=firefox&logoColor=00F7FF" alt="Portfolio Website" />
  </a>
  <a href="https://www.linkedin.com/in/ahilyacyber">
    <img src="https://img.shields.io/badge/LinkedIn-Ahilya%20Sarnaik-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/ahilyasavali12-prog">
    <img src="https://img.shields.io/badge/GitHub-ahilyasavali12--prog-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
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
  <img src="https://komarev.com/ghpvc/?username=ahilyasavali12-prog&label=Profile%20Views&color=0e75b6&style=flat" alt="Profile Views" />
</p>

<p align="center">
  <i>Cybersecurity Research • AI Security • Network Defense • Privacy-Preserving ML</i>
</p>

