print("================================")
print(" AI SMART TRAFFIC MANAGEMENT")
print("================================")

vehicles = int(input("Enter number of vehicles: "))

print("\nTotal vehicles:", vehicles)

if vehicles <= 10:
    print("Traffic Density: LOW")
    print("Green Signal: 20 seconds")

elif vehicles <= 30:
    print("Traffic Density: MEDIUM")
    print("Green Signal: 40 seconds")

else:
    print("Traffic Density: HIGH")
    print("Green Signal: 60 seconds")

print("\nTraffic analysis completed!")