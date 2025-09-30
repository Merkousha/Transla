# Contributing to Transla

Thanks for your interest in improving the Book Translator! We welcome bug reports, feature suggestions, documentation improvements, and pull requests from the community.

## Ways to Contribute

- **Bug reports** – Use the GitHub Issues tab and include steps to reproduce, the expected behaviour, and logs/output if available.
- **Feature requests** – Explain the problem you are trying to solve and any constraints or edge cases we should consider.
- **Pull requests** – Fix a bug, polish documentation, improve tests, or add new functionality that aligns with the project goals.
- **Discussions** – If you are unsure whether an idea fits the roadmap, open a discussion or draft issue to gather feedback before investing time.

## Development Setup

1. Fork the repository and clone your fork locally.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Copy the environment template and configure credentials:
   ```bash
   cp .env.example .env            # Windows: copy .env.example .env
   ```
4. Run the smoke test to confirm your configuration:
   ```bash
   python test_openai.py
   ```

## Coding Guidelines

- **Style** – Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code and keep line lengths reasonable (≤ 100 characters where practical).
- **Type hints** – When adding new functions or classes, include type hints for clarity.
- **Logging** – Prefer descriptive log or print messages that help users troubleshoot issues quickly.
- **Dependencies** – Avoid adding heavy dependencies; discuss major additions in an issue first.

## Testing

- Run `python test_openai.py` before submitting a pull request to ensure the connection workflow still works.
- If you add new modules, consider including unit tests or smoke tests that don't leak credentials.
- Document any manual verification steps in your pull request description.

## Commit & PR Process

1. Create a feature branch for your work.
2. Keep each pull request focused and include a summary of changes, testing performed, and any screenshots or logs that aid review.
3. Ensure the CI (once available) passes before requesting review.
4. Reference related issues with `Fixes #123` or `Closes #123` when applicable.
5. Be ready to iterate on reviewer feedback; we appreciate your patience and collaboration.

## Reporting Security Issues

Please do **not** open a public issue for security vulnerabilities. Instead, report the problem privately by contacting the maintainers through GitHub (e.g., via direct message or by requesting a private disclosure channel). We'll work with you to verify and patch the issue as quickly as possible.

## Recognition

All contributors are credited in the GitHub contributors graph. Thank you for helping us build a reliable Persian book translation tool for the community!
