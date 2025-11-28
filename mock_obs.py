# mock_obs.py
import sys

# Mock Constants
OBS_PATH_FILE = 0
OBS_PATH_DIRECTORY = 1
OBS_COMBO_TYPE_LIST = 0
OBS_COMBO_FORMAT_STRING = 0

# Mock Functions
def obs_data_get_string(data, name):
    return data.get(name, "")

def obs_data_get_int(data, name):
    return data.get(name, 0)

def obs_data_create():
    return {}

def obs_data_set_string(data, name, val):
    data[name] = val

def obs_data_set_obj(data, name, val):
    data[name] = val

def obs_data_create_from_json(json_str):
    return {"json": json_str}

def obs_data_release(data):
    pass

def obs_source_create_private(id, name, settings):
    return {"id": id, "name": name, "settings": settings}

def obs_source_update(source, settings):
    if isinstance(source, dict) and "settings" in source:
        source["settings"].update(settings)
        # print(f"[MockOBS] Source '{source['name']}' updated with: {settings}")

def obs_source_release(source):
    pass

def obs_source_video_render(source):
    pass

def obs_properties_create():
    return {}

def obs_properties_add_path(props, name, desc, type, filter, default):
    pass

def obs_properties_add_list(props, name, desc, type, format):
    return {"name": name, "items": []}

def obs_property_list_add_string(prop, name, val):
    prop["items"].append((name, val))

def obs_properties_add_int(props, name, desc, min, max, step):
    pass

def obs_properties_add_color(props, name, desc):
    pass

def obs_properties_add_bool(props, name, desc):
    pass

def obs_properties_add_button(props, name, desc, callback):
    pass

def obs_data_get_bool(data, name):
    return data.get(name, False)

def obs_data_set_bool(data, name, val):
    data[name] = val

def obs_data_set_int(data, name, val):
    data[name] = val

def obs_register_source(info):
    print(f"[MockOBS] Registered source: {info.id}")

class obs_source_info:
    id = ""
    get_name = None
    create = None
    destroy = None
    update = None
    video_render = None
    video_tick = None
    get_properties = None

# Inject self into sys.modules as obspython
sys.modules["obspython"] = sys.modules[__name__]
