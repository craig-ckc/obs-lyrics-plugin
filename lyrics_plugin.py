import obspython as obs
import os

# Global variable to hold the source instance
lyrics_source_instance = None

# Global registry of instances
lyrics_instances = []

class LyricsSource:
    def __init__(self, source, settings):
        self.source = source
        self.settings = settings
        self.image_path = ""
        self.songs_folder = ""
        self.current_song_file = ""
        self.lyrics_lines = []
        self.current_line_index = -1
        self.is_visible = True
        self.text_source = None
        self.image_texture = None
        self.width = 1920
        self.height = 1080
        
        # Register instance
        lyrics_instances.append(self)
        
        # Initialize text source
        # We use a private source to handle text rendering
        self.text_source = obs.obs_source_create_private("text_ft2_source", "lyrics_text", settings)
        
    def update(self, settings):
        self.image_path = obs.obs_data_get_string(settings, "background_image")
        self.songs_folder = obs.obs_data_get_string(settings, "songs_folder")
        self.current_song_file = obs.obs_data_get_string(settings, "song_selection")
        
        # Load image if changed
        if self.image_path:
            self.load_image(self.image_path)
            
        # Update text source settings
        text_settings = obs.obs_data_create()
        font_obj = obs.obs_data_create_from_json('{"face": "Arial", "size": 48, "style": "Bold"}')
        obs.obs_data_set_obj(text_settings, "font", font_obj)
        obs.obs_data_set_string(text_settings, "text", self.get_current_lyric())
        
        # Apply Styling
        obs.obs_data_set_int(text_settings, "color1", obs.obs_data_get_int(settings, "color1"))
        obs.obs_data_set_int(text_settings, "color2", obs.obs_data_get_int(settings, "color2"))
        
        obs.obs_data_set_bool(text_settings, "outline", obs.obs_data_get_bool(settings, "outline"))
        obs.obs_data_set_int(text_settings, "outline_size", obs.obs_data_get_int(settings, "outline_size"))
        obs.obs_data_set_int(text_settings, "outline_color", obs.obs_data_get_int(settings, "outline_color"))
        
        obs.obs_data_set_bool(text_settings, "drop_shadow", obs.obs_data_get_bool(settings, "drop_shadow"))
        obs.obs_data_set_int(text_settings, "drop_shadow_opacity", obs.obs_data_get_int(settings, "drop_shadow_opacity"))
        obs.obs_data_set_int(text_settings, "drop_shadow_off_x", obs.obs_data_get_int(settings, "drop_shadow_off_x"))
        obs.obs_data_set_int(text_settings, "drop_shadow_off_y", obs.obs_data_get_int(settings, "drop_shadow_off_y"))
        
        obs.obs_data_set_bool(text_settings, "word_wrap", obs.obs_data_get_bool(settings, "word_wrap"))
        obs.obs_data_set_int(text_settings, "custom_width", obs.obs_data_get_int(settings, "custom_width"))
        
        obs.obs_source_update(self.text_source, text_settings)
        obs.obs_data_release(text_settings)
        obs.obs_data_release(font_obj)
        
        # Load lyrics if song changed (simple check)
        if self.current_song_file:
             self.load_lyrics(self.current_song_file)

    def load_image(self, path):
        if self.image_texture:
            # In a real plugin we would release the old texture, but Python API for this is tricky.
            # Usually gs_image_file_free is used if using gs_image_file.
            pass
            
        # Note: Loading images in Python OBS script for rendering is complex because 
        # we need to use gs_image_file and it needs to be done in the graphics thread.
        # For now, we will handle this in video_render.
        pass

    def load_lyrics(self, file_path):
        self.lyrics_lines = []
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                self.lyrics_lines = [line.strip() for line in f.readlines() if line.strip()]
        self.current_line_index = -1
        self.update_text_display()

    def get_current_lyric(self):
        if not self.is_visible:
            return ""
        if 0 <= self.current_line_index < len(self.lyrics_lines):
            return self.lyrics_lines[self.current_line_index]
        return ""

    def video_render(self, effect):
        if not self.is_visible:
            return

        # 1. Draw Background
        # (Implementation of image drawing will go here)
        
        # 2. Draw Text
        if self.text_source:
            # Get offset from settings
            offset_x = obs.obs_data_get_int(self.settings, "text_offset_x")
            offset_y = obs.obs_data_get_int(self.settings, "text_offset_y")
            
            # We would use gs_matrix_push, gs_matrix_translate, etc. here
            # But for now we just call render
            obs.obs_source_video_render(self.text_source)

    def video_tick(self, seconds):
        pass

    def next_lyric(self):
        if self.current_line_index < len(self.lyrics_lines) - 1:
            self.current_line_index += 1
            self.update_text_display()

    def prev_lyric(self):
        if self.current_line_index > 0:
            self.current_line_index -= 1
            self.update_text_display()

    def stop_lyrics(self):
        self.current_line_index = -1
        self.update_text_display()
        
    def shutdown(self):
        self.is_visible = False
        self.update_text_display() # Clear text too
        
    def update_text_display(self):
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "text", self.get_current_lyric())
        obs.obs_source_update(self.text_source, settings)
        obs.obs_data_release(settings)

# -------------------------------------------------------------------
# Script Definitions
# -------------------------------------------------------------------

def script_description():
    return "Lyrics Overlay Plugin\n\nAdds a 'Lyrics Overlay' source to display lyrics from text files."

def script_load(settings):
    obs.obs_register_source(source_info)

def script_unload():
    pass

# -------------------------------------------------------------------
# Source Definition
# -------------------------------------------------------------------

def source_get_name(unversioned_settings):
    return "Lyrics Overlay"

def source_create(settings, source):
    return LyricsSource(source, settings)

def source_destroy(data):
    if data in lyrics_instances:
        lyrics_instances.remove(data)
    if data.text_source:
        obs.obs_source_release(data.text_source)

def source_update(data, settings):
    data.update(settings)

def source_video_render(data, effect):
    data.video_render(effect)

def source_video_tick(data, seconds):
    data.video_tick(seconds)

def source_get_properties(data):
    props = obs.obs_properties_create()
    
    # Groups could be used here for better UI, but Python API support varies.
    
    obs.obs_properties_add_path(props, "background_image", "Background Image", obs.OBS_PATH_FILE, "Images (*.png *.jpg *.jpeg)", "")
    
    obs.obs_properties_add_path(props, "songs_folder", "Songs Folder", obs.OBS_PATH_DIRECTORY, "", "")
    
    p = obs.obs_properties_add_list(props, "song_selection", "Select Song", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    # Populate list if folder is selected (would need a callback or refresh)
    if data and data.songs_folder:
         if os.path.exists(data.songs_folder):
            files = [f for f in os.listdir(data.songs_folder) if f.endswith(".txt")]
            for f in files:
                obs.obs_property_list_add_string(p, f, os.path.join(data.songs_folder, f))

    obs.obs_properties_add_int(props, "text_offset_x", "Text Offset X", -10000, 10000, 1)
    obs.obs_properties_add_int(props, "text_offset_y", "Text Offset Y", -10000, 10000, 1)
    
    # Styling Properties
    obs.obs_properties_add_color(props, "color1", "Text Color (Top)")
    obs.obs_properties_add_color(props, "color2", "Text Color (Bottom)")
    
    obs.obs_properties_add_bool(props, "outline", "Enable Outline")
    obs.obs_properties_add_int(props, "outline_size", "Outline Size", 1, 20, 1)
    obs.obs_properties_add_color(props, "outline_color", "Outline Color")
    
    obs.obs_properties_add_bool(props, "drop_shadow", "Enable Drop Shadow")
    obs.obs_properties_add_int(props, "drop_shadow_opacity", "Shadow Opacity (0-100)", 0, 100, 1)
    obs.obs_properties_add_int(props, "drop_shadow_off_x", "Shadow Offset X", -100, 100, 1)
    obs.obs_properties_add_int(props, "drop_shadow_off_y", "Shadow Offset Y", -100, 100, 1)
    
    obs.obs_properties_add_bool(props, "word_wrap", "Enable Word Wrap")
    obs.obs_properties_add_int(props, "custom_width", "Wrap Width", 100, 10000, 1)
    
    obs.obs_properties_add_button(props, "btn_next", "Next Lyric", on_next_clicked)
    obs.obs_properties_add_button(props, "btn_back", "Previous Lyric", on_back_clicked)
    obs.obs_properties_add_button(props, "btn_stop", "Stop/Clear", on_stop_clicked)
    obs.obs_properties_add_button(props, "btn_shutdown", "Shutdown Overlay", on_shutdown_clicked)
    
    return props

# Button Callbacks
def on_next_clicked(props, prop):
    for instance in lyrics_instances:
        instance.next_lyric()

def on_back_clicked(props, prop):
    for instance in lyrics_instances:
        instance.prev_lyric()

def on_stop_clicked(props, prop):
    for instance in lyrics_instances:
        instance.stop_lyrics()

def on_shutdown_clicked(props, prop):
    for instance in lyrics_instances:
        instance.shutdown()

source_info = obs.obs_source_info()
source_info.id = "lyrics_overlay"
source_info.get_name = source_get_name
source_info.create = source_create
source_info.destroy = source_destroy
source_info.update = source_update
source_info.video_render = source_video_render
source_info.video_tick = source_video_tick
source_info.get_properties = source_get_properties
