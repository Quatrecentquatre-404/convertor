import ffmpeg
from os import listdir
from sys import argv


def parse_io(arg):
    """
    Parses I/O args (all in lower case, remove dots)
    """
    return arg.lower().replace(".", "")


def log(content):
    """
    Logs the content only if --debug flag is specified
    """
    if "--debug" in argv or "-d" in argv:
        print(content)


if __name__ == "__main__":
    if len(argv) >= 3:
        log("Starting ...")

        io_in = parse_io(argv[1])  # Converting from ...
        io_out = parse_io(argv[2])  # to ...

        log("I/O :\nInput : " + io_in + ",\nOutput : " + io_out + ".")

        # Listing all files contained in '.' directory :
        for filename in listdir("."):

            # If the filename is a ont we want to convert :
            if filename.endswith(io_in):
                log("Analyzing file : " + filename + ".")

                # Try to convert the file using 'ffmpeg-python' library :
                try:
                    ffmpeg.input('./' + filename).output('./' + filename.replace(
                        '.' + io_in, '.' + io_out), format=io_out).overwrite_output().run()

                    log("Done. ( ./" + filename.replace('.' + io_in, '.' + io_out) + " )")

                except Exception as e:
                    log("Could not treat this file. ( ./" + filename + " )")

        log("Converion is done.")
