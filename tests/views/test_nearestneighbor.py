# from nose.tools import assert_equal
import numpy as np

from web.views.routes.nearestneighbor import NearestNeighbor


class TestNearestNeighbor:
    ref_matrix = [[50000., 6., 4., 8., 2.],
                  [50000., 50000., 5., 8., 6.],
                  [50000., 50000., 50000., 9., 4.],
                  [50000., 50000., 50000., 50000., 7.],
                  [50000., 50000., 50000., 50000., 50000.]]

    def test_idx_0(self):
        sum_val, result = NearestNeighbor().discover_path_and_weight(0, np.array(self.ref_matrix))
        assert np.array_equal(np.array([4, 2, 4, 4, 1]), result)
        assert 18 == sum_val

    def test_idx_1(self):
        sum_val, result = NearestNeighbor().discover_path_and_weight(1, np.array(self.ref_matrix))
        assert np.array_equal(np.array([4, 2, 4, 4, 1]), result)
        assert 18 == sum_val

    def test_idx_2(self):
        sum_val, result = NearestNeighbor().discover_path_and_weight(2, np.array(self.ref_matrix))
        assert np.array_equal(np.array([4, 4, 0, 4, 1]), result)
        assert 19 == sum_val

    def test_idx_3(self):
        sum_val, result = NearestNeighbor().discover_path_and_weight(3, np.array(self.ref_matrix))
        assert np.array_equal(np.array([4, 3, 4, 4, 1]), result)
        assert 18 == sum_val

    def test_idx_4(self):
        sum_val, result = NearestNeighbor().discover_path_and_weight(4, np.array(self.ref_matrix))
        assert np.array_equal(np.array([3, 3, 4, 1, 0]), result)
        assert 20 == sum_val
