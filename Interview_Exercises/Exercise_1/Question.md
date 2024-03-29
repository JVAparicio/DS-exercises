Python Questions
Question 1

NYC taxi trip record data can be downloaded from the below 4 links:

    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2018-09.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2018-10.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2018-11.csv
    https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2018-12.csv



Write a function that accepts a list of CSV files (all_file_paths) as the input. The function must create a tab-delimited file with each input file appended together. The function must check for the following:

    The function must include a check to confirm that each input file has the same headers/columns.
    The headers/columns of each file must be in the same order. If not, the columns must be re-ordered for consistency.
    The function must combine each file in (all_file_paths)
    The output file must be in tab-delimited format.

Question 2

Write a function that accepts the location of any kind of flat file (file_path) and prints out the following:

    file_name (list): Print out the file name including extension (not full URL)
    delimiter (string): Print out the delimiter of the file
    columns_and_dtypes (dictionary): Print out each column name and Redshift data type.

A list of accepted Redshift data types can be found here: https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html

Example output:
- file_name = random_file_name.csv
- delimiter = ","
- columns_and_dtypes = {"column_1": {"column_name": "date_time", "redshift_dtype": "timestamp"},
                      "column_2": {"column_name": "region_name", "redshift_dtype": "varchar(20)"},
                      "column_3": {"column_name": "sales_volume", "redshift_dtype": "integer"}}

Question 3

Explain what the following function is doing

def my_function(self, s3_key, data_df, stage_prefix, output_folder, delimiter=',', app_id='app_id'):
        config_file = os.path.join(self.config_path, 'app_map.json')
        if os.path.exists(config_file):
            with open(config_file) as json_file:
                map_data = json.load(json_file)
        else:
            logging.info('missing config file for mapping')
            exit(1)

        clients = []
        new_s3_path = []
        files = []
        filename = None
        for index, row in data_df.iterrows():
            headers = list(data_df.columns)
            for client in map_data.keys():
                if row[app_id].startswith(client) or row[app_id] in map_data[client]:
                    if client not in clients:
                        clients.append(client)
                    filename = f'{output_folder}/{client}-{os.path.splitext(s3_key)[0]}.csv'
                    if filename not in files:
                        files.append(filename)
                    with open(filename, 'a', encoding='utf-8') as f:
                        writer = csv.DictWriter(f, delimiter=delimiter,
                                                lineterminator='\n',
                                                fieldnames=headers,
                                                quotechar='"')
                        if os.stat(filename).st_size == 0:
                            writer.writeheader()
                        data = {col: val for col, val in zip(headers, list(row))}
                        writer.writerow(data)