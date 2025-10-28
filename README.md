# 🧭 AWS Auto-Tagger — Infrastructure Governance Automation
## 🌟 Overview

In large AWS environments, engineers often spin up EC2 instances without proper tagging. Untagged resources make it difficult to track costs, manage ownership, and enforce compliance. Manual tagging becomes a repetitive and error-prone task — a perfect target for automation.

This project automates the detection and tagging of untagged EC2 instances using Python and Boto3. It forms a foundational pattern for infrastructure governance and operational efficiency across AWS environments.

---

## ⚙️ How It Works

The Auto-Tagger script connects to AWS via the **Boto3 SDK** using a least-privilege IAM profile. It scans all EC2 instances in a region and identifies any that have no tags or empty tag lists.
You can specify a default tag key/value (e.g., `Environment=Dev`) to apply automatically.

### Example Usage

```
bash

python auto_tagger.py --region us-west-2 --tag "Environment=Dev"

```

### Example Output

```
csharp

✅ Tagged i-0abc12345ef6789 with Environment=Dev
✅ Tagged i-0def98765abcd4321 with Environment=Dev

```
All tagging actions are logged locally for traceability.

---

## 💡 Why It Matters

Consistent tagging drives:

- **Cost transparency** — Enables chargeback and budgeting by environment or team.

- **Automation** — Allows resource-level actions (stop, delete, monitor) by tag filters.

- **Governance** — Improves compliance and ownership visibility.

By automating these steps, the Auto-Tagger eliminates repetitive human work and reduces operational risk — the same efficiency principle applied in **AWS Fiber Automation**, where manual network management is replaced with intelligent workflows.

---

## 🚀 Next Steps

- Extend tagging logic to support **network resources** (VPCs, subnets, route tables).

- Integrate with **CloudWatch** or **Config Rules** for compliance auditing.

- Convert into a **Lambda** for scheduled execution.

---

## 🧩 Tech Stack

- **Python 3.9+**

- **Boto3 (AWS SDK)**

- **AWS CLI v2**

- IAM user with scoped EC2 read/write permissions

---

## 🧱 Project Structure

```
cpp

aws-auto-tagger/
├── auto_tagger.py
├── list_untagged_instances.py
├── README.md
├── requirements.txt
└── sample_output.json

```

---

## 🙌 Acknowledgment

This project is part of a personal learning path to deepen expertise in **AWS automation and infrastructure governance**, inspired by conversations with engineering mentors at AWS.
