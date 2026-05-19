import numpy as np 

def swap_rows(M, row1, row2):
    M = M.copy()

    M[[row1, row2], :] = M[[row2, row1], :]

    return M 

def get_index_of_non_zero_value_from_row(M, row, augmented = False):
    M = M.copy()

    if augmented == True:
        M = M[:, : -1]
    
    row_array = M[row]
    for i, val in enumerate(row_array):
        if not np.isclose(val, 0, atol = 1e-5):
            return i 
    return -1 

def get_index_of_non_zero_value_from_column(M, column, starting_row):

    column_array = M[stating_row :, column]

    for i, val in enumerate(column_array):
        index = i + starting_row
        return index

    return -1 

def augmented_matrix(A, B):
    augmented_M = np.hstack((A,B))
    return augmented_M

def row_echelon_form(A,B):
    
    det_A = np.linalg.det(A)
    if np.isclose(det_A, 0, atol = 1e-5) == True:
        return "Singular System"

    A = A.copy()
    B = B.copy()

    A = A.astype('float64')
    B = B.astype('float64')

    num_rows = len(A)

    M = augmented_matrix(A,B)

    for row in range(num_rows):
        pivot_candidate = M[row, row]

        if np.isclose(pivot_candidate, 0) == True:
            non_zero_below_pivot = get_index_of_non_zero_value_from_column(M, row, row)
            M = swap_rows(M , row, non_zero_below_pivot)

        else:
            pivot = pivot_candidate

        M[row] = (1/ pivot) * M[row]

        for j in range(row + 1, num_rows):
            val_below_pivot = M[j, row]

            M[j, :] = M[j, :] - val_below_pivot * M[row, :]

    return M 

def back_substitution(M):

    
    M = M.copy()
    num_rows = M.shape[0]

    for row in reversed(range(num_rows)):
        substitution_row = M[row, :]
        
        index = row
        for j in range(row):
            row_to_reduce = M[j, :]

            value = row_to_reduce[row]

            row_to_reduce = row_to_reduce - value * substitution_row

            M[j, :] = row_to_reduce

    solution = M[:,: -1]

    return solution

def main():
    A = np.array([[1,2,3],[0,1,0], [0,0,5]])
    B = np.array([[1], [2], [4]])

    echelon_M = row_echelon_form(A, B)

    solution = back_substitution(echelon_M)

    print(solution)


if __name__ == "__main__":
    main()


