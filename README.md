# Chat-with-ChatGPT

This repository contains a Python script that enables you to engage in conversations with the OpenAI GPT-3 language model using your API key. With this script, you can interact with GPT-3 and receive text-based responses to your queries.

## Getting Started

Follow these steps to set up and utilize the ChatGPT script:

### Prerequisites

- You must possess an OpenAI API key. You can obtain one by signing up on the [OpenAI website](https://beta.openai.com/signup/). Please note that it works exclusively for paid accounts or accounts with sufficient credits.

- Ensure that Python 3.x is installed on your machine.

### Installation

1. Clone this repository to your local machine or download the script.

   ```bash
   git clone https://github.com/Ganesamanian/Chat-with-ChatGPT.git
   ```

2. Open the script (`Chat-with-ChatGPT.py`) in a text editor of your choice.

3. Replace `'YOUR_API_KEY'` with your actual OpenAI API key.

   ```python
   api_key = 'YOUR_API_KEY'
   ```

### Usage

To initiate a chat with GPT-3, simply run the script and input your prompts as instructed:

```bash
python Chat-with-ChatGPT.py
```

- Enter your message as the user input, and GPT-3 will provide text-based responses.

### Customization

You can tailor the chatbot's behavior by adjusting script parameters:

- Modify the `max_tokens` parameter to control the response length. This parameter defines the maximum number of tokens in the response.

```python
max_tokens = 150  # You can adjust this value to control the response length
```

- Experiment with different GPT-3 engines by altering the `engine` parameter. The script currently employs "text-davinci-003," but you can select other engines like "text-davinci-001" or "davinci-codex" to suit your requirements.

```python
engine = "text-davinci-003"  # You can use other engines like "text-davinci-001" or "davinci-codex"
```

### Quitting

To exit the chat, you can uncomment the break statement in the main loop and then type "quit" as your input.

```python
# if user_input.lower() == "quit":
#     break
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script leverages the OpenAI GPT-3 API, and all credit for the powerful language model goes to OpenAI.

## Disclaimer

Please be aware that using this script may result in charges to your OpenAI account, depending on your usage. It is essential to adhere to OpenAI's terms of service and pricing guidelines.

Enjoy your engaging conversations with GPT-3!