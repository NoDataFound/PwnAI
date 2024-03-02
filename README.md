![PWNAI_logo](https://github.com/NoDataFound/PwnAI/assets/3261849/097345e6-ba50-46a1-9d2c-01de927a8112)

![AI](https://img.shields.io/badge/AI-Enabled-brightgreen)
![Generative AI](https://img.shields.io/badge/Generative%20AI-Enabled-blueviolet)
![OpenLLM](https://img.shields.io/badge/OpenLLM-Integrated-blue)

PWNAI is a Streamlit-based web application designed to allow a single input and facilitate the comparison of various services based on their capabilities, costs, API documentation, and more. It allows users to select single or multiple services.

## Features

- Multi-select sidebar to choose services for comparison.
- Dataframe display of service comparisons.
<img width="1792" alt="Screenshot 2024-03-02 at 3 49 44 PM" src="https://github.com/NoDataFound/PwnAI/assets/3261849/3bdba410-e383-4f33-a414-c6420f1b2600">

`note` 
```
This repo is under active development and not operational at time of writing.
PWNAI is an extension some of my prior "AI" which demostrate similar concepts at a smaller scale.

https://github.com/NoDataFound/hackGPT
https://github.com/NoDataFound/hackGPT/tree/main/hackerParents
https://github.com/NoDataFound/YouSureAboutThat
https://github.com/NoDataFound/SpeedCandidating live here: https://speedcandidating.org/
```

<img width="1556" alt="Screenshot 2024-03-02 at 4 20 28 PM" src="https://github.com/NoDataFound/PwnAI/assets/3261849/25e45dd2-97f1-4054-9bc7-6c873608ffcd">

<img width="930" alt="Screenshot 2024-03-02 at 3 55 47 PM" src="https://github.com/NoDataFound/PwnAI/assets/3261849/d539921e-3e3f-4894-bc10-01eda535dd8b">
<img width="1681" alt="235321459-35eb1ecb-58b6-4439-9fee-dbc63e13f3e1" src="https://github.com/NoDataFound/PwnAI/assets/3261849/d7cd0eca-d544-4af9-9783-e1676c56d3a6">

# Platforms and Services
`Hosted`
- PwnAI reads from [csv](https://docs.google.com/spreadsheets/d/1Ky-y5_8Feniv6OOTvB_3nYKmHcFaK8uFN3_mkvVKBhw/edit?usp=sharing) for selection of services.  
  
### Sample

<img width="1578" alt="Screenshot 2024-03-02 at 2 44 27 PM" src="https://github.com/NoDataFound/PwnAI/assets/3261849/2f807aaa-b990-4774-9520-60347a90775b">

`Local`
### Open LLM Leaderboard
```
local model selection will allow pull from here: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
```
<img width="1122" alt="Screenshot 2024-03-02 at 2 06 40 PM" src="https://github.com/NoDataFound/PwnAI/assets/3261849/ff1e2dff-5fe5-49e8-8060-7d66205eb088">

`Resources`

- https://github.com/steven2358/awesome-generative-ai

## Installation

To run the PWNAI app locally, you will need to have Python and Streamlit installed. Follow these steps to get started:

```bash
   git clone https://github.com/NoDataFound/PwnAI.git
   cd pwnai
```

`Create a Virtual Environment`

If you haven't already, install virtualenv via pip:

```bash
pip install virtualenv
```

Then, create a virtual environment in the project directory:

```bash
virtualenv venv
```

This command creates a virtual environment named venv. You can name it anything, but venv is a common convention.

`Activate the Virtual Environment`

`Before installing dependencies and running the app, you need to activate the virtual environment:`

`On Windows:`
```
cmd
Copy code
.\venv\Scripts\activate
```

`On macOS and Linux:`

```bash
source venv/bin/activate
```

You should now see (venv) at the beginning of your terminal line, indicating that the virtual environment is active.

`Install Dependencies`

With the virtual environment activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

`Running the pwnai.py`
Once the setup is complete and all dependencies are installed, you can run the app with Streamlit:


```bash
streamlit run pwnai.py
```
To stop the app, use Ctrl + C in your terminal. To deactivate the virtual environment when you're done, simply type:

```bash
deactivate
```
This ensures that your Python environment returns to normal.


