# src/spectrum_allocation.py

def first_fit(allocation_map, required_slots):
    for i in range(len(allocation_map) - required_slots + 1):
        if all(slot == 0 for slot in allocation_map[i:i + required_slots]):
            for j in range(i, i + required_slots):
                allocation_map[j] = 1
            return i
    return -1  # Bloqueo si no se encuentra espacio contiguo disponible
