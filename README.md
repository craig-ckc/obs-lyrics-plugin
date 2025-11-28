# OBS Lyrics Plugin

A Python-based OBS Studio plugin that provides a "Lyrics Overlay" source. This source allows you to display lyrics from text files over a background image, with advanced control over navigation and text styling.

## Features

- **Dynamic Lyrics**: Load lyrics from standard `.txt` files.
- **Background Overlay**: Display a custom background image (lyric bar) behind the text.
- **Navigation Controls**: Next, Previous, Stop, and Shutdown buttons directly in the source properties.
- **Advanced Text Styling**:
    - **Colors & Gradients**: Set top and bottom colors for a vertical gradient.
    - **Outlines**: Add a border around the text with custom size and color.
    - **Drop Shadows**: Add a hard drop shadow with custom opacity and offset.
    - **Word Wrapping**: Define a bounding box width to automatically wrap long lines.
- **Positioning**: Manually offset the text to align perfectly with your background graphics.

## Installation

1.  **Prerequisites**: Ensure you have OBS Studio installed.
2.  **Download**: Download the `lyrics_plugin.py` file.
3.  **Install in OBS**:
    - Open OBS Studio.
    - Go to **Tools** -> **Scripts**.
    - Click the **Python Settings** tab and ensure a valid Python 3 path is selected.
    - Click the **Scripts** tab.
    - Click the **+** (Plus) button.
    - Browse to and select `lyrics_plugin.py`.

## Usage

### Adding the Source
1.  In your Scene, click the **+** icon to add a new source.
2.  Select **Lyrics Overlay**.
3.  Name the source (e.g., "Lyrics").

### Configuration
Double-click the source to open its properties:

#### Content
- **Background Image**: Select the image file (PNG/JPG) to use as the background bar.
- **Songs Folder**: Select the directory containing your song text files.
- **Select Song**: Choose the specific song file to load.

#### Positioning
- **Text Offset X / Y**: Adjust these values to move the text relative to the top-left corner of the source.

#### Styling
- **Text Color (Top/Bottom)**: Set both to the same color for solid text, or different colors for a gradient.
- **Enable Outline**: Check to add a border. Adjust **Outline Size** and **Outline Color**.
- **Enable Drop Shadow**: Check to add a shadow. Adjust **Opacity** and **Offset X/Y**.
- **Enable Word Wrap**: Check to wrap text within a specific width. Adjust **Wrap Width** to match your background design.

### Controls
Use the buttons at the bottom of the properties window:
- **Next Lyric**: Advance to the next line.
- **Previous Lyric**: Go back to the previous line.
- **Stop/Clear**: Clear the text but keep the background visible.
- **Shutdown Overlay**: Hide the entire source (text and background).

## File Format
- Create `.txt` files in your songs folder.
- Each non-empty line in the file is treated as a separate lyric slide.
- Example:
  ```text
  Verse 1 line 1
  Verse 1 line 2
  
  Chorus line 1
  Chorus line 2
  ```

## Troubleshooting
- **Text not appearing?** Ensure "Stop/Clear" wasn't clicked. Try clicking "Next Lyric". Check if the text color matches the background.
- **Plugin not loading?** Check the Script Log in OBS (Tools -> Script Log) for Python errors. Ensure your Python installation matches the bitness (64-bit) of OBS.
