(Open Readme file in code view)
Points to remember
1. The model (Pneumonia_Model.h5) is trained on the data set provided on Kaggle (link: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia).
  Note : Download the data set and use the images provided in it for better prediction.

2. Hardware Specification:
  • CPU: multi-core processor (e.g., Intel Core i5 or AMD Ryzen 5).
  • RAM: 4 GB or higher
  • GPU (Optional): A compatible GPU with CUDA support for faster model training and prediction (e.g., NVIDIA GeForce GTX or Quadro series)

3. Minimum Requirements:
  • Operating System: Windows, macOS, or Linux
  • Python: Version 3.6 or later
  • TensorFlow: Version 2.x
  • Keras: Version compatible with TensorFlow 2.x
  • Flask: Latest version
  • NumPy: Latest version
  • VS Code: Latest version

5. Constraints
  • GUI: The GUI is only in English.
  • Model Loading: Ensure that the model file (chest-xray.h5) is properly validated and protected. Consider using a more secure method for model storage and loading.
  • User Experience: Provide informative messages to users for predictions.
  • Code Structure: Consider organising your code into separate files or modules for better maintainability, especially if the project grows.
  • Compatibility: Ensure compatibility with the latest versions of Python, TensorFlow, and Flask.
  • Data: Use publicly available data for training and testing.
  • Clear Folder Structure: Organise files into clear directories, such as “static” for CSS and JavaScript and “templates” for HTML.

6. Files Path(important)
  /WebApplication
    /static
        /css
            1 (1).jpg
            1 (2).jpg
            style.css
        /js
            script.js
    /templates
        index.html
        page2.html
        resultforNormal.html
        resultforPneumonia.html
    app.py
    Pneumonia_Model.h5

7. To execute the code, compile app.py by following the steps:
    Step 1: Open terminal in VS Code
    Step 2: Write python app.py
    Step 3: Click on the link that you will get during the compilation of the app.py
