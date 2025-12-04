from abc import ABC, abstractmethod

class BaseEnvironment(ABC):
    """Minimal RL environment with verification."""
    
    @abstractmethod
    def reset(self) -> str:
        """Return initial task prompt."""
        pass
    
    @abstractmethod
    def verify(self, trajectory: str) -> float:
        """Return score 0-100 for agent's solution."""
        pass