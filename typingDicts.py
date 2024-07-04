from typing import Union, Dict, List, Any
import json

# a recursively typed json object for ints, strs and lists
JSONVal = Union[str, int, 'JSONArray', 'JSONObject']
JSONArray = List[JSONVal]
JSONObject = Dict[str, JSONVal]

def load_json(file_path: str) -> Any:
    with open(file_path, 'r') as f:
        return json.load(f)

def check_types(data: Any) -> bool:
    try:
        typed_data: JSONObject = data
        return True
    except Exception as e:
        print(f"Type checking failed: {e}")
        return False

if __name__ == "__main__":
    file_path = 'photosets.json'  
    data = load_json(file_path)
    if check_types(data):
        print("The JSON object is correctly typed.")
    else:
        print("The JSON object is not correctly typed.")
