# Agentic Copilot Playbook

A concise, practical guide to adopting agentic workflows with Microsoft/GitHub Copilot, delegating safely with human-in-the-loop reviews, and scaling with guardrails.

---

### Purpose

### Agentic Workflow Quickstart (1‑page)
Use this to brief your team and kick off safely.

### What “agentic” means
- Copilot can autonomously implement scoped tasks you delegate, then open a PR and iterate like a junior teammate under review.
- Optional: extend with MCP so the agent can use approved tools and data.

### When to use
- Bug fixes and small refactors
- Tests and coverage improvements
- Docs updates
- Small, incremental features behind flags

### 5‑step flow
1. Issue → Write a well‑scoped issue with acceptance criteria and test expectations  
2. Delegate → Assign the issue to `@copilot` or request a draft PR  
3. CI → Let tests, lint, type‑checks run  
4. Review → Read the diff, leave actionable comments; mention `@copilot` to iterate  
5. Merge → Merge on green; monitor for regressions

### Guardrails to enable first
- Branch protections and required checks: tests, lint, type checks, SAST, deps scan
- Small PRs with rollbacks; feature flags for risky changes
- Least‑privilege MCP tools only

---

### Issue template (pasteable)

**Context**  
- Repo or service:  
- Area of code:  
- Related tickets/PRs:  

**Problem**  
- What is broken or missing?

**Acceptance criteria**  
- [ ] Tests updated or added  
- [ ] Backwards compatible  
- [ ] No public API changes  
- [ ] CI green on PR

**Change hints**  
- Files likely affected:  
- Known edge cases:  

**Out of scope**  
- Anything not listed above

**Definition of done**  
- Draft PR opened: `<ticket-id>: <short summary>`  
- Checklist satisfied and CI passing

---

### Reviewer checklist
- [ ] Scope limited to the issue  
- [ ] Tests cover edge cases  
- [ ] Security: inputs validated, secrets not logged, deps pinned  
- [ ] Perf: no obvious regressions  
- [ ] Reliability: behind flag if risky, rollback is simple  
- [ ] Observability and docs updated

---

### Rollout plan (first 4 weeks)
- Week 1: Docs, tests, tiny bugfixes via `@copilot`  
- Week 2: Refactors and dependency bumps with CI guardrails  
- Week 3: Feature flags and perf work with benchmarks  
- Week 4+: Add MCP integrations, measure lead time, review cycles, and defect rate

---

### Start here videos
- Demo: end‑to‑end agentic development (GitHub) [YouTube](https://www.youtube.com/watch?v=onVn-lnHZ9s&vl=en)  
- Copilot coding agent overview [Docs](https://docs.github.com/en/copilot/concepts/coding-agent/coding-agent)  
- Extend Copilot with MCP [Docs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/extending-copilot-coding-agent-with-mcp)  
- VS Code setup and agent mode [Guide](https://code.visualstudio.com/docs/copilot/getting-started)

---

### Quick start (for busy teams)
- Create an Issue using the Task template  
- Add label `agent:good-first`  
- Ask Copilot to open a draft PR for the Issue  
- Review with the checklist and iterate using comment snippets

---

### When to use Copilot as an agent
- Bug fixes and small refactors  
- Incremental features behind flags  
- Test coverage improvements  
- Documentation updates and code comments  
- Tech debt chores and dependency bumps

<span color="gray">Avoid delegating risky, ambiguous, or architectural changes without tight scoping.</span>

---

### Team Training Path: Adopting Agentic Workflows with Microsoft/GitHub Copilot
A step-by-step curriculum from basics to advanced, with hands-on exercises and checklists.

#### Phase 0 — Prereqs and Setup (1 day)
- Access: Ensure Copilot licenses, repo access, branch protections, CI checks, and SAST are enabled  
- Policies: Define acceptable use, data handling, secret management, and review rules  
- Sandboxes: Create a training repo with safe sample services and test suites  
Outcome: Everyone can use Copilot in PRs and issues without risking production.

#### Phase 1 — Foundations (Week 1)
Goal: Treat issues as prompts and run human-in-the-loop.
1. Issue-as-prompt basics  
   - Use the Task template to create 3 issues per person  
   - Scope to small bugfix, docs, or tests  
2. Copilot in the loop  
   - Ask Copilot to open a draft PR for each issue  
   - Use Comment snippets to iterate  
3. Review discipline  
   - Apply the Review checklist to each PR  
   - Require green CI before merge  
Exercise: Each dev ships 2 small PRs via Copilot with tests updated.

#### Phase 2 — Intermediate: Patterns and Safety (Week 2)
Goal: Delegate incrementally while maintaining safety and quality.
1. Refactors and tests  
   - Extract functions, add unit tests, improve coverage  
2. Dependency updates  
   - Use labels `agent:deps` and `agent:security` for safe bumps with lockfile updates  
3. Observability and docs  
   - Require log lines or metrics and README deltas for changed behavior  
4. Guardrails in CI  
   - Enforce lint, type-check, SAST, dependency scan on PRs  
Exercise: One refactor PR, one dependency PR, both delegated to Copilot with human review.

#### Phase 3 — Advanced: Agentic Workflows (Week 3)
Goal: Multi-step tasks with planning, tools, and rollback strategies.
1. Incremental features behind flags  
   - Copilot drafts feature branch, guarded by config flag or env var  
2. Test-first delegation  
   - Write failing tests, ask Copilot to make them pass, retain coverage thresholds  
3. Performance iteration  
   - Ask Copilot for a faster approach, add benchmark, target 2x speedup  
4. Risk management  
   - Dark launch or canary  
   - Add auto-rollback workflow for critical paths  
Exercise: One feature PR behind a flag plus a performance PR with benchmark and docs.

#### Phase 4 — Integrations and Scale (Week 4+)
Goal: Reduce toil with tool-use, light automations, and governance.
1. Issue/PR automation  
   - Triage labels: `agent:good-first`, `agent:docs`, `agent:tests`, `agent:deps`  
   - Templates for bugs, features, chores  
2. Copilot + MCP (optional)  
   - Start read-only actions, then add write actions for low-risk ops  
3. Knowledge capture  
   - Each PR gets a short "What changed" note and retro items  
4. Metrics and SLOs  
   - Track lead time, review cycles, coverage deltas, defects, and agent% of changes  
Exercise: Enable one safe MCP action and measure time saved across a sprint.

---

### Task template (treat issues like prompts)
Copy this into an Issue when delegating to Copilot.

<callout icon="📝">
	Paste as your issue body
</callout>

**Context**  
- Repo or service:  
- Area of code:  
- Related tickets/PRs:  

**Problem**  
- What is broken or missing?

**Acceptance criteria**  
- [ ] Unit tests updated or added  
- [ ] Backwards compatible  
- [ ] No public API changes  
- [ ] CI green on PR

**Change hints**  
- Files likely affected:  
- Known edge cases:  

**Out of scope**  
- Anything not listed above

**Definition of done**  
- Draft PR opened with title: `<ticket-id>: <short summary>`  
- Checklist satisfied and CI passing

---

### Delegation playbook
1. Write a well-scoped Issue using the template  
2. Ask Copilot to open a draft PR, or mention @copilot on an existing PR  
3. Let CI run. Review diffs like a teammate’s work  
4. Comment with precise, actionable feedback. Use @copilot to iterate  
5. Merge on green. Monitor and log learnings (see Retro template)

---

### Review checklist (human-in-the-loop)
- [ ] Scope: Does the PR address only the Issue?  
- [ ] Tests: Added or updated, cover edge cases  
- [ ] Security: Inputs validated, secrets not logged, dependencies pinned  
- [ ] Performance: No obvious regressions, big‑O sane for data sizes  
- [ ] Reliability: Feature behind flag if risky, rollbacks simple  
- [ ] Observability: Logs or metrics added when relevant  
- [ ] Docs: README or inline comments updated

---

### Comment snippets for fast iteration
- Tests: "@copilot Increase unit test coverage for `<module>`, add edge case for `<condition>`, keep runtime `<N s>`."  
- Refactor: "@copilot Extract `<logic>` into `<file/function>`, keep behavior identical, update imports."  
- Perf: "@copilot Replace O(n^2) loop with map+set, add benchmark, target 2x speedup."  
- Docs: "@copilot Add usage examples and parameter docs to `<function>`, match our docstring style."

---

### CI and guardrails (recommendations)
- Enforce required checks: tests, lint, type checks  
- Run SAST and dependency scanning on PRs  
- Use branch protections and small PRs  
- Canary or dark‑launch risky changes  
- Auto‑rollback workflows for critical paths

---

### Labels and taxonomy
- `agent:good-first` small, low‑risk  
- `agent:docs` documentation-only  
- `agent:tests` tests or coverage  
- `agent:deps` dependency bumps  
- `agent:security` automated remediations

---

### Metrics to track
- Lead time from Issue to merge  
- Review cycles per PR  
- Test coverage delta per week  
- Post-merge defect rate and rollback count  
- Percent of changes by agent vs human

---

### Retro template (copy in PR comments)
**What went well**  
-  

**What to improve**  
-  

**Next time we will**  
-  

---

### Suggested training schedule
- Day 1: Phase 0 kickoff + Phase 1 intro, 2 PRs per dev  
- Day 2–3: Phase 2 labs, dependency and refactor tasks  
- Day 4–5: Phase 3 labs, feature flag + perf benchmark  
- Week 2+: Phase 4 scaling, metrics review, MCP pilot

---

### Common pitfalls and fixes
- Vague issues → Use the template and add out-of-scope section  
- Large PRs → Enforce size limits and split by concern  
- Flaky tests → Quarantine and stabilize before delegating  
- Secret leakage → Pre-commit hooks and secret scanners in CI

---

### References
- GitHub Copilot coding agent overview and delegation entries  
- Best practices for scoping tasks and reviews  
- Org pilot and governance guidance  
- Responsible use on [GitHub.com](http://GitHub.com)  
- MCP for extending agent mode

<callout icon="🔗">
	For internal use, add your org’s links to CI policies, code style guides, and security requirements here.

	### References: Videos and training
	- Demo: end-to-end agentic development with GitHub Copilot — official GitHub video [YouTube](https://www.youtube.com/watch?v=onVn-lnHZ9s&vl=en)
	- From Issue to PR with Copilot Coding Agent — Luke Hoban [YouTube](https://www.youtube.com/watch?v=jq7Ls6T0LYM)
	- GitHub Copilot deep dive: model selection, prompting, agent mode [YouTube](https://www.youtube.com/watch?v=0Oz-WQi51aU)
	- How the GitHub Copilot coding agent works | GitHub Checkout [YouTube](https://www.youtube.com/watch?v=1GVBRhDI5No&pp=0gcJCfwAo7VqN5tD)
	- Building agentic systems with VS Code extensibility and GitHub Copilot at Uber [YouTube](https://www.youtube.com/watch?v=8rkA5vWUE4Y&pp=0gcJCdgAo7VqN5tD)
	- Agent Flows in Copilot Studio | Complete Tutorial [YouTube](https://www.youtube.com/watch?v=bCQGte09-Ko)
	- Piloting agents in GitHub Copilot — workshop session [YouTube](https://www.youtube.com/watch?v=DdaAABdAqZY)
	- Build Hour: Agentic Tool Calling — agents, tool use, evals [YouTube](https://www.youtube.com/watch?v=7E-qdsVEoB8)

	### Docs and tutorials
	- About GitHub Copilot coding agent [Docs](https://docs.github.com/en/copilot/concepts/coding-agent/coding-agent)
	- Extending Copilot coding agent with MCP [Docs](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/extending-copilot-coding-agent-with-mcp)
	- GitHub Copilot coding agent in VS Code [Docs](https://code.visualstudio.com/docs/copilot/copilot-coding-agent)
	- Get started with GitHub Copilot in VS Code [Guide](https://code.visualstudio.com/docs/copilot/getting-started)
	- Build agents with Copilot Studio (lite experience) [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-studio-lite-build)
	- Agent flows overview [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview)
	- Use agent flows with your agent [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-flow)
	- Build an autonomous agent in Copilot Studio [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/autonomous-agent/)
	- Employ Copilot Chat as your AI assistant [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/employ-copilot-assistant/)
	- Leveling up code reviews and PRs with GitHub Copilot [Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/code-reviews-pull-requests-github-copilot/)
	- Simplifying agents in Copilot: a field guide [Microsoft](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/simplifying-agents-in-copilot-a-field-guide/)
	- Unlocking autonomous agent capabilities with Copilot Studio [Microsoft](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/unlocking-autonomous-agent-capabilities-with-microsoft-copilot-studio/)
</callout>

