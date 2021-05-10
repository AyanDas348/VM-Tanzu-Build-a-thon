# VM-Tanzu-Build-a-thon
Nutrition Assistant Application

HTML,Bootstrap,MySQL,Python-Flask,Cloud Foundry,Tanzu Application Service,REST API's

Project Description:

Introduction :

Due to the improvement in people’s standards of living, obesity rates are increasing at an alarming speed, and this is reflective of the risks to people’s health. People need to control their daily calorie intake by eating healthier foods, which is the most basic method to avoid obesity. However, although food packaging comes with nutrition (and calorie) labels, it’s still not very convenient for people to refer. App-based nutrient dashboard systems that can analyze real-time images of the meal and analyze it for nutritional content can be very handy and improve dietary habits, and therefore, helps in maintaining a healthy lifestyle.

This project aims at building a web App that automatically estimates food attributes such as ingredients and nutritional value by classifying the input image of food. Our method employs IBM Watson's AI-Driven Food Detection Model for accurate food identification and Food API's to give the nutritional value to the identified food.


Work Flow of the Project:

The user interacts with the Web App Loads an image.

The image is passed to the server application, which uses Clarifai's AI-Driven Food Detection Model Service to analyze the images and Nutrition API to provide nutritional information about the analyzed Image.

Nutritional information of the analyzed image is returned to the app for display. 
