# Web Automation with Langchain, Browser-Use, and Playwright

This project automates web interactions using the following libraries:

- **langchain_openai**: For interacting with the OpenAI API.
- **browser-use**: browser-use automates web interactions, handles browser security pop-ups, manages login promptsyou cannot use browser-use without Playwright because Playwright is an essential dependency for the underlying browser automation.
- **playwright**: For automating and interacting with the browser (used internally by browser-use).
- **python-dotenv**: For loading environment variables from a `.env` file, such as API keys.

## Prerequisites

To run this project, make sure you have the following:

- Python (preferably Python 3.7 or higher)
- An OpenAI API key (for `langchain_openai`)
- Playwright browser dependencies installed

## Installation Guide

1. Clone this repository or create a new folder for the project.

2. Create a virtual environment to isolate dependencies (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - **Windows**:

        ```bash
        venv\Scripts\activate
        ```

    - **Mac/Linux**:

        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a `.env` file in the root directory and add your OpenAI API key like this:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

6. Install Playwright browser dependencies:

    ```bash
    playwright install
    ```

## Libraries Used

### 1. **langchain_openai**:
   - **Purpose**: Langchain allows you to chain together LLMs (Large Language Models) and various tools. In this case, it connects to the OpenAI API to generate responses for the given tasks.
   - **Why it's used**: It simplifies communication with the OpenAI API, allowing you to interact with the model without handling complex API requests manually.

   ```python
   from langchain_openai import ChatOpenAI


### 2. ** browser-use**:
   -**Purpose**: This library abstracts the automation of browser tasks, such as searching the web, clicking buttons, and interacting with web pages. It integrates with Playwright to provide a simpler interface for browser automation.
   -**Why it's used**: It helps automate web browsing actions with minimal code and offers features like privacy controls, preventing login pop-ups, and controlling browser sessions.

    ```python
    from browser_use import Agent

### 3.**playwright** :
    -**Purpose**: Playwright is an automation library that interacts with web browsers to perform actions like navigation, clicking, and extracting information. It’s used internally by browser-use.
    -**Why it's used**: Playwright powers browser automation. Though we interact with browser-use, it relies on Playwright for browser interactions.   
    -- Playwright is the underlying tool that browser-use leverages to perform the actual browser automation. It is the library that interacts with the browser (like Chrome, Firefox, or WebKit) to control actions such as opening pages, clicking elements, and extracting content.

