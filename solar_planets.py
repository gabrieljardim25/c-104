import cv2

img = cv2.imread("solar-system.jpg") 

cv2.putText(img,
            "Sol",
             (100,80),
             cv2.FONT_HERSHEY_COMPLEX,
             2,
             (0,0,255)
             )

cv2.putText(img,
            "Mercurio",
             (100,190),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (0,255,0)
             )

cv2.putText(img,
            "Venus",
             (200,190),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (0,255,0)
             )

cv2.putText(img,
            "Terra",
             (300,190),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (0,255,0)
             )

cv2.putText(img,
            "Marte",
             (400,190),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (0,255,0)
             )

cv2.putText(img,
            "Jupiter",
             (600,80),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (0,255,0)
             )

cv2.putText(img,
            "Saturno",
             (800,150 ),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (0,255,0)
             )

cv2.putText(img,
            "urano",
             (1000,150),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (0,255,0)
             )

cv2.putText(img,
            "Netuno",
             (1100,150),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (0,255,0)
             )










cv2.imshow("resultado", img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)
