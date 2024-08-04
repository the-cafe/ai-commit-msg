# AI Commit Message

**Tl;DR**

- An pre-commit hook that generates the perfect commit message for you
- Supports all projects and programming language, built on the [`pre-commit`](https://pre-commit.com/) git hooks framework
- Works alongside all your other git hooks

## Usage

TODO - Insert video of usage

## Getting Started

1. Install the [`pre-commit`](https://pre-commit.com/) git hooks framework

```bash
brew install pre-commit
pre-commit --version 
```

2. Create a `.pre-commit-config.yaml` files and add the following config

```yaml
repos:
  - repo: TODO - insert public github repo
    hooks:
    -   id: gen_ai_commit_message
```

3. Based on the config above, install your git hooks script

```bash
pre-commit install
```

1. Setup your OpenAI key, [see their docs for help](https://platform.openai.com/docs/quickstart)

```bash
gen_ai_commit_message_cli config --openai-key=<insert-your-key>
```

## CLI

TODO - add document on our CLI interface and options

## Fun Facts

- Every commit prefixed with `✨` was generated by AI
