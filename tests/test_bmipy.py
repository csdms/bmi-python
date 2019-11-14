import pytest

from bmipy import Bmi


class EmptyBmi(Bmi):
    def __init__(self):
        pass

    def initialize(self, config_file):
        pass

    def update(self):
        pass

    def update_until(self, then):
        pass

    def finalize(self):
        pass

    def get_var_type(self, var_name):
        pass

    def get_var_units(self, var_name):
        pass

    def get_var_nbytes(self, var_name):
        pass

    def get_var_itemsize(self, name):
        pass

    def get_var_location(self, name):
        pass

    def get_var_grid(self, var_name):
        pass

    def get_grid_rank(self, grid_id):
        pass

    def get_grid_size(self, grid_id):
        pass

    def get_value_ptr(self, var_name):
        pass

    def get_value(self, var_name):
        pass

    def get_value_at_indices(self, var_name, indices):
        pass

    def set_value(self, var_name, src):
        pass

    def set_value_at_indices(self, var_name, src, indices):
        pass

    def get_component_name(self):
        pass

    def get_input_item_count(self):
        pass

    def get_output_item_count(self):
        pass

    def get_input_var_names(self):
        pass

    def get_output_var_names(self):
        pass

    def get_grid_shape(self, grid_id):
        pass

    def get_grid_spacing(self, grid_id):
        pass

    def get_grid_origin(self, grid_id):
        pass

    def get_grid_type(self, grid_id):
        pass

    def get_start_time(self):
        pass

    def get_end_time(self):
        pass

    def get_current_time(self):
        pass

    def get_time_step(self):
        pass

    def get_time_units(self):
        pass

    def get_grid_edge_count(self, grid):
        pass

    def get_grid_edge_nodes(self, grid, edge_nodes):
        pass

    def get_grid_face_count(self, grid):
        pass

    def get_grid_face_nodes(self, grid, face_nodes):
        pass

    def get_grid_face_edges(self, grid, face_edges):
        pass

    def get_grid_node_count(self, grid):
        pass

    def get_grid_nodes_per_face(self, grid, nodes_per_face):
        pass

    def get_grid_x(self, grid, x):
        pass

    def get_grid_y(self, grid, y):
        pass

    def get_grid_z(self, grid, z):
        pass


def test_bmi_not_implemented():
    class MyBmi(Bmi):
        pass

    with pytest.raises(TypeError):
        Bmi()


def test_bmi_implemented():
    assert isinstance(EmptyBmi(), Bmi)
