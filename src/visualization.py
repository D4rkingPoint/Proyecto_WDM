# src/visualization.py
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20

class SpectrumVisualization(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        self.allocation_map = []  # Mapa de asignación de espectro

    def update_allocation(self, allocation_map):
        self.allocation_map = allocation_map

    def on_draw(self):
        arcade.start_render()
        for i, slot in enumerate(self.allocation_map):
            color = arcade.color.GREEN if slot == 0 else arcade.color.RED
            arcade.draw_rectangle_filled(CELL_SIZE * i + 10, SCREEN_HEIGHT // 2, CELL_SIZE, CELL_SIZE, color)
