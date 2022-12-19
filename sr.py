import cv2
def increase_resolution(path,frame):
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    path = 'models/EDSR_x4.pb'
    sr.readModel(path)
    sr.setModel("edsr",4)
    result = sr.upsample(frame)
    return result
if __name__ == "__main__":
    cv2.imshow(result)