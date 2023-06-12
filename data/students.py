import pandas as pd
PATH = "https://docs.google.com/spreadsheets/d/1ch0wtMEsdKVBPcceODlPWfi292ECNszzm11MU9xKXAw/export?format=csv&gid=1385521382"
DATA = pd.read_csv(PATH).to_dict("records")
