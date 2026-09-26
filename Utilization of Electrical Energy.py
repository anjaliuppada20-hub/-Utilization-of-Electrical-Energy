# -Utilization-of-Electrical-Energy
# -------------------------------------------------------------
# 3. ELECTRIC TRACTION: TRAPEZOIDAL SPEED-TIME CURVE
# -------------------------------------------------------------
import math

def traction_speed_time(distance_km, run_time_sec, stop_time_sec, alpha=1.5, beta=2.5):
    """
    distance_km  : Distance between two stops in km
    run_time_sec : Actual running time in seconds (T)
    stop_time_sec: Duration of stop at station (ts)
    alpha        : Acceleration in km/h/s
    beta         : Retardation / braking in km/h/s
    """
    D = distance_km
    T = run_time_sec
    
    # Constant K for trapezoidal curve: K = (alpha + beta) / (2 * alpha * beta)
    K = (alpha + beta) / (2 * alpha * beta)
    
    # Quadratic equation for Crest Speed (Vm): K * Vm^2 - T * Vm + 3600 * D = 0
    discriminant = (T ** 2) - (4 * K * 3600 * D)
    if discriminant < 0:
        print("Error: Train cannot cover this distance in the given running time!")
        return
        
    Vm = (T - math.sqrt(discriminant)) / (2 * K)  # Crest speed in km/h
    
    # Speeds
    avg_speed = (D * 3600) / T  # km/h
    schedule_speed = (D * 3600) / (T + stop_time_sec)  # km/h
    
    # Times for each phase
    t1 = Vm / alpha            # Acceleration time
    t3 = Vm / beta             # Braking time
    t2 = T - (t1 + t3)         # Free running time
    
    print("=" * 45)
    print("   ELECTRIC TRACTION: SPEED-TIME ANALYSIS")
    print("=" * 45)
    print(f"Distance Between Stops: {D} km")
    print(f"Actual Run Time (T)   : {T} s")
    print(f"Acceleration (α)      : {alpha} km/h/s")
    print(f"Braking (β)           : {beta} km/h/s")
    print("-" * 45)
    print(f"Crest Speed (Vm)      : {Vm:.2f} km/h")
    print(f"Average Speed         : {avg_speed:.2f} km/h")
    print(f"Schedule Speed        : {schedule_speed:.2f} km/h")
    print(f"Phase breakdown       : Accel = {t1:.1f}s | Free Run = {t2:.1f}s | Brake = {t3:.1f}s")
    print("=" * 45)

# Example: Suburban train run of 1.5 km in 120 seconds with a 20-second stop
traction_speed_time(distance_km=1.5, run_time_sec=120, stop_time_sec=20, alpha=1.8, beta=2.2)
