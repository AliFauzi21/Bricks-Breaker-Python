import pygame
from pygame.locals import Rect

# パドルクラス
class Paddle:
    # パドルの色
    PADDLE_COLOR = (250, 180, 0)
    # パドルの左上座標
    PADDLE_RECT_X, PADDLE_RECT_Y = 250, 700
    # パドルの幅、高さ
    PADDLE_RECT_WIDTH, PADDLE_RECT_HEIGHT = 100, 30
    # パドルの移動距離
    PADDLE_MOVE_X = 8
    
    # Ａ－１最初）コンストラクタ
    def __init__(self):
        # Ａ－２）描画用の色を設定
        self.col = Paddle.PADDLE_COLOR
        # Ａ－３）描画用の矩形を設定（横位置、幅は仮の値で設定）
        # Ｇ－５６ここのみ）横位置、幅を正しい値に設定）
        self.rect = Rect(Paddle.PADDLE_RECT_X, Paddle.PADDLE_RECT_Y,
                         Paddle.PADDLE_RECT_WIDTH, Paddle.PADDLE_RECT_HEIGHT)
        
    # Ａ－４）移動処理
    def move(self, dir):
        # Ａ－５）方向によって、クラス変数の移動距離分移動する
        self.rect.centerx += Paddle.PADDLE_MOVE_X * dir
    # Ａ－６mainへ）描画処理
    def draw(self, surface):
        pygame.draw.rect(surface, self.col, self.rect)
