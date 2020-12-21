from dbt.dataclass_schema import StrEnum
import json

from typing import Union, Dict, Any


class ModelHookType(StrEnum):
    PreHook = 'pre-hook'
    PostHook = 'post-hook'


def get_hook_dict(source: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
    """From a source string-or-dict, get a dictionary that can be passed to
    Hook.from_dict
    """
    # TODO: Not sure what changed here... Was getting error
    # "the JSON object must be str, bytes or bytearray, not int"
    # source was a single integer
    if isinstance(source, int):
        return {'sql': str(source)}

    if isinstance(source, dict):
        return source
    try:
        return json.loads(source)
    except ValueError:
        return {'sql': source}
