import random
import math
import pygame
from pygame.locals import Rect

# ボールクラス
class Ball:

    # ボールの色
    BALL_COLOR = (128, 0, 128)
    # ボールの左上位置
    BALL_RECT_X, BALL_RECT_Y = 300, 400
    # ボールの幅、高さ
    BALL_RECT_WIDTH, BALL_RECT_HEIGHT = 30, 30
    # 初期発射角度の範囲（25の場合は、-25度から25度にする）
    START_DIR_DIFF = 25
    
    # Ｂ－１１最初）コンストラクタ
    def __init__(self, speed):
        # Ｂ－１２）描画用の色を設定
        self.col = Ball.BALL_COLOR
        # Ｂ－１３）描画用の矩形を設定
        self.rect = Rect(Ball.BALL_RECT_X, Ball.BALL_RECT_Y,
                         Ball.BALL_RECT_WIDTH, Ball.BALL_RECT_HEIGHT)
        # Ｂ－１４）引数で受け取ったスピードを設定
        self.speed = speed
        # Ｂ－１５）初期の球の発射角度を、270度（下向き）
        #       ＋ある程度の範囲のランダムで決定
        self.dir = random.randint(-1 * Ball.START_DIR_DIFF, Ball.START_DIR_DIFF) + 270

    # Ｂ－１６）ボールの移動処理
    def move(self):
        # Ｂ－１７）角度に対して、三角関数で算出した値にスピードを掛ける
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed
        

    # Ｂ－１８mainへ）描画処理
    def draw(self, surface):
        pygame.draw.ellipse(surface, self.col, self.rect)
