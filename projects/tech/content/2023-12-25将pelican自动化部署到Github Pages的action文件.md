---
title: 将pelican自动化部署到Github Pages的action文件
slug: deploy-pelican-to-github-pages
date: 2023-12-25 14:44:07
modified: 2023-12-25 22:52:12
category: 
tags: pelican, github actions
summary: 本文展示了一个示例 Action 文件，其中包括从代码检出到构建和部署的所有步骤。此外，我们介绍了一些常用的 GitHub Actions 操作，如 'actions/checkout@v2' 和 'actions/setup-python@v2'，以及如何使用 'peaceiris/actions-gh-pages@v3' 操作将生成的网站发布到 GitHub Pages。这个文章帮助您轻松自动化部署 Pelican 网站并提高可访问性。
---

## 思路

将pelican项目push到github pages仓库main分支时，自动构建output文件夹到gh-pages分支。

因为github默认优先检查ph-pages分支来生成网站，所以可以使用同一个仓库来分别存储pelican项目代码和静态网页文件：main分支来存储项目代码，gh-pages存放pelican项目生成的静态网页文件。

## 准备

1. 设置好github pages，设置main，gh-pages两个分支。
2. 根目录`pip freeze > requirements.txt`。

## Action 文件

```yaml
# This YAML file is used to define a GitHub Actions workflow for deploying a Pelican website to GitHub Pages.
# The workflow will be triggered when there is a push event on the 'main' branch.

name: Deploy Pelican to GitHub Pages

on:
  push:
    branches:
      - main  

jobs:
  # This is the main job called 'deploy'.
  deploy:
    # The job will run on the latest version of Ubuntu.
    runs-on: ubuntu-latest
    steps:
      # The first step is to check out the repository.
      - name: Checkout
        uses: actions/checkout@v2

      # The second step is to set up Python.
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'

      # The third step is to install the project dependencies.
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install ghp-import

      # The fourth step is to build the Pelican website.
      - name: Build with Pelican
        run: pelican content -o output -s publishconf.py
        working-directory: projects/tech

      # The final step is to deploy the generated website to GitHub Pages using the 'peaceiris/actions-gh-pages' action.
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./projects/tech/output
```

### actions/checkout@v2

`actions/checkout@v2` 是一个 GitHub Actions 中的一个预定义的操作（也称为 Action），用于将代码仓库检出到工作环境中。这个操作允许您在 GitHub Actions 工作流程中获取代码库的副本，以便在后续步骤中执行构建、测试、部署等操作。

具体来说，`actions/checkout@v2` 操作做了以下事情：

1. 克隆或检出您的代码仓库，将代码复制到工作目录中。
2. 设置工作目录以包含检出的代码，以便后续步骤可以在其中运行。
3. 可以配置以检出特定分支、标签或提交，或者使用默认设置来检出默认分支（通常是 "main" 或 "master"）。

此操作是 GitHub Actions 社区维护的官方操作之一，通常用于设置工作流程以执行各种 CI/CD 任务。使用此操作可以使您的工作流程更容易编写和维护，因为它处理了代码检出的许多细节。

要在 GitHub Actions 工作流程中使用 `actions/checkout@v2` 操作，通常需要在 workflow 文件的步骤中添加一个名为 "Checkout"（或其他您喜欢的名称）的步骤，并指定使用 `actions/checkout@v2` 操作。

示例：

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v2
```

这个步骤将在工作流中使用 `actions/checkout@v2` 操作来检出代码。

### actions/setup-python@v2

`actions/setup-python@v2` 是 GitHub Actions 中的一个官方操作，用于设置 Python 环境，以便您可以在 GitHub Actions 工作流程中执行 Python 相关的任务。它允许您指定要使用的 Python 版本，并设置 Python 环境的各种配置选项。

具体来说，`actions/setup-python@v2` 操作可以执行以下操作：

1. 安装指定版本的 Python 或 PyPy。您可以指定所需的 Python 版本，例如 Python 3.6、Python 3.7、Python 3.8 等等。

2. 设置 PATH 环境变量，以便工作流程中的后续步骤可以访问所安装的 Python 可执行文件。

3. 可以选择安装 pip 包管理器，以便在工作流程中安装 Python 依赖项。

4. 支持各种操作系统，包括 Windows、Linux 和 macOS。

这个操作非常有用，因为它使得在 GitHub Actions 中设置 Python 环境变得简单，并且允许您轻松地切换和测试不同版本的 Python。您可以在工作流程中使用这个操作来执行各种 Python 相关的任务，例如运行测试、构建 Python 应用程序或执行其他与 Python 相关的操作。

示例用法：

```yaml
- name: Set up Python
  uses: actions/setup-python@v2
  with:
    python-version: 3.8  # 指定要安装的 Python 版本
```

上述示例中，工作流程将设置 Python 3.8 环境以供后续步骤使用。您可以根据您的项目需求和 Python 版本要求来配置此操作。

### peaceiris/actions-gh-pages@v3

`peaceiris/actions-gh-pages@v3` 是一个 GitHub Actions 的操作（Action），用于将静态网站或其他内容发布到 GitHub Pages。这个操作是由社区维护的，它简化了将内容发布到 GitHub Pages 的流程。

具体来说，`peaceiris/actions-gh-pages` 操作提供了以下功能：

1. 自动构建静态网站或其他内容：您可以配置操作来自动构建您的静态网站或其他内容，例如生成文档、编译应用程序等。

2. 将构建后的内容推送到 GitHub Pages 分支：操作会将构建后的内容推送到一个指定的 GitHub Pages 分支，通常是 `gh-pages` 分支。

3. 自动设置 GitHub Pages：操作还会自动设置 GitHub Pages，使您的网站或内容可以在 GitHub Pages 上在线访问。

4. 支持自定义配置：您可以根据需要自定义操作的行为，例如指定构建命令、指定发布的分支等。

GitHub Actions 的操作是用于自动化 CI/CD 流程的组件，您可以在 GitHub Actions 工作流程中使用它们。`peaceiris/actions-gh-pages` 操作通常用于构建和发布静态网站，以便在 GitHub Pages 上托管。

要了解如何在 GitHub Actions 中使用 `peaceiris/actions-gh-pages` 操作，请查阅相关文档和示例。操作的版本号 `v3` 表示操作的版本，通常建议使用最新版本以获得最新的功能和改进。

## 问题

### 权限问题报错

解决方法：修改actions权限。

参考：[Action failed with "The process '/usr/bin/git' failed with exit code 128"](https://stackoverflow.com/questions/76023778/action-failed-with-the-process-usr-bin-git-failed-with-exit-code-128)
