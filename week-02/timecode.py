frame = ("FPS")
duration = ("Duration")
seconds = ("Seconds")
print("Frames Per Second (24,30, or 60):)", frame)
frame = input(">")
while frame not in ["24", "30", "60"]:
        print("Invalid input. Please enter 24, 30, or 60.")
        frame = input(">")
print("Duration (Seconds): ", duration)
duration = input(">")
print("Total Frames: ", str(int(frame) * int(duration)))

# for i in range(int(duration)):
#    print ("Seconds: " + str(i))


for i in range(int(duration) + 1):
    print("Total Timecode: ", str(i // 3600).zfill(2) + ":" + str((i % 3600) // 60).zfill(2) + ":" + str(i % 60).zfill(2))    
print("Total Frames: " + str(int(frame) * int(duration)))  # 10

