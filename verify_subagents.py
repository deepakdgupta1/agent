import os
import glob
import re

class VerificationSubAgent:
    def __init__(self, name, tasks, docs_dir):
        self.name = name
        self.tasks = tasks
        self.docs_dir = docs_dir
        self.report = []

    def log(self, msg):
        self.report.append(f"[{self.name}] {msg}")

    def verify(self):
        raise NotImplementedError

class ScaffoldingAgent(VerificationSubAgent):
    def verify(self):
        self.log("Verifying Task 0 (Scaffolding)")
        expected_dirs = [
            "_research", "00_meta", "01_core_loop", "02_cognition",
            "03_context_engine", "04_memory", "05_action_and_tools",
            "06_orchestration", "07_permissions_and_governance", "08_user_interaction"
        ]
        all_ok = True
        for d in expected_dirs:
            path = os.path.join(self.docs_dir, d)
            if not os.path.isdir(path):
                self.log(f"❌ Missing directory: {d}")
                all_ok = False
        
        meta_files = ["architectural_hierarchy.md", "agent_registry.md", "glossary.md"]
        for f in meta_files:
            if not os.path.exists(os.path.join(self.docs_dir, "00_meta", f)):
                self.log(f"❌ Missing meta file: {f}")
                all_ok = False

        if all_ok:
            self.log("✅ All scaffolding directories and meta files exist.")

class Phase1Agent(VerificationSubAgent):
    def verify(self):
        self.log("Verifying Tasks 1, 2, 3 (Phase 1)")
        aider_res = os.path.join(self.docs_dir, "_research", "aider_research.md")
        baby_res = os.path.join(self.docs_dir, "_research", "babyagi_research.md")
        
        if os.path.exists(aider_res) and os.path.exists(baby_res):
            self.log("✅ Phase 1 research files exist.")
        else:
            self.log("❌ Missing Phase 1 research files.")
            
        # Check files populated in Task 3
        task3_files = [
            "01_core_loop/agentic_loop.md",
            "01_core_loop/prompt_orchestration.md",
            "01_core_loop/turn_lifecycle.md",
            "02_cognition/task_decomposition.md",
            "02_cognition/planning_strategies.md",
            "02_cognition/model_routing.md",
            "03_context_engine/repo_map_and_indexing.md",
            "03_context_engine/context_assembly.md",
            "03_context_engine/token_economics.md",
            "03_context_engine/retrieval_strategies.md",
            "04_memory/working_memory.md",
            "04_memory/semantic_memory.md",
            "05_action_and_tools/code_modification.md",
            "08_user_interaction/input_processing.md",
            "08_user_interaction/feedback_loops.md"
        ]
        
        for f in task3_files:
            path = os.path.join(self.docs_dir, f)
            if not os.path.exists(path):
                self.log(f"❌ Missing populated file: {f}")
                continue
            with open(path, "r") as file:
                content = file.read()
                # Check for tags
                has_tags = "[AIDER]" in content or "[BABYAGI]" in content
                has_mermaid = "```mermaid" in content
                if not has_tags:
                    self.log(f"❌ {f} missing [AIDER]/[BABYAGI] tags.")
                if not has_mermaid:
                    self.log(f"❌ {f} missing mermaid diagram.")
                if has_tags and has_mermaid:
                    self.log(f"✅ {f} looks correctly populated.")

class Phase2Agent(VerificationSubAgent):
    def verify(self):
        self.log("Verifying Tasks 4, 5, 6 (Phase 2)")
        res1 = os.path.join(self.docs_dir, "_research", "claude_code_research_part1.md")
        res2 = os.path.join(self.docs_dir, "_research", "claude_code_research_part2.md")
        
        if os.path.exists(res1) and os.path.exists(res2):
            self.log("✅ Phase 2 research files exist.")
        else:
            self.log("❌ Missing Phase 2 research files.")

        task6_files = [
            "01_core_loop/agentic_loop.md",
            "01_core_loop/prompt_orchestration.md",
            "01_core_loop/turn_lifecycle.md",
            "02_cognition/reasoning_patterns.md",
            "04_memory/persistent_memory.md",
            "05_action_and_tools/tool_architecture.md",
            "05_action_and_tools/command_execution.md",
            "05_action_and_tools/extensibility.md",
            "06_orchestration/multi_agent_patterns.md",
            "07_permissions_and_governance/permission_model.md",
            "07_permissions_and_governance/audit_and_observability.md",
            "08_user_interaction/input_processing.md"
        ]

        for f in task6_files:
            path = os.path.join(self.docs_dir, f)
            if not os.path.exists(path):
                self.log(f"❌ Missing populated file: {f}")
                continue
            with open(path, "r") as file:
                content = file.read()
                if "[CLAUDE]" not in content:
                    self.log(f"❌ {f} missing [CLAUDE] tags.")
                else:
                    self.log(f"✅ {f} contains [CLAUDE] tags.")
                    
        arch_path = os.path.join(self.docs_dir, "00_meta", "architectural_hierarchy.md")
        if os.path.exists(arch_path):
            with open(arch_path, "r") as file:
                content = file.read()
                if "v2" in content.lower():
                    self.log("✅ architectural_hierarchy.md contains v2 reference.")
                else:
                    self.log("❌ architectural_hierarchy.md missing v2 reference.")

if __name__ == "__main__":
    docs_dir = "/Users/deepg/Desktop/agent/docs"
    agents = [
        ScaffoldingAgent("ScaffoldingAgent", [0], docs_dir),
        Phase1Agent("Phase1Agent", [1, 2, 3], docs_dir),
        Phase2Agent("Phase2Agent", [4, 5, 6], docs_dir)
    ]
    
    for agent in agents:
        agent.verify()
        for line in agent.report:
            print(line)
        print("-" * 40)
