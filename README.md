# automate-colab-script-service


A service and a script to run a Google Colab file in headless mode in the background at scheduled time and download the generated artifact to respective directory.

Steps the script performs:

1. Open the specified colab file.
2. Run the project.
3. Wait until the required artifact is downloaded.
4. After download, close the web driver.
5. Tag the downloaded artifact with Date and Time. 
6. Move the artifact to required directory which is your datastore.

Sample run on a Colab Project which creates a .txt file:

<p align="center"><img src="https://imgur.com/ukvOU0B.gif"></p>
