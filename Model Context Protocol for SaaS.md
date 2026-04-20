# **Architectural Principles and Interface Design Patterns for the Model Context Protocol in SaaS Ecosystems**

The formalization of the Model Context Protocol (MCP) by Anthropic in late 2024 represents a fundamental shift in the structural integration of large language models with external data systems and executable environments.1 Prior to this standardization, the industry faced an "N×M" integration problem, characterized by the requirement for bespoke connectors for every unique combination of artificial intelligence (AI) application and data source.1 The protocol establishes a universal interface for reading files, executing functions, and handling contextual prompts, functioning as a standardized "USB-C" port for the AI ecosystem.1 For Software-as-a-Service (SaaS) providers, designing an MCP interface is not merely a task of API wrapping but an exercise in context engineering and agentic orchestration. This report examines the considerations, patterns, and principles essential for architecting robust MCP interfaces within SaaS environments.

## **Foundational Architecture and Protocol Mechanics**

The Model Context Protocol operates on a client-server architecture designed to maintain stateful communication over a variety of transport layers.3 Within this framework, three distinct roles are defined: the host, the client, and the server. The host is the primary LLM-powered application, such as an integrated development environment (IDE) or a corporate chat interface, which orchestrates the overall user experience.3 The client resides within the host and initiates connections to various MCP servers, managing the lifecycle of these sessions and enforcing security policies.3 The server acts as a lightweight process that exposes specific resources, tools, and prompts to the client.5

Communication is standardized using JSON-RPC 2.0, providing a structured format for requests, responses, and notifications.6 The choice of transport layer is a critical consideration for SaaS applications, as it dictates the physical path of data transmission and the scalability of the integration.

### **Comparative Analysis of Transport Protocols**

SaaS applications must select a transport layer based on the locality of resources and the requirement for real-time interaction. While local tools may rely on standard input/output (stdio), remote SaaS integrations predominantly utilize web-based protocols.7

| Transport Protocol | Mechanism | Primary Use Case | Scaling Characteristics |
| :---- | :---- | :---- | :---- |
| **Standard I/O (stdio)** | Pipe-based communication between local processes. | Local files, system tools, and development utilities.7 | High performance; limited to a single machine.7 |
| **Server-Sent Events (SSE)** | HTTP-based unidirectional streaming from server to client. | Remote SaaS APIs and cloud-hosted data sources.6 | Horizontally scalable; requires separate endpoint for client-to-server.7 |
| **Streamable HTTP** | Enhanced HTTP streaming introduced in 2026\. | Modern production SaaS environments and enterprise gateways.8 | Optimized single-endpoint model; simplifies dual-endpoint SSE.8 |

The evolution toward Streamable HTTP reflects the industry's need for a simplified, more efficient delivery mechanism for remote resources.9 This transition is particularly relevant for SaaS platforms that must support thousands of concurrent agentic sessions without the overhead of maintaining complex SSE state across distributed systems.8

### **Session Lifecycle and Version Negotiation**

The establishment of an MCP session begins with an initialization phase where the client and server negotiate protocol versions and exchange capabilities.8 This negotiation ensures that both parties agree on a single version for the duration of the session, using a YYYY-MM-DD versioning format.8 If negotiation fails, the protocol mandates a graceful termination, allowing the client to provide meaningful feedback to the host.8 This handshake is essential for SaaS environments where servers may be updated independently of the host applications, necessitating backward compatibility and robust error handling during the initial connection.5

## **Primitives of the Interface: Tools, Resources, and Prompts**

The MCP interface is composed of three primary building blocks that define how an AI model perceives and interacts with the SaaS application. These primitives must be modeled carefully to ensure the model can reason about them effectively while maintaining security and efficiency.5

### **Tools: The Verbs of Interaction**

Tools are executable functions that allow a model to take actions within the SaaS environment.11 In an MCP context, tools are not just API endpoints; they are "model-facing" affordances that carry descriptions of preconditions, success criteria, and intent.13 For a SaaS application like Slack, tools might include send\_message or list\_channels.3 A critical design principle is that tools should be narrow and atomic. Rather than a generic manage\_project tool, a SaaS provider should offer discrete tools like create\_task, assign\_user, and update\_status.5 This granularity reduces the cognitive load on the model, decreasing the likelihood of hallucinations or incorrect parameterization.5

### **Resources: The Nouns of Context**

Resources represent the data "nouns" that provide necessary context to the model.5 These can be static files, dynamic database schemas, or real-time application states like a Figma design frame.3 Each resource is uniquely identified by a URI, which allows the model to reference and retrieve specific pieces of information.3 For SaaS platforms, resources are often surfaced through application-driven heuristics or explicit user selection in a context picker.15 For example, a CRM application might expose a specific customer record as a resource, allowing the AI to analyze historical interactions before generating a response.3

### **Prompts: The Workflows of Guidance**

Prompts in MCP are predefined templates that guide complex tasks and standardize common LLM interactions.16 They can accept dynamic arguments and include context from resources, acting as guided workflows or "slash commands" in the client UI.16 For an enterprise troubleshooting tool, a prompt named analyze-logs might require a fileUri and a timeframe argument, providing the model with optimized instructions for diagnosing system issues.16 This allows SaaS vendors to encapsulate best practices and domain expertise into reusable templates that steer the model toward desired behaviors.16

## **SaaS Integration Patterns**

The implementation of MCP within a SaaS ecosystem typically follows one of several established architectural patterns, each addressing different integration challenges and use cases.3

### **The SaaS Platform Wrapper**

The most common pattern is the SaaS platform wrapper, where an enterprise vendor provides an MCP server that acts as a standardized adapter for their proprietary API.3 This pattern is exemplified by the official GitHub and Slack MCP servers.3 These wrappers abstract away the complexities of OAuth scopes, rate limiting, and real-time messaging APIs, presenting the AI with a clean set of tools and resources.3 This enables agent developers to integrate platform functionality seamlessly into workflows without managing the "plumbing" of individual SaaS integrations.3

### **The Tool Catalog and Adapter Hub**

In complex environments where agents must interact with dozens of different services, the Tool Catalog or "Adapter Hub" pattern is employed.3 Often provided by agent frameworks like LangChain, this server acts as a proxy for multiple underlying SaaS APIs (e.g., Stripe, HubSpot, and Salesforce).3 It re-emits these functionalities as a unified collection of MCP tools, allowing a central "manager agent" to select the appropriate tool for a given task deterministically.3 This pattern dramatically reduces the combinatorial explosion of connectors and centralizes the management of third-party capabilities.3

### **The Retrieval (RAG) Server**

The Retrieval-Augmented Generation (RAG) server pattern is critical for SaaS applications that manage large repositories of proprietary knowledge.3 Instead of exposing all data at once, the server provides tools like search\_corpus or get\_chunk to retrieve relevant document snippets on demand.3 This architecture ensures that sensitive, firewall-protected documents remain within the SaaS environment while still being accessible to external AI agents for context-aware generation.3 In some instances, the server may utilize "sampling" to pre-summarize long documents before returning them to the client, optimizing token usage and ensuring privacy.3

### **LLM-Powered and Specialized Reasoning Tools**

Some SaaS applications may offer specialized reasoning tools that utilize their own internal LLM instances. These "LLM-powered tools" can perform complex data analysis or transformation before returning a result to the primary agent.3 A "Sequential Thinking" server, for example, might provide a tool that helps an agent reflect on its problem-solving process, effectively acting as a sub-agent architecture that enhances the reasoning capabilities of the host model.17

## **Principles of Model-Centric Interface Design**

Designing an MCP interface requires shifting from traditional human-centric design to "model-centric" engineering. The goal is to make the model succeed on the first try by providing high-quality context and stable, predictable interfaces.5

### **Strict Schema Enforcement and Stable Types**

LLMs are prone to "hallucinating" types and parameters when faced with ambiguous APIs. SaaS providers must lock down tool interactions with explicit JSON schemas.5 This includes using enums for categorical data (e.g., status ∈ {OPEN, CLOSED, PENDING}) and requiring specific identifiers like UUIDs rather than raw names.5 Output schemas are equally important, as they guide the model in parsing and utilizing the returned data effectively.11 Once a tool's schema is defined, any changes must be managed through versioning or backward-compatible updates to avoid breaking existing agent workflows.5

### **Context Engineering and Information Density**

The "context" in MCP refers to the holistic state available to the model at any given time.17 Effective context engineering involves optimizing the utility of tokens against the inherent constraints of LLMs.17 SaaS interfaces should provide "token-efficient" information, using techniques like compaction and structured note-taking to ensure the most relevant data is present in the context window.17 Returning a raw data dump is an anti-pattern; instead, servers should provide a summary of the data alongside the machine-readable payload.5

| Context Component | Role in Interface Design | Implication for SaaS |
| :---- | :---- | :---- |
| **System Prompts** | Provide high-level heuristics and operational guardrails.17 | Defines the "Goldilocks zone" between vague guidance and brittle logic.17 |
| **Structured Output** | Ensures the model can parse results without ambiguity.11 | Essential for multi-step agentic pipelines.20 |
| **Resource Annotations** | Provide hints on priority, audience, and modification time.15 | Helps the client filter and prioritize context for the model.15 |
| **Progress Reporting** | Keeps the user and model informed during long operations.14 | Improves the perceived reliability of agentic actions.14 |

### **Determinism and Idempotency**

For state-changing operations, such as creating a record in a database or sending a transaction, the interface must be deterministic and idempotent.5 SaaS applications should implement idempotencyKey mechanisms to prevent duplicate actions if the model retries a tool call due to a network interruption or session failure.5 Treating the "last mile" of tool execution as a deterministic process ensures that non-deterministic model planning meets reliable, predictable execution.13

## **Multi-Tenancy and Gateway Architectures**

For SaaS applications serving multiple customers, enforcing tenant isolation and secure routing is a primary architectural concern.8 The MCP Gateway pattern provides a centralized point for governance, data isolation, and complex authentication.8

### **The MCP Gateway Pattern**

In a multi-tenant environment, the gateway acts as the intermediary between AI clients and backend MCP servers.8 It handles identity management (SSO, OIDC) and ensures that each customer's request is routed to their specific instance or data partition.8 This architecture allows SaaS vendors to manage API keys, metering, and billing centrally while maintaining strict data segregation between tenants.8

### **Tenant Isolation and Resource Routing**

Tenant isolation ensures that one customer cannot access another customer's tools or data.22 In an MCP context, this isolation can be implemented at multiple layers:

1. **URI-Based Isolation:** Designing resource URIs to include tenant identifiers (e.g., tenant://{tenant\_id}/docs/report.pdf).10  
2. **JWT Claim Mapping:** Using the authentication context provided by upstream middleware to evaluate access control policies based on user groups or tenant IDs.10  
3. **Database-Level Security:** Implementing row-level security or query rewriting to ensure the LLM only ever sees data it is authorized to access.5

| Isolation Layer | Mechanism | SaaS Benefit |
| :---- | :---- | :---- |
| **Gateway Policy** | Expression-based matching of JWT claims against tool/resource names.10 | Centralized "allow-lists" and fine-grained control.10 |
| **Service Middleware** | Automatic injection of tenant filters into MCP requests.5 | Prevents cross-tenant data leakage by design.10 |
| **Resource Filtering** | Dynamic removal of unauthorized items from tools/list or resources/list responses.10 | Reduces the discovery of sensitive capabilities by unauthorized agents.10 |

## **Human-Facing Interface Design Principles**

While much of MCP design focuses on the interaction between the client and the model, the protocol explicitly advocates for "human-in-the-loop" (HITL) designs to ensure safety and accountability.11 SaaS applications must provide UI elements that make the AI's actions transparent to the end-user.

### **Confirmation Dialogs and Visual Framing**

Critical or destructive actions, such as deleting a user account or modifying a production environment, should always require explicit human approval.11 The MCP specification suggests that applications should insert clear visual indicators when tools are invoked and present confirmation prompts that summarize the consequences of the action.11

| UI Pattern | Design Guideline | Impact on Trust |
| :---- | :---- | :---- |
| **Specific Titles** | Clearly state the action (e.g., "Permanently Delete Folder?").25 | Reduces cognitive load and prevents mistakes.25 |
| **Action-Based Labels** | Use buttons like "Delete File" and "Keep File".25 | Improves confidence and reduces misclicks.25 |
| **Visual Contrasts** | Use color (red) and iconography (warning signs) to signal risk.25 | Alerts the user to the severity of the action.25 |
| **Friction Mechanisms** | Require manual input (e.g., typing "DELETE") for high-risk actions.25 | Prevents "automated clicking" behavior.26 |

For SaaS designers, this means moving beyond generic "Are you sure?" prompts toward "Signature Interaction Designs" that use domain-specific color and metaphors to establish intent.27 This "Craft" foundation involves subtle surface layering and visual hierarchies that ensure the interface feels bespoke and aligned with the product's identity.27

### **Elicitation and Interactive Dialogs**

The June 2025 update to the protocol introduced "Elicitation," a mechanism allowing servers to request additional input from users via the client.20 This enables multi-step workflows where an agent can pause its execution to ask the user for a choice, a text input, or a confirmation before proceeding.20 For instance, a "GitHub" MCP server might use elicitation to ask a developer to choose which branch a pull request should be merged into after analyzing the repository's status.20 This interactive model ensures the user maintains control over the AI's decision-making process.3

## **Security Governance and Risk Mitigation**

Exposing SaaS systems to LLMs through MCP introduces significant security risks, including prompt injection, remote code execution (RCE), and the "confused deputy" problem.1 Security must be "baked in" from the start, following the principle of zero-trust architecture.5

### **Threat Models and Real-World Vulnerabilities**

Early deployments of MCP have revealed critical vulnerabilities that SaaS providers must address:

* **Remote Code Execution:** CVE-2025-49596 highlighted a flaw where an official tool allowed unauthenticated users to execute arbitrary commands on a host machine.30  
* **Prompt Injection:** "Poisoned" prompts smuggled into ticket comments or data sources can hijack an agent's elevated privileges to perform unauthorized actions, such as account deactivation.30  
* **Data Siphoning:** Maliciously crafted OAuth proxy flows can trick an MCP proxy into issuing authorized tokens to an attacker's domain.3

### **Security Principles for SaaS MCP Servers**

To mitigate these risks, SaaS providers must adhere to rigorous security standards:

* **Least Privilege:** Tools should only expose the minimum necessary surface area. For example, a "PostgreSQL" server should provide specific, pre-defined query tools rather than allowing arbitrary SQL execution.5  
* **Robust Auth and RBAC:** Treat MCP servers as protected resources. Use OAuth 2.1 with Resource Indicators to ensure tokens are used only for their intended purpose.20 Implement tool-level Role-Based Access Control to ensure only authorized users can call sensitive functions.8  
* **Data Redaction and Privacy:** Servers must sanitize outputs to ensure sensitive PII or raw system internals are never leaked to the model or recorded in logs.5  
* **Sandboxing:** Run MCP servers in isolated environments, such as Docker containers or sandboxed processes, to restrict their ability to exfiltrate data or access unauthorized system resources.23

## **Observability and Lifecycle Management**

Maintaining a production-ready MCP interface requires comprehensive observability and structured evaluation to ensure the system remains reliable and safe over time.5

### **The Three-Tier Error Model**

Effective error handling is vital for allowing AI agents to recover from failures without crashing the session.31 MCP servers should implement a hierarchy of errors:

1. **Transport Errors:** Handled by the underlying protocol (e.g., SSE connection drops).31  
2. **Protocol Errors:** Standard JSON-RPC errors (codes \-32000 to \-32768) for issues like "Method not found" or "Invalid params".11  
3. **Application Errors:** Reported in the tool result with isError: true for business logic failures or API timeouts.11 This allows the model to see the specific reason for failure and potentially attempt a different strategy or request help from the user.31

### **Logging and Monitoring**

The protocol provides a standardized logging/setLevel method that allows clients to control the verbosity of log messages sent by the server.21 SaaS providers should use these levels (debug, info, warning, error, critical) to provide an audit trail of agent activities while ensuring that sensitive data is redacted from the logs.21

| Log Level | Purpose | SaaS Example |
| :---- | :---- | :---- |
| **Debug** | Detailed technical information for troubleshooting. | Function entry/exit points in a custom tool.21 |
| **Info** | Significant operational updates. | Progress notifications for a long-running data export.21 |
| **Warning** | Indications of potential future issues. | Usage of a deprecated API or feature.21 |
| **Error** | Operational failures that prevent task completion. | External API timeout or validation failure.21 |
| **Critical** | Major system component failures. | Loss of connection to the primary database.21 |

### **Evaluation and Golden Tasks**

To ensure the interface continues to perform correctly as the underlying model or protocol evolves, developers should build a suite of "golden tasks".5 These are a curated set of prompts reflecting real-world usage (e.g., "Find all overdue invoices for Tenant A") that are run regularly against the MCP server.5 By storing and comparing the expected inputs and outputs, SaaS teams can identify regressions in tool usage, latency spikes, or increases in error rates before they impact end-users.5

## **Conclusion: The Strategic Evolution of SaaS Interoperability**

The Model Context Protocol represents more than just a technical standard; it is a strategic shift toward a modular, context-aware AI ecosystem. For SaaS applications, the interface is the primary boundary between their proprietary data and the increasing intelligence of global AI systems. By adopting established design patterns—such as the Gateway architecture for multi-tenancy and the HITL interactive model for safety—providers can securely and effectively empower AI agents to act on behalf of their users.2

Success in this new paradigm requires moving away from "YOLO-deployments" toward a disciplined approach to context engineering.5 This includes the implementation of narrow, atomic tools, stable type systems, and robust governance baked into the infrastructure.5 As the protocol evolves with features like Streamable HTTP and enhanced elicitation, the complexity of designing these interfaces will only increase.9 However, the reward is a significantly reduced barrier to entry for AI-driven workflows, transforming the SaaS application from a static data silo into a dynamic, agent-enabled platform capable of sophisticated reasoning and autonomous action in the service of its users.1

#### **Works cited**

1. Model Context Protocol \- Wikipedia, accessed April 5, 2026, [https://en.wikipedia.org/wiki/Model\_Context\_Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol)  
2. What is the Model Context Protocol (MCP)? \- Model Context Protocol, accessed April 5, 2026, [https://modelcontextprotocol.io/docs/getting-started/intro](https://modelcontextprotocol.io/docs/getting-started/intro)  
3. Model Context Protocol (MCP) explained: A practical technical overview for developers and architects \- CodiLime, accessed April 5, 2026, [https://codilime.com/blog/model-context-protocol-explained/](https://codilime.com/blog/model-context-protocol-explained/)  
4. Specification \- Model Context Protocol, accessed April 5, 2026, [https://modelcontextprotocol.io/specification/2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25)  
5. Building Smarter MCP Servers — From Theory to Practice | Clever ..., accessed April 5, 2026, [https://www.clever.cloud/blog/engineering/2025/10/01/building-smarter-mcp-servers/](https://www.clever.cloud/blog/engineering/2025/10/01/building-smarter-mcp-servers/)  
6. Model Context Protocol (MCP) Explained With Examples \- AltexSoft, accessed April 5, 2026, [https://www.altexsoft.com/blog/model-context-protocol/](https://www.altexsoft.com/blog/model-context-protocol/)  
7. What is Model Context Protocol (MCP)? A guide | Google Cloud, accessed April 5, 2026, [https://cloud.google.com/discover/what-is-model-context-protocol](https://cloud.google.com/discover/what-is-model-context-protocol)  
8. Model Context Protocol (MCP): The Complete Engineering Guide ..., accessed April 5, 2026, [https://medium.com/@rishabhkr954/model-context-protocol-mcp-the-complete-engineering-guide-architecture-internals-and-0d7b5d988b08](https://medium.com/@rishabhkr954/model-context-protocol-mcp-the-complete-engineering-guide-architecture-internals-and-0d7b5d988b08)  
9. Why MCP's Move Away from Server Sent Events Simplifies Security, accessed April 5, 2026, [https://auth0.com/blog/mcp-streamable-http/](https://auth0.com/blog/mcp-streamable-http/)  
10. Model Context Protocol (MCP) | Traefik Hub Documentation, accessed April 5, 2026, [https://doc.traefik.io/traefik-hub/mcp-gateway/mcp](https://doc.traefik.io/traefik-hub/mcp-gateway/mcp)  
11. Tools \- Model Context Protocol, accessed April 5, 2026, [https://modelcontextprotocol.io/specification/2025-11-25/server/tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)  
12. MCP Architecture Deep Dive: Tools, Resources, and Prompts Explained \- Knit API, accessed April 5, 2026, [https://www.getknit.dev/blog/mcp-architecture-deep-dive-tools-resources-and-prompts-explained](https://www.getknit.dev/blog/mcp-architecture-deep-dive-tools-resources-and-prompts-explained)  
13. Model Context Protocol (MCP): 3 Misconceptions and Fixes \- Docker, accessed April 5, 2026, [https://www.docker.com/blog/mcp-misconceptions-tools-agents-not-api/](https://www.docker.com/blog/mcp-misconceptions-tools-agents-not-api/)  
14. Tools \- Stainless MCP Portal, accessed April 5, 2026, [https://www.stainless.com/mcp/tools](https://www.stainless.com/mcp/tools)  
15. Resources \- Model Context Protocol, accessed April 5, 2026, [https://modelcontextprotocol.io/specification/draft/server/resources](https://modelcontextprotocol.io/specification/draft/server/resources)  
16. Prompts \- Model Context Protocol, accessed April 5, 2026, [https://modelcontextprotocol.io/legacy/concepts/prompts](https://modelcontextprotocol.io/legacy/concepts/prompts)  
17. Effective context engineering for AI agents \- Anthropic, accessed April 5, 2026, [https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)  
18. Developing a sample app with the Slack MCP Server, accessed April 5, 2026, [https://docs.slack.dev/ai/slack-mcp-server/developing/](https://docs.slack.dev/ai/slack-mcp-server/developing/)  
19. modelcontextprotocol/servers: Model Context Protocol Servers \- GitHub, accessed April 5, 2026, [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)  
20. MCP Elicitation: Human-in-the-Loop for MCP Servers \- DEV Community, accessed April 5, 2026, [https://dev.to/kachurun/mcp-elicitation-human-in-the-loop-for-mcp-servers-m6a](https://dev.to/kachurun/mcp-elicitation-human-in-the-loop-for-mcp-servers-m6a)  
21. Logging \- Model Context Protocol, accessed April 5, 2026, [https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/logging](https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/logging)  
22. Enforcing tenant isolation \- AWS Prescriptive Guidance, accessed April 5, 2026, [https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/enforcing-tenant-isolation.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/enforcing-tenant-isolation.html)  
23. Model Context Protocol (MCP) Security Risks Explained \- Veeam, accessed April 5, 2026, [https://www.veeam.com/blog/model-context-protocol-security-risks.html](https://www.veeam.com/blog/model-context-protocol-security-risks.html)  
24. Tools \- Model Context Protocol, accessed April 5, 2026, [https://modelcontextprotocol.io/specification/2025-06-18/server/tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)  
25. Confirmation dialogs: How to design dialogs without irritation \- UX Planet, accessed April 5, 2026, [https://uxplanet.org/confirmation-dialogs-how-to-design-dialogues-without-irritation-7b4cf2599956](https://uxplanet.org/confirmation-dialogs-how-to-design-dialogues-without-irritation-7b4cf2599956)  
26. Confirmation Dialogs Can Prevent User Errors (If Not Overused) \- NN/G, accessed April 5, 2026, [https://www.nngroup.com/articles/confirmation-dialog/](https://www.nngroup.com/articles/confirmation-dialog/)  
27. Interface Design Claude Code Skill | Custom SaaS UI Tool \- MCP Market, accessed April 5, 2026, [https://mcpmarket.com/tools/skills/interface-design-specialist](https://mcpmarket.com/tools/skills/interface-design-specialist)  
28. Interface Design Claude Code Skill | SaaS UI Architect \- MCP Market, accessed April 5, 2026, [https://mcpmarket.com/tools/skills/saas-app-interface-design](https://mcpmarket.com/tools/skills/saas-app-interface-design)  
29. GongRzhe/Human-In-the-Loop-MCP-Server \- GitHub, accessed April 5, 2026, [https://github.com/GongRzhe/Human-In-the-Loop-MCP-Server](https://github.com/GongRzhe/Human-In-the-Loop-MCP-Server)  
30. The MCP Security Survival Guide: Best Practices, Pitfalls, and Real ..., accessed April 5, 2026, [https://towardsdatascience.com/the-mcp-security-survival-guide-best-practices-pitfalls-and-real-world-lessons/](https://towardsdatascience.com/the-mcp-security-survival-guide-best-practices-pitfalls-and-real-world-lessons/)  
31. Error Handling in MCP Servers \- Best Practices Guide \- MCPcat, accessed April 5, 2026, [https://mcpcat.io/guides/error-handling-custom-mcp-servers/](https://mcpcat.io/guides/error-handling-custom-mcp-servers/)