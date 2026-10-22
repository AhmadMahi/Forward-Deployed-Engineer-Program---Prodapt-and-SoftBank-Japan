# Days 11 to 20: Course Materials

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

| Day | Topic |
|---|---|
| 11 | React Basics (assessment day) |
| 12 | React UI Logic and API Integration |
| 13 | Testing and Data Engineering Intro |
| 14 | Data Pipelines and Spark Intro |
| 15 | FDE Professional Skills 1 (full day) |
| 16 | PySpark Batch Pipelines and SQL |
| 17 | DevOps and Cloud Fundamentals (assessment day) |
| 18 | Git, CI/CD and Docker |
| 19 | Containers and Azure Deployment |
| 20 | FDE Professional Skills 2 (full day) |

## What each day folder contains

- **Deck** (.pptx), **pre-read** (PDF), **post-read** (PDF), **Colab notebook** (.ipynb), **app build prompts** (.md),
  **hands-on activities** (PDF), **workbook** (.docx) and the **quiz** on the previous day (.txt, CSV rows).
- On Days 15 and 20 the hands-on document holds **simulation and role play cards**, and the workbook uses writing practice instead of code boxes.
- The `Day21` folder holds only the quiz on Day 20, ready for the start of Day 21.

## Running the notebooks

- **React (Days 11 and 12):** `show_react()` renders React inside the notebook output (needs internet for the React CDN). For real projects, use Vite in VS Code as described in the notebook.
- **Full stack (Day 12):** in Colab the app opens inside the notebook; in VS Code run `uvicorn fullstack:app --reload` and open http://127.0.0.1:8000.
- **Spark (Days 14 and 16):** works in Colab after `pip install pyspark`. In VS Code install Java 17 first.
- **Docker and Azure (Days 18 and 19):** Docker commands need Docker Desktop. Azure commands run in Azure Cloud Shell. Only use subscriptions you have permission to use, and delete test resource groups afterwards.
