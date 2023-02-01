try:
    # with - automatically release external resource. (like using in c#).
    # files can be multiple.
    # Close method will be called on file automatically.
    # Work with magic obj methods (supports content management protocol):
    # exit, enter
    with open("app.py") as file:
        print("File was opened")
        file.__exit__
except Exception as ex:
    print(f"Exception during. Type: {type(ex)}")
