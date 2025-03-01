# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
from .PromptSearch import PromptSearch

NODE_CLASS_MAPPINGS = {
    "PromptSearch": PromptSearch,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptSearch": "Pixu.ai prompt search",
}