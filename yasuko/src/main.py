import glob
import cv2
import random

# ファイルのパスを取得
files = glob.glob("img/*.jpg")
files += glob.glob("img/*yasuko*.jpg")

# ファイルが見つからない場合はエラーを出力して終了
if not files:
    print("Error: No image files found.")
    exit()

# ウィンドウの名前を定義
window_name = "Yasuko Game"

# フルスクリーン表示にする
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # ファイルをランダムに選択して読み込む
    file_path = random.choice(files)
    image = cv2.imread(file_path)

    # 画像が読み込めなかった場合はスキップ
    if image is None:
        print("Error: Failed to read image file: " + file_path)
        continue

    # 画像をリサイズして表示
    height, width, _ = image.shape
    resized_width = 800
    resized_height = int(height * resized_width / width)
    resized_image = cv2.resize(image, (resized_width, resized_height))
    cv2.imshow(window_name, resized_image)

    # キー入力を待機
    key = cv2.waitKey(0)

    # キーに応じて処理を行う
    if key == 13: # enterキー
        continue
    elif key == 27: # escキー
        break

# ウィンドウを閉じる
cv2.destroyAllWindows()
