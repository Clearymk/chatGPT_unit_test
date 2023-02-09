import time

import openai
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
MAX_TOKENS = 4097


def ask(prompt):
    openai.api_key = "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"
    prompt_tokens = get_prompt_tokens(prompt)

    if prompt_tokens > 4097:
        split_prompt(prompt)
        return "too many tokens"

    max_tokens = MAX_TOKENS - prompt_tokens

    response = openai.Completion.create(
        model="text-ada-001",
        prompt=prompt,
        temperature=0.7,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text


# TODO prompt拆分
def split_prompt(prompt):
    pass


def get_prompt_tokens(prompt):
    driver.get("https://platform.openai.com/tokenizer")
    input_area = driver.find_element(By.XPATH, "//textarea[@class=\"text-input text-input-md\"]")
    input_area.send_keys(prompt)
    time.sleep(1)
    tokens_text = driver.find_element(By.XPATH, "//div[@class=\"tokenizer-stat-val\"]")
    return int(tokens_text.text.replace(",", ""))


if __name__ == '__main__':
    get_prompt_tokens("test")
