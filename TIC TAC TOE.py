import cv2
import numpy as np
clicked = False
x1 = 0
y1 = 0
co = 0
cx = 0
eo = 0
w1 = 0
w2 = 0
cl = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
chances1 = "First person chances"
chances2 = "Second person chances"
bg = 255*np.ones((700, 600, 3), np.uint8)
cv2.line(bg, (200, 0), (200, 600), (0, 0, 0), 3)
cv2.line(bg, (400, 0), (400, 600), (0, 0, 0), 3)
cv2.line(bg, (0, 200), (600, 200), (0, 0, 0), 3)
cv2.line(bg, (0, 400), (600, 400), (0, 0, 0), 3)
cv2.line(bg, (0, 600), (600, 600), (0, 0, 0), 3)
cv2.imshow("criss_cross", bg)


def func(event, x, y, flags, param):

    global clicked, x1, y1, eo, cx, co, c1, c2, c3, c4, c5, c6, c7, c8, c9, w1, w2
    if event == cv2.EVENT_LBUTTONDOWN:
        eo += 1
        if eo % 2 == 0:
            cx += 1
        else:
            co += 1
        clicked = True
        if(x < 200 and y < 200):
            x1 = 100
            y1 = 100
            if eo % 2 == 0:
                cl[0, 0] = 1
            else:
                cl[0, 0] = 4

        if((x > 200 and x < 400) and y < 200):
            x1 = 300
            y1 = 100
            if eo % 2 == 0:
                cl[0, 1] = 1
            else:
                cl[0, 1] = 4

        if(x > 400 and y < 200):
            x1 = 500
            y1 = 100
            if eo % 2 == 0:
                cl[0, 2] = 1
            else:
                cl[0, 2] = 4

        if((y > 200 and y < 400) and x < 200):
            x1 = 100
            y1 = 300
            if eo % 2 == 0:
                cl[1, 0] = 1
            else:
                cl[1, 0] = 4

        if((x > 200 and x < 400) and y > 200 and y < 400):
            x1 = 300
            y1 = 300
            if eo % 2 == 0:
                cl[1, 1] = 1
            else:
                cl[1, 1] = 4

        if((x > 400 and y > 200) and y < 400):
            x1 = 500
            y1 = 300
            if eo % 2 == 0:
                cl[1, 2] = 1
            else:
                cl[1, 2] = 4

        if((x < 200 and y > 400) and y < 600):
            x1 = 100
            y1 = 500
            if eo % 2 == 0:
                cl[2, 0] = 1
            else:
                cl[2, 0] = 4

        if((x > 200 and x < 400) and (y > 400 and y < 600)):
            x1 = 300
            y1 = 500
            if eo % 2 == 0:
                cl[2, 1] = 1
            else:
                cl[2, 1] = 4

        if((x > 400 and x < 600) and (y > 400 and y < 600)):
            x1 = 500
            y1 = 500

            if eo % 2 == 0:
                cl[2, 2] = 1
            else:
                cl[2, 2] = 4


def win(cl):
    global w1, w2
    if (cl[0, 0]+cl[1, 1]+cl[2, 2]) == 12:
        w2 = 1
    if (cl[0, 0]+cl[1, 1]+cl[2, 2]) == 3:
        w1 = 1
    if (cl[0, 0]+cl[0, 1]+cl[0, 2]) == 12:
        w2 = 1
    if (cl[0, 0]+cl[0, 1]+cl[0, 2]) == 3:
        w1 = 1
    if (cl[1, 0]+cl[1, 1]+cl[1, 2]) == 12:
        w2 = 1
    if (cl[1, 0]+cl[1, 1]+cl[1, 2]) == 3:
        w1 = 1
    if (cl[2, 0]+cl[2, 1]+cl[2, 2]) == 12:
        w2 = 1
    if (cl[2, 0]+cl[2, 1]+cl[2, 2]) == 3:
        w1 = 1
    if (cl[2, 0]+cl[1, 1]+cl[0, 2]) == 12:
        w2 = 1
    if (cl[2, 0]+cl[1, 1]+cl[0, 2]) == 3:
        w1 = 1
    if (cl[0, 1]+cl[1, 1]+cl[2, 1]) == 12:
        w2 = 1
    if (cl[0, 2]+cl[1, 2]+cl[2, 2]) == 12:
        w2 = 1
    if (cl[0, 0]+cl[1, 0]+cl[2, 0]) == 12:
        w2 = 1
    if (cl[0, 1]+cl[1, 1]+cl[2, 1]) == 3:
        w1 = 1
    if (cl[0, 2]+cl[1, 2]+cl[2, 2]) == 3:
        w1 = 1
    if (cl[0, 0]+cl[1, 0]+cl[2, 0]) == 3:
        w1 = 1


while 1:
    cv2.imshow("criss_cross", bg)
    cv2.setMouseCallback('criss_cross', func)
    if clicked == True:
        if eo % 2 == 0:
            cv2.line(bg, (x1-70, y1-70), (x1+60, y1+60), (0, 0, 0), 3)
            cv2.line(bg, (x1-70, y1+60), (x1+60, y1-70), (0, 0, 0), 3)
        else:
            cv2.circle(bg, (x1, y1), 70, (0, 0, 0), 3)
        win(cl)
        if w1 == 1:
            cv2.putText(bg, "X WINS", (280, 680),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if w2 == 1:
            cv2.putText(bg, "O WINS", (280, 680),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if((w2 != 1 and w1 != 1) and eo == 9):
            cv2.putText(bg, "DRAW", (280, 680),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
