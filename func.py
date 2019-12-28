def choose_face(input):
    #choose face
    #input,output はnumpy
    from detector import Detector
    import cv2
    import os
    import glob
    
    dim = 128
    
    obj = Detector(dim = dim)
    
    frame = input
    
    faces, landmarks, boxes = obj.face_detector(frame)
    
    for face, landmark, box in zip(faces, landmarks, boxes):
        x, y, w, h = box
        #align = obj.align(frame, landmark, obj.INNER_EYES_AND_BOTTOM_LIP)
        align = obj.align(frame, landmark, obj.NOSE_AND_LIP)
        cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255))
        obj.show_landmark(frame, landmark)
        face = cv2.resize(face, (dim, dim))
        frame[0 : dim, 0 : dim] = align
        frame[0 : dim, dim : dim + dim] = face
    return frame[0 : dim, 0 : dim]

def oppo(imput):
    #画像を左右反転する
    import cv2
    vflip_img = cv2.flip(imput, 1)
    return vflip_img

def make_dir(path):
    import os
    import glob
    folders = sorted(glob.glob(path + '/*'))
    for i in folders:    
        try:
            os.makedirs(path + '_d/' + i.split('/')[-1])
        except:
            print('warmming: the name of dir is exited!!!')
        

if __name__ == "__main__":
    make_dir('/Users/songminglun/Desktop/research/github/processing_pictures/new_data_20191128')
