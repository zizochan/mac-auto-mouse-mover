import pyautogui
import time
import sys
from typing import Tuple

# 設定定数
MOVE_DISTANCE = 1  # マウス移動距離（ピクセル）
MOVE_DURATION = 0.5  # マウス移動後の待機時間（秒）
CYCLE_INTERVAL = 20  # サイクル間隔（秒）


def get_current_position() -> Tuple[int, int]:
    return pyautogui.position()


def move_mouse_slightly(x: int, y: int, distance: int = MOVE_DISTANCE) -> None:
    try:
        # マウス座標をちょこっと動かす
        pyautogui.moveTo(x + distance, y)
        time.sleep(MOVE_DURATION)
        pyautogui.moveTo(x, y)
    except pyautogui.FailSafeException:
        print("マウスが画面の隅に移動されました。安全のため終了します。")
        sys.exit(1)


def main() -> None:
    print("カーソルを定期的に動かして画面ロックを防ぎます（Ctrl+Cで終了）")
    print(
        f"設定: 移動距離={MOVE_DISTANCE}px, 移動間隔={MOVE_DURATION}秒, サイクル間隔={CYCLE_INTERVAL}秒"
    )

    try:
        while True:
            # 現在のマウス座標を取得
            x, y = get_current_position()

            # マウス座標をちょこっと動かす
            move_mouse_slightly(x, y)

            # 次の動作まで待機
            time.sleep(CYCLE_INTERVAL)

    except KeyboardInterrupt:
        print("\n終了します")
        sys.exit(0)
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
