"""importacoes"""
import os
from dotenv import load_dotenv
from app import config
from app import extract
from app import transform
from app import load



def main ():
    """main"""




    df = extract.load_data(config.INPUT_DIR / "2026.xlsx")
    df_nielsen = extract.load_data(config.INPUT_DIR / "export.xlsx")
    
    
    # df_junto = transform.fazer_merge(df, df_nielsen)
    # print(df_junto.head(50))
    
    # print(df.columns)
    # print(df_nielsen.columns)
    
    df.info()
    df_nielsen.info()

if __name__ == "__main__":
    main()
