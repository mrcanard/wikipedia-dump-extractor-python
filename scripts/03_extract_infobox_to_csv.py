
from wikipedia.etl.tools import batch_extract

if __name__ == '__main__':
    batch_extract("en", "infoboxes", "extract_infoboxes")
