# ASTRO AI - Autonomous Red Team Assistant 🌌

ASTRO AI is a powerful, autonomous pentesting assistant powered by **Mistral AI**. It integrates directly with the Kali Linux terminal to perform reconnaissance, scanning, and exploitation tasks.

## 🚀 Features
- **Autonomous Command Suggestions**: Tell ASTRO what you want to achieve, and it generates the precise Kali command.
- **Direct Execution**: Run commands directly from the interface (with user consent).
- **Intelligent Result Analysis**: ASTRO analyzes the output of tools like `nmap` and `metasploit` to suggest follow-up actions.
- **Offensive Persona**: Built specifically for red-teaming and ethical hacking.

## 🛠️ Setup in Kali Linux

1. **Clone the repository**:
   ```bash
   git clone <your-private-repo-url>
   cd astro-ai
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**:
   ```bash
   cp .env.example .env
   nano .env
   # Add your MISTRAL_API_KEY
   ```

4. **Run ASTRO AI**:
   ```bash
   python astro.py
   ```

## ⚠️ Important
- Ensure you have the necessary tools installed in Kali (e.g., `nmap`, `metasploit-framework`, etc.).
- Always test in a controlled environment.

---
*Created for security research and offensive security excellence.*
