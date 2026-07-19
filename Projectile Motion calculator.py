import math

def calculate_projectile(velocity,angle_degrees):
    g = 9.81
    angle_rad = math.radians(angle_degrees)
    
    max_height = (velocity**2*(math.sin(angle_rad)**2)) / (2 * g)
    range_val = (velocity**2 * math.sin(2 * angle_rad)) / g
    
    return max_height, range_val

print('--Projectile Calculator --')
v = float(input('Initial Velocity (m/s): '))
a = float(input("Launch Angle (degrees): "))

h, r = calculate_projectile(v,a)
print(f'Max Height: {h:.4f} meters')
print(f'Max range: {r:.4f} meters')