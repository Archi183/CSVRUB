import sys
from pipeline import run_pipeline

def load_config(config_path):
    # loads CONFIG from a python file
    namespace = {}
    with open(config_path, "r", encoding="utf-8") as f:
        code = f.read()
    exec(code, namespace)
    return namespace["CONFIG"]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python run.py configs/my_config.py input.csv [output_dir]")
        sys.exit(1)

    config_path = sys.argv[1]
    input_csv = sys.argv[2]
    out_dir = sys.argv[3] if len(sys.argv) >= 4 else "output"

    config = load_config(config_path)
    run_pipeline(input_csv, out_dir, config)