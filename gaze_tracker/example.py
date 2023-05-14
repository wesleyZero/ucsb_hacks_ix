"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
from cheatchecker.views import path
# class Example():
gaze = GazeTracking()
# video = cv2.VideoCapture(0)
video = cv2.VideoCapture(path)
total_frames = 0
fps = video.get(cv2.CAP_PROP_FPS)
eye_detected_ratio = 0  # this is the % of the time eyes are detected
# test comment

no_eye_times = []           # these are the times where no eyes are detected
no_eye_duration = 1
last_eye_detection_state = None
durations = {}

while True:
    # We get a new frame from the video
    _, frame = video.read()

    if frame is None:
        break  # end of the video file
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60),
                cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()

    # calculating the % time eyes are detected
    if left_pupil:
        print("_")
    else:
        print(f"frame # = {total_frames} no eyes {no_eye_duration}")

    eyes_detected = 1 if left_pupil else 0
    eye_detected_ratio = (eye_detected_ratio * total_frames +
                          eyes_detected) / (total_frames + 1)

    # if not eyes_detected and eyes_detected != last_eye_detection_state:
    # 	no_eye_duration += 1
    # elif not eyes_detected and last_eye_detection_state == 0:
    # 	no_eye_times.append(total_frames)
    # 	no_eye_duration += 1
    # else:
    # 	no_eye_duration = 1

    if not eyes_detected and last_eye_detection_state == 1:
        no_eye_times.append(total_frames)
        no_eye_duration += 1
    elif not eyes_detected and last_eye_detection_state == 0:
        no_eye_duration += 1
    # else:
    # 	if len(no_eye_times): durations[no_eye_times[-1]] = no_eye_duration
    # 	no_eye_duration = 1
    elif eyes_detected and last_eye_detection_state == 0:
        if len(no_eye_times):
            durations[no_eye_times[-1]] = no_eye_duration - 1
        no_eye_duration = 1
    # else:
        # no_eye_duration = 1

    total_frames += 1

    last_eye_detection_state = eyes_detected

    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130),
                cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165),
                cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, f"horiz ratio {gaze.horizontal_ratio()}",
                (90, 195), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, f"vert ratio {gaze.vertical_ratio()}",
                (90, 230), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, f"% eye detect {eye_detected_ratio}",
                (90, 260), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break

# print(no_eye_times)
print(durations)
video.release()
cv2.destroyAllWindows()
