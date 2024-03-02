![PWNAI_logo](https://github.com/NoDataFound/PwnAI/assets/3261849/097345e6-ba50-46a1-9d2c-01de927a8112)

![AI](https://img.shields.io/badge/AI-Enabled-brightgreen)
![Generative AI](https://img.shields.io/badge/Generative%20AI-Enabled-blueviolet)
![OpenLLM](https://img.shields.io/badge/OpenLLM-Integrated-blue)

PWNAI is a Streamlit-based web application designed to allow a single input and facilitate the comparison of various services based on their capabilities, costs, API documentation, and more. It allows users to select single or multiple services.

## Features

- Multi-select sidebar to choose services for comparison.
- Dataframe display of service comparisons.

## Installation

To run the PWNAI app locally, you will need to have Python and Streamlit installed. Follow these steps to get started:


```bash
   git clone https://github.com/NoDataFound/PwnAI.git
   cd pwnai
```

Create a Virtual Environment

If you haven't already, install virtualenv via pip:

```bash
pip install virtualenv
```
Then, create a virtual environment in the project directory:

```bash
virtualenv venv
```

This command creates a virtual environment named venv. You can name it anything, but venv is a common convention.

Activate the Virtual Environment

`Before installing dependencies and running the app, you need to activate the virtual environment:`

On Windows:
```
cmd
Copy code
.\venv\Scripts\activate
```

On macOS and Linux:

```bash
source venv/bin/activate
```

You should now see (venv) at the beginning of your terminal line, indicating that the virtual environment is active.

Install Dependencies

With the virtual environment activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

Running the App
Once the setup is complete and all dependencies are installed, you can run the app with Streamlit:


```bash
streamlit run pwnai.py
```
To stop the app, use Ctrl + C in your terminal. To deactivate the virtual environment when you're done, simply type:

```bash
deactivate
```
This ensures that your Python environment returns to normal.



`Hosted Services`

- Reads [csv](https://docs.google.com/spreadsheets/d/1Ky-y5_8Feniv6OOTvB_3nYKmHcFaK8uFN3_mkvVKBhw/edit?usp=sharing)  input
- Allows multi select for comparison
  
`Services Sample`

<img width="1578" alt="Screenshot 2024-03-02 at 2 44 27 PM" src="https://github.com/NoDataFound/PwnAI/assets/3261849/2f807aaa-b990-4774-9520-60347a90775b">



<img width="1122" alt="Screenshot 2024-03-02 at 2 06 40 PM" src="https://github.com/NoDataFound/PwnAI/assets/3261849/ff1e2dff-5fe5-49e8-8060-7d66205eb088">



https://github.com/steven2358/awesome-generative-ai
