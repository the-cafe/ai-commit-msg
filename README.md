# 🤖 AI Commit Message

<a href="https://pypi.org/project/git-ai-commit"><img src="https://img.shields.io/pypi/v/git-ai-commit" alt="Current version"></a>

## 🚀 Tl;DR

- A CLI and git hook that generates the perfect commit message every time you run `git commit`

- Integrates with the [`pre-commit`](https://pre-commit.com/) framework, works alongside all your git hooks

- Supports all projects and programming languages

## 📺 Usage

![Usage Demo](assets/videos/ai-commit-msg.gif)

This tool currently supports the following LLM source...

- **Open AI**: `gpt-4o-mini`(default), `gpt-4`, `gpt-3.5`, and [more...](https://github.com/ming1in/ai-commit-msg/blob/a1e62be64c1f877bfa26c45d2d61508f94504ec0/ai_commit_msg/utils/models.py#L1)

- **Anthropic**: `claude-3-haiku`, `claude-3-sonnet`, `claude-3-opus`
  - [Wiki: Setup Anthropic Model](./wiki/anthropic.md)

- **Local Ollama**: `llama3`, `mistral`, `phi-3`, `gemma`, and [more..](https://github.com/ming1in/ai-commit-msg/blob/a1e62be64c1f877bfa26c45d2d61508f94504ec0/ai_commit_msg/utils/models.py#L1)
  - [Wiki: Using local Ollama LLM model](./wiki/ollama.md)

## 🚀 Let's Get Started

1. To install the AI Commit Message tool, run:

```bash
pip install git-ai-commit

git-ai-commit --version # Check the installed version 
```

2. Run the command to start configuring your tool:

```bash
git-ai-commit config --setup
```

### 🪝 Integrate with `pre-commit` framework

`git-ai-commit` integrated easily with your other git hook using the `pre-commit` framework.

1. Install the [`pre-commit`](https://pre-commit.com/) git hooks framework

```bash
brew install pre-commit
pre-commit --version 
```

2. Create a `.pre-commit-config.yaml` files and add the following config.

```bash
touch .pre-commit-config.yaml 
```

```yaml
default_install_hook_types: 
  # make sure you include `prepare-commit-msg` in `default_install_hook_types`
  - prepare-commit-msg
repos:
  - repo: https://github.com/ming1in/ai-commit-msg
    rev: v1.0.0
    hooks:
    -   id: git-ai-commit
```

3. Based on the config above, install your git hooks script

```bash
pre-commit install 
```

4. Setup your OpenAI key, [see their docs for help](https://platform.openai.com/docs/quickstart)

```bash
git-ai-commit config --openai-key=...
```

## 🛠️ CLI Commands & Options

✨ `git-ai-commit  config`
This subcommand allows you to show your current config settings. Config flags are used to configure various settings in your configuration. For example...

```bash
git-ai-commit config --openai-key=... --model=gpt-4o-mini
```
  
`--openai-key`
`-k`

This flag allows you to set a new or update the OpenAI API key for the CLI to use. Replace `<your-new-key>` with your actual API key to enable the functionality.

`--anthropic-key`
`-a`

This flag allows you to set or update the Anthropic API key for AI-powered commit messages.
  
`--ollama-url`
`-ou`

This flag allows you to set the Ollama URL for local LLM models.

`--reset`
`-r`

Use this flag to reset the entire configuration database to its default state. This will reset all settings, including the OpenAI API key and logger status

`--logger`
`-l`

This flag displays the log status for the CLI

`--model`
`-m`

This flag allows you to set the OpenAI model to use for generating commit messages.

`--setup`
`-s`

Config your git hook, model, and API keys via the NUX flow.

📌 `git-ai-commit  help`, `-h`

This subcommand displays a list of all available commands and their usage, helping users understand how to interact with the CLI.

  ```bash
  git-ai-commit help # -h
  ```

## 🤝 Wanna Contribute?

If you would like to contribute code and improve our product, please read our
[Local Development Wiki](./wiki/local_development.md) to get started

## 🎉 Fun Facts

- Every commit prefixed with `✨` was generated by AI
