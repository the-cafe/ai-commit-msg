# 🤖 AI Commit Message

## 📚 Table of Contents
  - [🚀 Tl;DR](#-tldr)
  - [📺 Usage](#-usage)
  - [🚀 Let's Get Started](#-lets-get-started)
  - [CLI](#cli)
    - [Subcommands](#subcommands)
  - [🤝 Wanna Contribute?](#-wanna-contribute)
  - [🎉 Fun Facts](#-fun-facts)

## 🚀 Tl;DR

- 🤖 An pre-commit hook that generates the perfect commit message for you

- 🌐 Supports all projects and programming languages, built on the [`pre-commit`](https://pre-commit.com/) git hooks framework

- 🔗 Works alongside all your other git hooks

## 📺 Usage

TODO - Insert video of usage

This tool currently supports the following LLM source...

- **Open AI**: gpt-4o-mini(default), gpt-4o, gpt-3.5

- **Anthropic**: claude-3-haiku, claude-3-sonnet, claude-3-opus
  - [Wiki: Setup Anthropic Model](./wiki/anthropic.md)

- **Local Ollama**: llama3, mistral, phi-3, gemma
  - [Wiki: Using local Ollama LLM model](./wiki/ollama.md)

## 🚀 Let's Get Started

1. Install the [`pre-commit`](https://pre-commit.com/) git hooks framework

```bash
brew install pre-commit
pre-commit --version 
```

2. Create a `.pre-commit-config.yaml` files and add the following config

```bash
touch .pre-commit-config.yaml 
```

🚨 Make sure you include `prepare-commit-msg` in `default_install_hook_types`🚨

```yaml
default_install_hook_types: 
  - prepare-commit-msg
repos:
  - repo: https://github.com/ming1in/ai-commit-msg
    rev: v0.0.1
    hooks:
    -   id: git_ai_commit
```

3. Based on the config above, install your git hooks script

```bash
pre-commit install
```

4. Setup your OpenAI key, [see their docs for help](https://platform.openai.com/docs/quickstart)

```bash
git_ai_commit config --openai-key=<insert-your-key>
```

## CLI

### Subcommands

✨ **config**:
  This subcommand allows you to configure various settings for the CLI.

- 🔑 **--openai-key**, **-k**:
    This flag allows you to set a new or update the OpenAI API key for the CLI to use. Replace `<your-new-key>` with your actual API key to enable the functionality.

  ```bash
  git_ai_commit config --openai-key=<your-new-key> 
  ```
  
- 🔑 **--anthropic-key**, **-a**:
This flag allows you to set or update the Anthropic API key for AI-powered commit messages.

  ```bash
  git_ai_commit config --anthropic-key=<your-anthropic-key>
  ```
  
- 🌐 **--ollama-url**, **-ou**:
  This flag allows you to set the Ollama URL for local LLM models.

  ```bash
  git_ai_commit config --ollama-url=<ollama-url>
  ```

- 🔄 **--reset**, **-r**:
  Use this flag to reset the entire configuration database to its default state.

  ```bash
  git_ai_commit config --reset
  ```

  This will reset all settings, including the OpenAI API key and logger status

- 🖨️ **--logger**, **-l**:
  This flag displays the log status for the CLI

  ```bash
  git_ai_commit config --logger=<boolean>
  ```

- 🧠 **--model**, **-m**:
  This flag allows you to set the OpenAI model to use for generating commit messages.

  ```bash
  git_ai_commit config --model=<model-name>
  ```

- 📚 **help**, **-h**:
  This subcommand displays a list of all available commands and their usage, helping users understand how to interact with the CLI.

  ```bash
  git_ai_commit help
  ```


## 🤝 Wanna Contribute?

If you would like to contribute code and improve our product, please read our
[Local Development Wiki](./wiki/local_development.md)

## 🎉 Fun Facts

- Every commit prefixed with `✨` was generated by AI
