from globals import *

atlas_texture_data = {
    'grass': {'type': 'block', 'size': (TILESIZE,TILESIZE), 'position': (0*TILESIZE,0*TILESIZE)},
    'stone': {'type': 'block', 'size': (TILESIZE,TILESIZE), 'position': (1*TILESIZE,0*TILESIZE)},
    'dirt': {'type': 'block', 'size': (TILESIZE,TILESIZE), 'position': (0*TILESIZE,1*TILESIZE)},
    
}

solo_texture_data = {
    'player_static': {'type': 'player', 'file_path': 'res/player.png', 'size': (TILESIZE,TILESIZE)},
} 