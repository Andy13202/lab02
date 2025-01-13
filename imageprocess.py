import cv2

# 開啟原始影片
video = cv2.VideoCapture('path_to_video.mp4')

# 檢查影片是否成功開啟
if not video.isOpened():
    print("Error: Could not open video.")
    exit()

# 獲取原始影片的寬度和高度
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 設置輸出影片的編碼、檔名、幀率和分辨率
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height), isColor=False)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # 轉換為灰階
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 應用高斯模糊
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    # 顯示處理後的影像
    cv2.imshow('Filtered Frame', blurred_frame)

    # 儲存處理後的影像
    out.write(blurred_frame)

    # 按 'q' 鍵退出
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 釋放資源和關閉視窗
video.release()
out.release()
cv2.destroyAllWindows()