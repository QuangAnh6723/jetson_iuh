import cv2

def cat_video(path):
    vidObj = cv2.VideoCapture(path)
    count = 0
    success = 1
    while success:
        success, image = vidObj.read()
        if count % 10 == 0:
            cv2.imwrite("yolo-seg-tuan3/img_cut/img%d.jpg" %(count/10), image)
        count += 1


if __name__ == '__main__':
    cat_video("yolo-seg-tuan3/video_data.mp4")