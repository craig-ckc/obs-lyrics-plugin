import mock_obs
import lyrics_plugin
import os

def test_lyrics_logic():
    print("Testing Lyrics Plugin Logic...")
    
    # Setup sample data
    os.makedirs("test_songs", exist_ok=True)
    with open("test_songs/song1.txt", "w") as f:
        f.write("Verse 1 Line 1\nVerse 1 Line 2\nVerse 2 Line 1")
    
    # Create Source
    settings = {
        "background_image": "bg.png",
        "songs_folder": os.path.abspath("test_songs"),
        "song_selection": os.path.abspath("test_songs/song1.txt"),
        "text_offset_x": 10,
        "text_offset_y": 20,
        "color1": 0xFFFFFF,
        "color2": 0xFF0000,
        "outline": True,
        "outline_size": 2,
        "outline_color": 0x000000,
        "drop_shadow": True,
        "drop_shadow_opacity": 80,
        "drop_shadow_off_x": 4,
        "drop_shadow_off_y": 4,
        "word_wrap": True,
        "custom_width": 800
    }
    
    source = lyrics_plugin.LyricsSource(None, settings)
    
    # Test Update (Loading)
    print("\n--- Testing Update/Load ---")
    source.update(settings)
    source.load_lyrics(settings["song_selection"])
    
    assert len(source.lyrics_lines) == 3
    print(f"Loaded {len(source.lyrics_lines)} lines.")
    
    # Test Navigation
    print("\n--- Testing Navigation ---")
    print(f"Current Lyric (Initial): '{source.get_current_lyric()}'") # Should be empty or first? Logic says -1 initially.
    
    source.next_lyric()
    print(f"Current Lyric (Next): '{source.get_current_lyric()}'")
    assert source.get_current_lyric() == "Verse 1 Line 1"
    
    source.next_lyric()
    print(f"Current Lyric (Next): '{source.get_current_lyric()}'")
    assert source.get_current_lyric() == "Verse 1 Line 2"
    
    source.prev_lyric()
    print(f"Current Lyric (Prev): '{source.get_current_lyric()}'")
    assert source.get_current_lyric() == "Verse 1 Line 1"
    
    # Test Stop
    print("\n--- Testing Stop ---")
    source.stop_lyrics()
    print(f"Current Lyric (Stop): '{source.get_current_lyric()}'")
    assert source.get_current_lyric() == ""
    
    print("\nTest Complete!")

if __name__ == "__main__":
    test_lyrics_logic()
