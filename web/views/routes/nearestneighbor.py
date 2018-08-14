#
# NEAREST NEIGHBOR
#
import numpy as np

def_dst = 50000


class NearestNeighbor:
    """
    For every vertex in the distance matrix
    1. Define a node as the pivotal vertex.
    2. Remove all edges adjacent to the vertex.
    3. Identify all lowest values per column thats in the upper right.
    4. Add the two lowest edges that are connected to the pivotal vertex.
    4. Total all values as the nearest neighbor path.

    """

    def find_min_distance(self, ref_m):
        m = np.array(ref_m)

        # prevent numpy exponential notation on print, default False
        np.set_printoptions(suppress=True)
        print(np.around(m, 3))

        for idx in range(len(m)):
            self.discover_path_and_weight(idx, m)

    def discover_path_and_weight(self, idx: int, m):
        # Create a sub-matrix by removing the row/col at the given idx
        ref_m = np.delete(np.delete(m, idx, 0), idx, 1)
        # Get minimum value for each row
        min_pos_per_row = np.argmin(ref_m, axis=1)
        # Get minimum position along each row
        min_val_per_row = np.amin(ref_m, axis=1)
        # Sum all values except for undefined distance cells.
        # ref_vertex_edges = m[..., idx][:idx]
        ref_edges = np.minimum(m[..., idx], m[idx, ...])
        # np.amin(ref_edges, axis=0)
        # get each idx for the consecutive lowest distances, from pos of lowest distance up to the highest distance pos
        idx_pos = ref_edges.argsort()
        # print(idx_pos)
        # get values at each of the indexes...
        idx_vals = ref_edges[ref_edges.argsort()]
        # print(idx_vals)
        min_pos_per_row = min_pos_per_row + 1
        adj_min_pos = np.insert(min_pos_per_row, idx, idx_pos[0], axis=0)
        adj_min_val = np.insert(min_val_per_row, idx, idx_vals[0], axis=0)
        sum_of_min_vals = adj_min_val.sum() - 50000.
        print(adj_min_pos, np.around(adj_min_val, 3), sum_of_min_vals)
        return sum_of_min_vals, adj_min_pos
