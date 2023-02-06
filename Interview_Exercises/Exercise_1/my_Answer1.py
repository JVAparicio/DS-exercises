

from pathlib import Path
import pandas as pd
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')


def check_columns(headers: list[str], file: Path):
    """
    Checks if set of column names of two dataframes match. Logs and exits with error if not matching.
    """

    header2 = pd.read_csv(file, index_col=0, nrows=0).columns.tolist()

    if set(headers) != set(header2):
        logging.debug(f"{set(headers)} does not match {set(header2)}")
        exit(1)
    return



def check_paths(paths: list[str]) -> None:
    if not paths:
        logging.debug("No argument provided, only lists are allowed")
        exit(1)
    if not isinstance(paths, list):
        logging.debug(f"{type(paths)} only lists are allowed")
        exit(1)
    for path in paths:
        if not os.path.exists(path):
            logging.debug(f'{path} does not exist')
            exit(1)
    return


def merge_data(all_file_paths: Path):
    ''' Merges all data on folder into a tab-delimited file

    The function must include a check to confirm that each input file has the same headers/columns.
    The headers/columns of each file must be in the same order. If not, the columns must be re-ordered for consistency.
    The function must combine each file in (all_file_paths)
    The output file must be in tab-delimited format.

    '''

    #assert all_file_paths.is_dir()
    check_paths(all_file_paths) 
    
    
    df_columns = pd.read_csv(file_list[0], index_col=0, nrows=0).columns.tolist() ## Read columns from first file

    for file in file_list[1:]:
        check_columns(df_columns, file)
        df_temp = df_temp[columns]  
        
    logging.info("All columns checked") 

    #df_final = pd.concat([df_final, df_temp])   ##concat to final

    #df_final.to_csv('combined', sep='\t')    

    return file


if __name__ == '__main__':
    data_dir = Path("data/")
    file_list  = list(data_dir.iterdir())
    files = merge_data(file_list)



