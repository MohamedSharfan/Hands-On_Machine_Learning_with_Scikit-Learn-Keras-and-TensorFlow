# Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow — Companion Code

This repository contains companion code, notebooks, scripts and example projects that go along with the book "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron. It is intended to help you follow the book, reproduce experiments, and learn practical machine learning and deep learning techniques using scikit-learn, Keras, and TensorFlow.

Important: the book text and figures are copyrighted by the book's author and publisher. This repository contains code examples and supplemental material only. If you distribute or reuse book content beyond code, ensure you follow the book's license and publisher permissions.

## Contents

- Chapter folders and notebooks (e.g., `ch01/`, `ch02/`, ...). Each chapter folder typically contains Jupyter notebooks (.ipynb) with annotated examples.
- `notebooks/` — alternative or consolidated notebooks (project dependent).
- `scripts/` — helper scripts and utilities used across notebooks.
- `data/` or data download helpers — small sample datasets or links to fetch large datasets on demand.
- `requirements.txt` or `environment.yml` — Python package requirements (if present).

Note: exact structure may vary. Browse the repo to see the actual folders and files.

## Quick start

1. Clone the repository:
   git clone https://github.com/MohamedSharfan/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow.git
   cd Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow

2. Create and activate a virtual environment (recommended)
   - Using venv (Python 3.8+):
     python -m venv .venv
     source .venv/bin/activate    # macOS / Linux
     .venv\Scripts\activate       # Windows (PowerShell)
   - Or use conda:
     conda create -n holtf python=3.10
     conda activate holtf

3. Install dependencies
   - If the repo includes a requirements.txt:
     pip install -r requirements.txt
   - If there is an environment.yml:
     conda env create -f environment.yml
   - Otherwise, install typical packages used in the book:
     pip install numpy scipy scikit-learn matplotlib pandas seaborn jupyterlab notebook tensorflow keras

   Note: TensorFlow installation depends on your platform and whether you want GPU support. See https://www.tensorflow.org/install for the recommended package and instructions for your system.

4. Start Jupyter Lab / Notebook
   jupyter lab
   or
   jupyter notebook

5. Open the notebook for the chapter you want and run the cells. If a notebook fetches a large dataset, it will often download data on first run or provide a helper script to fetch it.

## Running notebooks non-interactively

- Convert a notebook to a Python script:
  jupyter nbconvert --to script my_notebook.ipynb
- Execute a notebook headlessly:
  jupyter nbconvert --to notebook --execute my_notebook.ipynb --output executed.ipynb

## Data

Many examples use datasets available from:
- scikit-learn (`sklearn.datasets`)
- OpenML (via `sklearn.datasets.fetch_openml`)
- Keras datasets (`tf.keras.datasets`)
Large datasets are typically fetched on demand to avoid including them in the repository. Check each notebook for dataset download or preprocessing steps.

## Tips & troubleshooting

- Kernel crashes / out-of-memory: reduce dataset size (use a sample), increase swap, or use a machine with more RAM / GPU.
- TensorFlow GPU: ensure correct CUDA and cuDNN versions for the TensorFlow release you install.
- Reproducibility: set random seeds in numpy, tensorflow, and scikit-learn when reproducing experiments (not all operations are fully deterministic across platforms).

## Contributing

Contributions are welcome (issues, bug reports, small fixes). If you want to submit changes:
- Open an issue describing the bug or improvement.
- Fork the repo and create a branch for your change.
- Submit a pull request with a clear description of what you changed and why.

Please follow standard contribution etiquette: keep changes focused, run notebooks or scripts you modify, and update requirements if you add new dependencies.

## License

This repository includes code examples inspired by the book. The code in this repository is provided under the license included in the repo (check the LICENSE file). The book text, figures, and published content remain the property of the original copyright holders.

## Citation / Acknowledgement

If you use this repository in your work, please cite the original book:
Aurélien Géron, "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", O'Reilly Media.

## Contact / Maintainer

Maintained by MohamedSharfan (GitHub: @MohamedSharfan). For questions, open an issue or contact via GitHub.

Happy learning!
