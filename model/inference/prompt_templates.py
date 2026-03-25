"""
Prompt templates for model generation
"""


class PromptTemplate:
    """Base prompt template class"""
    
    def __init__(self, template: str):
        self.template = template
    
    def format(self, **kwargs) -> str:
        """Format template with provided variables"""
        return self.template.format(**kwargs)


# Example templates
EXPLANATION_TEMPLATE = PromptTemplate(
    "Explain {topic} in a way that is clear and easy to understand."
)

ANIMATION_TEMPLATE = PromptTemplate(
    "Create an animation script for: {content}"
)
