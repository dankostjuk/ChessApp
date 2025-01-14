import pygame as pg


class Button:
    def __init__(self,x,y,width,height,title,color,idx,idy):
        self.rect = pg.Rect(x,y,width,height)
        self.text = title
        self.font = pg.font.Font(None, 36)
        self.text_surface = self.font.render(self.text, True, 'black')
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.clicked = False
        self.color = color
        self.idx = idx
        self.idy = idy
    def draw(self,surface):
        mouse_pos = pg.mouse.get_pos()
        action = False
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1:
                action = True
                self.clicked = True
                color = self.color[1:]
                color = int(color,16)
                if color > int('AAAAAA',16):
                    pg.draw.rect(surface, color - int('777777',16) , self.rect)
                else:
                    pg.draw.rect(surface, color + int('222222',16), self.rect)
                surface.blit(self.text_surface, self.text_rect)
            elif not self.clicked:
                color = self.color[1:]
                color = int(color,16)
                if color > int('AAAAAA',16):
                    pg.draw.rect(surface, color - int('777777',16), self.rect)
                else:
                    pg.draw.rect(surface, color + int('222222',16), self.rect)
                surface.blit(self.text_surface, self.text_rect)

            else:
                pg.draw.rect(surface, self.color, self.rect)
                surface.blit(self.text_surface, self.text_rect)

        else:
            pg.draw.rect(surface,self.color,self.rect)
            surface.blit(self.text_surface,self.text_rect)
            self.clicked = False

        return action, self.idx, self.idy