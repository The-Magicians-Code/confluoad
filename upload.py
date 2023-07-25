from configparser import ConfigParser
from atlassian import Confluence
from pathlib import Path

conf = ConfigParser()
conf.read("config.cfg")

path = Path(conf["File_params"]["absolute_path"])

# Log in to Confluence
confluence = Confluence(
    url=conf["Params"]["url"],
    username=conf["Params"]["username"],
    password=conf["Params"]["password"],
    verify_ssl = False
)

if int(conf["File_params"]["manual_type"]):
    content_type = conf["File_params"]["content_type"]  # Manual setting
else:
    import magic
    content_type = magic.from_file(conf["File_params"]["absolute_path"], mime=True) # Automatic detection

# Attach (upload) a file to a page, if it exists it will update the
# automatically version the new file and keep the old one
confluence.attach_file(path, content_type=content_type, page_id=conf["Params"]["page_id"])
