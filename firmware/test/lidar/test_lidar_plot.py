import subprocess
import math
import matplotlib.pyplot as plt

# start lidar process
process = subprocess.Popen(
    ["sudo", "./ultra_simple", "--channel", "--serial", "/dev/ttyUSB0", "115200"],
    stdout=subprocess.PIPE,
    text=True
)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

angles = []
distances = []

for line in process.stdout:
    if "theta" in line:
        try:
            parts = line.split()
            theta = float(parts[1])
            dist = float(parts[3])

            if dist > 0:
                angles.append(math.radians(theta))
                distances.append(dist)

            # update plot tiap beberapa data
            if len(angles) > 100:
                ax.clear()
                ax.scatter(angles, distances, s=5)
                ax.set_title("LiDAR Scan")
                plt.pause(0.01)

                angles.clear()
                distances.clear()

        except:
            pass
