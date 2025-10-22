import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path
import time

# List of notebooks to be executed in order
notebooks = [
    "code/Preprocessing.ipynb",
    "code/Calculating_XGBMASV.ipynb",
    "code/FS_SMOTE_Detection.ipynb",
]

# Folder to save executed notebook
output_dir = Path("results/executed_notebooks")
output_dir.mkdir(parents=True, exist_ok=True)

for nb_path in notebooks:
    nb_path = Path(nb_path)
    out_path = output_dir / f"{nb_path.stem}_executed.ipynb"
    working_dir = nb_path.parent  # Ensure the notebook runs in its original directory

    print(f"\n[INFO] Running notebook: {nb_path}")
    print(f"[INFO] Working directory: {working_dir}")
    start_time = time.time()

    with open(nb_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=0, kernel_name="python3")

    try:
        # Important: set the metadata path to the notebook folder
        ep.preprocess(nb, {"metadata": {"path": str(working_dir)}})
    except Exception as e:
        print(f"[ERROR] Failed to execute {nb_path.name}: {e}")
        continue

    # Save the executed notebook
    with open(out_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    elapsed = time.time() - start_time
    print(f"[DONE] {nb_path.name} -> {out_path}")
    print(f"[TIME] Execution completed in {elapsed:.2f} detik")

print("\n All notebooks have been executed and saved in the folder 'results/executed_notebooks'")
