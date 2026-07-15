import cv2
import numpy as np
import sys

def show_menu():
    print("\n" + "="*50) # for aesthetic 50 time = sign
    print("           OPENCV COMPUTER VISION MENU          ")
    print("="*50)
    print("1.  Read, Display, and Save Image")
    print("2.  Resize Image (Exact & Scaled)")
    print("3.  Flip Image (Horizontal, Vertical, Both)")
    print("4.  Draw Shapes and Add Text")
    print("5.  Image Translation (Shifting)")
    print("6.  Image Rotation")
    print("7.  Thresholding (Binary or Edges)")
    print("8.  Blurring (Gaussian & Median)")
    print("9.  Morphological Operations (Tophat & Blackhat)")
    print("10. Edge Detection (Canny)")
    print("11. Read and Write Video File")
    print("12. Capture Live Video from Webcam")
    print("0.  Exit")
    print("="*50) # for aesthetic 50 time = sign

def load_image():
    img = cv2.imread("D:\Ramesh Python\Open CV\Highway.jpeg")
    return img

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (0-12): ").strip()
        
        if choice == '0':
            print("\nExiting program. Goodbye!")
            sys.exit()
            
        elif choice == '1':
            img = load_image()
            if img is not None:
                print("\n[INFO] Displaying image. Press ANY key on the image window to close it.")
                cv2.imshow('Original Image', img)
                cv2.imwrite('saved_image.jpg', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
                

        elif choice == '2':
            img = load_image()
            if img is not None:
                width1 = img.shape[1]
                height1 = img.shape[0]
                resized_75 = cv2.resize(img, (int(width1*0.75), int(height1*.75)))
                
                resized_50 = cv2.resize(img, (int(width1*0.50), int(height1*0.50)))
                
                cv2.imshow("Original",img)
                cv2.waitKey(0)
                cv2.imshow('Resized to 75', resized_75)
                cv2.waitKey(0)
                cv2.imshow('Resized to 50% Scale', resized_50)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '3':
            img = load_image()
            if img is not None:
                flip_h = cv2.flip(img, 1)
                flip_v = cv2.flip(img, 0)
                flip_b = cv2.flip(img, -1)
                
                cv2.imshow('Horizontal Flip', flip_h)
                cv2.waitKey(0)
                cv2.imshow('Vertical Flip', flip_v)
                cv2.waitKey(0)
                cv2.imshow('Both Axes Flip', flip_b)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '4':
            img = load_image()
            if img is not None:
                drawing_img = img.copy()
                # Line
                cv2.line(img, (0, 0), (150, 150), (255, 0, 0), 2)
                cv2.rectangle(img, (200, 150), (250, 300), (0, 255, 0), 3)
                cv2.circle(img, (300, 75), 70, (255, 0, 255), 3)
                pts_polygon = np.array([[100, 50], [100, 300], [500, 50], [500, 300]],np.int32)
                cv2.polylines(img, [pts_polygon], True, (0, 255, 255), 3)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(img,'CFO RAMESH!',(50, 500),font,3,(200, 255, 255),2,cv2.LINE_AA)
                cv2.imshow('Shapes and Text', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '5':
            img = load_image()
            if img is not None:
                column = img.shape[1]
                row = img.shape[0]

                s = np.float32([[1, 0, 150], [0, 1, 70]])

                shifted = cv2.warpAffine(img, s, (column, row))

                cv2.imshow('Shifted Image', shifted)
                cv2.imshow('Original Image', img)
                

                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '6':
            img = load_image()
            if img is not None:
                row = img.shape[1]
                column=img.shape[0]
                
                center = (column / 2, row / 2)
                angle = 90
                r = cv2.getRotationMatrix2D(center, angle, 1)
                rotate = cv2.warpAffine(img, r, (column, row))
                
                cv2.imshow('Rotated Image (45 deg)', rotate)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '7':
            img = load_image()
            # img = cv2.imread(load_image(),0)
            if img is not None:
                
                min_thresh = 100
                max_thresh = 200
                edges = cv2.Canny(img, min_thresh, max_thresh)
                
                
                cv2.imshow('Edges', edges)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '8':
            img = load_image()
            if img is not None:
                resize_mb = cv2.resize(img, (1000, 1000))
                kernel = 3
                blur_mb = cv2.medianBlur(resize_mb, kernel)
                

                resize_gb = cv2.resize(img, (1000, 1000))
                ksize = (7, 7)
                sigmax = 0
                sigmay = 0
                
                blur_gb = cv2.GaussianBlur(resize_gb, ksize, sigmax)

                cv2.imshow("Original", img)
                cv2.imshow('Gaussian Blur', resize_gb)
                cv2.waitKey(0)
                cv2.imshow('Median Blur', resize_mb)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '9':
            img = load_image()
            if img is not None:
                width = 1200
                height = 1000
                dim9 = (width, height)
                resized9 = cv2.resize(img, dim9)
                kernel=np.ones((5,5),dtype="uint8")
                tophat = cv2.morphologyEx(resized9, cv2.MORPH_TOPHAT, kernel)
                blackhat = cv2.morphologyEx(resized9, cv2.MORPH_BLACKHAT, kernel)
                
                cv2.imshow('Tophat Morphology', tophat)
                cv2.waitKey(0)
                cv2.imshow('Blackhat Morphology', blackhat)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '10':
            img = load_image()
            if img is not None:
                edges = cv2.Canny(img, 100, 200)
                cv2.imshow('Canny Edge Detection', edges)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '11':
            video = cv2.VideoCapture("D:\Ramesh Python\Open CV\Vehicles.mp4")
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            output11 = cv2.VideoWriter("output.mp4",fourcc,25.0,(1280,720))
            while video.isOpened():
                ret,frame = video.read()
                if ret:
                    output11.write(frame)
                    cv2.imshow("frame",frame)

                    if cv2.waitKey(1) & 0xFF==ord("s"):
                        break
                else:
                    break
            cv2.destroyAllWindows()
            video.release()
            output11.release()
            print("[INFO] Video processed and saved successfully.")

        elif choice == '12':
            cap = cv2.VideoCapture(0)
            while cap.isOpened():
                _,frame = cap.read()
                cv2.imshow("Live", frame)
                if cv2.waitKey(1) & 0xFF==ord("z"):
                    break
            cv2.destroyAllWindows()

        else:
            print("\n[INVALID] Please enter a valid number between 0 and 12.")

if __name__ == '__main__': # for running all codes options in single file
    main()



