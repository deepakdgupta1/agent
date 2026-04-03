# Goal: Functional and Architectural Synthesis of the "Master AI Agent Blueprint"

**Context:**
I am designing a next-generation AI Agent. I have an indicative 7-level analysis framework/ feature hierarchy (`AI Agent Feature Hierarchy Development.md`) and a set of popular reference agents (`references.md`). 

## Task Description
You are an AI Systems Architect tasked with creating a modular, technical, and functional documentation suite that deconstructs modern AI agents. You will ground your analysis by reverse-engineering and researching real-world agents found in `references.md` using appropriate framework. You can refer to `AI Agent Feature Hierarchy Development.md` as an initial baseline for such a framework but you are free to iteratively modify it throughout this exercise based on your learnings from the analysis and your judgment regarding the best possible representation of the functional and technical architecture of AI agents.

## Objective
Produce a logically organized folder structure (`docs/`) containing modular files that detail the functional and technical "super-set" of capabilities across all analyzed agents.

## Core Methodology: The Iterative Refinement Loop
1. **Selection**: Pick the first agent from `references.md` (e.g., Aider or Claude Code). 
2. **Deep-Dive (Version 1)**: Perform a deep-dive into its technical and functional architecture.
    - Create a modular documentation set.
    - Technical details must reach "flow-chart" depth using Mermaid diagrams.
    - **Analysis Framework & Feature Hierarchy Evolution**: Refine the analysis framework and the feature hierarchy based on the findings from the deep-dive, if deemed useful, valuable and therefore required.
    - Map features to the improved analysis framework and the feature hierarchy.
3. **Refinement (Version N)**: Select the next agent from the list and perform a deep-dive into its technical and functional architecture.
    - Compare its capabilities with the current documentation.
    - **Analysis Framework & Feature Hierarchy Evolution**: Refine or expand the analysis framework and the feature hierarchy if real-world discoveries suggest a more accurate structure.
    - Update the documents to reflect new discovered patterns, technical flows, or functional capabilities while maintaining the modularity of the documentation.
    - Any new technical details (or improvements to existing ones) discovered must be documented upto the same depth as the previous versions.
    - Use a mechanism to delineate or tag individual real-world agent specific contents from the agnostic blueprint. Reading the final output should tell me which specific real-world agent contributed what specific content to the blueprint
4. **Finalization**: Continue until all agents in `references.md` are analyzed, resulting in a comprehensive "Master Framework."

## Documentation Requirements
- **Location**: All outputs under a `docs/` folder. Create one if one doesn't already exist.
- **Modularity**: Avoid monolithic files. Split documentation by topic (e.g., `memory/`, `cognition/`, `action_orchestration/`).
- **Functional and Technical Depth**: Every major functional and technical flow (e.g., prompt loops, tool calling sequences, memory retrieval) must be detailed with step-by-step logic flow and accompanied by a Mermaid diagram and a sequence diagram (showing data and control flow). Avoid high-level marketing descriptions.
- **Hierarchy Mapping**: Maintain an `architectural_hierarchy.md` file that evolves through each version.
- **Out of Scope**: Harness Engineering (installation/packaging details) content that is built outside the AI Agents in order to enable the AI Agents perform long complex tasks autonomously without experiencing context loss or drift. 
- **In Scope**: Focus strictly on the logic, flow, and architecture of the AI Agent itself.

## Starting Instructions
Ask me further clarification questions if needed. Then draft a plan to execute this massive exercise (`implementation_plan.md`) and get my approval for the same.
