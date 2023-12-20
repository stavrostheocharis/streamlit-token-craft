# 🌟 Streamlit Token Craft Component 🚀

[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link] [![Download][download_badge]][download_link]

Welcome to the Streamlit Token Craft Component, where managing tokens is as fun as a barrel of monkeys! 🐒 This custom Streamlit component is designed to bring joy and efficiency to your data management needs of displaying tokens in your Streamlit app.

## Features 🎉
* Inline Editing: Edit tokens directly in the table like a ninja! 🥷
* Dynamic Column Visibility: Play hide and seek with your columns! 🙈🙉
* Action Handling: Manage token deletion with style. It's like having a mini-command center. 🎮
* Responsive Design: Looks great on screens of all sizes, even on your grandma's old monitor! 👵💻

## Demo 📺

Watch the Token Craft strut its stuff!


Peek at more cool tricks up its sleeve!


## Installation 🛠️
Get this party started with a simple command:
```python
pip install streamlit-token-craft
```

## Usage 📚
Here’s a very simple example on how to unleash the power of the Token Craft in your app:

```python
import streamlit as st
from token_craft import st_token_table

mock_tokens = [
    {
        "id": "token98a1c077",
        "key": "token98-e316-49d9",
        "display_key": "token98a...e5437d75",
        "name": "Token 1",
        "dateCreated": "2023-12-20",
        "lastUsed": "Never",
        "is_active": True,
    },
]

rendered_tokens = st_token_table(
    tokens=mock_tokens,
    key="token_table",
)
```
> [!IMPORTANT]
> Keep in mind that the functionality of this component has to be combined with your token management service.
>
>For more complex functionality have a look at [demo full app](demo_full_app.py) & [demo for column selection](demo_col_selection_app.py).

## Contributing 🤝
Got ideas? Jump in! Contributions are as welcome as puppies at a park! 🐶

For more information, see [CONTRIBUTING](CONTRIBUTING.md) instructions.

## License 📜
This project is licenced under an [MIT Licence](LICENSE).




[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label

[github_link]: https://github.com/stavrostheocharis/streamlit-token-craft

[pypi_badge]: 

[pypi_link]: 

[download_badge]: 

[download_link]: 