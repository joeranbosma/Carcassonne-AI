from PIL import Image, ImageFilter
import networkx as nx

def pixels_equal(pix1, pix2):
    return pix1 == pix2

def pixels_connected(image, pos_a, pos_b, compare=pixels_equal):
    # -1 unsearched, 0 not connected, 1 connected
    imwidth, imheight = image.size
    state = [[-1] * imwidth for _ in range(imheight)]
    pix_a = image.getpixel(pos_a)

    def depth_first(pos):
        if pos == pos_b:
            return True

        poss_nxbours = [
            (pos[0] - 1, pos[1] + 0),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
        ]
        nxbours = [
            nx for nx in poss_nxbours
            if  nx[0] >= 0 and nx[0] < imwidth
            and nx[1] >= 0 and nx[1] < imheight
            and state[nx[0]][nx[1]] == -1
        ]

        for nx in nxbours:
            pix_b = image.getpixel(nx)
            state[nx[0]][nx[1]] = 1 if compare(pix_a, pix_b) else 0

        for nx in nxbours:
            if state[nx[0]][nx[1]] == 1 and depth_first(nx):
                return True

        return False

    return depth_first(pos_a)


def tile_from_bitmap(image):
    # just testing func atm
    if pixels_connected(image, (1, 4), (3, 0)):
        print("BL connected to TR")
    else:
        print("BL NOT connected to TR")

    return image

def all_tiles_from_bitmap(filename="tiles.png", w=7, h=12, res=5):
    im = Image.open(filename)
    return [
        tile_from_bitmap(im.crop((x * res, y * res, (x + 1) * res, (y + 1) * res)))
        for x in range(w) for y in range(h)
    ]
