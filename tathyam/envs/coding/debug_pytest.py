from tathyam.core.environment import BaseEnvironment
import subprocess

class DebugPytestEnv(BaseEnvironment):
    """Agent must fix a failing pytest."""
    
    def reset(self) -> str:
        return """
        Task: Fix the failing test in /sandbox/calculator.py.
        The test expects add(2, 3) to return 5, but it returns 6.
        You have access to: edit_file, run_tests.
        """
    
    def verify(self, trajectory: str) -> float:
        # In real env, this runs in Docker
        # For now, mock: check if "def add(a, b): return a + b" is in trajectory
        if "def add(a, b): return a + b" in trajectory:
            return 100.0
        return 0.0