from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from openenv.core.env_server import Action as BaseAction, Observation as BaseObservation, State as BaseState

# As per requirements, we use Pydantic V2 for typed Observation, Action, and Reward models.
# These will be the primary data structures for the OpenEnv interaction.

class Observation(BaseObservation):
    """
    Typed Observation model.
    Includes user input, interaction history, and raw tool output.
    Note: 'done' and 'reward' are inherited from BaseObservation.
    """
    user_input: str = Field(..., description="The current instruction or query. The primary attack vector.")
    history: List[Dict[str, Any]] = Field(default_factory=list, description="Sequential log of prior interactions to detect multi-turn attacks.")
    tool_output: Optional[str] = Field(None, description="Raw string returned by external tools; highly susceptible to compromise.")
    risk_level: float = Field(0.0, description="A heuristic risk metric (0.0 to 1.0) provided by the firewall's internal classifier.")

class Action(BaseAction):
    """
    Typed Action model compatible with OpenEnv standards.
    Note: 'metadata' is inherited from BaseAction.
    """
    response: str = Field(..., description="Natural language directed back to the user.")
    thought: Optional[str] = Field("", description="Internal reasoning log for the AI agent.")
    use_tool: bool = Field(False, description="Binary flag indicating tool execution.")
    tool_name: Optional[str] = Field(None, description="Identifier of the tool (e.g., query_database).")
    tool_payload: Optional[Dict[str, Any]] = Field(None, description="Parameters passed to the tool.")
    tool_calls: List[Dict[str, Any]] = Field(default_factory=list, description="Structured tool calls as per framework requirements.")

class State(BaseState):
    """
    Internal State model.
    Tracks the current task progress and metadata.
    Inherits 'episode_id' and 'step_count' from BaseState.
    """
    task_id: str = Field("", description="Unique identifier for the current task.")
    max_steps: int = Field(5, description="Maximum allowed steps before termination.")
    finished: bool = Field(False, description="Whether the episode has ended.")
    success: bool = Field(False, description="Whether the task was completed successfully.")
    total_reward: float = Field(0.0, description="Cumulative reward earned in the episode.")
    task_metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional context for specific tasks.")
