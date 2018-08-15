"""

 NEAREST NEIGHBOR

"""
import numpy as np



class NearestNeighbor:
    max_dst = 50000
    """
    For every vertex in the distance matrix
    1. Define a node as the pivotal vertex.
    2. Remove all edges adjacent to the vertex.
    3. Identify all lowest values per column thats in the upper right.
    4. Add the two lowest edges that are connected to the pivotal vertex.
    4. Total all values as the nearest neighbor path.

    From lecture notes, it seems the spliced_row_col addition placed two of the consecutive
    edges back into the graph.
    Due to experimentation it seems only one edge is needed to ensure all vertices are connected.

    """

    def find_min_distance(self, ref_m):
        """
        With a two dim array (reference matrix ref_m) ask the
        nearest neighbor algorithm to find the min distance and path.
        :param ref_m: 2D array of distances.  A row idx is the lat,lon that was passed here from the
        map.  a col idx equal to row is the same lat,lon.  So its distance will always be insignificant (0 or inf).
        :return: total distance and path of idxs for two points
            Exaplanation for 'path of idxs':

            ['1','0'] means:
                src idx of 0 (position in array) traverses to dst idx of '1' (value in array).
                src idx of 1 (position in array) traverses to dst idx of '0' (value in array).
                    Use of "'" is only to explain, actual values will be numeric.

        """
        m = np.array(ref_m)
        # Prevent numpy exponential notation on print, default False
        # np.set_printoptions(suppress=True)
        # print(np.around(m, 3))

        return self._calc_paths(m)

    def _calc_paths(self, m):
        """
        For each node in the map calculate the minimum path.
        With the resulting min path compare it to current path mins.
        Keep the overall lowest path and its total distance.
        """
        min_total = self.max_dst
        min_path = []
        for idx in range(len(m)):
            ref_total, ref_path = self.process(idx, m)
            if ref_total < min_total:
                min_path = ref_path
                min_total = ref_total
        return min_total, min_path

    def process(self, idx: int, m):
        """
        Calc the total distance for the minimum path found for this idx position.

        :param idx, int: idx of row/col that we're going to remove.
        :param m, np.array: Entire matriz of distances each row=i is the same node as the col=i
        :return: total distance for the given path (given in the adj_min_positions array)
        """
        ref_m = self._splice(idx, m)
        min_pos_per_row = self._get_row_min_positions(ref_m)
        min_val_per_row = self._get_row_min_values(ref_m)
        idx_pos, idx_vals = self._get_mins_by_pos_and_val_on_spliced_row_col(idx, m)
        # print(idx_vals)
        adj_min_pos, adj_min_val = self._get_adj_pos_val_path(idx, idx_pos, idx_vals, min_pos_per_row, min_val_per_row)
        sum_of_min_vals = self._calc_path_total_dst(adj_min_val)
        # print(adj_min_pos, np.around(adj_min_val, 3), sum_of_min_vals)
        return sum_of_min_vals, adj_min_pos

    def _calc_path_total_dst(self, adj_min_val):
        sum_of_min_vals = adj_min_val.sum() - self.max_dst
        return sum_of_min_vals

    @staticmethod
    def _get_adj_pos_val_path(idx, idx_pos, idx_vals, min_pos_per_row, min_val_per_row):
        min_pos_per_row = min_pos_per_row + 1
        adj_min_pos = np.insert(min_pos_per_row, idx, idx_pos[0], axis=0)
        adj_min_val = np.insert(min_val_per_row, idx, idx_vals[0], axis=0)
        return adj_min_pos, adj_min_val

    @staticmethod
    def _get_mins_by_pos_and_val_on_spliced_row_col(idx, m):
        """ Sum all values except for undefined (i.e. 50000) distance cells. """
        # Merge everything on row[idx] with everything in col[idx],
        # but only keep the minimum between the two.
        ref_edges = np.minimum(m[..., idx], m[idx, ...])
        # Get idx's for the consecutive lowest distances.
        # That is, sort from pos of lowest distance up to the highest distance pos
        idx_pos = ref_edges.argsort()
        # Get values at each of the identified position indexes.
        # That is, retrieve the values in the order of the given 'idx' positions.
        idx_vals = ref_edges[idx_pos]
        return idx_pos, idx_vals

    @staticmethod
    def _get_row_min_values(ref_m):
        """ Get minimum position along each row """
        min_val_per_row = np.amin(ref_m, axis=1)
        return min_val_per_row

    @staticmethod
    def _get_row_min_positions(ref_m):
        """ Get minimum value for each row """
        min_pos_per_row = np.argmin(ref_m, axis=1)
        return min_pos_per_row

    @staticmethod
    def _splice(idx, m):
        """ Create a sub-matrix by removing the row/col at the given idx """
        ref_m = np.delete(np.delete(m, idx, 0), idx, 1)
        return ref_m
