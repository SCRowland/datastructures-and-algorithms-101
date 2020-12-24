import pytest
from datastructures.graphs.dag import DAG


@pytest.fixture
def dag():
    vertices = [1, 2, 3, 4]
    edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
    return DAG(vertices=vertices, edges=edges)


def test_dag(dag):
    expected_vertices = [1, 2, 3, 4]
    expected_edges = {
        1: [2, 3],
        2: [4],
        3: [4],
    }

    assert dag._vertices == expected_vertices
    assert dict(dag._edges) == expected_edges


def test_dag_double_add(dag):
    expected_vertices = [1, 2, 3, 4]
    expected_edges = {
        1: [2, 3],
        2: [4],
        3: [4],
    }

    dag.add_vertex(2)
    dag.add_edge(1, 2)

    assert dag._vertices == expected_vertices
    assert dict(dag._edges) == expected_edges
