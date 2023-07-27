## Contactless rPPG Python Project
This project implements a contactless heart rate and respiratory rate measurement using Python and OpenCV.</br>
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/downloads/)
[![Instagram](https://img.shields.io/badge/Instagram-Follow%20Me-red)](https://www.instagram.com/blood_burner_47/)


## Prerequisites
Make sure you have the following installed on your system:
1. Python (>=3.6)</br>
2. OpenCV (cv2)</br>
3. NumPy</br>
4. pandas</br>

You can install the required dependencies using the following command:
```
pip install opencv-python numpy pandas
```
## Usage
1. Clone the repository:
```
git clone https://github.com/RahulPatil-Tech/Contactless rPPG Python Project.git
cd Contactless rPPG Python Project
```
2. Download the haarcascade_frontalface_default.xml file for face detection and place it in the project directory.

3. Run the script:
```
app.py
```
4. The script will open a webcam feed showing your face with a blue rectangle around it, indicating successful face detection.

5. The heart rate and respiratory rate will be displayed on the screen in real-time, along with a constant number of your choice.

6. The heart rate and respiratory rate data will be saved to a CSV file named data.csv in the project directory.

7. Press 'Q' or 'q' to quit the application.

## Configuration
You can modify the constant number displayed on the screen by changing the constant_number variable in the main function of the main.py script.

## Contributing
Contributions to this project are welcome. If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
The face detection is based on the Haar Cascade classifier provided by OpenCV.</br>
The idea for this project was inspired by (https://www.youtube.com/watch?v=D_KYv7pXAvQ).

## Contact
If you have any questions or suggestions, feel free to contact me at rp3252154@gmail.com.
