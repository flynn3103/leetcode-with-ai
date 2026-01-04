# LeetCode Trainer with AI

This project is personal LeetCode training repository configured to use an AI as a senior software engineer and interview coach. The AI is instructed to use the **Socratic method**, guiding you to solutions through questioning rather than providing direct answers.

## 🚀 How to Set Up the AI Trainer

The AI trainer is powered by a specific set of instructions located in `.agent/rules/leetcode-trainer.md`. 

To ensure the AI follows these rules:
1.  **Instruction File**: Ensure `.agent/rules/leetcode-trainer.md` exists with the "always_on" trigger.
2.  **AI Configuration**: If using a tool (like Cursor, Windsurf, or Antigravity) that respects `.agent/rules`, the AI will automatically adopt the "Interview Coach" persona when you work on algorithmic problems.
3.  **Manual Setup**: If your tool doesn't support `.agent/rules` automatically, copy the content of `.agent/rules/leetcode-trainer.md` into your system prompt or custom instructions.

## 🧠 Socratic Thinking Process

To find all reachable solutions and deeply understand the problem, follow this structured thinking flow with the AI:

1.  **Problem Translation**: Explain the problem in your own words to the AI.
2.  **Examples & Edge Cases**: Discuss various inputs, including empty values, large numbers, or negative values.
3.  **Brute Force Exploration**: Propose a simple, first-instinct solution. The AI will acknowledge it and ask about its limitations.
4.  **Guided Optimization**: Through targeted questions (e.g., *"How could we reduce the lookup time?"*), the AI helps you discover more efficient data structures or algorithms (Sliding Window, Two Pointers, Dynamic Programming, etc.).

## 📝 Thinking Journal (`*_thinking.md`)

For every problem, maintain a companion thinking file (e.g., `BinaryTreeInorderTraversal_thinking.md`) to capture the journey:

*   **Thinking Journal**: Record your initial ideas, the AI's hints, and the refinements you make.
*   **Reachable Ways**: List different approaches discovered (e.g., Iterative vs. Recursive, Time vs. Space trade-offs).
*   **Key Learnings & Summaries**: Once the optimal solution is reached, the AI will provide a summary of patterns and takeaways. Save these at the end of the file for future review.
*   **Example Structure**:
    ```markdown
    # Thinking: [Problem Name]
    ## Approach 1: Brute Force
    - Thinking: ...
    - Complexity: ...
    ## Approach 2: Optimal
    - Thinking: ...
    - Complexity: ...
    ## Key Learnings
    - Pattern: ...
    - Takeaway: ...
    ```

## 🛠 Python Environment Setup

The project uses `uv` for dependency management and `pytest` for testing.

1.  **Install `uv`**:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
2.  **Initialize/Sync Virtual Environment**:
    ```bash
    uv sync
    ```
3.  **Run Tests**:
    Tests are located alongside the source code or in specific folders. Run them using:
    ```bash
    uv run pytest
    ```

---
*Happy Coding! Use the AI to challenge your thinking, not just to get the green checkmark.*