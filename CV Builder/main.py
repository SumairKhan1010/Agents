from llm import gen_html
from pdf_build import create

info = """
# PROFESSIONAL PROFILE: AI ENGINEER APPLICATION

## PERSONAL INFORMATION
* **Full Name:** Sumair khan
* **Target Position:** AI Engineer
* **Target Company:** OpenAI
* **Contact Email:** sumair10100@gamil.com
* **GitHub / Portfolio:** github.com

---

## 🎯 OBJECTIVE & POSITION ALIGNMENT
Highly motivated software engineer applying for the **AI Engineer** position at OpenAI. Passionate about moving the needle on Artificial General Intelligence (AGI) by engineering scalable, robust infrastructure and bridging the gap between raw research models and highly efficient production deployments. Seeking to contribute directly to OpenAI's mission of ensuring that artificial general intelligence benefits all of humanity.

---

## 🛠️ CORE TECHNICAL COMPETENCIES

### 1. Model Lifecycle & Engineering
* **Inference Optimization:** Optimizing large language models (LLMs) via quantization (FP8, INT4), pruning, and caching mechanisms.
* **Fine-Tuning Pipelines:** Designing robust pipelines for Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF).
* **Agentic Frameworks:** Building complex autonomous workflows, RAG systems, and tool-use orchestrations.

### 2. Systems & Infrastructure
* **Distributed Training:** Familiarity with high-performance computing clusters and framework scaling (PyTorch, Megatron-LM).
* **Serving & API Architecture:** Implementing high-throughput, low-latency API layers and custom SDK wrapper setups.
* **Data Pipelines:** Architectural scaling for tokenization, heavy data ingestion, and cleaning frameworks.

---

## 💼 ARCHITECTURAL EXPERIENCES (CUSTOM ENTRIES)
*[Tip: Replace these placeholders with the 'weird and good' stuff you are building right now!]*

* **[Project Name 1 / Current Role]:** Led the development of an automated AI agent network that utilizes custom system instructions to execute highly optimized code tasks.
* **[Project Name 2 / Past Role]:** Built an internal data-to-PDF pipeline that ingests raw HTML streams and renders enterprise-grade analytical reports.

---

## 🧬 OPENAI CORE VALUE ALIGNMENT

* **Scale:** Committed to solving architectural bottlenecks that only appear when systems are scaled to extreme limits.
* **AGI Focus:** Aligning engineering patterns with long-term safety, predictability, and safety guardrails.
* **Team-First Orientation:** Excited to collaborate closely with both research scientists and systems engineers to ship iterative, high-impact features.

"""
photo_path = "Assassins-Creed-IV-Black-Flag_PC-cover.jpg"

html = gen_html(info, photo_path=photo_path)

print("=============     HTML has been written ============")
print("=============     Generating the pdf    ============")
print(html)

pdf = create("\n".join(html.split("\n")[1:-2]))
print("=============    Sucessfully made the pdf ==========")
