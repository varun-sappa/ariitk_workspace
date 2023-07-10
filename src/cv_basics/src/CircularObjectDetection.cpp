#include <opencv2/opencv.hpp>

int main() {
    cv::VideoCapture cap(0); // Open the default camera
    if (!cap.isOpened()) {
        std::cout << "Failed to open the camera." << std::endl;
        return -1;
    }

    cv::namedWindow("Ball Detection", cv::WINDOW_NORMAL);

    while (true) {
        cv::Mat frame;
        cap >> frame; // Capture frame from camera

        if (frame.empty()) {
            std::cout << "Failed to capture frame." << std::endl;
            break;
        }

        cv::blur(frame, frame, cv::Size(3, 3)); // Apply blur to reduce noise

        cv::Mat hsv;
        cv::cvtColor(frame, hsv, cv::COLOR_BGR2HSV); // Convert frame to HSV color space

        cv::Scalar lowerGreen(0, 0, 180); // Lower HSV threshold for green color (adjust as needed)
        cv::Scalar upperGreen(180, 25, 255); // Upper HSV threshold for green color (adjust as needed)

        cv::Mat mask;
        cv::inRange(hsv, lowerGreen, upperGreen, mask); // Create a binary mask of the green color

        cv::Mat contoursImg = frame.clone();

        std::vector<std::vector<cv::Point>> contours;
        cv::findContours(mask, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE); // Find contours

        for (size_t i = 0; i < contours.size(); i++) {
            double area = cv::contourArea(contours[i]);
            if (area > 1) { // Filter out small contours based on area
                cv::drawContours(contoursImg, contours, static_cast<int>(i), cv::Scalar(0, 255, 0), 2); // Draw contours on the frame
            }
        }

        cv::imshow("Ball Detection", contoursImg); // Show the resulting frame

        if (cv::waitKey(1) == 27) { // Wait for ESC key press
            break;
        }
    }

    cap.release(); // Release the camera
    cv::destroyAllWindows(); // Close all OpenCV windows

    return 0;
}
