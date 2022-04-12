# Draw an ER Diagram and convert it into relational modal for a Company which has several Employees working on different type of projects Several Employees are working for one Department every Department has a Manager Several Employees are supervised by one Employee
# Draw ER Diagram for hospital management system
# Draw ER Diagram for online Ticket Railway Reservation System
# Construct ER diagram for library management system
# Construct an ER diagram for a hospital with a set of patients and a set of medical doctors associatrd with each patient a log of various tests and examination conducted
import cv2
from cvzone.HandTrackingModule import HandDetector
from question import *

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 780)
detector = HandDetector(detectionCon=0.8, maxHands=1)
colorR = 225, 0, 225


completeQuestionEntityDataset = ["department", "manager", "employee", "projects", "hospital", "library", "doctors", "patient", "employee", "wards"]
incompleteQuestionEntitydataset = {
    "hospital": ["doctors", "patient", "employee", "wards"],
    "library": ["books", "employee", "customers"]
}
entityList = []

attributeDataset = {
    "department": ["name", "id", "manager"],
    "manager": ["name", "id", "phone", "department"],
    "employee": ["name", "id", "phone", "position"],
    "company": ["name", "id"],
    "projects": ["name", "id", "duration", "employee"],
    "hospital": ["name", "no_wards", "no_doctors", "specialist"],
    "doctors": ["name", "id", "specialization", "phone"],
    "patient": ["id", "name", "test", "problem"],
    "wards": ["id", "name", "class", "count"]
}

question = ter()
question = question.lower()
print(question)
questionSet = question.split(" ")
print(questionSet)

for word in questionSet:
    if word in completeQuestionEntityDataset:
        # print(word)
        if word not in entityList:
            entityList.append(word)

if len(entityList) == 1:
    token = entityList[0];
    entityList.pop(0)
    entityList = incompleteQuestionEntitydataset.get(token);
# else:
#     token = entityList[0]
#     if token in incompleteQuestionEntitydataset:
#         entityList.pop(0)


# entityList.sort()

# print(entityList)


class DragRect():
    def __init__(self, posCenter, size=[200, 70]):
        self.posCenter = posCenter
        self.size = size

    def updates(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # if the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor


def drawAttributes(attributeList, cx, cy):
    font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(r, entityList[text], (cx - 80, cy), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    for x in range(0, len(attributeList)):
        if x == 0:
            cv2.ellipse(img, (cx - 60, cy + 100), (50, 30), 0, 0, 360, colorR, 3)
            cv2.putText(img, attributeList[x], (cx - 95, cy + 100), font, 0.6, (0, 225, 0), 2, cv2.LINE_AA)
            cv2.arrowedLine(img, (cx, cy + 35), (cx - 60, cy + 65), colorR, 3)
        elif x == 1:
            cv2.ellipse(img, (cx + 60, cy + 100), (50, 30), 0, 0, 360, colorR, 3)
            cv2.putText(img, attributeList[x], (cx + 25, cy + 100), font, 0.6, (0, 225, 0), 2, cv2.LINE_AA)
            cv2.arrowedLine(img, (cx, cy + 35), (cx + 60, cy + 65), colorR, 3)
        elif x == 2:
            cv2.ellipse(img, (cx - 60, cy - 100), (50, 30), 0, 0, 360, colorR, 3)
            cv2.putText(img, attributeList[x], (cx - 95, cy - 100), font, 0.6, (0, 225, 0), 2, cv2.LINE_AA)
            cv2.arrowedLine(img, (cx, cy - 35), (cx - 60, cy - 65), colorR, 3)
        elif x == 3:
            cv2.ellipse(img, (cx + 60, cy - 100), (50, 30), 0, 0, 360, colorR, 3)
            cv2.putText(img, attributeList[x], (cx + 25, cy - 100), font, 0.6, (0, 225, 0), 2, cv2.LINE_AA)
            cv2.arrowedLine(img, (cx, cy - 35), (cx + 60, cy - 65), colorR, 3)







rectList = []
for x in range(0, len(entityList)):
    rectList.append(DragRect([x * 250 + 150, 150]))
    # print(rectList)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hand, _ = detector.findHands(img)
    if hand:
        hand1 = hand[0]
        lmList = hand1["lmList"]
        type = hand1["type"]
        # print(type)
        a = detector.fingersUp(hand1)
        print(a)
        # print(lmList)
        length, info = detector.findDistance((lmList[8][0], lmList[8][1]), (lmList[12][0], lmList[12][1]))
        # print(length)

        if length < 45:
            cursor = lmList[8][0], lmList[8][1]
            # call the update here
            for rect in rectList:
                rect.updates(cursor)
    text = 0
    for rect in rectList:

        # print(rect.posCenter)
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(img, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), colorR, 3)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, entityList[text], (cx - 80, cy), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        if attributeDataset.get(entityList[text]):
            #cv2.ellipse(img, (cx - 50, cy + 100), (50, 30), 0, 0, 360, colorR, 3)
            attributeList = attributeDataset.get(entityList[text])
            drawAttributes(attributeList, cx, cy)
        text = text + 1
        # print(text)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
