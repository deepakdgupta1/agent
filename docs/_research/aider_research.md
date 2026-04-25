# Aider Architecture Research Report

## 1. Core Loop Analysis
Aider's core execution loop is managed in `aider/coders/base_coder.py`. The execution flows as follows:
- **Input Processing**: The `run_one` method captures user input. It preprocesses inputs, checking for in-chat commands (e.g., `/add`, `/commit`) and resolving URLs.
- **Message Assembly**: `send_message` formats the context. It gathers system prompts, chat history, the repository map (if enabled), and active file contents. Token limits are checked before submission.
- **LLM Request & Streaming**: The message is sent to the LLM. The output is streamed and accumulated (`partial_response_content`).
- **Edit Extraction**: Upon completion, the response is parsed based on the selected `edit_format` (e.g., `editblock`, `udiff`, `wholefile`). The `apply_updates()` method executes these changes on the local file system.
- **Git Integration (Auto-Commit)**: If changes are applied successfully, `auto_commit(edited)` commits the modifications to the local Git repository.
- **Reflections (Auto-Linting/Testing)**: If enabled, Aider runs the linter and tests automatically. If either fails, the errors are captured as a `reflected_message`. Aider feeds this back into the loop autonomously up to `max_reflections` (default: 3) to fix the issues without user intervention.

## 2. Context Engine (Repo-Map)
Aider uses a sophisticated repository map to provide cross-file context without exceeding token limits, implemented in `aider/repomap.py`.
- **AST Parsing**: It uses `tree-sitter` to parse the codebase and extract tags specifically focusing on definitions (`def`) and references (`ref`).
- **Graph Construction**: A directed graph (`networkx.MultiDiGraph`) is built where nodes are files/tags and edges are references. Edge weights scale based on the number of references.
- **PageRank Algorithm**: It runs the PageRank algorithm on this graph. Files currently in the chat and identifiers mentioned by the user receive higher "personalization" (initial weighting). 
- **Context Injection**: The highest-ranked tags are selected up to the `max_map_tokens` limit. These tags are then formatted into a highly condensed tree structure using `grep_ast.TreeContext` and injected into the LLM prompt.

## 3. Edit Formats
Aider supports multiple edit formats depending on the model's capabilities:
- **SEARCH/REPLACE Blocks**: The default for capable models (like GPT-4). The LLM outputs the exact file path, the lines to search for (`<<<<<<< SEARCH`), and the replacement lines (`======= ... >>>>>>> REPLACE`).
- **Whole-file**: The LLM outputs the entire file content. Used for weaker models that struggle with precise diffing.
- **UDiff (Unified Diff)**: Uses standard unified diff formats.
- **Architect/Editor Pattern**: Found in `architect_coder.py`. The "Architect" model acts purely as a planner, thinking through the problem and outlining the solution in natural language. Once the user approves the plan, an "Editor" sub-coder is instantiated with a specific edit format (e.g., SEARCH/REPLACE) to autonomously implement the Architect's plan.

## 4. Git & Shell Integrations
- **Git Backing**: Aider requires a Git repository to function safely. It commits dirty states before making edits and commits its own edits immediately after.
- **Undo Mechanism**: The `/undo` command (`cmd_undo`) identifies the last commit. If it was made by Aider during the current session, it performs a soft reset (`git reset --soft HEAD~1`) and restores the files.
- **Shell Commands**: Aider can propose shell commands for tasks like renaming files or running scripts. Models are explicitly instructed whether they are allowed to propose shell commands via system prompts.
