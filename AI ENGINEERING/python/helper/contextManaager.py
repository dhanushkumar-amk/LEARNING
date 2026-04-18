class ManagedResource:
    def __enter__(self):
        print("Setting up")
        return self          # this becomes the `as` target

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Tearing down")
        return False         # False = don't suppress exceptions

with ManagedResource() as r:
    print("Using resource")

# Output:
# Setting up
# Using resource
# Tearing down
