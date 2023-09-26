import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    bg_img2 = pg.transform.flip(bg_img, True, False) 
    kk_img1 = pg.transform.flip(kk_img, True, False)
    kk_img2 = pg.transform.rotozoom(kk_img1, 1, 1.0)
    kk_img3 = pg.transform.rotozoom(kk_img1, 2, 1.0)
    kk_img4 = pg.transform.rotozoom(kk_img1, 3, 1.0)
    kk_img5 = pg.transform.rotozoom(kk_img1, 4, 1.0)
    kk_img6 = pg.transform.rotozoom(kk_img1, 5, 1.0)
    kk_img7 = pg.transform.rotozoom(kk_img1, 6, 1.0)
    kk_img8 = pg.transform.rotozoom(kk_img1, 7, 1.0)
    kk_img9 = pg.transform.rotozoom(kk_img1, 8, 1.0)
    kk_img10 = pg.transform.rotozoom(kk_img1, 9, 1.0)
    kk_img11 = pg.transform.rotozoom(kk_img1, 10, 1.0)
    kk_img12 = pg.transform.rotozoom(kk_img1, 9, 1.0)
    kk_img13 = pg.transform.rotozoom(kk_img1, 8, 1.0)
    kk_img14 = pg.transform.rotozoom(kk_img1, 7, 1.0)
    kk_img15 = pg.transform.rotozoom(kk_img1, 6, 1.0)
    kk_img16 = pg.transform.rotozoom(kk_img1, 5, 1.0)
    kk_img17 = pg.transform.rotozoom(kk_img1, 4, 1.0)
    kk_img18 = pg.transform.rotozoom(kk_img1, 3, 1.0)
    kk_img19 = pg.transform.rotozoom(kk_img1, 2, 1.0)
    kk_img20 = pg.transform.rotozoom(kk_img1, 1, 1.0)
    kk_imgs = [kk_img1, kk_img2, kk_img3, kk_img4, kk_img5, kk_img6, kk_img7, kk_img8, kk_img9, kk_img10, kk_img11,
               kk_img12, kk_img13, kk_img14, kk_img15, kk_img16, kk_img17, kk_img18, kk_img19, kk_img20]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(kk_imgs[tmr%20], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()