import pygame
from pygame.locals import Rect

# ブロッククラス
class Block:
    
    # コンストラクタ
    # widthとheightは指定がない場合はデフォルトの値となる
    def __init__(self, col, x, y, width=80, height=30):
        # 色、描画用の矩形を設定
        self.col = col 
        self.rect = Rect(x, y, width, height)
    # 描画処理
    def draw(self, surface):
        pygame.draw.rect(surface, self.col, self.rect)
