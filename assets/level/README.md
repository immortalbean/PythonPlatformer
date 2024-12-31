### Format
The levels are stored in the JSON format. Each object in the level's array is a building block to the level
### "Type"
The type parameter is used for the type of object you're adding to the level. The different currently available types go as followed:
 - 0 - Rectangular ground - A rectangle the player can walk on - Requires the "position_x", "position_y", "width", "height", and "texture" parameters.
 - 1 - Death box - Kills the player - Requires the "position_x", "position_y", "width", and "height" parameters.
### "Texture"
The texture parameter is used for the texture the object is rendered as.
 - The parameter is either supposed to be set to "none", or an integer value that reads from a JSON file located at: assets/textures.json
 - Textures.json stores a set of textures with parameters. These parameters are:
    - "file" - The path of the texture file, can be any format accepted by the PyGame module.
    - (More to come)
### Levels.json (in assets folder)
In order for a level to be loaded in-game, it has to be included in the project's levels.json file. This file is an array of every level, each being an object within it.
The properties goes as followed:
  - "level_name" - The name of the level
  - "level_path" - The path of the level's JSON.
  - "background_color" - A 3 value array which corrospond to RGB.