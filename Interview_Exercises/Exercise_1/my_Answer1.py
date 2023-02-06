

from pathlib import Path
import pandas as pd

data_dir = Path("data/")

print(data_dir)

def merge_data(all_file_paths: Path):
    ''' Merges all data on folder into a tab-delimited file

    The function must include a check to confirm that each input file has the same headers/columns.
    The headers/columns of each file must be in the same order. If not, the columns must be re-ordered for consistency.
    The function must combine each file in (all_file_paths)
    The output file must be in tab-delimited format.

    '''

    assert all_file_paths.is_dir()

    file_list  = list(all_file_paths.iterdir())

    for file in file_list:
        

    

    return True


if __name__ == '__main__':
    files = merge_data(data_dir)
    print(files)




