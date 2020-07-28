#include <opencv2/opencv.hpp>
#include <iostream>
#include <opencv/cv.h>
#include <opencv/cxcore.h>
#include <opencv2/highgui.hpp>
#include <iostream>
#include<string.h>
#include <stdlib.h>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
using namespace cv;
using namespace std;
int thresh = 100;
    int max_thresh = 255;
    Mat frame;
    Mat frame_HSV;
    Mat frame_threshold;

void thresh_callback(int, void* );
int main(int argc, char* argv[])
{
    VideoCapture cap(argc > 1 ? atoi(argv[1]) : 0);
    for(;;)
    {
    cap >> frame;
    GaussianBlur(frame,frame,Size(3,3), 0); //smoothing
    cvtColor( frame, frame_HSV, CV_BGR2HSV );
    thresh_callback( 0, 0 );
    waitKey(1);
    }
  }

    /** @function thresh_callback */
 void thresh_callback(int, void* )
    {

      Mat threshold_output;
      vector<vector<Point> > contours; //list of number used to represent an image- or an image handler used to quantify an image
      vector<Vec4i> hierarchy;
      inRange(frame_HSV, Scalar(0,32,0), Scalar(97, 255, 255), threshold_output);// binary image or mask
     erode(threshold_output, frame_threshold, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) ); // Morphological filtering elements
      dilate(threshold_output, frame_threshold, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) );
      imshow("Thresholded Image", frame_threshold); // binary image

       findContours( frame_threshold, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) ); //rectangular contour encoded with 4pts
      /// Approximate contours to  get a bounding rects or circles if used
      vector<RotatedRect> minRect( contours.size() ); //

      for( float i = 0; i < contours.size(); i++ )//calculating the min area for rect and discarding the unnecessary contours
     {
      float area = contourArea(contours[i]);
      if (area>1000)                //anything less than this should be discarded or not taken into consideration
      minRect[i] = minAreaRect( Mat(contours[i]) );
      }

      for( int i = 0; i< int (contours.size()); i++ )// calculating area for only desired contours
      {
      float area = contourArea(contours[i]);
      if (area>1000)
      drawContours( frame, contours, i, Scalar( 255, 0, 0 ), 1, 8, vector<Vec4i>(), 0, Point() );
      Point2f rect_points[4];
      minRect[i].points( rect_points );
      //float angle = minRect[i].angle;
      float height = minRect[i].size.height;
      float width = minRect[i].size.width;
      if(height>width){
                   minRect[i].size.height =(float)(0.32)*minRect[i].size.height; // calculating ROI and scaling it down

                   minRect[i].center = (rect_points[1]+rect_points[2])/2 + (rect_points[0]-rect_points[1])/5;
               } else {
                  minRect[i].size.width =(float)(0.32)*minRect[i].size.width;
                   minRect[i].center = (rect_points[2]+rect_points[3])/2 + (rect_points[0]-rect_points[3])/5;
              }

      minRect[i].points( rect_points );
      for( int j = 0; j < 4; j++ )
      line( frame, rect_points[j], rect_points[(j+1)%4], Scalar(100, 0, 255), 2, 8 ); //basically used for connecting points by the contour
      }
      namedWindow( "Detecting Contours for Finger", CV_WINDOW_AUTOSIZE );
      imshow( "Detecting Contours for Finger", frame );
      }




