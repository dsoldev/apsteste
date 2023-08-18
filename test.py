import openai

def test_openai_authentication():
    with open("openai_config.txt", "r") as f:
        config = f.read().strip()
    key = config.split('=')[1]

    openai.api_key = key

    # Make a simple completion request to test the authentication
    response = openai.Completion.create(
        engine="davinci",
        prompt="Translate the following English text to French: 'Hello, how are you?'",
        max_tokens=60
    )

    result = response.choices[0].text.strip()

    # Save the result to feedback.txt
    with open("feedback.txt", "w") as f:
        f.write(result)

    assert result == "Bonjour, comment ça va?", "OpenAI API call failed or returned unexpected result."
