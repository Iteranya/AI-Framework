import json


def save_to_json_file(data: list[dict], file_path: str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def compile_ai(sounds: list[dict]) -> dict:
    combined_dict = {}
    for sound_dict in sounds:
        combined_dict.update(sound_dict)
    return combined_dict

def ai_compile(name,sounds):
    result = compile_ai(sounds)
    save_to_json_file(result,name+".json")