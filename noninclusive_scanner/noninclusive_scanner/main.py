from noninclusive_scanner.get_config import config_det
from noninclusive_scanner.get_postgres_data import get_now
import pandas as pd

def init_scan(config_dir, section_name):
    db_connect = config_det(config_dir, section_name)
    # Logic to read non-inclusive words file

    ni_word_lst = [line.strip() for line in open(f"{config_dir}/noninclusive_words.txt", 'r')]
    # Convert values to lowever case
    ni_word_lst = list(map(lambda x: x.lower(), ni_word_lst))

    # Read Dictionary from any Database
    df = get_now(db_connect)
    # Convert DF to lower case
    df = df.apply(lambda x: x.astype(str).str.lower())
    final_df = pd.DataFrame(columns = ['table_schema', 'table_name', 'table_type', 'column_name'])
    print(df)
    col_list = df.columns.to_list()
    print("================================\n")
    for col_idx in range(len(col_list)):
        col_name = col_list[col_idx]
        for key_idx in range(len(ni_word_lst)):
            keyword = ni_word_lst[key_idx]
            final_df = pd.concat([final_df,df[df[col_name].str.contains(keyword)]], axis=0)

    final_df = final_df.reset_index()
    final_df = final_df.drop_duplicates()
    print(final_df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config_dir = "/Users/kashbagare/projectdir/python/certs"
    section_name = "SCANNER"
    init_scan(config_dir, section_name)


