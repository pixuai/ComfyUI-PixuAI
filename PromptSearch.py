class PromptSearch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "search_terms": ("STRING", {
                    "multiline": True,  # True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Black dress"
                }),
            },
            "optional": {
                "search_results": ("INT", {
                    "default": 5,
                    "min": 1,  # Minimum value
                    "max": 200,  # Maximum value
                    "step": 1,  # Slider's step
                    "display": "number"  # Cosmetic only: display as "number" or "slider"
                }),
            },
        }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ( "Prompts",)

    OUTPUT_IS_LIST = (True,)

    FUNCTION = "run"

    # OUTPUT_NODE = False

    CATEGORY = "Pixu"

    def run(self, search_terms, search_results):

        results = ["exmple1", "example2", "example3", "example4", "example5"]
        return (results)

