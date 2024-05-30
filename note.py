from langchain.tools import tool


def note_tool(note):
    """
        saves a note to a local file

        Args:
            note: the text note to save
        """
    with open("note.txt", "a") as f:
        f.write(note+"\n")
