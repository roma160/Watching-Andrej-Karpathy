import os
import re
import urllib.request as request
from typing import Optional, IO

def get_file(url: str, local_name: Optional[str] = None, mode: str = "r") -> IO:
    # Creating local name if it is not given
    if not local_name:
        m = re.match(r".+/([^/]*)", url)
        if not m or not m.group(1):
            local_name = "./" + url
        else:
            local_name = "./" + m.group(1)

    # If there is no such file => downloading
    if not os.path.exists(local_name): # type: ignore
        request.urlretrieve(url, local_name)

    return open(local_name, mode) # type: ignore


if __name__ == "__main__":
    get_file(
        "https://raw.githubusercontent.com/karpathy/makemore/master/README.md",
        "testing.txt"
    )
