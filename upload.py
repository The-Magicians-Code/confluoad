from configparser import ConfigParser
from atlassian import Confluence
from pathlib import Path

conf = ConfigParser()
conf.read("config.ini")

path = Path(conf["File_params"]["absolute_path"])

# Log in to Confluence
confluence = Confluence(
    url=conf["Params"]["url"],
    username=conf["Params"]["username"],
    password=conf["Params"]["password"],
    verify_ssl = False
)

# Attach (upload) a file to a page, if it exists it will update the
# automatically version the new file and keep the old one
confluence.attach_file(path, name=None, content_type=conf["File_params"]["content_type"], page_id=conf["Params"]["page_id"], title=None, space=None, comment="")
