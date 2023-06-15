from atlassian import Confluence
from pathlib import Path

file = "file.csv"
path = Path("") / file

# Log in to Confluence
confluence = Confluence(
    url="",
    username="",
    password="",
    verify_ssl = False
)

# Attach (upload) a file to a page, if it exists it will update the
# automatically version the new file and keep the old one
confluence.attach_file(path, name=None, content_type="text/csv", page_id="316211592", title=None, space=None, comment="")
