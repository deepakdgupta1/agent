# Glossary

| Term | Definition |
|---|---|
| Agentic Loop | The core perceive-think-act-observe cycle that an autonomous agent executes. |
| Tool-Call | The mechanism by which an LLM requests execution of an external function (usually via JSON schema). |
| MCP | Model Context Protocol, a standard for connecting AI models to context and tools. |
| Repo-Map | A compressed representation of a codebase (often built with tree-sitter) used to give the LLM context. |
| Context Window | The maximum number of tokens an LLM can process in a single inference pass. |
| Vector Store | A database optimized for storing and retrieving high-dimensional vector embeddings (used for semantic memory). |
| Tree-sitter | A parser generator tool used to build concrete syntax trees and extract structural codebase information. |
| RAG | Retrieval-Augmented Generation, fetching relevant documents from a database to ground the LLM's response. |
| Context Assembly | The process of selecting, truncating, and formatting information to fit within the context window. |
| Semantic Memory | Long-term factual knowledge stored typically in a vector database. |
| Working Memory | Short-term context, such as the conversation buffer of the current session. |
| Episodic Memory | Logs of past events, tool executions, or exact conversational turns. |
| Procedural Memory | Structural logic or behavioral rules the agent follows. |
| Sub-Agent | A subordinate agent spawned by a main agent to handle a specific sub-task with a restricted toolset. |
| CoT (Chain of Thought) | A prompting technique forcing the model to articulate intermediate reasoning steps before answering. |
