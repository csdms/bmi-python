from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any

from bmipy.bmi import Bmi

if TYPE_CHECKING:
    import numpy as np
    from numpy.typing import NDArray


class BmiStub(Bmi):
    """Concrete BMI base for partial implementations.

    Unless overridden, all methods raise ``NotImplementedError``.
    """

    def initialize(self, config_file: str) -> None:
        raise NotImplementedError("initialize")

    def update(self) -> None:
        raise NotImplementedError("update")

    def update_until(self, time: float) -> None:
        raise NotImplementedError("update_until")

    def finalize(self) -> None:
        raise NotImplementedError("finalize")

    def get_component_name(self) -> str:
        raise NotImplementedError("get_component_name")

    def get_input_item_count(self) -> int:
        raise NotImplementedError("get_input_item_count")

    def get_input_var_names(self) -> tuple[str, ...]:
        raise NotImplementedError("get_input_var_names")

    def get_output_item_count(self) -> int:
        raise NotImplementedError("get_output_item_count")

    def get_output_var_names(self) -> tuple[str, ...]:
        raise NotImplementedError("get_output_var_names")

    def get_var_grid(self, name: str) -> int:
        raise NotImplementedError("get_var_grid")

    def get_var_itemsize(self, name: str) -> int:
        raise NotImplementedError("get_var_itemsize")

    def get_var_location(self, name: str) -> str:
        raise NotImplementedError("get_var_location")

    def get_var_nbytes(self, name: str) -> int:
        raise NotImplementedError("get_var_nbytes")

    def get_var_type(self, name: str) -> str:
        raise NotImplementedError("get_var_type")

    def get_var_units(self, name: str) -> str:
        raise NotImplementedError("get_var_units")

    def get_current_time(self) -> float:
        raise NotImplementedError("get_current_time")

    def get_end_time(self) -> float:
        raise NotImplementedError("get_end_time")

    def get_start_time(self) -> float:
        raise NotImplementedError("get_start_time")

    def get_time_step(self) -> float:
        raise NotImplementedError("get_time_step")

    def get_time_units(self) -> str:
        raise NotImplementedError("get_time_units")

    def get_value(self, name: str, dest: NDArray[Any]) -> NDArray[Any]:
        raise NotImplementedError("get_value")

    def get_value_at_indices(
        self, name: str, dest: NDArray[Any], inds: NDArray[np.int_]
    ) -> NDArray[Any]:
        raise NotImplementedError("get_value_at_indices")

    def get_value_ptr(self, name: str) -> NDArray[Any]:
        raise NotImplementedError("get_value_ptr")

    def set_value(self, name: str, src: NDArray[Any]) -> None:
        raise NotImplementedError("set_value")

    def set_value_at_indices(
        self, name: str, inds: NDArray[np.int_], src: NDArray[Any]
    ) -> None:
        raise NotImplementedError("set_value_at_indices")

    def get_grid_edge_count(self, grid: int) -> int:
        raise NotImplementedError("get_grid_edge_count")

    def get_grid_edge_nodes(
        self, grid: int, edge_nodes: NDArray[np.int_]
    ) -> NDArray[np.int_]:
        raise NotImplementedError("get_grid_edge_nodes")

    def get_grid_face_count(self, grid: int) -> int:
        raise NotImplementedError("get_grid_face_count")

    def get_grid_face_edges(
        self, grid: int, face_edges: NDArray[np.int_]
    ) -> NDArray[np.int_]:
        raise NotImplementedError("get_grid_face_edges")

    def get_grid_face_nodes(
        self, grid: int, face_nodes: NDArray[np.int_]
    ) -> NDArray[np.int_]:
        raise NotImplementedError("get_grid_face_nodes")

    def get_grid_node_count(self, grid: int) -> int:
        raise NotImplementedError("get_grid_node_count")

    def get_grid_nodes_per_face(
        self, grid: int, nodes_per_face: NDArray[np.int_]
    ) -> NDArray[np.int_]:
        raise NotImplementedError("get_grid_nodes_per_face")

    def get_grid_origin(
        self, grid: int, origin: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        raise NotImplementedError("get_grid_origin")

    def get_grid_rank(self, grid: int) -> int:
        raise NotImplementedError("get_grid_rank")

    def get_grid_shape(self, grid: int, shape: NDArray[np.int_]) -> NDArray[np.int_]:
        raise NotImplementedError("get_grid_shape")

    def get_grid_size(self, grid: int) -> int:
        raise NotImplementedError("get_grid_size")

    def get_grid_spacing(
        self, grid: int, spacing: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        raise NotImplementedError("get_grid_spacing")

    def get_grid_type(self, grid: int) -> str:
        raise NotImplementedError("get_grid_type")

    def get_grid_x(self, grid: int, x: NDArray[np.float64]) -> NDArray[np.float64]:
        raise NotImplementedError("get_grid_x")

    def get_grid_y(self, grid: int, y: NDArray[np.float64]) -> NDArray[np.float64]:
        raise NotImplementedError("get_grid_y")

    def get_grid_z(self, grid: int, z: NDArray[np.float64]) -> NDArray[np.float64]:
        raise NotImplementedError("get_grid_z")
