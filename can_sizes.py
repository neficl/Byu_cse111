import math

def main():
    with open ("book3.txt") as records:
        max_size = 0
        print()
        for record in records:
            record = record.strip()
            record = record.split(";")
            name = record[0]
            radius = float(record[1])
            height = float(record[2])
            price = record[3].replace("$", "")
            volume = calculate_volume(radius, height)
            surface = calculate_surface_area(radius, height)
            storage_efficiency = compute_storage_efficiency(volume, surface)
            volume_cost = compute_cost_efficiency(volume, price)
            print (f"{name} {storage_efficiency:.1f} {volume_cost:.2f}")
            if volume_cost > max_size:
                name_max = name
                max_size = volume_cost
        print(f"\n{name_max} {max_size:.2f}")
                
    
def calculate_volume (ratio, height):
  return math.pi * pow(ratio,2) * height   
    
def calculate_surface_area(ratio, height):
  return 2.0*math.pi*ratio*(ratio+height)
     
def compute_storage_efficiency(volume, area):
    storage_efficiency = volume / area
    return storage_efficiency

def compute_cost_efficiency(volume, price):
    return volume / float(price)

main()