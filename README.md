1. Project Overview
   This project uses Python Producer-Consumer threads to process a large CSV dataset and count phone numbers that start with 805.
   The project consists of three Python files:
       producer.py: Reads the CSV dataset in chunks and sends them to a queue.
       consumer.py: Processes the chunks and counts phone numbers starting with 805.
       main.py: Coordinates the Producer and Consumer threads and manages the execution.
   
2. Connect Google Drive to Google Colab
     First, open Google Colab and create a new notebook.
     Connect Google Drive using:
   
            from google.colab import drive
            drive.mount('/content/drive')
   
4. Download the Dataset
      The dataset is provided through the following link:
           https://tinyurl.com/BigCSV-Fall2026
      Download the RAR archive and save it in Google Drive as my_file.rar.
      The following code downloads the file directly into Google Drive:
   
            import requests
            
            url = "https://tinyurl.com/BigCSV-Fall2026?download=1"
            output_path = "/content/drive/MyDrive/my_file.rar"
            
            response = requests.get(url, stream=True, timeout=60)
            response.raise_for_status()
            
            with open(output_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        file.write(chunk)
            
            print("Download finished!")

4.Verify the Downloaded Dataset
     After downloading the dataset to Google Drive, check that the RAR file exists and verify its size before extracting it.
     
              import os
              
              path = "/content/drive/MyDrive/my_file.rar"
              
              print("File exists:", os.path.exists(path))
              
              if os.path.exists(path):
                  print("File size (MB):", round(os.path.getsize(path) / (1024 * 1024), 2))

5. Extract the Dataset
   Install the RAR extraction utility:
   
           !apt-get update -qq
           !apt-get install -y unrar
   
   Create an extraction directory and extract the archive:
   
          !mkdir -p /content/extracted
          !unrar x -o+ /content/drive/MyDrive/my_file.rar /content/extracted/
   
7. Get the Project from GitHub
    Clone the project repository:
   
          !git clone https://github.com/alaamahmoudgaad24/csv_threading_code.git
   
   Enter the project directory and list the files:
   
           %cd /content/csv_threading_code
           !ls
   
   The repository contains:
            producer.py
            consumer.py
            main.py
            README.md

9. Run the Program
    Run the main Python file:
   
            %cd /content/csv_threading_code
            !python main.py

11. Execution Results
     The program was successfully executed in Google Colab.
     Output:
    
          Total matching rows: 632
          Total rows processed: 46080374
          All threads finished!
          Total matching rows: 632
          Total rows processed: 46080374
          All threads finished! لو استخدمت الاكواد دي كده تمام
