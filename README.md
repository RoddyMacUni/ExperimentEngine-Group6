# Installation Instructions
1. Clone the repo with 

    `git clone https://github.com/RoddyMacUni/ExperimentEngine-Group6`

3. Install any pip dependencies with

    `pip install -r ./requirements.txt`

# Adding a dependency
1. Ensure the correct version of the module is installed in the virtual environment
2. Update the `requirement.txt` by running the following command 
 
    `pip freeze > ./requirements.txt`

3. Ensure the requirements file has updated correctly by running the following command and checking the project runs as expected

   `pip install -r ./requirements.txt`

# Installing WSL2 on Windows 11

1. Open Powershell as administrator and run `wsl --install`
2. Run the `wsl --install -d Ubuntu-22.04 ` command to install Ubuntu
3. Download the project to the correct folder by using the `cd ~/ && git clone https://github.com/RoddyMacUni/ExperimentEngine-Group6.git`
4. Open Pycharm and open the project, it will be located at the path below where <DS_Name> is the username you log into PEGASUS with
   "\\wsl.localhost\Ubuntu\home\<DS_Name>\ExperimentEngine-Group6"
5. Select the interpreter button in the bottom left of the Pycharm window
   ![Pasted image 20250514144225.png](guide-images/Pasted%20image%2020250514144225.png)
6. Select "On WSL" from the "Add new interpreter" drop down
   ![Pasted image 20250514144426.png](guide-images/Pasted%20image%2020250514144426.png)
7. Select the "Existing" radio button and enter the path to your python executable then select the "Create" button<br>
   a. The path will look something like "\\wsl.localhost\Ubuntu\home\mkb22202\ExperimentEngine-Group6\.venv\bin\python"
   ![Pasted image 20250514144205.png](guide-images/Pasted%20image%2020250514144205.png)
   ![Pasted image 20250514144144.png](guide-images/Pasted%20image%2020250514144144.png)
