import subprocess
import math

process = subprocess.Popen(
    ["sudo", "./ultra_simple", "--channel", "--serial", "/dev/ttyUSB0", "115200"],
    stdout=subprocess.PIPE,
    text=True
)

for line in process.stdout:
    if "theta" in line:
        try:
            parts = line.split()
            theta = float(parts[1])
            dist = float(parts[3])

            if dist > 0:
                x = dist * math.cos(math.radians(theta))
                y = dist * math.sin(math.radians(theta))

                print(f"Angle: {theta:.2f} | Distance: {dist:.2f} mm | X: {x:.2f} | Y: {y:.2f}")
        except:
            pass
