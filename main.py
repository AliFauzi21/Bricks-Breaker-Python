import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT
from ball import Ball
from paddle import Paddle
from block import Block

# ウィンドウサイズとメッセージの中央位置の設定
WINDOW_SIZE = (600, 800)
MSG_CENTER = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

# ボールのスピード（３段階）
SPEED_START = 7
SPEED_NORMAL = 10
SPEED_UPPER = 15

# Ｃ－２５最初）ボール反射チェック処理
def check_reflection():
    # Ｅ－４５最初）グローバル宣言
    global block_list
    
    # ===== ブロックとの反射チェック =====
    # Ｅ－４６）反射チェック前のブロックリストの数
    prev_len = len(block_list)
    # Ｅ－４７）それぞれのブロックとボールとが接触しているかを判定
    # 「接触していない」ブロックで新しくリストを作る
    # colliderect：２つの四角が接触しているかをチェックする関数
    block_list = [x for x in block_list
                  if not x.rect.colliderect(ball.rect)]
    
    # Ｅ－４８）反射チェック前とチェック後でブロックリストの数が変わっている場合
    if len(block_list) != prev_len:
        # Ｅ－４９最後）ボールの進行方向を「上下方向に反転」させる
        ball.dir *= -1

    # ===== パドルとの反射チェック =====
    # Ｃ－２６）パドルとボールが接触しているかを判定
    if paddle.rect.colliderect(ball.rect):
        # Ｃ－２７）接触した場合、パドルのどの位置と接触したかによって、
        #       ボールの進行方向を決定する
        ball.dir = 90 + (paddle.rect.centerx - ball.rect.centerx) \
                        / paddle.rect.width * 80
        # Ｃ－２８）ボールのスピードがスタート時のものだったら
        if ball.speed == SPEED_START:
            # Ｃ－２９）ボールのスピードを通常にする
            ball.speed = SPEED_NORMAL
    
    # ===== 壁との反射チェック =====
    # Ｃ－３０）ボールが横の壁と接触した場合
    if ball.rect.centerx < 0 or ball.rect.centerx > WINDOW_SIZE[0]:
        # Ｃ－３１）ボールを左右方向に反転させる
        ball.dir = 180 - ball.dir
    # Ｃ－３２）ボールが上の壁と接触した場合
    if ball.rect.centery < 0:
        # Ｃ－３３）ボールを上下方向に反転させる
        ball.dir =- ball.dir
        # Ｃ－３４）ボールのスピードを１段階速いものにする
        ball.speed = SPEED_UPPER

# Pygameの初期処理
pygame.init()
# キー押下判定を 5ミリ秒単位にする
pygame.key.set_repeat(5, 5)
surface = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('*** ブロックくずし ***')

# 画面に表示する各オブジェクトの作成
# Ｄ－３９blockから）ブロックリスト
block_list = []
# Ａ－７paddleから）パドルクラスのインスタンスを作成
paddle = Paddle()
# Ｂ－１９ballから）ボールクラスのインスタンスを作成
ball = Ball(SPEED_START)

# メイン処理
def main():
    # ゲームオーバーフラグ
    is_gameover = False
    # ステージクリアフラグ
    is_clear = False
    
    # Ｆ－５０最初）表示メッセージ
    myfont = pygame.font.SysFont(None, 80)
    msg_clear = myfont.render('Cleared!', True, (255, 255, 0))
    msg_gameover = myfont.render('Game Over!', True, (255, 255, 0))
    
    # ===== ブロックリストの作成処理 =====
    # ブロックの色リスト
    block_colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
                    (0, 128, 0), (128, 0, 128), (0, 0, 250)]
    # Ｄ－４０）ブロックの色リストの数だけ繰り返す
    # enumerate を用いて、０から始まる数を用意する
    for ypos, color in enumerate(block_colors):
        # Ｄ－４１）横には５つ並べる
        for xpos in range(5):
            # Ｄ－４２）x方向、y方向、ちょうど良い間隔を開けて配置
            block_list.append(Block(color, xpos * 100 + 60, ypos * 50 + 40))
    
    # メイン処理ループ
    while True:
        # Ｃ－３５最後）ボール反射チェック処理
        check_reflection()

        # ===== イベント処理 =====
        for event in pygame.event.get():
            # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Ａ－８）キー押下処理
            elif event.type == KEYDOWN:
                # Ａ－９）左右キーの場合、パドルを移動する（引数で方向を指定）
                if event.key == K_LEFT:
                    paddle.move(-1)
                elif event.key == K_RIGHT:
                    paddle.move(1)
                
        # Ｂ－２０）ボールが画面の最下部に行ってない場合
        if ball.rect.centery <= WINDOW_SIZE[1]:
            # Ｂ－２１）ボールの移動処理
            ball.move()
        # Ｂ－２２）ボールが画面下に行ったら
        else:
            # Ｂ－２３）ゲームオーバーフラグをセット
            is_gameover = True
        # Ｆ－５１）ブロックがすべて消えたらクリア
        if len(block_list) == 0:
            is_clear = True
        
        # ===== 各種描画処理 =====
        # 背景を黒にする
        surface.fill((0, 0, 0))
        # Ａ－１０最後）パドルの描画処理
        paddle.draw(surface)
        # Ｂ－２４最後）ボールの描画処理
        ball.draw(surface)
        # Ｄ－４３最後）ブロックの描画処理
        for block in block_list:
            block.draw(surface)
            
        # Ｆ－５２）クリア時のメッセージ表示
        if is_clear:
            # Ｆ－５３）表示位置の中心を調整
            msg_rect = msg_clear.get_rect()
            msg_rect.center = MSG_CENTER
            surface.blit(msg_clear, msg_rect.topleft)
        # Ｆ－５４）ゲームオーバー時のメッセージ表示
        elif is_gameover:
            # Ｆ－５５最後）表示位置の中心を調整
            msg_rect = msg_gameover.get_rect()
            msg_rect.center = MSG_CENTER
            surface.blit(msg_gameover, msg_rect.topleft)
            
        # 画面の更新
        pygame.display.update()
        # 全体を一定時間ごとに処理する
        clock.tick(30)

if __name__ == '__main__':
    main()
