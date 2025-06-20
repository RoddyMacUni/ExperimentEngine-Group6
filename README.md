# User Instructions
## Installation
2. Install WSL2 by running `wsl --install` in Administrator Powershell
2. Download the WSL instance for running this application from [this link](https://strath-my.sharepoint.com/:u:/g/personal/roderick_macrae_2022_uni_strath_ac_uk/ETGdyocvSqtDn8t2IdTEM7MBuh2AAxVrZceVSRkm8L4xLw?e=MKurY9)
3. Double-click the downloaded file and WSL2 should install it
4. Set the repo up by running `./root/setup.sh`
---

# Developer Instructions

## Installation 
1. Open Powershell as administrator and run `wsl --install`
2. Follow the user installation instructions
4. Open Pycharm and open the project from the following path: "\\wsl.localhost\ne-arch\root\ExperimentEngine-Group6"
5. Select the interpreter button in the bottom left of the Pycharm window
   ![Pasted image 20250514144225.png](guide-images/Pasted%20image%2020250514144225.png)
6. Select "On WSL" from the "Add new interpreter" drop down
   ![Pasted image 20250514144426.png](guide-images/Pasted%20image%2020250514144426.png)
7. Select the "Existing" radio button and enter the path to your python executable then select the "Create" button<br>
   a. The path will look something like "\\wsl.localhost\ne-arch\root\ExperimentEngine-Group6\.venv\bin\python"
   ![Pasted image 20250514144205.png](guide-images/Pasted%20image%2020250514144205.png)
   ![Pasted image 20250514144144.png](guide-images/Pasted%20image%2020250514144144.png)

## Adding a dependency
1. Ensure the correct version of the module is installed in the virtual environment
2. Update the `requirement.txt` by running the following command

   `pip freeze > ./requirements.txt`

3. Ensure the requirements file has updated correctly by running the following command and checking the project runs as expected

   `pip install -r ./requirements.txt`