import importlib.util
import os

def find_label_studio_path():
    label_studio_spec = importlib.util.find_spec("label_studio")
    if label_studio_spec is not None:
        label_studio_path = os.path.dirname(label_studio_spec.origin)
        label_studio_path += '/core/settings'
        print(f"Label Studio is installed in: {label_studio_path}")
    else:
        print("Label Studio is not installed.")

if __name__ == "__main__":
    find_label_studio_path()



