import tilemap as tm
import rect as rect

class Level():
    tilemap = None
    start_x = 0
    start_y = 0
    name = ""

levels = []
current_level_id = 0

# Just throw all the data in the executable :)
def load_levels():
    global levels
    tilemap = tm.tilemap_init(0, 0, 16, 16, 50, 50, None, None, 'bricks2.png', None)
    tilemap.src_rect = rect.init_rect(0, 0, tilemap.tile_width, tilemap.tile_height)
    new_level = Level()

    # Level 1 -----------------------------------------------------------------
    tilemap.tile_ids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1]

    tilemap.collision = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,
                         1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,]
    tilemap.map_width = 20
    tilemap.map_height = 20
    new_level.tilemap = tilemap
    new_level.name = "Wall Jump"
    new_level.start_x = 150
    new_level.start_y = 150
    levels.append(new_level)

    # Level 2 -----------------------------------------------------------------
    tilemap.tile_ids = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,
                        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1]

    tilemap.collision = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                         1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,
                         1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,]
    new_level.tilemap = tilemap
    new_level.name = "Wall Jump 2"
    levels.append(new_level)
    