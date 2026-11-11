import cv2
import time
from ultralytics import YOLO

# ==========================================
# 1. AI SMART TRAFFIC MANAGEMENT SYSTEM
# ==========================================

print("=" * 45)
print(" AI SMART TRAFFIC MANAGEMENT SYSTEM")
print("=" * 45)

# Load YOLO AI model
print("\nLoading YOLO AI model...")

model = YOLO("yolo11n.pt")

print("YOLO model loaded successfully!")

# ==========================================
# 2. CAMERA INITIALIZATION
# ==========================================

print("\nOpening laptop camera...")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("DirectShow camera unavailable. Trying default...")
    cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Camera not found!")
    print("Check Windows camera permissions.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Camera connected successfully!")

# ==========================================
# 3. VEHICLE CLASS NAMES
# ==========================================

VEHICLE_CLASSES = {
    2: "Car",
    3: "Motorcycle",
    5: "Bus",
    7: "Truck"
}

# ==========================================
# 4. TRAFFIC DENSITY FUNCTION
# ==========================================

def calculate_traffic(total):

    if total <= 3:
        density = "LOW"
        green_time = 15

    elif total <= 7:
        density = "MEDIUM"
        green_time = 30

    else:
        density = "HIGH"
        green_time = 45

    return density, green_time


# ==========================================
# 5. MAIN AI DETECTION SYSTEM
# ==========================================

print("\nAI TRAFFIC DETECTION STARTED!")
print("Press Q to exit.")

previous_time = time.time()

while True:

    success, frame = cap.read()

    if not success:
        print("Camera frame not received!")
        break

    # AI vehicle detection
    results = model(
        frame,
        conf=0.35,
        verbose=False
    )

    # Vehicle counters
    car = 0
    bike = 0
    bus = 0
    truck = 0

    # ======================================
    # 6. COUNT VEHICLES
    # ======================================

    for box in results[0].boxes:

        class_id = int(box.cls[0])

        if class_id == 2:
            car += 1

        elif class_id == 3:
            bike += 1

        elif class_id == 5:
            bus += 1

        elif class_id == 7:
            truck += 1

    total = car + bike + bus + truck

    # ======================================
    # 7. TRAFFIC DENSITY
    # ======================================

    density, green_time = calculate_traffic(total)

    # ======================================
    # 8. FPS CALCULATION
    # ======================================

    current_time = time.time()

    fps = 1 / max(current_time - previous_time, 0.001)

    previous_time = current_time

    # ======================================
    # 9. DRAW AI DETECTION BOXES
    # ======================================

    output = results[0].plot()

    # ======================================
    # 10. DISPLAY DASHBOARD
    # ======================================

    cv2.rectangle(
        output,
        (5, 5),
        (400, 245),
        (0, 0, 0),
        2
    )

    cv2.putText(
        output,
        "AI SMART TRAFFIC SYSTEM",
        (15, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0, 255, 255),
        2
    )

    cv2.putText(
        output,
        f"Total Vehicles: {total}",
        (15, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0, 255, 0),
        2
    )

    cv2.putText(
        output,
        f"Cars: {car}  Bikes: {bike}",
        (15, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2
    )

    cv2.putText(
        output,
        f"Buses: {bus}  Trucks: {truck}",
        (15, 135),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        2
    )

    cv2.putText(
        output,
        f"Traffic Density: {density}",
        (15, 170),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0, 255, 255),
        2
    )

    cv2.putText(
        output,
        f"Green Signal: {green_time} sec",
        (15, 205),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (0, 255, 0),
        2
    )

    cv2.putText(
        output,
        f"FPS: {fps:.1f}",
        (15, 235),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 255, 255),
        1
    )

    # ======================================
    # 11. DISPLAY LIVE TRAFFIC WINDOW
    # ======================================

    cv2.imshow(
        "AI Smart Traffic Management System",
        output
    )

    # ======================================
    # 12. TERMINAL OUTPUT
    # ======================================

    print(
        f"\rVehicles: {total} | "
        f"Cars: {car} | "
        f"Bikes: {bike} | "
        f"Buses: {bus} | "
        f"Trucks: {truck} | "
        f"Density: {density} | "
        f"Green: {green_time}s",
        end=""
    )

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ==========================================
# 13. CLOSE SYSTEM
# ==========================================

cap.release()

cv2.destroyAllWindows()

print("\n\nAI TRAFFIC SYSTEM STOPPED.")
print("Thank you!")