# src/main.py
from environment import NetworkEnvironment
from routing import get_shortest_path
from modulation import select_modulation
from spectrum_allocation import first_fit
from drl_agent import DRLAgent
from visualization import SpectrumVisualization

def main():
    # Configurar entorno de red
    env = NetworkEnvironment("data/network_topology.json")
    agent = DRLAgent(action_space=[0, 1])  # Ejemplo de espacio de acciones
    visualization = SpectrumVisualization(800, 600)

    # Ejecutar una simulación simple
    source, target = 'A', 'B'  # Reemplazar con nodos válidos
    path = get_shortest_path(env.graph, source, target)
    if path:
        distance = sum(env.graph[path[i]][path[i+1]]['distance'] for i in range(len(path) - 1))
        modulation = select_modulation(distance)
        allocation_map = [0] * 100  # Ejemplo de asignación con 100 FSUs
        start_slot = first_fit(allocation_map, required_slots=5)

        if start_slot >= 0:
            print(f"Path: {path}, Modulation: {modulation}, Start Slot: {start_slot}")
            visualization.update_allocation(allocation_map)
            visualization.run()  # Iniciar visualización
        else:
            print("Bloqueo: no se encontró espectro disponible")
    else:
        print("Bloqueo: no se encontró ruta")

if __name__ == "__main__":
    main()
