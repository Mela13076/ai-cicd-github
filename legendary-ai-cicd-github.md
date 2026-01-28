<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Your First GitHub Actions AI workflow

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-cicd-github)

**Author:** Amelia Trevino  
**Email:** trevinoamelia25@gmail.com

---

![Image](http://learn.nextwork.org/easygoing_brown_zealous_tayberry/uploads/ai-cicd-github_d2f6s4y1)

---

## Introducing Today's Project!

In this project, I'm going to build a github CI/CD pipeline that will use github actions test my python project with pytest. 

### Key tools and concepts

The key tools I used include pytest and CI workflows. Key concepts I learnt included running pytest automatically when a push or PR is made to main. 

### Challenges and wins

This project took me approximately 20-30 mins. 

### Why I did this project

I did this project today to learn how to set up a CI workflow for running test on my code. 

---

## Setting Up the Python Environment

In this step, I'm setting up the project repository and setting up my python venv, installed with dependencies. 

![Image](http://learn.nextwork.org/easygoing_brown_zealous_tayberry/uploads/ai-cicd-github_m5v9b3x7)

### Activating the virtual environment

I activated my venv by running the command "source .venv/bin/activate"

![Image](http://learn.nextwork.org/easygoing_brown_zealous_tayberry/uploads/ai-cicd-github_p2w8n4r6)

### Exploring the project structure

I found key files including app.py, requirements.txt, README.md, all the files found in the Repo.

---

## Writing and Testing a Python Function

In this step, I'm writing test with pytest to check the funcions in my python files. 

![Image](http://learn.nextwork.org/easygoing_brown_zealous_tayberry/uploads/ai-cicd-github_q8j4m1h6)

### Creating the multiply function

I wrote a multiply function that takes two integer intputs and returns their multiplaction as an integer. 

![Image](http://learn.nextwork.org/easygoing_brown_zealous_tayberry/uploads/ai-cicd-github_a6s2v5t8)

### Running and verifying tests

I verified my tests by running pytest -v and then checking the ouput to see which test passed. If any failed it will show an error. 

---

## Building a CI Pipeline with GitHub Actions

In this step, I'm creating the CI pipeline that will run on every push and run pytest. This will help catch any test that fail when pushed to main. 

![Image](http://learn.nextwork.org/easygoing_brown_zealous_tayberry/uploads/ai-cicd-github_g1k5n9r3)

### Configuring the workflow

I configured the workflow to run when thre is a push or PR for the main branch. It will install dependencies and then run pytest. 

### Testing the pipeline

CI caught the bug when I pushed it to the main branch. It ran the CI workflow and ran pytest to check if all test passed. 

---

## Packaging Code with CI Artifacts

I will be packagain my code to prepare it for distribution and to make it easier to use by others. 

![Image](http://learn.nextwork.org/easygoing_brown_zealous_tayberry/uploads/ai-cicd-github_n3m7k1w9)

### Adding build and upload steps

I added a build step that packages the python files into a installable file, then upload artifact which uploads the contents as an artifact named python-package. Artifacts are useful because they preserve build outputs from CI without publishing them, let reviewers pull the exact built package for testing, and are useful for debugging. 

![Image](http://learn.nextwork.org/easygoing_brown_zealous_tayberry/uploads/ai-cicd-github_s6p9c4v1)

### Downloading the packaged artifact

The workflow builds the package with python -m build. Artifacts are created only after the job passes. Artifacts are useful as they preserve the exact build output form CI so I or others can download and tst it without rebuilding. 

---

---
