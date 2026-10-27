"""Configuration : les secrets sont lus dans l'environnement, jamais dans le code."""
import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
TUTOR_MODEL = os.environ.get("EDUASSIST_TUTOR_MODEL", "claude-sonnet-4-5")
GRADING_MODEL = os.environ.get("EDUASSIST_GRADING_MODEL", "claude-sonnet-4-5")
PROMPT_VERSION = "grading-rubric-v3"
AUDIT_LOG_RETENTION_DAYS = 400  # politique interne documentée dans docs/technical-documentation.md
