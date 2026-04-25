# BabyAGI Architecture Research Report

## 1. Core Agentic Loop
The original BabyAGI framework (as seen in `babyagi_archive`) operates on a simple, infinite execution loop driven by an overarching **Objective** and an **Initial Task**. The loop is controlled by the `main()` function and consists of four main phases:
1. **Execution**: The first task is pulled from the queue and passed to the `execution_agent`, along with retrieved context from memory.
2. **Memory Storage**: The result of the execution is saved in a vector database (e.g., Chroma, Weaviate, Pinecone) via `results_storage.add()`.
3. **Task Creation**: The `task_creation_agent` evaluates the result of the completed task against the main objective and generates new tasks if necessary.
4. **Prioritization**: The `prioritization_agent` takes the updated list of pending tasks and reorders them based on their importance to the main objective.

This loop repeats as long as there are tasks in the queue.

## 2. Task Management & Queueing
- **Task Storage**: Tasks are maintained in memory using a simple double-ended queue (`collections.deque`), managed by the `SingleTaskListStorage` class (or `CooperativeTaskListStorage` for distributed runs). 
- **Task Structure**: Each task is a dictionary containing a `task_id` and a `task_name` (which acts as the description).
- **Queue Operations**: Tasks are popped from the left (`popleft()`), and new tasks are appended to the right. The entire queue can be completely replaced after reprioritization.

## 3. Feedback Loops & Agents
BabyAGI relies on three specialized LLM prompts (agents) to manage the feedback loop:

### Execution Agent (`execution_agent`)
- **Inputs**: Main Objective, current Task, Context (up to 5 relevant past task results retrieved from the vector DB).
- **Role**: Performs the task given the context and objective, returning a result string.

### Task Creation Agent (`task_creation_agent`)
- **Inputs**: Main Objective, Result of the last task, Description of the last task, List of currently incomplete tasks.
- **Role**: Analyzes the outcome of the last task. Determines what new tasks need to be created to achieve the overarching objective.
- **Constraint**: It is explicitly instructed not to overlap with the existing incomplete tasks. It returns a numbered list of new tasks.

### Prioritization Agent (`prioritization_agent`)
- **Inputs**: Main Objective, List of all incomplete tasks.
- **Role**: Evaluates the list of tasks and reorders them from highest to lowest priority, prioritizing tasks that are prerequisites. It returns a newly ordered numbered list, which replaces the existing queue.

## 4. Context & Memory Management
- BabyAGI uses an embedding database (Chroma by default) to store completed tasks as vectors.
- The `context_agent` function queries this database using the main objective (or current task) to retrieve the top `n` most relevant past results, which are then fed into the `execution_agent` to provide historical context and prevent redundant work.

## Summary
BabyAGI's architecture is a seminal example of a **Plan-Execute-Evaluate** loop. Its strength lies in its dynamic queue management, where the system continuously evaluates its own outputs and adjusts its roadmap (task list) autonomously based on the current state.
