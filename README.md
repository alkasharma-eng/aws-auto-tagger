# 🧭 AWS Auto-Tagger — Infrastructure Governance Automation
## 🌟 Overview

In large AWS environments, engineers often spin up EC2 instances without applying proper tags.
Untagged resources make it difficult to track costs, manage ownership, and maintain compliance — while manual tagging quickly turns into a repetitive, error-prone task.

This project automates the detection and tagging of untagged EC2 instances using **Python** and **Boto3**, creating a lightweight yet durable pattern for infrastructure governance. It demonstrates how simple automation can improve operational efficiency, reduce risk, and reinforce engineering best practices across AWS environments.

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

## 🚀 Next Steps & Extensions

This project is designed to evolve naturally toward full-scale infrastructure automation.
Here are several directions for future enhancement:

- **Integrate with AWS Config Rules or CloudWatch** to continuously audit resource compliance and alert when untagged instances appear.

- **Deploy as an AWS Lambda function** to schedule regular tagging runs and remove manual triggers.

- **Extend resource coverage** to include S3 buckets, VPCs, and network interfaces for complete tagging hygiene.

- **Add a simple CLI or dashboard layer** to visualize compliance across multiple regions or accounts.

- **Feed data into the Network Visualizer project**, creating an end-to-end view of infrastructure governance.

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

## 🧠 How to Run the AWS Auto-Tagger

**1. Prerequisites**

- Python 3.9 or higher installed
- An [AWS IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) with permission to tag EC2 instances (for testing, `AmazonEc2FullAccess` works fine)
- AWS CLI configured locally (`aws configure`) or a profile with credentials set


**2. Clone the Repository**

```
bash

git clone https://github.com/alkasharma-eng/aws-auto-tagger.git
cd aws-auto-tagger
```


**3. Create and Activate a Virtual Environment**

```

bash

python -m venv .venv
.\.venv\Scripts\Activate
```


**4. Install Dependencies**

```
bash

pip install -r requirements.txt
```


**5. Configure Your AWS Profile**

You can use your default credentials or set a named profile:
```
bash

aws configure --profile auto-tagger-dev
```


**6. Run the Script**

To tag all untagged EC2 instances in a specific region:

```
bash

python auto_tagger.py --region us-west-2 --tag Environment=Dev
```

✅ Example output:

```

csharp

[INFO] Scanning for untagged instances in us-west-2 ...
[INFO] Tagged i-0abc12345ef6789 with Environment=Dev
[INFO] Results saved to sample_output.json
```


**7. View the Output**

Open the generated file:

```
bash

cat sample_output.json
```
This file lists all instances that were tagged (or skipped).


**8. Clean Up (Optional)**

When you're done:

```
bash

deactivate
```
---

## 🌟 What This Script Demonstrates

This simple automation showcases:

- AWS governance hygiene (enforcing consistent tagging)
- Boto3 API usage for real-world DevOps scripting
- Infrastructure automation principles aligned with **AWS Fiber Automation:** eliminating reptitive manual steps to improve operational efficiency.

---

## 🙌 Acknowledgment

This project is part of a personal learning path to deepen expertise in **AWS automation and infrastructure governance**, inspired by conversations with engineering mentors at AWS.
